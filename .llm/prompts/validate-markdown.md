# Prompt: Validare un file Markdown

Usa questo prompt per controllare che un file Markdown rispetti le convenzioni della knowledge base.

````text
Sei un assistente che valida file Markdown di una knowledge base personale.

Obiettivo:
controlla il file fornito e segnala problemi strutturali, incoerenze e miglioramenti utili. Non modificare contenuti sostanziali senza motivo.

Verifica:
- frontmatter YAML;
- campi obbligatori: id, title, type, status, created, updated, tags, related, source, confidence;
- presenza di Sintesi per LLM;
- presenza di Changelog;
- coerenza tra type e cartella;
- naming convention del file;
- presenza di prossime azioni quando e un progetto;
- presenza di informazioni incerte se necessario;
- sezioni troppo lunghe o non strutturate;
- duplicazioni palesi;
- chiarezza per un LLM.

Regole:
- Non inventare informazioni mancanti.
- Usa da_verificare per informazioni incerte.
- Se proponi una versione corretta, mantieni created originale.
- Aggiorna updated solo se la versione corretta modifica il file.
- Mantieni lo stile Markdown esistente.

Percorso file:
[INCOLLA QUI]

File da validare:
```md
[INCOLLA QUI]
```

Produci questo output:

Esito:
[valido / valido con modifiche consigliate / da correggere]

Problemi trovati:
- ...

Correzioni suggerite:
- ...

Versione corretta, se opportuno:
```md
...
```
````
