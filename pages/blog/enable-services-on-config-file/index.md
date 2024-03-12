---
title: "Enabling service key on config file"
slug: "enable-services-on-config-file"
date: 2024-01-25
authors: ["Joel Vega"]
tags: ["sugar", "containerization", "feature", "devops", "open-source"]
categories: ["devops", "automation", "python"]
description: |
 Sugar project reads its data from a config file, a new scenario was enabled allowing to check if the "group" or "service" paradigm is used.
thumbnail: "/header.jpg"
template: "blog-post.html"
---
# **Enabling service key on config file**

Welcome to the world of [Sugar](https://github.com/osl-incubator/sugar), it is growing and adding more useful features in its workflow. 
Simplify the usage of containers.

You may be thinking, why do I need a new library that wrap-up docker-compose or podman-compose if they are already really simple to use?

Yes, they are simple to use, but if you have some other parameters to the compose command line, it could be very tedious to write them every time such as --env-file, --project-name, --file, etc.

So, in this case we could use something like a script or make, right?

Yes, and just for one project it would be good enough. But, if you maintain or collaborate a bunch of projects, it would be like a boiler plate.

Additionally, if you are maintaining some extra scripts in order to improve your containers stack, these scripts would be like a boilerplate as well.

So, the idea of this project is to organize your stack of containers, gathering some useful scripts and keeping this information centralized in a configuration file. So the command line would be very simple.

Free software: BSD 3 Clause
Documentation: https://osl-incubator.github.io/sugar

![image.png](index_files/image.png)

# Installing Sugar
We need to execute the following command:


```python
! pip install containers-sugar
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Requirement already satisfied: containers-sugar in /usr/local/python/3.10.13/lib/python3.10/site-packages (1.10.0)
Requirement already satisfied: Jinja2>=2 in /home/codespace/.local/lib/python3.10/site-packages (from containers-sugar) (3.1.2)
Requirement already satisfied: colorama>=0.4.6 in /home/codespace/.local/lib/python3.10/site-packages (from containers-sugar) (0.4.6)
Requirement already satisfied: python-dotenv>=0.21.1 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from containers-sugar) (1.0.1)
Requirement already satisfied: pyyaml>=6 in /home/codespace/.local/lib/python3.10/site-packages (from containers-sugar) (6.0.1)
Requirement already satisfied: sh>=2.0.0 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from containers-sugar) (2.0.6)
Requirement already satisfied: MarkupSafe>=2.0 in /home/codespace/.local/lib/python3.10/site-packages (from Jinja2>=2->containers-sugar) (2.1.3)

</span></code>
</pre>
</div>

## The config file

The config file is the skeleton of the app, and determine its functioning and requirements.


```python
%%writefile .env
KXGR_GROUP=group1
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting .env

</span></code>
</pre>
</div>


```python
%%writefile compose.yaml
version: '3.4'

services:
  service1-1:
    hostname: service1-1
    image: python:latest
    ports:
      - 18000:8000
    command: python -m http.server

  service1-2:
    hostname: service1-2
    image: python:latest
    ports:
      - 18001:8000
    command: python -m http.server

  service1-3:
    hostname: service1-3
    image: python:latest
    ports:
      - 18002:8000
    command: python -m http.server

  service1-4:
    hostname: service1-4
    image: python:latest
    ports:
      - 18003:8000
    command: python -m http.server
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Writing compose.yaml

</span></code>
</pre>
</div>

### Group layout
The following is an example of a group config file
Usually we just use sugar.yaml but for this example we will create a config file: group.sugar.yaml


```python
%%writefile .group.sugar.yaml
version: 1.0
compose-app: docker compose
env-file: .env
defaults:
  group: {{ env.KXGR_GROUP }}
  project-name: sugar-{{ env.KXGR_PROJECT_NAME }}
groups:
  group1:
    project-name: project1  # optional
    compose-path: ./compose.yaml
    env-file: .env
    services:
      default: service1-1,service1-3
      available:
        - name: service1-1
        - name: service1-2
        - name: service1-3
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting .group.sugar.yaml

</span></code>
</pre>
</div>

### Service Layout
The following is an example of a group config file
Usually we just use sugar.yaml but for this example we will create a config file: services.sugar.yaml


```python
%%writefile .services.sugar.yaml
version: 1.0
compose-app: docker compose
env-file: .env
defaults:
  group: {{ env.KXGR_GROUP }}
  project-name: sugar-{{ env.KXGR_PROJECT_NAME }}
services:
  project-name: project1  # optional
  compose-path: ./compose.yaml
  env-file: .env
  default: service1-1,service1-3
  available:
    - name: service1-1
    - name: service1-2
    - name: service1-3
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting .services.sugar.yaml

</span></code>
</pre>
</div>

## Testing the functioning
To test the functioning we need to execute the following commands:


```python
!sugar build --config-file ./.group.sugar.yaml
!sugar build --config-file ./.services.sugar.yaml
```

## Why is it helpful?

The hability to use either group configuration or service configuration allows the project to be more flexible and allow many applications.

1. **Flexibility in Configuration:**
    Different targets or groups may require different execution environments. The working-directory attribute provides the flexibility to customize these environments, tailoring them to the unique needs of each segment of your project.

2. **Ease of Use:**
    Users can easily understand and manage the execution context of commands within the Makim configuration. This makes the configuration more readable and maintainable, especially when dealing with complex project structures.


## Conclusion

In conclusion, Sugars's service config feature empowers users with a flexible and efficient approach to project management. Throughout this blog, we explored how this feature, applied with the group layout, and services layout, provides unparalleled customization and control over the execution environment.

By isolating commands, offering flexibility in configuration, and ensuring ease of use, Sugar's working-directory feature becomes an invaluable asset in your toolkit. It not only streamlines the execution of commands but also enhances the overall organization and maintainability of your projects.

Harness the power of simplifying your usage of Sugar generating cleaner code. As you integrate this tool into your workflow, you'll discover a newfound simplicity and clarity in your command execution. Enjoy the benefits of an organized and optimized project environment, courtesy of Sugar's innovative features.

Start optimizing your projects with Sugar today!
