---
title: "GSoC - noWorkflow Project Ideas"
description: "GSoC - noWorkflow Project Ideas"
date: "2024-01-29"
authors: ["OSL Team"]
---

[&lt;&lt; Back](/programs/internship/gsoc)

# noWorkflow

## Project Idea 1: Verify the reproducibility of an experiment

### Abstract

Implement an algorithm to compare the provenance from two (or more) trials
(i.e., executions of an experiment) to check their reproducibility. The
provenance stored in the relational (sqlite) database by noWorkflow 2 contains
intermediate variable values from a trial. These values could be compared to
check how much or where executions deviate from each other.

### License

MIT: https://github.com/gems-uff/noworkflow/blob/master/LICENSE

### Code of Conduct

Contributor Covenant:
https://github.com/gems-uff/noworkflow/blob/master/CODE_OF_CONDUCT.md

### Current State

It currently has some methods to explicitly tag variables of different trials
and methods to compare them. It would be nice to have a way to compare the whole
trial and estimate how much a trial deviate from another.

### Tasks

- Compare trials of the same script
- Estimate how much on trial deviate from another
- Consider different scripts and execution flows
- Indicate which parts of the scripts are not reproducible

### Expected Outcomes

Each task has a different outcome

### Details

- Prerequisites:
    - Python
    - SQL or SQLAlchemy ORM
- Expected Time: 350h
- Potential Mentor(s): João Felipe Pimentel

---

## Project Idea 2: Control levels of provenance collection

### Abstract

Add support for different levels of provenance collection in noWorkflow 2.

### License

MIT: https://github.com/gems-uff/noworkflow/blob/master/LICENSE

### Code of Conduct

Contributor Covenant:
https://github.com/gems-uff/noworkflow/blob/master/CODE_OF_CONDUCT.md

### Current State

Currently, noWorkflow 2 collects Python construct evaluations and all the
dependencies among the evaluations. However, this collection is inefficient,
since some of the collected provenance may not be necessary for end-users.

### Tasks

- Disable the collection inside specific functions (through decorators?)
- Disable the collection inside specific regions of the code (through with
  statements?)
- Collect only function activations in a region, instead of all variable
  dependencies
- Disable the collection of specific modules
- Design a DSL to express general dependencies for parts of the code where the
  collection is disabled

### Expected Outcomes

In this project, it is desirable to provide ways to temporarily disable the
provenance collection and to manually indicate the provenance in this situation.

### Details

- Prerequisites:
  - Python
- Expected Time: 350h
- Potential Mentor(s): João Felipe Pimentel

---

## Project Idea 3: Upgrade noWorkflow collection to support new Python constructs

### Abstract

Implement new AST transformations for provenance collection.

### License

MIT: https://github.com/gems-uff/noworkflow/blob/master/LICENSE

### Code of Conduct

Contributor Covenant:
https://github.com/gems-uff/noworkflow/blob/master/CODE_OF_CONDUCT.md

### Current State

While noWorkflow 2 works for newer Python versions, most of its implementation
was targeted at Python 3.7. Newer Python versions have new constructs in which
the provenance is ignored.

### Tasks

- Identify which AST constructs implementations are missing
- Design AST transformations to execute functions before and after the
  evaluation of the constructs
- Create the dependencies for the new constructs

### Expected Outcomes

A new version of noWorkflow that supports Python constructs from newer versions.

### Details

- Prerequisites:
    - Python
- Expected Time: 240h
- Potential Mentor(s): João Felipe Pimentel

[&lt;&lt; Back](/programs/internship/gsoc)
