# Model Monitoring

- Gutes Abschneiden von ML Modellen in Experimenten bedeutet nicht, dass ein Modell in der Praxis immer ähnlich gut funktioniert.
- Daten aus der Produktivumgebung müssen forlaufend ausgewertet werden.
- MLFlow ermöglicht fortlaufende Evaluationen registrierter Modelle mit neuen Daten.
- Wenn Drift erkannt wird, kann mit den neuen Daten ein neues Training initiiert werden. 

## Data drift
Data drift oder auch Concept drift tritt auf, wenn sich statistische Eigenschaften der Eingabedaten eines ML Modells verändern und dieses dadurch schlechter wird.

Drifts treten auf:
- Plötzlich: Rapide änderungen in der Produktivumgebung z.B. Änderung von Messverfahren.
- Inkrementell: Schleichende Änderungen z.B. Abnutzung von Sensorik.
- Saisonal: Gut Vorhersagbar, z.B. bei Wetterdaten.
