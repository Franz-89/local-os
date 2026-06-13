---
name: kb-ingest-chat
description: Usa questa skill quando l'utente incolla una conversazione, trascrizione, nota grezza o riassunto non strutturato e chiede di trasformarlo in conoscenza Markdown per la knowledge base. Attivala per condensare il contenuto, aggiornare file esistenti o creare pochi nuovi file strutturati senza salvare tutta la conversazione.
---

# KB Ingest Chat

## Quando usarla

Usa questa skill quando devi trasformare una conversazione, una trascrizione, una chat con AI o una nota lunga in uno o piu file Markdown utili per la knowledge base.

## Quando non usarla

Non usarla per piccoli aggiornamenti mirati a un singolo file: usa `kb-update-file`. Non usarla per creare una scheda gia chiara e autonoma: usa `kb-create-file`. Non usarla per archiviare integralmente una chat.

## Processo

1. Leggi il contenuto fornito e non salvarlo integralmente.
2. Condensa solo cio che e utile per la knowledge base.
3. Distingui:
   - informazioni operative;
   - idee;
   - decisioni;
   - preferenze;
   - risorse;
   - prossime azioni;
   - domande aperte;
   - informazioni da verificare.
4. Cerca file correlati nel repository quando possibile.
5. Preferisci aggiornare file esistenti se il contenuto appartiene a progetti, aree, idee, persone o risorse gia presenti.
6. Crea nuovi file solo quando il contenuto e distinto e non appartiene chiaramente a file esistenti.
7. Evita frammentazione inutile: raggruppa contenuti collegati nello stesso file quando ha senso.
8. Usa `da_verificare` per informazioni incerte.
9. Aggiorna sempre `updated` nei file modificati e mantieni `created`.
10. Aggiungi sempre una voce in `Changelog`.

## Separazione dei contenuti

- Stato attuale: cio che deve restare vero dopo l'aggiornamento.
- Decisioni: scelte prese, con data e motivazione.
- Idee: possibilita non ancora approvate.
- Prossime azioni: checklist concreta.
- Domande aperte: elementi da chiarire.
- Informazioni da verificare: elementi incerti marcati con `da_verificare`.

## Output atteso

Quando possibile, applica direttamente le modifiche al repository.

Alla fine fornisci un riepilogo in questo formato:

```text
File creati:
- percorso/file.md - motivo

File aggiornati:
- percorso/file.md - motivo

Informazioni incerte:
- punto da verificare

Prossime azioni:
- azione consigliata
```

Se il contenuto e troppo ambiguo per essere strutturato, aggiorna `00-inbox/raw-notes.md` con una nota condensata e una possibile destinazione.

