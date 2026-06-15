---
id: resource-sixt-price-comparison-script
title: Script confronto prezzi SIXT multi-nazionalita
type: resource
status: active
created: 2026-06-15
updated: 2026-06-15
tags:
  - sixt
  - autonoleggio
  - playwright
  - script
  - travel
related:
  - 50-resources/scripts/sixt_compare.py
source: user_upload
confidence: high
---

# Script confronto prezzi SIXT multi-nazionalita

## Sintesi

Script Python pensato per confrontare i prezzi di noleggio auto SIXT aprendo diversi domini nazionali del sito SIXT e cercando la stessa combinazione di localita, date e orari.

Lo scopo e verificare se, a parita di ricerca, le pagine nazionali di SIXT mostrano prezzi diversi.

File collegato: [`50-resources/scripts/sixt_compare.py`](scripts/sixt_compare.py)

## Cosa fa

- Apre in sequenza piu domini SIXT nazionali.
- Prova ad accettare i cookie usando etichette in piu lingue.
- Prova a compilare il campo localita con `Milano Linate Airport`.
- Prova a selezionare date e orari tramite il calendario custom di SIXT.
- Avvia la ricerca auto.
- Estrae tutte le auto/prezzi visibili che riconosce come card veicolo.
- Salva i risultati in un file CSV.
- Stampa a terminale un riepilogo per dominio.

## Configurazione attuale nello script

- Localita ritiro: `Milano Linate Airport`
- Data ritiro: `15/09/2026`
- Data restituzione: `22/09/2026`
- Ora ritiro: `11:30`
- Ora restituzione: `15:00`
- Browser: Chromium via Playwright, canale Chrome
- Lingua browser: `it-IT`
- Output default: `sixt_results.csv`

Nota: nella docstring originale e indicato agosto 2026, mentre le costanti operative dello script usano settembre 2026. Per l'esecuzione contano le costanti `PICKUP_DATE` e `RETURN_DATE`.

## Domini confrontati

Lo script confronta questi domini SIXT:

- `sixt.de`
- `sixt.fr`
- `sixt.it`
- `sixt.pt`
- `sixt.es`
- `sixt.at`
- `sixt.ie`
- `sixt.ch`
- `sixt.nl`
- `sixt.co.uk`

## Dipendenze

Richiede Python e Playwright.

Installazione tipica:

```bash
pip install playwright
playwright install chrome
```

Lo script usa `playwright.sync_api` e avvia un contesto persistente con profilo locale `./chrome-profile`.

## Esecuzione

Esecuzione base:

```bash
python 50-resources/scripts/sixt_compare.py
```

Output CSV personalizzato:

```bash
python 50-resources/scripts/sixt_compare.py --output sixt_results.csv
```

Browser lasciato aperto alla fine:

```bash
python 50-resources/scripts/sixt_compare.py --headed
```

Rallentamento azioni:

```bash
python 50-resources/scripts/sixt_compare.py --slow 800
```

## Output CSV

Il CSV contiene, quando disponibili, colonne come:

- `paese`: dominio/nazione SIXT usata.
- `url_finale`: URL finale dopo la ricerca.
- `location_compilata`: indica se la localita e stata compilata automaticamente.
- `ricerca_avviata`: indica se il click di ricerca e stato eseguito.
- `auto`: nome/modello riconosciuto.
- `valuta`: valuta trovata nella card.
- `prezzo_giornaliero`: primo prezzo rilevato nella card.
- `prezzo_giornaliero_raw`: prezzo giornaliero come testo grezzo.
- `prezzi_visibili_card`: prezzi visibili nella card.
- `testo_card`: estratto testuale della card usato per debug.

## Come riconosce auto e prezzi

Lo script cerca blocchi pagina che contengano:

- un prezzo in valuta riconosciuta, per esempio `EUR`, `€`, `GBP`, `£`, `CHF`, `USD`;
- segnali testuali da card auto, come brand o parole tipo `or similar`, `automatic`, `manual`, `SUV`, ecc.;
- un modello/brand riconoscibile tra BMW, Audi, Mercedes, Volkswagen, Fiat, Peugeot, Renault, Ford, Opel, Toyota, Skoda, Mini, Seat, Hyundai, Kia, Nissan, Volvo.

Per evitare falsi positivi scarta blocchi troppo lunghi e alcuni testi promozionali o sezioni generiche della pagina.

## Limiti noti

- I siti SIXT possono cambiare DOM, testi, data-testid e flusso di prenotazione.
- L'automazione puo fallire se il popup cookie, il campo localita, il calendario o il bottone ricerca cambiano.
- L'estrazione prezzi e euristica: non garantisce che il prezzo scelto sia sempre il prezzo totale finale.
- Lo script non finalizza prenotazioni e non seleziona optional.
- Lo script e pensato per confronto assistito, non per scraping robusto o produzione.
- La docstring cita un seggiolino per bimbo, ma nello script attuale non risulta una selezione automatica dell'optional seggiolino.

## Informazioni utili per future richieste AI

Quando serve recuperare informazioni su questo script, considerare questi punti:

- E un tool personale per confrontare prezzi SIXT tra domini nazionali.
- La fonte tecnica principale e `50-resources/scripts/sixt_compare.py`.
- Questa scheda serve come descrizione consultabile: scopo, dipendenze, esecuzione, output, limiti e configurazione.
- Se bisogna modificarlo, controllare prima le costanti iniziali (`PICKUP_LOCATION`, `PICKUP_DATE`, `RETURN_DATE`, `PICKUP_TIME`, `RETURN_TIME`, `DOMAINS`).
- Se bisogna analizzare risultati, partire dal CSV generato (`sixt_results.csv` o file passato con `--output`).

## Changelog

- 2026-06-15: creata scheda documentale per lo script di confronto prezzi SIXT.
