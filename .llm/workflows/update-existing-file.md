# Workflow: Aggiornare un file esistente

Usa questo workflow quando una nuova informazione appartiene a un file gia presente.

## Passaggi

1. Fornire alla chat il file attuale completo.
2. Fornire la nuova conversazione o nota.
3. Fornire `.llm/system-context.md`.
4. Usare `.llm/prompts/update-file.md`.
5. Controllare le modifiche proposte.
6. Verificare che `created` sia invariato.
7. Verificare che `updated` e `Changelog` siano aggiornati.
8. Sostituire il file nel repository.
9. Leggere il diff Git.
10. Fare commit.

## Controlli

- Il file deve descrivere lo stato attuale, non una cronologia lunga.
- Le decisioni nuove devono stare in `Decisioni prese`.
- Le idee devono restare separate dalle decisioni.
- Le azioni devono essere concrete e verificabili.

