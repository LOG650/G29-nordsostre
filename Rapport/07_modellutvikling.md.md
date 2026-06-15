# 7 Modellutvikling
Prosjektdata
      ↓
Sekvensiering
      ↓
Ressursallokering
      ↓
Kapasitetskontroll
      ↓
Risikovurdering
      ↓
Scenarioanalyse

## 7.1 Oversikt over modellen
Modellen er utviklet som en beslutningsstøtteprototype for ressursallokering i AXTech. Formålet er å undersøke hvordan begrenset engineeringkapasitet kan fordeles mellom parallelle prosjekter på en systematisk måte.

Modellen består av seks hovedtrinn:

Registrering av prosjektdata
Sekvensiering av prosjekter
Ressursallokering
Kapasitetskontroll
Risikovurdering
Scenarioanalyse
## 7.2 Datagrunnlag
Datagrunnlaget består av simulerte prosjekter basert på AXTechs markedsområder og produkttyper. Hvert prosjekt er tilordnet prioritet, frist og estimert engineeringbehov.

Tabell X viser prosjektporteføljen som brukes i modellen.
## 7.3 Sekvensieringslogikk
Prosjektene sorteres etter følgende kriterier:

Prosjektprioritet
Nærmeste frist
Kritisk prosjektfase

Denne sekvensieringen sikrer at kritiske prosjekter behandles før mindre kritiske prosjekter dersom kapasiteten er begrenset.
## 7.4 Ressursallokering
Etter sekvensiering fordeles tilgjengelig kapasitet mellom prosjektene.

Modellen tildeler kapasitet til ett prosjekt av gangen. Dersom tilgjengelig kapasitet er tilstrekkelig, mottar prosjektet full tildeling. Dersom kapasiteten ikke er tilstrekkelig, registreres manglende timer som grunnlag for risikovurdering.

Tabell X viser resultatet av ressursallokeringen.
## 7.5 Risikovurdering
Manglende kapasitet brukes som indikator på prosjektmessig risiko.

Prosjekter som mottar full kapasitet klassifiseres som lav risiko. Prosjekter med manglende timer klassifiseres som moderat eller høy risiko avhengig av omfanget av ressursmangelen.

Risikovurderingen brukes videre i scenarioanalysen.
## 7.6 Scenarioanalyse
For å undersøke effekten av ulike beslutningsstrategier analyseres tre scenarioer:

Scenario 1: Lik fordeling av kapasitet
Scenario 2: Prioritetsbasert sekvensiering
Scenario 3: Økt kapasitet

Scenarioene sammenlignes med hensyn til manglende timer, forsinkelsesrisiko og ressursutnyttelse.