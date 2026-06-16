#!/usr/bin/env python3
"""
SIXT multi-sito opener per confrontare prezzi.

Cerca su una location dal-al, confrontando le pagine SIXT
per varie nazionalita. Lo script usa Playwright per aprire i domini, compilare
quanto possibile la ricerca, estrarre le auto/prezzi visibili e salvare un CSV.

Nota: i siti di noleggio cambiano spesso DOM e flow. Lo script e pensato come
automazione assistita: prova a compilare ed estrarre i dati, poi lascia i
risultati verificabili manualmente.
"""

from __future__ import annotations

import argparse
import csv
import re
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, sync_playwright

PICKUP_LOCATION = "Milano Linate Airport"
PICKUP_DATE = "15/09/2026"
RETURN_DATE = "22/09/2026"
PICKUP_TIME = "11:30"
RETURN_TIME = "15:00"

DOMAINS = [
    "https://www.sixt.de/",
    "https://www.sixt.fr/",
    "https://www.sixt.it/",
    "https://www.sixt.pt/",
    "https://www.sixt.es/",
    "https://www.sixt.at/",
    "https://www.sixt.ie/",
    "https://www.sixt.ch/",
    "https://www.sixt.nl/",
    "https://www.sixt.co.uk/",
]

COOKIE_BUTTONS = [
    "I agree",
    "Accetta tutto",
    "Accetta i cookie",
    "Accepter",
    "Acepto",
    "Einverstanden",
    "Eu concordo",
    "Ik ga akkoord",
]

LOCATION_PLACEHOLDERS = [
    "Airport, city or address",
    "Aeroporto, città o indirizzo",
    "Aéroport, ville ou adresse",
    "Aeropuerto, ciudad o dirección",
    "Flughafen, Stadt oder Adresse",
    "Luchthaven, stad of adres",
    "Aeroporto, cidade ou endereço",
]

SEARCH_BUTTONS = [
    "Show cars",
    "Mostra auto",
    "Voir les véhicule",
    "Mostrar coches",
    "Autos anzeigen",
    "Mostrar veículos",
    "Auto's weergeven",
]

CAR_KEYWORDS = [
    "or similar", "oder ähnlich", "ou similaire", "o simile", "o similar",
    "bmw", "audi", "mercedes", "volkswagen", "vw", "fiat", "peugeot",
    "renault", "citroen", "citroën", "ford", "opel", "toyota", "skoda",
    "mini", "seat", "hyundai", "kia", "nissan", "volvo",
    "automatic", "manual", "automatica", "manuale", "automatique",
    "suv", "sedan", "estate", "wagon", "compact", "intermediate",
]

BRAND_PATTERN = re.compile(
    r"\b(BMW|AUDI|PEUGEOT|MERCEDES|MERCEDES-BENZ|MAZDA|MINI|VW|VOLKSWAGEN|FIAT|RENAULT|TOYOTA|FORD|OPEL|SKODA|SEAT|HYUNDAI|KIA|NISSAN|VOLVO)\b",
    flags=re.I,
)
PRICE_PATTERN = re.compile(
    r"(?:€|EUR|£|GBP|CHF|USD)\s?\d+[\d.,]*|\d+[\d.,]*\s?(?:€|EUR|£|GBP|CHF|USD)",
    flags=re.I,
)


@dataclass(frozen=True)
class SearchConfig:
    pickup_location: str = PICKUP_LOCATION
    pickup_date_display: str = PICKUP_DATE
    return_date_display: str = RETURN_DATE
    pickup_time: str = PICKUP_TIME
    return_time: str = RETURN_TIME


