# Personal Knowledge Base

Questa repository contiene una knowledge base personale in Markdown, pensata per essere letta, modificata e versionata con Git. Serve a raccogliere progetti, idee, decisioni, note operative, riferimenti e sintesi di conversazioni con AI.

I file sono scritti per essere comprensibili sia da una persona sia da un LLM. Ogni contenuto dovrebbe essere aggiornabile manualmente sostituendo o modificando file Markdown, senza database, framework o dipendenze esterne.

## Organizzazione

- `00-inbox/`: note grezze non ancora strutturate.
- `10-areas/`: aree continue della vita, del lavoro o dello studio.
- `20-projects/`: progetti con obiettivi, decisioni, log, idee e riferimenti.
- `30-ideas/`: idee non ancora trasformate in progetto.
- `40-people/`: schede su persone rilevanti, solo se utile e consentito.
- `50-resources/`: libri, tool, articoli, documenti e altre fonti.
- `90-archive/`: contenuti chiusi o non piu attivi.
- `templates/`: modelli Markdown da copiare per creare nuovi file.

## Workflow consigliato

1. Conversare con un modello AI.
2. Chiedere al modello di riassumere la conversazione usando il prompt in `templates/chat-summary-template.md`.
3. Decidere se creare un nuovo file o aggiornarne uno esistente.
4. Copiare il Markdown nel file corretto.
5. Fare commit su Git.

## Uso con chat AI normali

La cartella `.llm/` contiene prompt e workflow portabili per usare questa knowledge base con chat AI normali, anche quando non supportano direttamente le skill Codex.

Per iniziare, fornire alla chat:

- `.llm/system-context.md`
- il prompt piu adatto da `.llm/prompts/`
- i file Markdown rilevanti da creare, aggiornare o analizzare

Le Codex Skills in `.agents/skills/` sono pensate per agenti compatibili con Codex, mentre `.llm/` e pensata per qualsiasi LLM.

## Salvare una nuova conversazione

1. Chiedere al modello AI una sintesi strutturata usando `templates/chat-summary-template.md`.
2. Salvare la sintesi in un file dedicato, se deve restare consultabile.
3. Aggiornare i file gia esistenti se la conversazione contiene informazioni su progetti, aree, decisioni o prossime azioni.
4. Inserire le informazioni incerte in una sezione dedicata o in `00-inbox/raw-notes.md`.

Esempi di destinazione:

- Nuova sintesi: `00-inbox/YYYY-MM-DD-titolo-breve.md`
- Aggiornamento progetto: `20-projects/nome-progetto/project.md`
- Nuova idea: `30-ideas/idea-titolo-breve.md`

## Aggiornare un file esistente

Quando aggiorni un file:

- modifica il contenuto esistente invece di duplicarlo;
- aggiorna il campo `updated` nel frontmatter YAML, se presente;
- aggiungi una voce sintetica nel `Changelog`;
- mantieni separate decisioni, idee, azioni e storico;
- non trasformare informazioni incerte in fatti.

## Convenzioni di naming

Usare nomi descrittivi, brevi e stabili:

```text
nome-progetto.md
idea-titolo-breve.md
nome-persona.md
YYYY-MM-DD-titolo-breve.md
```

Evitare nomi generici:

```text
note.md
varie.md
chat.md
test.md
```

Usare lettere minuscole, trattini tra parole e niente spazi nei nomi file.

## Tipi di contenuto

- `project`: progetto con obiettivi e prossime azioni.
- `area`: area continua della vita o del lavoro.
- `idea`: intuizione o possibilita da valutare.
- `person`: persona rilevante.
- `resource`: fonte, tool, libro, articolo o documento.
- `chat-summary`: sintesi di una conversazione.

## Stati

- `draft`: bozza.
- `active`: attivo.
- `paused`: in pausa.
- `completed`: completato.
- `archived`: archiviato.

## Link interni

Usare link Markdown o wiki-link coerenti con lo stile del file:

```md
[Progetto esempio](20-projects/example-project/project.md)
[[20-projects/example-project/project.md]]
```

Preferire percorsi relativi chiari quando il file deve essere letto anche fuori da editor specializzati.

## Regole di commit consigliate

Fare commit piccoli e leggibili. Esempi:

```text
docs: add idea about note workflow
docs: update smart home area
docs: record project decision
docs: archive completed project
```

Prima del commit, controllare che:

- i file modificati siano nel percorso corretto;
- il campo `updated` sia aggiornato;
- le informazioni incerte siano marcate come tali;
- non siano stati inseriti dati personali non necessari.

## Esempi di percorsi

- `10-areas/lavoro.md`
- `20-projects/example-project/project.md`
- `20-projects/example-project/decisions.md`
- `30-ideas/example-idea.md`
- `50-resources/libri.md`
- `00-inbox/raw-notes.md`
