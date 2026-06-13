# Workflow: Da chat a knowledge base

Usa questo workflow per trasformare una conversazione in conoscenza strutturata.

## Passaggi

1. Recuperare o incollare la conversazione.
2. Fornire alla chat `.llm/system-context.md`.
3. Fornire il prompt `.llm/prompts/ingest-chat.md`.
4. Fornire eventuali file correlati gia esistenti.
5. Chiedere alla chat se il contenuto richiede creazione, aggiornamento o inbox.
6. Copiare il Markdown nel percorso suggerito.
7. Validare il risultato con `.llm/prompts/validate-markdown.md`.
8. Leggere il diff Git.
9. Fare commit.

## Controlli

- La conversazione non deve essere salvata integralmente.
- Le informazioni incerte devono essere marcate come `da_verificare`.
- I file aggiornati devono mantenere `created`.
- I file modificati devono aggiornare `updated` e `Changelog`.

