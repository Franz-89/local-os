# Guida Uso con Chat AI

Questa guida spiega come usare la knowledge base con una chat AI normale.

## 1. Chat AI con accesso al repository

Se la chat puo leggere il repository:

1. Chiedi di leggere `.llm/system-context.md`.
2. Chiedi di leggere `AI_CONTEXT.md`.
3. Indica il prompt da usare in `.llm/prompts/`.
4. Indica i file rilevanti da aggiornare o analizzare.
5. Chiedi alla chat di proporre modifiche Markdown pronte da copiare.

## 2. Chat AI senza accesso al repository

Se la chat non puo leggere il repository:

1. Incolla `.llm/system-context.md`.
2. Incolla il prompt adatto.
3. Incolla il file Markdown da aggiornare, se esiste.
4. Incolla l'elenco dei file principali del repository.
5. Incolla la nuova conversazione, nota o richiesta.

## 3. File da fornire sempre

Quando possibile, fornire alla chat almeno:

- `.llm/system-context.md`
- `.llm/prompts/ingest-chat.md`
- `AI_CONTEXT.md`
- il file Markdown da aggiornare, se esiste
- l'elenco dei file principali del repository

## 4. Prompt per casi comuni

- Nuova conversazione da trasformare: `.llm/prompts/ingest-chat.md`
- Nuovo file: `.llm/prompts/create-file.md`
- Aggiornamento file esistente: `.llm/prompts/update-file.md`
- Scelta percorso: `.llm/prompts/choose-location.md`
- Validazione Markdown: `.llm/prompts/validate-markdown.md`
- Riepilogo repository: `.llm/prompts/summarize-repository.md`

## 5. Creare un nuovo file

1. Fornisci il contesto generale.
2. Usa `.llm/prompts/create-file.md`.
3. Specifica il tipo, se lo sai.
4. Chiedi un percorso consigliato e Markdown completo.
5. Copia il contenuto nel file suggerito.
6. Valida con `.llm/prompts/validate-markdown.md`.

## 6. Aggiornare un file esistente

1. Fornisci il file attuale completo.
2. Fornisci la nuova informazione o conversazione.
3. Usa `.llm/prompts/update-file.md`.
4. Verifica che `created` sia invariato.
5. Verifica che `updated` e `Changelog` siano aggiornati.
6. Sostituisci il file nel repository.

## 7. Trasformare una conversazione in knowledge base

1. Fornisci la conversazione o sintesi grezza.
2. Usa `.llm/prompts/ingest-chat.md`.
3. Chiedi se creare, aggiornare o salvare in inbox.
4. Copia il Markdown nei percorsi suggeriti.
5. Valida i file risultanti.

## 8. Verifica prima del commit

Prima di fare commit:

- controlla che non ci siano informazioni inventate;
- verifica che le informazioni incerte siano marcate come `da_verificare`;
- controlla `created`, `updated` e `Changelog`;
- verifica naming e percorso;
- leggi il diff Git.

