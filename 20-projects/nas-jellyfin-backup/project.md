---
id: project-nas-jellyfin-backup
title: NAS Jellyfin e backup cloud
type: project
status: draft
created: 2026-06-18
updated: 2026-06-18
tags:
  - nas
  - jellyfin
  - backup
  - google-photos
  - google-drive
  - ugreen
related: []
source:
  type: chat
  date: 2026-06-18
confidence: medium
---

# NAS Jellyfin e backup cloud

## Sintesi per LLM
Francesco vuole usare un NAS UGREEN 4800 Plus come server Jellyfin condiviso con la famiglia e come destinazione di backup per tutte le foto da Google Photos e per Google Drive. L'obiettivo a lungo termine e arrivare a una configurazione con 4 dischi da 8 TB, iniziando pero con l'acquisto di un solo disco per motivi di budget.

## Stato attuale
Il NAS previsto e un UGREEN 4800 Plus. Gli usi principali indicati sono:

- server Jellyfin condiviso con piu utenti della famiglia;
- backup completo delle foto da Google Photos;
- backup di Google Drive;
- archiviazione dati personale su NAS.

La strategia attuale prevede di iniziare con un singolo Seagate IronWolf NAS ST8000VN002 8TB 3.5 SATA3 e aggiungere progressivamente altri dischi fino a raggiungere una configurazione da 4 x 8 TB.

## Obiettivi
- Usare Jellyfin sul NAS per organizzare e riprodurre contenuti multimediali.
- Condividere Jellyfin con membri della famiglia tramite account separati.
- Centralizzare sul NAS il backup delle foto oggi presenti su Google Photos.
- Centralizzare sul NAS il backup dei file presenti su Google Drive.
- Scegliere dischi adatti a uso NAS continuativo e possibilmente espandibili nel tempo.

## Decisioni prese
- 2026-06-18 - Il NAS scelto o in valutazione e UGREEN 4800 Plus.
- 2026-06-18 - Il NAS dovra supportare Jellyfin e backup da Google Photos e Google Drive.
- 2026-06-18 - Obiettivo finale: configurazione con 4 dischi da 8 TB.
- 2026-06-18 - Acquisto iniziale previsto: un solo disco da 8 TB, con espansione graduale successiva.

## Idee aperte
- Valutare il momento migliore per passare da disco singolo a configurazione ridondante.
- Valutare una strategia di backup 3-2-1 per evitare che il NAS diventi l'unica copia dei dati.
- Valutare se usare dischi IronWolf, IronWolf Pro, Exos o alternative equivalenti.

## Prossime azioni
- [ ] Stimare lo spazio occupato attuale da Google Photos.
- [ ] Stimare lo spazio occupato attuale da Google Drive.
- [ ] Stimare la crescita annua prevista di foto, video e media Jellyfin.
- [ ] Pianificare l'aggiunta progressiva dei quattro dischi.
- [ ] Definire una copia di sicurezza esterna al NAS per i dati piu importanti.

## Vincoli e preferenze
- Il disco deve essere adatto a un NAS e a funzionamento continuativo.
- Lo storage deve supportare sia media server sia backup personali.
- Jellyfin deve poter essere utilizzato da piu utenti della famiglia.
- Le foto e i documenti cloud sono dati importanti: non vanno considerati protetti solo perche presenti sul NAS.
- L'investimento nei dischi verra distribuito nel tempo.

## Informazioni importanti
- Modello NAS: UGREEN 4800 Plus.
- Servizio multimediale previsto: Jellyfin.
- Utilizzo Jellyfin: condivisione con la famiglia e utenti multipli.
- Backup sorgenti cloud: Google Photos e Google Drive.
- Strategia storage finale: 4 x 8 TB.
- Disco iniziale previsto: Seagate IronWolf NAS ST8000VN002 8TB 3.5 SATA3.

## Domande aperte
- Quanti TB occupano oggi Google Photos e Google Drive?
- Jellyfin verra usato soprattutto in Direct Play o servira transcoding, anche 4K?
- I backup saranno solo locali sul NAS o anche replicati su disco esterno/cloud secondario?

## Changelog
### 2026-06-18
- Creata scheda progetto per NAS UGREEN 4800 Plus con Jellyfin e backup Google Photos/Google Drive.
- Aggiunta strategia di crescita verso 4 dischi da 8 TB e condivisione Jellyfin con la famiglia.
