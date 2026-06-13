---
name: kb-create-file
description: Usa questa skill quando l'utente chiede di creare un nuovo file Markdown strutturato nella knowledge base personale, inclusi project, area, idea, person, resource o chat-summary. Attivala anche quando il contenuto fornito deve diventare una nuova scheda con frontmatter YAML, sezioni standard, percorso corretto e changelog.
---

# KB Create File

## Quando usarla

Usa questa skill quando devi creare un nuovo file `.md` della knowledge base a partire da informazioni fornite dall'utente, da una nota breve o da una sintesi gia condensata.

Tipi supportati:

- `project`
- `area`
- `idea`
- `person`
- `resource`
- `chat-summary`

## Quando non usarla

Non usarla quando il contenuto aggiorna chiaramente un file esistente: in quel caso usa `kb-update-file`. Non usarla per validare file gia presenti: usa `kb-validate-markdown`. Non creare file nuovi se il contesto e ambiguo o incompleto: usa `00-inbox/raw-notes.md`.

## Processo

1. Analizza il contenuto fornito e separa fatti, decisioni, idee, azioni, risorse e informazioni incerte.
2. Cerca file esistenti correlati prima di creare un nuovo file.
3. Scegli il tipo corretto:
   - obiettivi, stato, decisioni, prossime azioni: `project`;
   - ambito continuo senza fine precisa: `area`;
   - possibilita non ancora trasformata in progetto: `idea`;
   - persona rilevante: `person`;
   - libro, articolo, video, software, sito o fonte: `resource`;
   - sintesi di conversazione: `chat-summary`.
4. Scegli il percorso piu adatto:
   - `10-areas/`
   - `20-projects/`
   - `30-ideas/`
   - `40-people/`
   - `50-resources/`
   - `00-inbox/`
   - `90-archive/`
5. Usa un nome file descrittivo, lowercase e con trattini.
6. Crea frontmatter YAML valido con `id`, `title`, `type`, `status`, `created`, `updated`, `tags`, `related`, `source`, `confidence`.
7. Usa un `id` leggibile e stabile, derivato dal tipo e dal titolo.
8. Compila le sezioni usando i template in `templates/` quando disponibili.
9. Inserisci `da_verificare` per ogni informazione incerta.
10. Aggiungi sempre una voce in `Changelog`.

## Regole

- Non inventare informazioni personali mancanti.
- Non inserire dettagli non forniti dall'utente o gia presenti nella repository.
- Preserva lo stile Markdown della knowledge base.
- Preferisci aggiornare file esistenti quando il contenuto appartiene a un progetto o area gia presente.
- Se non e chiaro dove salvare il contenuto, non creare una scheda definitiva.

## Gestione contenuto ambiguo

Se il percorso o il tipo non sono chiari, aggiungi una nota in `00-inbox/raw-notes.md` con una sezione:

```md
### YYYY-MM-DD - Titolo breve
- Nota grezza.
- Informazioni da_verificare:
  - Punto incerto.
- Possibile destinazione: `percorso/file.md`
```

## Output atteso

Quando il contesto e chiaro, applica modifiche effettive al repository creando il file Markdown corretto.

Quando il contesto non e chiaro, aggiorna `00-inbox/raw-notes.md` e segnala la possibile destinazione senza inventare dettagli.

