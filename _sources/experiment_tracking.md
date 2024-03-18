# Tracking von ML Experimenten

**Ziele:** **Reproduzierbare** Resultate, Ermöglichen von **Kollaboration**, **Transparenz** und **Dokumentation** von Workflows. 

- Ein Experiment bezieht sich immer auf ein konkretes Machine Learning Problem.
- Ein Experiment besteht auch mehereren Durchläufen (Runs), in denen unterschiedliche Modellparameter getestet werden.
- Runs können von verschiedenen Personen dezentral initiiert werden, Ergebnisse und Metadaten werden jedoch zentral gespeichert.
- Im Sinne der Nachvollziehbarkeit und Reproduzierbarkeit werden alle Parametereinstellungen, Evaluationsmetriken, und weitere Metadaten eines Durchlaufs gespeichert.
- Durchläufe eines Experiments können miteinander verglichen werden

![mflow_tracking](img/tracking-basics.png)