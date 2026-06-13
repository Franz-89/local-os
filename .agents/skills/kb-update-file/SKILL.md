---
name: kb-update-file
description: Usa questa skill quando l'utente fornisce nuove informazioni per aggiornare un file Markdown esistente della knowledge base personale. Attivala per aggiornare stato, sintesi, decisioni, idee, prossime azioni, domande aperte, informazioni da verificare e changelog preservando frontmatter YAML e created.
---

# KB Update File

## Quando usarla

Usa questa skill quando il contenuto fornito appartiene a un file `.md` gia presente nella knowledge base, soprattutto per progetti, aree, idee, persone, risorse o sintesi gia esistenti.

## Quando non usarla

Non usarla per creare una nuova scheda se non esiste un file correlato: usa `kb-create-file`. Non usarla per trasformare una conversazione lunga in piu aggiornamenti: usa prima `kb-ingest-chat`. Non usarla per controlli generali di coerenza: usa `kb-validate-markdown`.

## Processo

1. Leggi il file esistente prima di modificarlo.
2. Preserva il frontmatter YAML.
3. Mantieni il valore originale di `created`.
4. Aggiorna sempre `updated` alla data dell'intervento.
5. Aggiorna `Sintesi per LLM` in modo che rifletta lo stato attuale.
6. Se il file e un progetto, aggiorna `Stato attuale`.
7. Aggiungi nuove decisioni in `Decisioni prese` con data e motivazione.
8. Aggiungi nuove idee in `Idee aperte`, senza trattarle come decisioni.
9. Aggiorna `Prossime azioni` con checklist concrete.
10. Se emerge che una azione e completata, marcala come completata o spostala in una sezione coerente se esiste.
11. Inserisci informazioni incerte in `Domande aperte` o `Informazioni incerte o da verificare`, usando `da_verificare`.
12. Aggiungi sempre una voce sintetica in `Changelog`.

## Regole

- Non cancellare informazioni vecchie se non sono chiaramente superate.
- Se una nuova informazione contraddice una vecchia, aggiorna lo stato attuale e spiega il cambiamento nel `Changelog`.
- Evita duplicazioni: un'informazione deve comparire nella sezione piu adatta.
- Non trasformare il file in una cronologia lunga.
- Il file deve rappresentare lo stato attuale della conoscenza, con storico sintetico nel `Changelog`.
- Non inventare informazioni mancanti.
- Mantieni modifiche minimali, leggibili e coerenti con lo stile esistente.

## Output atteso

Applica modifiche effettive al file esistente quando l'aggiornamento e chiaro.

Se il file da aggiornare non e chiaro, non creare duplicati: aggiungi una nota in `00-inbox/raw-notes.md` con possibile destinazione e punti `da_verificare`.

