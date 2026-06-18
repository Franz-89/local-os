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
  - tailscale
related:
  - 10-areas/media-server-jellyfin.md
  - 20-projects/home-lab-smart-home/project.md
source:
  type: chat
  date: 2026-06-18
confidence: medium
---

# NAS Jellyfin e backup cloud

## Sintesi per LLM
Francesco vuole usare un NAS UGREEN NASync DXP4800 Plus come server Jellyfin condiviso con la famiglia e come destinazione di backup per tutte le foto da Google Photos e per Google Drive. Jellyfin dovrebbe essere accessibile anche dai familiari in Italia, probabilmente tramite Tailscale, con utenti separati sia su Jellyfin sia nella tailnet. L'obiettivo storage a lungo termine e arrivare a una configurazione con 4 dischi da 8 TB, iniziando pero con l'acquisto di un solo disco per motivi di budget.

## Stato attuale
Il NAS previsto e un UGREEN NASync DXP4800 Plus. Gli usi principali indicati sono:

- server Jellyfin condiviso con piu utenti della famiglia;
- backup completo delle foto da Google Photos;
- backup di Google Drive;
- archiviazione dati personale su NAS.

La strategia attuale prevede di iniziare con un singolo Seagate IronWolf NAS ST8000VN002 8TB 3.5 SATA3 e aggiungere progressivamente altri dischi fino a raggiungere una configurazione da 4 x 8 TB.

Per l'accesso remoto a Jellyfin e stata valutata l'installazione di Tailscale sul NAS e sui Fire TV Stick dei familiari, cosi da condividere il servizio tra l'abitazione principale e la casa dei genitori in Italia senza esporre direttamente il NAS su Internet.

## Obiettivi
- Usare Jellyfin sul NAS per organizzare e riprodurre contenuti multimediali.
- Condividere Jellyfin con membri della famiglia tramite account separati.
- Centralizzare sul NAS il backup delle foto oggi presenti su Google Photos.
- Centralizzare sul NAS il backup dei file presenti su Google Drive.
- Scegliere dischi adatti a uso NAS continuativo e possibilmente espandibili nel tempo.
- Rendere l'accesso remoto a Jellyfin semplice per la famiglia e limitato al servizio necessario.

## Decisioni prese
- 2026-06-18 - Il NAS scelto o in valutazione e UGREEN 4800 Plus.
- 2026-06-18 - Il NAS dovra supportare Jellyfin e backup da Google Photos e Google Drive.
- 2026-06-18 - Obiettivo finale: configurazione con 4 dischi da 8 TB.
- 2026-06-18 - Acquisto iniziale previsto: un solo disco da 8 TB, con espansione graduale successiva.
- 2026-06-18 - Per l'accesso familiare a Jellyfin e preferibile invitare i familiari nella tailnet con account Tailscale separati, invece di condividere un unico account.
- 2026-06-18 - Sono previsti utenti Jellyfin separati per ciascun familiare.

## Idee aperte
- Valutare il momento migliore per passare da disco singolo a configurazione ridondante.
- Valutare una strategia di backup 3-2-1 per evitare che il NAS diventi l'unica copia dei dati.
- Valutare se usare dischi IronWolf, IronWolf Pro, Exos o alternative equivalenti.
- Valutare ACL Tailscale per limitare l'accesso dei familiari al solo NAS/Jellyfin.

## Prossime azioni
- [ ] Stimare lo spazio occupato attuale da Google Photos.
- [ ] Stimare lo spazio occupato attuale da Google Drive.
- [ ] Stimare la crescita annua prevista di foto, video e media Jellyfin.
- [ ] Pianificare l'aggiunta progressiva dei quattro dischi.
- [ ] Definire una copia di sicurezza esterna al NAS per i dati piu importanti.
- [ ] Definire configurazione Tailscale per NAS e Fire TV Stick dei familiari.
- [ ] Verificare Direct Play sui client previsti, in particolare Fire TV Stick.

## Vincoli e preferenze
- Il disco deve essere adatto a un NAS e a funzionamento continuativo.
- Lo storage deve supportare sia media server sia backup personali.
- Jellyfin deve poter essere utilizzato da piu utenti della famiglia.
- Le foto e i documenti cloud sono dati importanti: non vanno considerati protetti solo perche presenti sul NAS.
- L'investimento nei dischi verra distribuito nel tempo.
- La connessione domestica FTTH ha upload considerato adeguato per piu streaming Full HD.
- I contenuti Jellyfin previsti sono principalmente Full HD, non 4K.
- Quando possibile va favorito Direct Play per ridurre la necessita di transcoding.

## Informazioni importanti
- Modello NAS: UGREEN NASync DXP4800 Plus, citato anche come UGREEN 4800 Plus.
- Servizio multimediale previsto: Jellyfin.
- Utilizzo Jellyfin: condivisione con la famiglia e utenti multipli, anche tra abitazione principale e casa dei genitori in Italia.
- Accesso remoto valutato: Tailscale su NAS e Fire TV Stick dei familiari.
- Backup sorgenti cloud: Google Photos e Google Drive.
- Strategia storage finale: 4 x 8 TB.
- Disco iniziale previsto: Seagate IronWolf NAS ST8000VN002 8TB 3.5 SATA3.
- Watchlist e contenuti da aggiungere a Jellyfin: `10-areas/media-server-jellyfin.md`.

## Domande aperte
- Quanti TB occupano oggi Google Photos e Google Drive?
- I backup saranno solo locali sul NAS o anche replicati su disco esterno/cloud secondario?
- Quali ACL Tailscale usare per consentire ai familiari l'accesso solo a Jellyfin/NAS?
- I Fire TV Stick disponibili supportano Direct Play per i formati principali della libreria?

## Changelog
### 2026-06-18
- Consolidate nel progetto le note su Tailscale, accesso familiare, Full HD, Direct Play e relazione con la watchlist Jellyfin.
- Creata scheda progetto per NAS UGREEN 4800 Plus con Jellyfin e backup Google Photos/Google Drive.
- Aggiunta strategia di crescita verso 4 dischi da 8 TB e condivisione Jellyfin con la famiglia.
