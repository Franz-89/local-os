# Workflow: Creare un nuovo progetto

Usa questo workflow per aggiungere un nuovo progetto alla knowledge base.

## Passaggi

1. Definire obiettivo del progetto.
2. Raccogliere stato iniziale, vincoli, decisioni note e prossime azioni.
3. Fornire `.llm/system-context.md`.
4. Usare `.llm/prompts/create-file.md`.
5. Scegliere un percorso in `20-projects/`.
6. Creare `project.md`.
7. Eventualmente creare:
   - `decisions.md`;
   - `log.md`;
   - `ideas.md`;
   - `references.md`.
8. Validare con `.llm/prompts/validate-markdown.md`.
9. Leggere il diff Git.
10. Fare commit.

## Controlli

- Il progetto deve avere obiettivi e prossime azioni.
- Le informazioni mancanti non devono essere inventate.
- I punti incerti devono essere marcati come `da_verificare`.
- Il nome cartella deve essere descrittivo, lowercase e con trattini.

