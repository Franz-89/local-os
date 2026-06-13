# AI Context

Questo file contiene istruzioni generali per ogni LLM che consulta o aiuta ad aggiornare questa knowledge base.

## Scopo della knowledge base

La repository serve a mantenere una memoria personale strutturata in Markdown: progetti, aree, idee, decisioni, log, persone, risorse, conversazioni e prossime azioni.

L'obiettivo non e generare contenuto creativo non richiesto, ma organizzare e aggiornare informazioni fornite dall'utente o gia presenti nei file.

## Regole per l'AI

- Non inventare dati personali, preferenze, eventi, persone, date o decisioni.
- Se una informazione non e presente o non e chiara, dichiararla come incerta.
- Preferire aggiornamenti puntuali a nuove duplicazioni.
- Conservare lo stile Markdown esistente.
- Mantenere separate informazioni attuali, decisioni, idee e storico.
- Non cancellare contenuti personali senza istruzioni esplicite.
- Usare esempi solo se chiaramente marcati come fittizi.

## Prompt portabili

La cartella `.llm/` contiene prompt e workflow pensati per chat AI normali.  
Quando un modello AI non puo usare direttamente le Codex Skills, deve usare i file in `.llm/` come istruzioni operative.

## Come interpretare i tipi di file

- `project`: contiene stato, obiettivi, decisioni, prossime azioni e informazioni operative di un progetto.
- `area`: contiene contesto stabile e ricorrente su un'area continua.
- `idea`: contiene possibilita non ancora validate o trasformate in progetto.
- `person`: contiene solo informazioni utili, rilevanti e appropriate su una persona.
- `resource`: contiene fonti, libri, tool, articoli, documenti o link utili.
- `chat-summary`: contiene una sintesi strutturata di una conversazione.

## Come aggiornare file esistenti

Quando viene richiesto un aggiornamento:

1. Individua il file piu adatto.
2. Modifica il file esistente invece di crearne uno duplicato.
3. Aggiorna il campo `updated` nel frontmatter YAML.
4. Inserisci nuove decisioni nella sezione decisioni.
5. Inserisci nuove azioni nella sezione prossime azioni.
6. Inserisci informazioni storiche nel changelog o nel log.
7. Mantieni le informazioni incerte in una sezione dedicata.

Se il file adatto non e chiaro, aggiungi una nota in `00-inbox/raw-notes.md`.

## Informazioni incerte

Le informazioni incerte devono essere:

- marcate come non confermate;
- accompagnate dalla fonte, se disponibile;
- escluse da sezioni che descrivono lo stato attuale;
- inserite in `Informazioni incerte o da verificare`, `Domande aperte` o `00-inbox/raw-notes.md`.

## Evitare invenzioni

Non dedurre dettagli personali da indizi incompleti. Non completare nomi, date, luoghi, relazioni o preferenze se non sono esplicitamente presenti.

Se serve un placeholder, usare testo generico come:

```md
- Da completare.
- Informazione non ancora confermata.
```

## Link interni Markdown

Usare link interni per collegare contenuti correlati:

```md
[Nome leggibile](../20-projects/example-project/project.md)
[[20-projects/example-project/project.md]]
```

Preferire percorsi relativi chiari quando il collegamento deve essere robusto anche fuori da editor specializzati.

## Distinzione tra contenuti

- Stato attuale: cio che e vero o valido adesso.
- Decisioni: scelte gia prese, con data e motivazione.
- Idee: possibilita non ancora decise.
- Storico: eventi, aggiornamenti e cambiamenti nel tempo.
- Prossime azioni: attivita concrete da fare.
