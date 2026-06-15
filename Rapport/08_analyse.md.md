# 8 Analyse og resultater

## 8.1 Prosjektportefølje
| Prosjekt | Fase | Prioritet | Frist | Behov |
|-----------|------|-----------|--------|--------|
| Offshore Wind Foundation Handling System | Engineering | Kritisk | 20.03.2026 | 480 |
| Subsea LARS System | Engineering | Kritisk | 28.03.2026 | 500 |
| Buoy Pull-In System | Detailed Design | Høy | 25.03.2026 | 360 |
| A-Frame Cable Lay System | Installation Prep | Høy | 05.04.2026 | 400 |
| Offshore Gangway System | Concept | Medium | 18.04.2026 | 310 |

Den simulerte prosjektporteføljen representerer typiske engineer-to-order-prosjekter som AXTech kan gjennomføre parallelt. Prosjektene varierer i kompleksitet, prioritet og ressursbehov, og konkurrerer om de samme engineeringressursene.


## 8.2 Resultater fra sekvensieringsmodellen
Offshore Wind
Subsea LARS
Buoy Pull-In
A-Frame
Offshore Gangway

Sekvensieringsmodellen prioriterte først prosjekter med kritisk prioritet. Deretter ble prosjekter med høy prioritet behandlet. Modellen sikret dermed at de mest forretningskritiske prosjektene fikk tilgang til engineeringkapasitet først.
## 8.3 Resultater fra ressursallokeringen
| Prosjekt         | Behov | Tildelt | Mangler |
| ---------------- | ----- | ------- | ------- |
| Offshore Wind    | 480   | 480     | 0       |
| Subsea LARS      | 500   | 500     | 0       |
| Buoy Pull-In     | 360   | 360     | 0       |
| A-Frame          | 400   | 160     | 240     |
| Offshore Gangway | 310   | 0       | 310     |


## 8.4 Flaskehalsanalyse
Analysen viser at engineeringkapasiteten representerer systemets primære flaskehals. Den totale kapasiteten på 1500 timer var utilstrekkelig til å dekke det samlede behovet på 2050 timer.

480 + 500 + 360 + 400 + 310 = 2050

2050 - 1500 = 550 timer mangler

## 8.5 Scenarioanalyse
## 8.5 Scenarioanalyse

Scenarioanalysen sammenligner tre ulike strategier for ressursfordeling. Formålet er å undersøke hvordan ulike beslutningsregler påvirker manglende kapasitet og antall prosjekter med forsinkelsesrisiko.

| Scenario | Kapasitet | Regel | Manglende timer | Prosjekter i risiko |
|---|---:|---|---:|---:|
| Scenario 1 | 1500 | Lik fordeling | 550 | 5 |
| Scenario 2 | 1500 | Prioritetsbasert sekvensiering | 550 | 2 |
| Scenario 3 | 2000 | Økt kapasitet og prioritering | 50 | 1 |

Scenario 1 viser at lik fordeling gir risiko i alle prosjektene. Selv om fordelingen kan fremstå rettferdig, gir den svak beslutningsstøtte fordi den ikke skiller mellom kritiske og mindre kritiske prosjekter.

Scenario 2 har samme totale kapasitetsmangel som scenario 1, men reduserer antall prosjekter med risiko fra fem til to. Dette viser at sekvensiering ikke nødvendigvis fjerner kapasitetsproblemet, men styrer hvilke prosjekter som rammes.

Scenario 3 gir best samlet resultat. Når kapasiteten økes til 2000 timer, reduseres manglende kapasitet fra 550 til 50 timer. Antall prosjekter med risiko reduseres til ett.
## 8.6 Diskusjon av resultater
Resultatene viser at engineeringkapasitet er den viktigste begrensende ressursen i den simulerte prosjektporteføljen. Selv om prosjektene varierer i størrelse og prioritet, konkurrerer de om de samme ressursene. Dette fører til kapasitetskonflikter når flere prosjekter krever engineeringtimer samtidig.

Analysen viser at sekvensiering har stor betydning for hvilke prosjekter som påvirkes av kapasitetsmangel. Scenario 1, hvor kapasiteten fordeles likt mellom prosjektene, gir høy risiko i hele prosjektporteføljen. Ingen prosjekter prioriteres, og alle påvirkes av ressursmangelen. Dette kan føre til at flere prosjekter forsinkes samtidig.

I scenario 2 benyttes prioritetsbasert sekvensiering. Selv om den totale kapasitetsmangelen fortsatt er 550 timer, reduseres antall prosjekter med risiko betydelig. Dette viser at beslutningsregler kan være like viktige som økt kapasitet. Ved å prioritere de mest kritiske prosjektene kan virksomheten redusere konsekvensene av ressursmangel og sikre leveranser som har størst forretningsmessig betydning.

Scenario 3 gir de beste resultatene. Økt kapasitet kombinert med prioritetsbasert sekvensiering reduserer både manglende timer og antall prosjekter med risiko. Resultatene indikerer at en kombinasjon av god prioritering og tilstrekkelig kapasitet gir den mest robuste ressursplanleggingen.

For AXTech kan en slik modell fungere som beslutningsstøtte ved planlegging av engineeringressurser. Modellen gjør det mulig å identifisere flaskehalser tidlig, vurdere konsekvensene av ulike prioriteringer og undersøke effekten av kapasitetsendringer før beslutninger tas. Dette kan bidra til bedre ressursutnyttelse, redusert forsinkelsesrisiko og mer forutsigbar prosjektgjennomføring.

Samtidig må resultatene tolkes med forsiktighet. Analysen er basert på simulerte data og en forenklet modell av virkeligheten. Faktiske prosjekter vil ofte være påvirket av usikkerhet knyttet til estimater, endringer i kundekrav, leverandørforsinkelser og tilgjengelighet på spesialkompetanse. Modellen bør derfor sees som en prototype som demonstrerer metodikken, snarere enn et ferdig operativt verktøy.
