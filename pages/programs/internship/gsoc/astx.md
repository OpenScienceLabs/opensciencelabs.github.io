---
title: "GSoC - ASTx Project Ideas"
description: "GSoC - ASTx Project Ideas"
date: "2024-01-29"
authors: ["OSL Team"]
---

[&lt;&lt; Back](/programs/internship/gsoc)

# ArxLang/ASTx

## Project Idea 1: Extending Data Type Support in ASTx

### Abstract

The ASTx project, a component of the ArxLang ecosystem, serves as an agnostic
framework for constructing and representing Abstract Syntax Trees (ASTs). Its
primary objective is to provide a versatile and language-independent structure
for ASTs, primarily catering to the needs of the ArxLang project but with the
flexibility to be utilized across various programming languages and parsing
tools. The current state of ASTx includes features like support for basic AST
blocks, control flow elements, integer data types, operators, and visibility and
scope handling for objects, along with a symbol table organized by scope.

This proposal aims to significantly extend the data type capabilities of ASTx by
introducing a broader spectrum of types. The envisioned expansion includes:

- **Integer Kinds**: Enriching the current integer type support (i8, i16, i32,
  i64) to handle a wider range of integer-based operations and representations.
- **Real Kinds**: Adding support for real number types (f32, f64), enabling ASTx
  to represent floating-point operations and values with varying precision.
- **Complex Kinds**: Integrating complex number types (c32, c64) to facilitate
  operations and representations involving complex numbers.
- **Character Types**: Implementing UTF-8 character and string support, allowing
  ASTx to handle character and string data efficiently and in a more
  standardized format.
- **Logical Kinds**: Introducing boolean (bool) data types, essential for
  representing logical operations and conditions.
- **Generic and Collection Types**: Expanding the framework to include 'Any',
  'Set', 'List', and 'Tuple' types, enhancing its ability to represent more
  complex data structures and generic type handling.

### License

BSD 3 Clause: https://github.com/arxlang/astx/blob/main/LICENSE

### Code of Conduct

https://github.com/arxlang/astx/blob/main/CODE_OF_CONDUCT.md

### Current State

Currently there are already some data types, such as Integer, Float, and
Boolean, but we need also to expand these datatypes to Literals and Variables,
so we can have a real implementation for each data type and create tests and
tutorials for that.

### Tasks

- https://github.com/arxlang/astx/issues/20

### Expected Outcomes

- Support for more datatypes, including it for literals and variables
- Update the documentation
- Create tutorials for the new datatypes
- Create tests for the new datatypes
- Create a blog post for the new datatypes

### Details

- Prerequisites:
  - Python
  - Object-oriented programming (OOP)
  - AST (basic knowledge)
- Expected Time: 350 hours
- Potential Mentor(s): Ivan Ogasawara

### References

- https://github.com/arxlang/astx/blob/main/src/astx/datatypes.py

---

## Project Idea 2: Implementing Console-Based AST Representation in ASTx

### Abstract

The ASTx framework, integral to the ArxLang project, currently supports
visualizing Abstract Syntax Trees (ASTs) using Graphviz, which is highly
beneficial for graphical interpretation and debugging. However, this
visualization is limited to environments like jupyter notebooks. To enhance the
debugging and analysis capabilities of ASTx, particularly in environments like a
pdb session, this proposal introduces the development of a console-based AST
representation feature.

The core idea of this proposal is to implement a functionality in ASTx that
enables the rendering of ASTs directly in the console using ASCII art. The
proposed approach involves integrating a library like `asciinet` or an
equivalent ASCII art generation tool, which will transform the AST structure
into a textual representation. This textual representation will allow developers
to visualize the AST hierarchy and structure directly in their terminals,
enhancing the debugging and inspection process in a wide range of development
environments.

Key aspects of this proposal include:

- **ASCII Art Generation**: Develop a mechanism to convert AST nodes and their
  relationships into an ASCII-based tree structure. The representation should be
  clear, structured, and easily interpretable.
- **Integration with ASTx**: Seamlessly integrate this ASCII art generation with
  the existing ASTx structure. It should function as an additional feature, not
  replacing but complementing the existing Graphviz visualization.
- **Interactivity and Customization**: Provide options for customizing the level
  of detail in the console output, potentially allowing users to expand or
  collapse certain nodes for better clarity.
- **Cross-Platform Compatibility**: Ensure that the ASCII representation works
  consistently across different terminal environments and operating systems.

This enhancement will significantly improve the utility of ASTx, particularly
for developers working in non-GUI environments or those who prefer
terminal-based toolchains. It will also facilitate quick and easy inspection of
AST structures during development and debugging, without the need for additional
graphical tools.

### License

BSD 3 Clause: https://github.com/arxlang/astx/blob/main/LICENSE

### Code of Conduct

https://github.com/arxlang/astx/blob/main/CODE_OF_CONDUCT.md

### Current State

Currently, astx can show a graphical representation of the AST in jupyter
notebooks with Graphviz.

### Tasks

- https://github.com/arxlang/astx/issues/22

### Expected Outcomes

- Support for AST representation in the console
- Update the documentation
- Create tutorials for this new feature
- Create a blog post for this new feature

### Details

- Prerequisites:
    - Python
    - Object-oriented programming (OOP)
    - AST (basic knowledge)
- Expected Time: 350 hours
- Potential Mentor(s): Ivan Ogasawara

### References

- https://github.com/cosminbasca/asciinet


[&lt;&lt; Back](/programs/internship/gsoc)
