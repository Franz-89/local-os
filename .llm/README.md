# LLM Prompt Pack

La cartella `.llm/` contiene prompt, workflow e istruzioni operative per usare questa knowledge base con chat AI normali, anche quando non supportano Codex Skills.

I file sono pensati per essere copiati direttamente in una chat AI oppure letti da un modello che ha accesso al repository tramite connettore, progetto, workspace, MCP o integrazione simile.

## Contenuto

- `system-context.md`: contesto generale da fornire all'inizio di una sessione.
- `usage-guide.md`: guida pratica per usare la knowledge base con una chat AI.
- `prompts/`: prompt riutilizzabili per creare, aggiornare, validare e riassumere file.
- `workflows/`: procedure passo-passo per i casi d'uso piu comuni.

## Quando usare i prompt

Usa i prompt in `.llm/prompts/` quando vuoi:

- trasformare una conversazione in conoscenza strutturata;
- creare un nuovo file Markdown;
- aggiornare un file esistente;
- scegliere dove salvare una nuova informazione;
- validare un file della knowledge base;
- ottenere un riepilogo complessivo del repository.

## Differenza tra `.llm/` e `.agents/skills/`

- `.agents/skills/` contiene skill pensate per Codex o agenti compatibili.
- `.llm/` contiene prompt e workflow portabili, leggibili da qualsiasi modello AI.
- Una chat AI normale potrebbe non usare automaticamente le skill Codex, ma può leggere o ricevere i file in `.llm/`.

## Uso con chat AI normale

All'inizio della sessione, fornisci alla chat:

1. `.llm/system-context.md`;
2. il prompt piu adatto da `.llm/prompts/`;
3. i file Markdown rilevanti da creare, aggiornare o analizzare.

Chiedi alla chat di produrre Markdown pronto da copiare, senza inventare informazioni e marcando ogni informazione incerta come `da_verificare`.

## Se il repository e collegato alla chat

Chiedi alla chat di leggere:

- `AI_CONTEXT.md`;
- `.llm/system-context.md`;
- il prompt specifico in `.llm/prompts/`;
- eventuali file gia esistenti correlati.

Poi chiedi una proposta di modifica o il contenuto Markdown completo del file aggiornato.

## Se il repository non e collegato alla chat

Incolla manualmente:

- `.llm/system-context.md`;
- il prompt specifico;
- il contenuto del file da aggiornare, se esiste;
- l'elenco dei percorsi principali del repository;
- la nuova conversazione, nota o informazione da trasformare.

Verifica sempre il risultato prima di copiarlo nel repository e fare commit.

