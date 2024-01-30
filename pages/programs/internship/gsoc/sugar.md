---
title: "GSoC - Sugar Project Ideas"
description: "GSoC - Sugar Project Ideas"
date: "2024-01-29"
authors: ["OSL Team"]
---

[&lt;&lt; Back](/programs/internship/gsoc)

# Sugar

## Project Idea 1: Create TUI for Sugar Using Textual

### Abstract

The goal of this project is to develop a Terminal User Interface (TUI) for
Sugar, a tool that simplifies container management. This TUI will provide a
visual and interactive way to access all functionalities of Sugar directly from
the terminal, akin to the user experience offered by k9s for Kubernetes.

The Sugar TUI aims to enhance the user experience by providing a graphical
interface within the terminal, allowing users to interact with Sugar's features
more intuitively. The interface will be accessible via the command `sugar tui`
and will be developed using the Textual library in Python, known for its
capabilities in building modern, interactive TUIs.

**Key Features:**

1. **Group Selection:** Users can select which group of services they want to
   interact with.
2. **Service Management:** Functionalities to start, restart, and stop services
   within the chosen group.
3. **Logs and Stats Viewing:** Capability to view logs and check statistics for
   individual services.
4. **Service Details:** Display detailed information about services, such as IP
   addresses, volumes, and configuration settings.

**Technical Approach:**

- Utilize the Textual library to create a rich, interactive TUI. Textual's
  modern design and integration capabilities make it an ideal choice for
  developing a user-friendly interface.
- Design the interface to reflect the hierarchical structure of Sugar's
  configuration, allowing users to navigate between different groups and
  services effortlessly.
- Implement command handling in the TUI to perform actions such as starting,
  stopping, and restarting services.
- Fetch and display real-time data from Sugar, such as service logs, stats, and
  configuration details.

**Development Plan:**

1. **Initial Setup:** Setting up the project structure and integrating the
   Textual library.
2. **Interface Design:** Designing the layout and navigation of the TUI,
   including menus and panels.
3. **Feature Implementation:** Developing the core functionalities - group
   selection, service management, log viewing, and displaying service details.
4. **Testing and Refinement:** Rigorous testing of the TUI for usability,
   performance, and compatibility with existing Sugar functionalities.
5. **Documentation and Examples:** Creating comprehensive documentation and
   usage examples to assist users in leveraging the new TUI.

**Expected Outcomes:**

### License

BSD 3 Clause: https://github.com/osl-incubator/sugar/blob/main/LICENSE

### Code of Conduct

https://github.com/osl-incubator/sugar/blob/main/CODE_OF_CONDUCT.md

### Current State

Sugar is already published on pypi and conda-forge, and currently works on top
of docker compose v2.

### Tasks

- https://github.com/osl-incubator/sugar/issues/42

### Expected Outcomes

- Sugar TUI working from the CLI `sugar tui`
- Documentation should be updated in order to include this new feature
- The creation of a blog post that explains this new implementation
- Add tests on CI for TUI (as much as possible)

### Details

- Prerequisites:
    - Python
    - Object-oriented programming (OOP)
    - docker compose
    - ansible
    - ssh
    - YAML
- Expected Time: 350 hours
- Potential Mentor(s): Ivan Ogasawara

### References

- https://dev.to/rimelek/ansible-playbook-and-ssh-keys-33bo
- https://docs.docker.com/compose/
- https://realpython.com/python3-object-oriented-programming/
- https://www.mkdocs.org/
- https://squidfunk.github.io/mkdocs-material/

---

## Project Idea 2: Enhancing Sugar with Deployment Capabilities

### Abstract

The primary objective of this project is to augment Sugar, a container
management tool, with comprehensive deployment capabilities. Sugar simplifies
the usage of container orchestration tools like Docker Compose by centralizing
configurations and streamlining command-line options. The proposed enhancement
aims to incorporate a deployment module into Sugar's existing framework,
allowing for seamless deployment processes alongside container management.

The core idea is to integrate a new configuration section within Sugar's
configuration file, dedicated to deployment settings. This section would specify
various deployment parameters such as server details, credentials, file paths,
and environment variables. By leveraging Ansible as a backend library (not just
its CLI), the deployment process can achieve greater flexibility and
adaptability to different environments.

This enhancement proposes the introduction of a new class, potentially named
`SugarDeployment`, which would integrate into Sugar’s existing plugin system.
This class would handle the deployment logic, interpreting the
deployment-specific configuration and executing necessary actions. Users would
interact with this functionality through a simple command like `sugar deploy`,
following Sugar's philosophy of simplicity and ease of use.

The project will involve working on aspects such as:

- Designing and implementing the `SugarDeployment` class.
- Integrating Ansible library to handle deployment tasks.
- Defining and parsing new configuration schema for deployment settings.
- Ensuring compatibility and integration with existing Sugar functionalities.

This enhancement not only aims to add deployment capabilities to Sugar but also
to maintain its user-friendly and flexible nature. The project offers interns an
opportunity to contribute to a tool that simplifies and organizes container
stacks, making the life of developers and system administrators easier.

### License

BSD 3 Clause: https://github.com/osl-incubator/sugar/blob/main/LICENSE

### Code of Conduct

https://github.com/osl-incubator/sugar/blob/main/CODE_OF_CONDUCT.md

### Current State

Sugar is already published on pypi and conda-forge, and currently works on top
of docker compose v2.

### Tasks

- https://github.com/osl-incubator/sugar/issues/85

### Expected Outcomes

- The Deployment of a docker stack on a remote server using `sugar deploy`
  command.
- The update of the documentation
- The creation of a blog post
- Tests for this new feature on CI

### Details

- Prerequisites:
    - Python
    - Object-oriented programming (OOP)
    - docker compose
    - ansible
    - ssh
    - YAML
  - Expected Time: 350 hours
- Potential Mentor(s): Ivan Ogasawara

### References

- https://dev.to/rimelek/ansible-playbook-and-ssh-keys-33bo
- https://docs.docker.com/compose/
- https://realpython.com/python3-object-oriented-programming/
- https://www.mkdocs.org/
- https://squidfunk.github.io/mkdocs-material/

[&lt;&lt; Back](/programs/internship/gsoc)
