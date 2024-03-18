# Model Serving

- Aus der Modelling Phase sind viele verschiedene Modelle entstanden.
- Es wird das beste ausgewählt und für Anwendungen zur Verfügung gestellt.
- Sollte während des Betriebs ein anderes Modell gewählt werden oder ein Modell weiterentwickelt werden, brauchen die Anwendungen nicht angepasst werden!

![Deployment](img/mlflow-deployment-overview.png)
*Quelle: https://mlflow.org/docs/latest/deployment/index.html*

**Beispiel**

Bereitstellen des Modelles *crack-tip-detection-production* Version 1
```mlflow models serve -m models:/crack-tip-detection-production/1```

Anwendungen können nun über einen API Endpunkt auf das Modell zugreifen.
```curl http://127.0.0.1:5000/invocations -H "Content-Type:application/json;"  --data '{"inputs": ...}'```



