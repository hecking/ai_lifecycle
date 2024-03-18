# MLOps

## Definition

![ML Ops](img/ml_ops.png)
MLOps vereinigt die KI Anwendungsentwicklung (Dev) mit Systembereitstellung und -betrieb (Ops). Durch die Bereitstellung von systematischen und automatisierbaren Workflows über den ML Lifecycle und die beteiligten Personen hinweg soll die Gefahr von Hidden Technical Debt reduziert werden. 

:::{admonition} MLOps
- **Tools** und **Prinzipien** unterstützen den gesamten ML Lifecycle
- **Systematisierung und Automatisierung** von Datenanalyse bis Model Deployment
- Etablierung und Anwendunge von **Best Practices**  
:::

## MLOps Prinzipien
::::{grid} 1 1 2 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: basics/organize
:link-type: doc
:class-header: bg-light

**Reproducible** &#x1F501;
^^^

Ausführung des selben Workflows mit den selben Ergebnissen jederzeit möglich.
:::

:::{grid-item-card}
:link: content/myst
:link-type: doc
:class-header: bg-light

**Accountable** &#x1F4D3;
^^^

Alle Entscheidungen werden dokumentiert.

:::

:::{grid-item-card}
:link: content/executable/index
:link-type: doc
:class-header: bg-light

**Collaborative** &#x1F469;
^^^

Arbeiten anderer sind zugreifbar und können erweitert werden.

:::

:::{grid-item-card}
:link: interactive/launchbuttons
:link-type: doc
:class-header: bg-light

**Continuous** &#x23E9;
^^^

Automatische Ausführung standartisierter Workflows, z.B. Testen und Verfügbarmachen von Modellen.
:::

:::{grid-item-card}
:link: publish/web
:link-type: doc
:class-header: bg-light

**Scalable** &#x1F5A5;
^^^

Das System kann bei Bedarf auf größeren Infrastrukturen betrieben werden.
:::

:::{grid-item-card}
:link: content/components
:link-type: doc
:class-header: bg-light

**Trustworthy** &#x1F453;
^^^

Vertrauen in ML Lösungen durch Transparenz und einhaltung von ML Prinzipien.
:::

::::

## Tool Unterstützung mit MLFlow

Es gibt eine Reihe von Unterstützungswerkzeuge für MLOps.

Wir nutzen hier ML Flow als eins der meistverbreitetsten Open Source Frameworks.

- Einige Funktionalitäten
    - Einheitliche Plattorm für die **Entwicklung**, **Deployment** und **Management** von ML Anwendungen.
    - Management und Koordinierung von ML Experimenten mit mehreren Beteiligten. 
    - Reproduzierbarkeit von Resultaten durch Tracking von Daten und Modellparametern.
    - Management und Versionierung von ML Modellen.
    - Einheitliches Deployment unabhängig von ML Libraries.
