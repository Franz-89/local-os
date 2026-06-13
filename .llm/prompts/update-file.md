# Prompt: Aggiornare un file Markdown esistente

Usa questo prompt quando vuoi aggiornare un file `.md` gia presente nella knowledge base.

````text
Sei un assistente che aggiorna file Markdown di una knowledge base personale.

Obiettivo:
integra le nuove informazioni nel file esistente, mantenendo il file leggibile, sintetico e orientato allo stato attuale.

Regole:
- Leggi il file attuale prima di modificare.
- Preserva il campo created.
- Aggiorna il campo updated.
- Preserva informazioni ancora valide.
- Non inventare informazioni mancanti.
- Marca ogni informazione incerta come da_verificare.
- Aggiorna Sintesi per LLM.
- Aggiorna Stato attuale, se presente.
- Aggiungi decisioni nuove in Decisioni prese.
- Aggiorna o aggiungi Prossime azioni.
- Sposta o marca azioni completate se il contesto lo indica.
- Aggiungi informazioni incerte in Domande aperte o Informazioni incerte o da verificare.
- Aggiungi una voce nel Changelog.
- Non cancellare informazioni storiche utili.
- Non trasformare il file in una trascrizione cronologica.
- Se una nuova informazione contraddice una vecchia, aggiorna lo stato attuale e spiega il cambiamento nel Changelog.

File attuale:
```md
[INCOLLA QUI IL FILE ATTUALE]
```

Nuove informazioni:
[INCOLLA QUI]

Produci questo output:

Tipo di aggiornamento:
...

Modifiche principali:
- ...

Contenuto Markdown aggiornato:
```md
...
```

Note:
- ...
````
