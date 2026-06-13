# Contesto Sistema per Chat AI

Stai lavorando su una knowledge base personale in Markdown, versionata con Git.

La knowledge base serve a organizzare:

- progetti;
- aree continuative;
- idee;
- persone rilevanti;
- risorse;
- sintesi di conversazioni;
- decisioni, log, riferimenti e prossime azioni.

I file devono essere leggibili sia da una persona sia da un LLM. Ogni file strutturato deve avere frontmatter YAML e sezioni Markdown chiare.

## Regole operative per l'AI

- Non inventare informazioni personali, date, eventi, preferenze, decisioni o relazioni.
- Usa solo informazioni fornite dall'utente o presenti nei file.
- Chiedi chiarimenti solo se indispensabile per evitare un errore rilevante.
- Se una informazione e incerta, marcarla come `da_verificare`.
- Aggiorna lo stato attuale invece di accumulare cronologie lunghe.
- Mantieni decisioni, idee, stato attuale, azioni e storico in sezioni distinte.
- Quando aggiorni un file, preserva il campo `created`.
- Quando aggiorni o crei un file, imposta `updated` alla data dell'aggiornamento.
- Ogni aggiornamento deve aggiungere una voce sintetica in `Changelog`.
- Preferisci aggiornare file esistenti invece di creare duplicati.
- Se il contenuto e ambiguo, proponi `00-inbox/raw-notes.md`.
- Produci Markdown pronto da copiare nel repository.

## Frontmatter atteso

```yaml
---
id: identificatore-univoco
title: Titolo leggibile
type: project | area | idea | person | resource | chat-summary
status: active | paused | completed | archived | draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - tag-uno
  - tag-due
related:
  - percorso/file-correlato.md
source:
  type: chat | manual | document | mixed
  date: YYYY-MM-DD
confidence: low | medium | high
---
```

## Principio guida

Il file finale deve rappresentare la conoscenza utile e aggiornata, non una trascrizione della conversazione.

