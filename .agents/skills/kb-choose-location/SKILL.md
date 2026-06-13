---
name: kb-choose-location
description: Usa questa skill quando Codex deve decidere dove salvare una nuova informazione nella knowledge base personale Markdown. Attivala per scegliere tra 10-areas, 20-projects, 30-ideas, 40-people, 50-resources, 00-inbox e 90-archive, preferendo file esistenti quando il contenuto e correlato.
---

# KB Choose Location

## Quando usarla

Usa questa skill quando devi proporre o decidere il percorso corretto per una nuova informazione, nota, idea, risorsa, persona, area, progetto o sintesi.

## Quando non usarla

Non usarla da sola per creare o aggiornare contenuti completi: dopo aver scelto il percorso, usa `kb-create-file` o `kb-update-file`. Non usarla per validare file gia scritti: usa `kb-validate-markdown`.

## Criteri di scelta

- Se ha obiettivi, stato, decisioni e prossime azioni: `20-projects/`.
- Se e un ambito continuo senza fine precisa: `10-areas/`.
- Se e una possibilita non ancora trasformata in progetto: `30-ideas/`.
- Se riguarda una persona: `40-people/`.
- Se riguarda libro, articolo, video, software, sito o fonte: `50-resources/`.
- Se e grezza, ambigua o incompleta: `00-inbox/raw-notes.md`.
- Se e conclusa o non piu attiva: `90-archive/`.

## Processo

1. Identifica il contenuto principale.
2. Cerca file esistenti simili o correlati.
3. Se c'e forte somiglianza, proponi l'aggiornamento del file esistente.
4. Se serve un nuovo file, scegli cartella e nome.
5. Usa nomi descrittivi, lowercase e con trattini.
6. Evita nomi generici.
7. Se mancano informazioni essenziali, usa `00-inbox/raw-notes.md`.

## Naming

Usare:

```text
nome-progetto.md
idea-titolo-breve.md
nome-persona.md
YYYY-MM-DD-titolo-breve.md
```

Evitare:

```text
note.md
varie.md
chat.md
test.md
```

## Output atteso

Restituisci o applica una scelta chiara:

```text
Percorso consigliato: `percorso/file.md`
Tipo: project | area | idea | person | resource | chat-summary
Motivo: spiegazione sintetica
Alternativa: `percorso/alternativo.md`, se utile
```

Se il contenuto appartiene a un file esistente, indica quel file come destinazione preferita.

