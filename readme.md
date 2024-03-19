# KI Lifecycle Management Beispiel

Beispiel zum Management einer Machine Learning Anwendung mit MLFlow.

## Use Case
Convulutional Neural Network zum Erkennen von Ermüdungsrissen in Aluminiumteilen, wie sie oft in Flugzeugrümpfen verbaut werden. 

https://www.nature.com/articles/s41598-022-13275-1

**Eingabedaten:** 3D Messungen von Dehnung und Deformation von Materialabschnitten.

**Ausgabe:** Segmentierung der Eingabebilder anhand von Ermüdungsrissen.

## Ausführen der Beispiele

1. Clonen des Repositories https://github.com/dlr-wf/explainable-crack-tip-detection
2. Ausführen der Schritte zur Installation der nötigen Dependencies und Hereunterladen der Daten https://github.com/dlr-wf/explainable-crack-tip-detection?tab=readme-ov-file#usage
3. In examples/ctd_path.py muss die Variable ```cracktip_dir={Absoluter Phard zu /explainable-crack-tip-detection}``` gesetzt werden.
4. Installation von MLFlow
```pip install mlflow```
5. Starten eines lokalen Tracking Servers  
```mlflow ui```
6. Ausführen der Jupyter Notebooks

