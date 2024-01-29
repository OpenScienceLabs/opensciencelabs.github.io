---
title: "Enabling service key on config file"
slug: "enable-services-on-config-file"
date: 2024-01-25
authors: ["Joel Vega"]
tags: ["sugar", "containerization", "feature", "devops", "open-source"]
categories: ["devops", "automation", "python"]
description: |
  Sugar project reads its data from a config file, a new scenario was enabled allowing to check if the "group" or "service" paradigm is used.
thumbnail: "/header.png"
template: "blog-post.html"
---

<!-- # How to test this feature? -->
<!-- **By Joel Vega** -->

Sugar is growing and adding more useful features in its workflow. 

<!-- TEASER_END -->

## The config file
The config file is the skeleton of the app, and determine its functioning and requirements.
This is the config file: ".services.sugar.yaml" that was used to test this feature
```yaml
version: 1.0
compose-app: docker compose
env-file: .env
defaults:
  group: {{ env.KXGR_GROUP }}
  project-name: sugar-{{ env.KXGR_PROJECT_NAME }}
services:
  project-name: project1  # optional
  compose-path: tests/containers/group1/compose.yaml
  env-file: .env
  default: service1-1,service1-3
  available:
    - name: service1-1
    - name: service1-2
    - name: service1-3

```
The main aspect to note is that we are omitting the traditional group key at root, and are using the "services" key instead.
## Testing
You can use the Jupiter notebook to test the functioning.
also you can run this command

```bash
sugar build --config-file tests/containers/.services.sugar.yaml
```
## References

[Manual de Capacitación sobre Ciencia abierta](<(https://book.fosteropenscience.eu/es/)>)
[Guía de expertos en Gestión de Datos](https://www.cessda.eu/Training/Training-Resources/Library/Data-Management-Expert-Guide)
[5 reglas básicas y 5 pasos para documentar tu proyecto web](https://www.socialancer.com/como-documentar-un-proyecto-web/)
