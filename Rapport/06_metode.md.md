# 6 Metode

## 6.1 Forskningsdesign

Studien benytter et design science-inspirert forskningsdesign hvor målet er å utvikle og evaluere en beslutningsstøtteprototype for ressursallokering i AXTech. Fokus er ikke å beskrive eksisterende praksis, men å utvikle en modell som kan bidra til bedre beslutninger ved kapasitetsbegrensninger.

## 6.2 Simulerte data
Ettersom interne prosjektdata fra AXTech ikke var tilgjengelige, ble det utviklet et simulert datasett basert på offentlig tilgjengelig informasjon om selskapets produkter og prosjekttyper. Datasettet representerer realistiske engineeringprosjekter innen offshore wind, subsea, cable lay og marine operasjoner.

For hvert prosjekt ble det definert prioritet, prosjektfase, frist og ressursbehov innen engineering.

## 6.3 Datamodell
Datamodellen består av følgende variabler:

Prosjektnavn
Prosjektfase
Prioritet
Frist
Engineeringbehov
Tilgjengelig kapasitet
Tildelt kapasitet
Manglende kapasitet
Risiko

Variablene danner grunnlaget for sekvensiering, ressursallokering og scenarioanalyse.
## 6.4 Sekvensieringsmodell
Prosjektene prioriteres etter tre kriterier:

Prosjektprioritet
Nærmeste frist
Kritisk prosjektfase

Formålet er å sikre at kritiske prosjekter mottar kapasitet før mindre kritiske prosjekter når ressursene er begrenset.
## 6.5 Ressursallokeringsmodell
Den tilgjengelige engineeringkapasiteten fordeles sekvensielt mellom prosjektene basert på resultatet fra sekvensieringsmodellen. Prosjekter med høyere prioritet mottar kapasitet først.

Modellen beregner hvor mye kapasitet som tildeles hvert prosjekt og hvor mange timer som eventuelt mangler.
## 6.6 Scenarioanalyse
Tre scenarioer analyseres:

Scenario 1: Lik fordeling av kapasitet
Scenario 2: Prioritetsbasert sekvensiering
Scenario 3: Økt kapasitet

Scenarioene sammenlignes med hensyn til manglende timer, ressursutnyttelse og forsinkelsesrisiko.
## 6.7 Begrensninger
Studien er basert på simulerte data og representerer derfor ikke faktiske prosjektdata fra AXTech. Resultatene må derfor betraktes som en demonstrasjon av metodikken og ikke som en eksakt representasjon av selskapets operative situasjon.