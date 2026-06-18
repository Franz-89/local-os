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
Francesco vuole usare un NAS UGREEN 4800 Plus come server Jellyfin e come destinazione di backup per tutte le foto da Google Photos e per Google Drive. Il progetto riguarda la scelta e configurazione dello storage, con attenzione a capacita, affidabilita, espandibilita e uso multimediale. La valutazione attuale include un disco Seagate IronWolf NAS ST8000VN002 8TB 3.5" SATA3 come possibile disco iniziale.

## Stato attuale
Il NAS previsto e un UGREEN 4800 Plus. Gli usi principali indicati sono:

- server Jellyfin;
- backup completo delle foto da Google Photos;
- backup di Google Drive;
- archiviazione dati personale su NAS.

E in valutazione l'acquisto di un Seagate IronWolf NAS ST8000VN002 8TB 3.5" SATA3.

## Obiettivi
- Usare Jellyfin sul NAS per organizzare e riprodurre contenuti multimediali.
- Centralizzare sul NAS il backup delle foto oggi presenti su Google Photos.
- Centralizzare sul NAS il backup dei file presenti su Google Drive.
- Scegliere dischi adatti a uso NAS continuativo e possibilmente espandibili nel tempo.

## Decisioni prese
- 2026-06-18 - Il NAS scelto o in valutazione e UGREEN 4800 Plus.
- 2026-06-18 - Il NAS dovra supportare Jellyfin e backup da Google Photos e Google Drive.

## Idee aperte
- Valutare se partire con un singolo disco o con piu dischi in RAID/mirror.
- Valutare se 8 TB sono sufficienti o se conviene partire direttamente da 12 TB o 16 TB.
- Valutare una strategia di backup 3-2-1 per evitare che il NAS diventi l'unica copia dei dati.
- Valutare se usare dischi IronWolf, IronWolf Pro, Exos o alternative equivalenti.

## Prossime azioni
- [ ] Stimare lo spazio occupato attuale da Google Photos.
- [ ] Stimare lo spazio occupato attuale da Google Drive.
- [ ] Stimare la crescita annua prevista di foto, video e media Jellyfin.
- [ ] Decidere configurazione dischi: singolo disco, mirror/RAID1, RAID5/SHR-like o altra configurazione.
- [ ] Definire una copia di sicurezza esterna al NAS per i dati piu importanti.

## Vincoli e preferenze
- Il disco deve essere adatto a un NAS e a funzionamento continuativo.
- Lo storage deve supportare sia media server sia backup personali.
- Le foto e i documenti cloud sono dati importanti: non vanno considerati protetti solo perche presenti sul NAS.

## Informazioni importanti
- Modello NAS: UGREEN 4800 Plus.
- Servizio multimediale previsto: Jellyfin.
- Backup sorgenti cloud: Google Photos e Google Drive.
- Disco in valutazione: Seagate IronWolf NAS ST8000VN002 8TB 3.5" SATA3.

## Domande aperte
- Quanti bay del NAS verranno popolati inizialmente?
- Quanti TB occupano oggi Google Photos e Google Drive?
- Jellyfin verra usato soprattutto in Direct Play o servira transcoding, anche 4K?
- I backup saranno solo locali sul NAS o anche replicati su disco esterno/cloud secondario?

## Changelog
### 2026-06-18
- Creata scheda progetto per NAS UGREEN 4800 Plus con Jellyfin e backup Google Photos/Google Drive.
