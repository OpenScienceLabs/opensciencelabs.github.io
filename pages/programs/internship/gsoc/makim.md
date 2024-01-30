---
title: "GSoC - Makim Project Ideas"
description: "GSoC - Makim Project Ideas"
date: "2024-01-29"
authors: ["OSL Team"]
---

[&lt;&lt; Back](/programs/internship/gsoc)

# Makim

## Project Idea 1: Adding Windows Support for Makim

### Abstract

Makim is a powerful and versatile automation tool used widely in software
development for task orchestration and workflow management. However, one
significant limitation has been its lack of native support for Windows, a
platform frequently used by developers. This project proposal aims to bridge
this gap by enhancing Makim's compatibility with Windows environments.

Currently, Makim relies on the `sh` library, which is not fully compatible with
Windows. The proposed project seeks to abstract the usage of `sh` within Makim
and introduce an alternative approach that seamlessly integrates with Windows
systems. Two promising alternatives, `subprocess` and `plumbum`, will be
explored for this purpose.

The primary objectives of this project are as follows:

1. **Windows Compatibility:** Implement a platform detection mechanism within
   Makim to identify when it's running on Windows. When running on Windows, the
   tool should automatically switch to using the Windows-compatible alternative
   (e.g., `subprocess` or `plumbum`) for executing commands.

2. **Testing and Evaluation:** Thoroughly test the compatibility and performance
   of the chosen alternative(s) on both Windows and Unix-like systems.
   Benchmarking will be conducted to determine if the alternative(s) offer
   advantages over the current `sh` implementation.

3. **Documentation:** Update Makim's documentation to reflect the new Windows
   compatibility features and provide clear guidelines for users on how to
   utilize the tool effectively on Windows platforms.

4. **Community Engagement:** Encourage community involvement by seeking feedback
   and contributions from users and developers, especially those working in
   Windows-centric environments. Create blog posts.

This project presents an exciting opportunity to make Makim more accessible to a
broader audience of developers, including those working in Windows-based
environments. By addressing this limitation, we aim to enhance the usability and
adoption of Makim, further solidifying its position as a valuable automation
tool in the software development ecosystem.

### License

BSD 3 Clause: https://github.com/osl-incubator/makim/blob/main/LICENSE

### Code of Conduct

https://github.com/osl-incubator/makim/blob/main/CODE_OF_CONDUCT.md

### Current State

Current, Makim doesn't support windows, because it relays on the library `sh`
that doesn't work on windows.

### Tasks

- https://github.com/osl-incubator/makim/issues/47

### Expected Outcomes

- The project should be able to be installed on Windows.
- The packaging recipe on conda-forge should be updated
- The creation of a blog post about new support
- Documentation should be updated
- The test on CI for windows should be enabled and any issues should be fixed

### Details

- Prerequisites:
    - Python
    - Object-oriented programming (OOP)
    - YAML
    - shell script
- Expected Time: 350 hours
- Potential Mentor(s): Ivan Ogasawara

### References

- https://www.mkdocs.org/
- https://squidfunk.github.io/mkdocs-material/

---

## Project Idea 2: Adding Pipeline Support to Makim and Change from dependencies to hooks

### Abstract

Makim is a versatile and extensible automation tool designed to simplify complex
workflows and tasks in software development. While it excels at managing
individual targets, it currently lacks native support for defining and executing
pipelines, a critical feature for orchestrating sequences of tasks efficiently.
This proposal aims to extend Makim's capabilities by introducing support for
defining, running, and visualizing pipelines within Makim configuration files.

The core objectives of this project are as follows:

1. **Change from dependencies to hooks:** Instead of dependencies that just
   define pre-run targets, hooks would allow pre-run (setup) and post-run
   (teardown).

2. **Pipeline Definition:** Extend Makim configuration file (YAML format) to
   include a dedicated section for defining pipelines. Pipelines will consist of
   a sequence of steps, where each step can be associated with any existing
   Makim target.

3. **Pipeline Execution:** Implement a pipeline execution mechanism within
   Makim, allowing users to run defined pipelines using a simple command-line
   interface. Pipelines should support both linear and branching flows, enabling
   complex task orchestration.

4. **Pipeline Visualization:** Integrate a graph visualization tool, such as
   `asciinet`, to allow users to view the structure and dependencies of defined
   pipelines. This feature will enhance transparency and aid in debugging
   complex workflows.

5. **Documentation:** Update Makim's documentation to include comprehensive
   guidance on defining and executing pipelines. Provide examples and best
   practices for creating efficient and maintainable pipeline configurations.

### License

BSD 3 Clause: https://github.com/osl-incubator/makim/blob/main/LICENSE

### Code of Conduct

https://github.com/osl-incubator/makim/blob/main/CODE_OF_CONDUCT.md

### Current State

Makim is very well structured in order to allow the inclusion of the pipelines
support.

### Tasks

- https://github.com/osl-incubator/makim/issues/75
- https://github.com/osl-incubator/makim/issues/26

### Expected Outcomes

- Support for pipelines with Makim
- The package on conda-forge should be updated
- The creation of a blog post about pipelines with Makim
- Documentation should be updated
- Add the correspondent tests (unit test, and smoke tests) on CI

### Details

- Prerequisites:
    - Python
    - Object-oriented programming (OOP)
    - YAML
    - basic concepts about pipelines between commands
- Expected Time: 350 hours
- Potential Mentor(s): Ivan Ogasawara

### References

- https://www.gnu.org/software/bash/manual/html_node/Pipelines.html
- https://airflow.apache.org/docs/apache-airflow/stable/index.html
- https://www.mkdocs.org/
- https://squidfunk.github.io/mkdocs-material/


[&lt;&lt; Back](/programs/internship/gsoc)