def log(message: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {message}", flush=True)


def short_wait(page: Page, ms: int = 300) -> None:
    page.wait_for_timeout(ms)


def safe_click(locator, label: str, timeout_ms: int = 700) -> bool:
    try:
        locator.first.click(timeout=timeout_ms, force=True)
        log(f"OK click: {label}")
        return True
    except Exception as exc:
        log(f"SKIP click: {label} ({type(exc).__name__})")
        return False


def accept_cookies(page: Page) -> bool:
    log("Cerco popup cookie")
    for text in COOKIE_BUTTONS:
        try:
            button = page.get_by_role("button", name=text)
            if button.count() > 0 and safe_click(button, f"cookie button '{text}'", timeout_ms=600):
                short_wait(page, 250)
                return True
        except Exception:
            continue

    try:
        buttons = page.locator("button")
        for i in range(min(buttons.count(), 12)):
            try:
                button = buttons.nth(i)
                label = button.inner_text(timeout=180).strip()
                if label and any(word.lower() in label.lower() for word in COOKIE_BUTTONS):
                    if safe_click(button, f"cookie fallback '{label}'", timeout_ms=500):
                        short_wait(page, 250)
                        return True
            except Exception:
                continue
    except Exception as exc:
        log(f"Fallback cookie saltato: {type(exc).__name__}")

    log("Cookie non trovati o saltati")
    return False


def fill_first_matching_input(page: Page, terms: Iterable[str], value: str) -> bool:
    log(f"Cerco campo località per inserire: {value}")
    for term in terms:
        candidates = [
            (f"placeholder '{term}'", page.get_by_placeholder(term, exact=False)),
            (f"label '{term}'", page.get_by_label(term, exact=False)),
            (f"name contains '{term}'", page.locator(f"input[name*='{term}' i]")),
            (f"aria-label contains '{term}'", page.locator(f"input[aria-label*='{term}' i]")),
        ]
        for label, locator in candidates:
            try:
                first = locator.first
                if first.count() == 0:
                    continue
                first.click(timeout=700, force=True)
                first.fill(value, timeout=500)
                short_wait(page, 2500)
                page.keyboard.press("Enter")
                short_wait(page, 500)
                log(f"OK località compilata usando {label}")
                return True
            except Exception as exc:
                log(f"SKIP campo {label}: {type(exc).__name__}")
    log("Località non compilata automaticamente")
    return False


def click_first_visible_text(page: Page, texts: Iterable[str], timeout_ms: int = 700) -> bool:
    for text in texts:
        try:
            page.get_by_text(text, exact=False).first.click(timeout=timeout_ms, force=True)
            log(f"OK click testo: {text}")
            return True
        except Exception:
            continue
    log("Nessun testo cliccato tra: " + ", ".join(list(texts)[:6]))
    return False


def click_in_block(page: Page, testid: str, index: int, label: str) -> bool:
    try:
        block = page.locator(f"[data-testid='{testid}']")
        block.locator("button").nth(index).click(timeout=400, force=True)
        log(f"OK click {label}")
        short_wait(page, 400)
        return True
    except Exception as exc:
        log(f"SKIP click {label}: {type(exc).__name__}")
        return False


def date_display_to_iso(date_display: str) -> str:
    return datetime.strptime(date_display, "%d/%m/%Y").strftime("%Y-%m-%d")


def go_until_month_visible(page: Page, target_month: str, max_clicks: int = 12) -> bool:
    for attempt in range(max_clicks + 1):
        try:
            month = page.locator(f"time[datetime='{target_month}']").first
            if month.count() > 0 and month.is_visible(timeout=500):
                log(f"OK mese visibile: {target_month}")
                return True
        except Exception:
            pass

        try:
            next_button = page.locator(
                "[data-testid='rent-search-date-picker-overlay'] button[aria-label='Next']"
            ).first
            next_button.click(timeout=500, force=True)
            log(f"Click mese successivo: tentativo {attempt + 1}")
            short_wait(page, 500)
        except Exception as exc:
            log(f"Impossibile cliccare mese successivo: {type(exc).__name__}")
            return False
    return False


def click_calendar_date(page: Page, iso_date: str) -> bool:
    try:
        locator = page.locator(f"time[datetime='{iso_date}'] button[data-disabled='false']").first
        if locator.count() > 0:
            locator.scroll_into_view_if_needed(timeout=800)
            locator.click(timeout=400, force=True)
            log(f"OK selezionata data {iso_date}")
            short_wait(page, 400)
            return True
    except Exception as exc:
        log(f"SKIP data {iso_date}: {type(exc).__name__}")
    log(f"Data non trovata/cliccabile: {iso_date}")
    return False


def select_calendar_date(page: Page, iso_date: str) -> bool:
    return go_until_month_visible(page, iso_date[:7]) and click_calendar_date(page, iso_date)


def click_time_option(page: Page, wanted_time: str) -> bool:
    candidates = [
        page.get_by_text(wanted_time, exact=True),
        page.locator("button", has_text=wanted_time),
        page.locator("[role='option']", has_text=wanted_time),
        page.locator("li", has_text=wanted_time),
    ]
    for locator in candidates:
        try:
            for i in range(min(locator.count(), 30)):
                item = locator.nth(i)
                if item.is_visible(timeout=300):
                    item.click(timeout=800, force=True)
                    log(f"OK selezionata ora {wanted_time}")
                    short_wait(page, 300)
                    return True
        except Exception:
            continue
    log(f"Ora {wanted_time} non trovata")
    return False


def fill_dates_and_times(page: Page, cfg: SearchConfig) -> None:
    log("Seleziono data/ora tramite calendario SIXT custom")
    pickup_iso = date_display_to_iso(cfg.pickup_date_display)
    return_iso = date_display_to_iso(cfg.return_date_display)

    if click_in_block(page, "rent-search-form-pickup-date-input", 0, "data ritiro"):
        select_calendar_date(page, pickup_iso)
    if click_in_block(page, "rent-search-form-pickup-date-input", 1, "ora ritiro"):
        click_time_option(page, cfg.pickup_time)
    if click_in_block(page, "rent-search-form-return-date-input", 0, "data restituzione"):
        select_calendar_date(page, return_iso)
    if click_in_block(page, "rent-search-form-return-date-input", 1, "ora restituzione"):
        click_time_option(page, cfg.return_time)


def parse_price_value(price: str) -> float | None:
    cleaned = re.sub(r"(EUR|GBP|CHF|USD|€|£)", "", price.upper(), flags=re.I)
    cleaned = cleaned.strip().replace(" ", "")
    if "," in cleaned and "." in cleaned:
        cleaned = cleaned.replace(".", "").replace(",", ".") if cleaned.rfind(",") > cleaned.rfind(".") else cleaned.replace(",", "")
    elif "," in cleaned:
        cleaned = cleaned.replace(".", "").replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None


def extract_prices_from_text(text: str) -> list[str]:
    prices = PRICE_PATTERN.findall(text)
    out: list[str] = []
    for price in prices:
        norm = " ".join(price.split())
        if norm not in out:
            out.append(norm)
    return out


def split_price(price: str) -> dict[str, str]:
    match = re.search(
        r"(€|EUR|£|GBP|CHF|USD)\s?(\d+[\d.,]*)|(\d+[\d.,]*)\s?(€|EUR|£|GBP|CHF|USD)",
        price,
        flags=re.I,
    )
    if not match:
        return {"currency": "", "value": "", "raw": price}
    return {
        "currency": match.group(1) or match.group(4),
        "value": match.group(2) or match.group(3),
        "raw": price,
    }


def choose_total_price(prices: list[str]) -> str:
    parsed = [(price, parse_price_value(price)) for price in prices]
    parsed = [(price, value) for price, value in parsed if value is not None]
    return max(parsed, key=lambda item: item[1])[0] if parsed else (prices[0] if prices else "")


def is_car_card_text(text: str) -> bool:
    lowered = text.lower()
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not PRICE_PATTERN.search(text):
        return False
    if len(lines) > 25 or len(text) > 1200:
        return False
    hard_non_car = [
        "mailand flughafen linate", "milan airport linate", "milano aeroporto linate",
        "la voiture idéale", "bis zu", "rabatt", "jusqu’à", "jusqu'a", "à partir de",
        "top-angebot", "empfohlen",
    ]
    if any(keyword in lowered for keyword in hard_non_car):
        return False
    return any(keyword in lowered for keyword in CAR_KEYWORDS) and any(
        BRAND_PATTERN.search(line) for line in lines[:8]
    )


def clean_car_name(text: str) -> str:
    noise = [
        "or similar", "o simile", "ou similaire", "oder ähnlich", "o similar",
        "select", "seleziona", "sélectionner", "auswählen", "scegli",
        "top-angebot", "empfohlen", "à partir de", "unbegrenzte kilometer",
    ]
    for line in [line.strip() for line in text.splitlines() if line.strip()][:12]:
        low = line.lower()
        if any(item in low for item in noise):
            continue
        if PRICE_PATTERN.search(line):
            continue
        if BRAND_PATTERN.search(line):
            return line
    return ""


def extract_available_cars(page: Page) -> list[dict[str, str]]:
    log("Estraggo tutte le auto disponibili con prezzi")
    selectors = [
        "[data-testid*='vehicle']",
        "[data-testid*='offer']",
        "[data-testid*='car']",
        "article",
        "li:has-text('€')",
        "div:has-text('€')",
    ]
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for selector in selectors:
        try:
            cards = page.locator(selector)
            count = min(cards.count(), 80)
            log(f"Controllo selector card '{selector}': {count} elementi")
        except Exception:
            continue

        for i in range(count):
            try:
                card = cards.nth(i)
                if not card.is_visible(timeout=250):
                    continue
                text = card.inner_text(timeout=1000).strip()
            except Exception:
                continue
            if not is_car_card_text(text):
                continue
            prices = extract_prices_from_text(text)
            if not prices:
                continue
            total_price = choose_total_price(prices)
            daily_price = split_price(prices[0])
            car_name = clean_car_name(text)
            key = (car_name, total_price)
            if key in seen:
                continue
            seen.add(key)
            rows.append({
                "auto": car_name,
                "valuta": daily_price["currency"],
                "prezzo_giornaliero": daily_price["value"],
                "prezzo_giornaliero_raw": daily_price["raw"],
                "prezzi_visibili_card": " | ".join(prices[:10]),
                "testo_card": " / ".join(text.splitlines()[:10])[:500],
            })

    if not rows:
        try:
            body_text = page.locator("body").inner_text(timeout=1500)
        except Exception:
            body_text = ""
        for price in extract_prices_from_text(body_text)[:20]:
            rows.append({
                "auto": "n/d",
                "valuta": "",
                "prezzo_giornaliero": "",
                "prezzo_giornaliero_raw": price,
                "prezzi_visibili_card": price,
                "testo_card": "fallback pagina intera",
            })
    log(f"Auto/prezzi estratti: {len(rows)}")
    return rows


def country_from_url(url: str) -> str:
    match = re.search(r"sixt\.([a-z.]+)", url)
    if not match:
        return url
    tld = match.group(1)
    return "uk" if tld == "co.uk" else tld.split(".")[-1]


def run_domain(page: Page, url: str, cfg: SearchConfig) -> list[dict[str, str]]:
    log(f"Apro sito: {url}")
    page.goto(url, wait_until="domcontentloaded", timeout=30000)
    short_wait(page, 3000)

    accept_cookies(page)
    filled_location = fill_first_matching_input(page, LOCATION_PLACEHOLDERS, cfg.pickup_location)
    short_wait(page, 500)
    fill_dates_and_times(page, cfg)
    short_wait(page, 500)

    log("Provo ad avviare la ricerca")
    clicked_search = click_first_visible_text(page, SEARCH_BUTTONS, timeout_ms=500)
    if clicked_search:
        try:
            log("Attendo caricamento risultati")
            page.wait_for_load_state("domcontentloaded", timeout=7000)
        except PlaywrightTimeoutError:
            log("Timeout caricamento risultati: continuo comunque")
    short_wait(page, 2500)

    output_rows: list[dict[str, str]] = []
    for row in extract_available_cars(page):
        output_rows.append({
            "paese": country_from_url(url),
            "url_finale": page.url,
            "location_compilata": str(filled_location),
            "ricerca_avviata": str(clicked_search),
            **row,
        })
    return output_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Apre e confronta ricerche SIXT su più domini.")
    parser.add_argument("--headed", action="store_true", help="Lascia il browser aperto alla fine.")
    parser.add_argument("--slow", type=int, default=500, help="Rallentamento azioni in ms.")
    parser.add_argument("--output", default="sixt_results.csv", help="File CSV di output.")
    args = parser.parse_args()

    cfg = SearchConfig()
    results: list[dict[str, str]] = []

    with sync_playwright() as playwright:
        log(f"Avvio browser, slow_mo={args.slow}ms")
        context = playwright.chromium.launch_persistent_context(
            user_data_dir="./chrome-profile",
            channel="chrome",
            headless=False,
            slow_mo=args.slow,
            locale="it-IT",
            viewport={"width": 1440, "height": 900},
        )
        context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        """)
        context.set_default_timeout(1200)

        try:
            for url in DOMAINS:
                page = context.new_page()
                try:
                    domain_rows = run_domain(page, url, cfg)
                except Exception as exc:
                    log(f"ERRORE su {url}: {type(exc).__name__}: {exc}")
                    domain_rows = [{
                        "paese": country_from_url(url),
                        "url_finale": page.url if page else "",
                        "location_compilata": "False",
                        "ricerca_avviata": "False",
                        "auto": "ERRORE",
                        "valuta": "",
                        "prezzo_giornaliero": "",
                        "prezzo_giornaliero_raw": "",
                        "prezzi_visibili_card": "",
                        "testo_card": str(exc),
                    }]
                results.extend(domain_rows)
                print(f"\n--- {url} ---")
                if domain_rows:
                    print(domain_rows[0].get("url_finale", ""))
                for row in domain_rows:
                    print(
                        f"- {row.get('auto') or 'n/d'} | "
                        f"{row.get('valuta') or ''} {row.get('prezzo_giornaliero') or 'n/d'} / giorno"
                    )
        finally:
            if results:
                output = Path(args.output)
                with output.open("w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=list(results[0].keys()))
                    writer.writeheader()
                    writer.writerows(results)
                log(f"CSV salvato in: {output.resolve()}")

            if args.headed:
                input("\nBrowser lasciato aperto. Premi INVIO qui per chiuderlo...")
            context.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Script fermato dall'utente")
