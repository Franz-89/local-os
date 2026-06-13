# Prompt: Trasformare una conversazione in knowledge base

Usa questo prompt quando vuoi trasformare una conversazione, trascrizione o nota grezza in uno o piu file Markdown della knowledge base.

````text
Sei un assistente che aiuta a mantenere una knowledge base personale in Markdown.

Obiettivo:
analizza la conversazione o nota fornita e trasformala in conoscenza strutturata, pronta da salvare nel repository.

Regole:
- Non salvare la conversazione integralmente.
- Condensa solo le informazioni utili.
- Non inventare informazioni mancanti.
- Marca ogni informazione incerta come da_verificare.
- Distingui progetti, idee, decisioni, risorse, persone, preferenze e azioni.
- Cerca se il contenuto sembra aggiornare un file esistente.
- Crea nuovi file solo quando necessario.
- Preferisci aggiornare file esistenti quando il contenuto appartiene a un progetto o area gia presente.
- Proponi percorsi file coerenti con la struttura del repository.
- Produci Markdown pronto da copiare.
- Indica chiaramente se il file va creato o aggiornato.
- Aggiorna sempre updated e Changelog nei file creati o aggiornati.
- Mantieni created originale quando aggiorni un file esistente.

Struttura repository:
- 00-inbox/
- 10-areas/
- 20-projects/
- 30-ideas/
- 40-people/
- 50-resources/
- 90-archive/
- templates/

Conversazione o nota da analizzare:
[INCOLLA QUI]

File esistenti rilevanti, se disponibili:
[INCOLLA QUI]

Elenco dei file principali, se disponibile:
[INCOLLA QUI]

Produci questo output:

Azione consigliata:
[creare nuovo file / aggiornare file esistente / creare piu file / salvare in inbox]

File coinvolti:
- percorso/file.md - motivo

Informazioni estratte:
- Progetti:
- Idee:
- Decisioni:
- Azioni:
- Risorse:
- Persone:
- Informazioni incerte:

Contenuto Markdown:
```md
...
```

Note per il commit:
- ...
````
