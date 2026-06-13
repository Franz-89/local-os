---
name: kb-validate-markdown
description: Usa questa skill quando l'utente chiede di controllare, validare, revisionare o correggere file Markdown della knowledge base personale. Attivala per verificare frontmatter YAML, campi obbligatori, sezioni Sintesi per LLM e Changelog, coerenza tipo-cartella, naming convention, duplicazioni e struttura leggibile.
---

# KB Validate Markdown

## Quando usarla

Usa questa skill per controllare che uno o piu file `.md` rispettino le convenzioni della knowledge base.

## Quando non usarla

Non usarla per creare nuovi file: usa `kb-create-file`. Non usarla per aggiornare contenuti sostanziali da nuove informazioni: usa `kb-update-file` o `kb-ingest-chat`.

## Verifiche

Controlla:

1. presenza del frontmatter YAML;
2. presenza di `id`;
3. presenza di `title`;
4. presenza di `type`;
5. presenza di `status`;
6. presenza di `created`;
7. presenza di `updated`;
8. presenza di `tags`;
9. presenza di `related`;
10. presenza di `source`;
11. presenza di `confidence`;
12. presenza di `Sintesi per LLM`;
13. presenza di `Changelog`;
14. coerenza tra tipo file e cartella;
15. naming convention del file;
16. assenza di contenuti palesemente duplicati;
17. assenza di sezioni troppo lunghe o non strutturate.

## Correzioni consentite

Puoi correggere automaticamente piccoli errori strutturali:

- campo `updated` mancante;
- sezione `Changelog` mancante;
- titolo non coerente;
- tag vuoti;
- formattazione Markdown rotta;
- frontmatter incompleto quando il valore corretto e deducibile dal file.

## Correzioni da proporre

Per modifiche piu profonde, proponi prima le modifiche invece di applicarle:

- riorganizzazione sostanziale del contenuto;
- cancellazione o fusione di sezioni;
- deduplicazione non ovvia;
- cambio di tipo;
- spostamento in altra cartella;
- interpretazione di informazioni personali ambigue.

## Regole

- Non inventare informazioni mancanti.
- Usa `da_verificare` per contenuti incerti.
- Preserva frontmatter YAML esistente quando possibile.
- Mantieni `created` originale.
- Aggiorna `updated` solo se modifichi il file.
- Aggiungi una voce in `Changelog` solo se applichi correzioni.
- Mantieni modifiche minimali e leggibili.

## Output atteso

Se applichi correzioni, riepiloga:

```text
File corretti:
- percorso/file.md - correzione applicata

Problemi residui:
- punto da risolvere manualmente
```

Se fai solo una revisione, riepiloga:

```text
Problemi trovati:
- percorso/file.md - descrizione

Correzioni consigliate:
- intervento consigliato
```

