# AGENTS

Questa repository e una knowledge base personale in Markdown. Contiene note, progetti, aree, idee, persone, risorse, log e sintesi di conversazioni AI.

## Regole di modifica

- Non modificare contenuti personali senza istruzioni esplicite.
- Non inventare dati personali, decisioni, preferenze o relazioni.
- Preservare sempre il frontmatter YAML.
- Aggiornare sempre il campo `updated` quando si modifica un file con frontmatter.
- Mantenere lo stile Markdown esistente.
- Non introdurre dipendenze esterne.
- Non creare codice, script, database o framework se non richiesto.
- Se viene richiesto un aggiornamento, modificare i file esistenti invece di duplicarli.
- Se il contesto e ambiguo, creare una nota in `00-inbox/raw-notes.md` invece di inventare.

## Struttura attesa

- `00-inbox/`: note temporanee e non ancora strutturate.
- `10-areas/`: aree continuative.
- `20-projects/`: progetti attivi, in pausa o completati.
- `30-ideas/`: idee da valutare.
- `40-people/`: schede persona.
- `50-resources/`: risorse.
- `90-archive/`: contenuti archiviati.
- `templates/`: modelli da copiare.

## Aggiornamenti

Quando aggiorni un file:

1. Leggi il file prima di modificarlo.
2. Mantieni le sezioni esistenti quando possibile.
3. Inserisci le nuove informazioni nella sezione piu adatta.
4. Aggiorna `updated`.
5. Aggiungi una voce nel `Changelog`, se presente.
6. Lascia le informazioni incerte come incerte.

## Knowledge Base Skills

Questo repository contiene skill Codex in `.agents/skills/` per creare, aggiornare, condensare e validare file Markdown della knowledge base.

Quando lavori su contenuti della knowledge base:

- usa `kb-create-file` per creare nuovi file strutturati;
- usa `kb-update-file` per aggiornare file esistenti;
- usa `kb-ingest-chat` per trasformare conversazioni in conoscenza strutturata;
- usa `kb-choose-location` per decidere dove salvare un contenuto;
- usa `kb-validate-markdown` per controllare coerenza e qualita dei file.

Regole generali:

- non inventare informazioni;
- preserva il frontmatter YAML;
- mantieni `created` quando aggiorni un file;
- aggiorna sempre `updated`;
- aggiungi sempre una voce in `Changelog`;
- se il contesto e ambiguo, usa `00-inbox/raw-notes.md`;
- preferisci aggiornare file esistenti invece di duplicare contenuti.
