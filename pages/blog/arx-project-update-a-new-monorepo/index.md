---
title: "Arx Project Update: A New Monorepo, Better Tooling, and the First Steps Toward a Bigger Ecosystem"
slug: "arx-project-update-a-new-monorepo"
date: 2026-04-29
authors: ["Ivan Ogasawara"]
tags: ["compiler", "arx", "llvm"]
categories: ["compilers"]
description: >-
  Arx is evolving into a broader language ecosystem for data-oriented computing.
  Recent updates include the new monorepo for ASTx, IRx, and Arx, early tooling
  like ArxPM, VS Code syntax highlighting, Douki docstring support, and an 
  experimental Jupyter kernel. The language itself is also growing with features 
  such as typed functions, classes, templates, collections, dataframes, and 
  compiler/runtime improvements.
thumbnail: "/header.png"
template: "blog-post.html"
---

The Arx project has been moving fast lately, and it feels like a good moment to share where things are today.

Arx is still an early-stage programming language and compiler project, but the direction is becoming much clearer: a language focused on data-oriented computing, native collection abstractions, and a compiler pipeline that can grow into something practical for scientific, analytical, and systems-oriented work. The project currently aims to provide native list, tensor, and dataframe abstractions, backed internally by IRx runtime support, while using LLVM for native code generation. ([ArxLang][1])

A lot has changed recently, not only in the language itself, but also around the ecosystem: project management, editor support, documentation tooling, and early notebook integration.

## The Arx monorepo

One of the biggest changes is that Arx is now organized as a monorepo.

The main repository now brings together the three core packages of the compiler stack:

* `packages/astx` — ASTx, the abstract syntax tree foundation
* `packages/irx` — IRx, the intermediate representation, semantic/lowering layer, backend, and runtime integration
* `packages/arx` — Arx, the language frontend and user-facing compiler tooling

This is a big step for the project. Previously, these pieces evolved more independently. Now, they can move together in a more coordinated way. The repository uses a lockstep release workflow, where ASTx, IRx, and Arx share one version and are built/published together. ([GitHub][2])

That matters because language features often touch more than one layer. For example, a new syntax feature in Arx may require AST support in ASTx, semantic or lowering support in IRx, and user-facing behavior in the Arx compiler. Keeping these packages close together makes it easier to evolve the compiler pipeline without scattering related changes across multiple repositories.

In practice, this should make development simpler, reviews more coherent, and cross-package refactors easier to manage.

## What Arx supports today

Arx is still a prototype, but it already has several important language pieces in place.

The language has a Python-like feel, with indentation-based blocks and familiar control-flow syntax, while also taking inspiration from C++ and YAML. The current documentation describes Arx as a language focused on data-oriented computing, with planned static typing and native abstractions for lists, tensors, and dataframes. ([ArxLang][1])

Some of the current highlights include:

### Functions and typed signatures

Arx functions are defined with `fn`, typed parameters, and an explicit return type. Function return types are required, including `-> none` for functions that do not return a value. ([ArxLang][3])

```arx
fn add(x: i32, y: i32) -> i32:
  return x + y
```

Arx also supports function calls, default parameter values, extern prototypes, and template functions with bounded type parameters. ([ArxLang][3])

```arx
@<T: i32 | f64>
fn add(x: T, y: T) -> T:
  return x + y
```

This is especially exciting because it points toward a language that can express generic behavior while still keeping types explicit and compiler-friendly.

### Classes

Class support has also landed. Arx class declarations support fields, methods, annotations, visibility modifiers, static fields/methods, abstract declarations, and default construction. ([ArxLang][4])

```arx
class Counter:
  value: int32 = 0

  fn get(self) -> int32:
    return self.value
```

There is still a lot to grow here, but the current model already establishes the basic structure for object-oriented patterns in Arx.

### Lists, tensors, and dataframes

Arx now exposes `list[...]` and `tensor[...]` as distinct collection forms, including fixed-shape tensors such as `tensor[i32, 2, 2]` and runtime-shaped tensor parameters such as `tensor[i32, ...]`. ([GitHub][2])

The docs also describe dataframe and series annotations, including static-schema dataframe forms such as:

```arx
dataframe[id: i32, score: f64]
```

and typed series such as:

```arx
series[f64]
```

These APIs are still evolving, but they show the direction clearly: Arx wants data structures to be first-class language concepts, not only library-level conventions. ([ArxLang][5])

### Control flow

Arx currently supports `if`/`else`, `while`, and two forms of `for` loops: a for-in style and a count-style loop. ([ArxLang][6])

```arx
fn sum_values() -> i32:
  var total: i32 = 0
  for value in [1, 2, 3]:
    total = total + value
  return total
```

The for-in loop can iterate over list-valued expressions, including list literals, list variables, and the builtin `range(start, stop[, step])`. ([ArxLang][6])

### Builtins and standard library direction

Arx now has a bundled pure-Arx standard library under the reserved `stdlib` namespace. The compiler also has internal builtin modules, separate from user-facing stdlib imports. The first builtin module is `generators`, currently exposing a `range(start, stop[, step]) -> list[i32]` MVP. ([GitHub][2])

That separation is important: builtins are compiler-provided, while `stdlib` is where regular Arx library code can grow.

### CLI and compiler outputs

Arx supports multiple output modes, including inspecting tokens, AST, LLVM IR, and compiling to object/native outputs. The README also documents explicit executable link modes such as `auto`, `pie`, and `no-pie`, which helps in environments where the linker defaults can cause PIE-related issues. ([ArxLang][1])

## Recent compiler progress

The changelog shows a lot of activity in April 2026. Recent releases added or improved class support, imports, settings, testing, template call parsing, parser organization, lexer layout, and alignment of the Arx surface syntax with IRx array-first naming. ([ArxLang][7])

That may sound like internal compiler plumbing, but it is exactly the kind of work a young language needs. Better parsing, clearer syntax rules, stronger tests, and tighter AST/IR alignment make it easier to add future language features without constantly fighting the foundations.

## arxpm: project management for Arx

Another important piece is `arxpm`, the Arx project manager and workspace tool.

The goal of `arxpm` is to make Arx projects easier to create, build, run, package, publish, and validate. It owns project layout inference, `.arxproject.toml` rendering, manifest validation, default target selection, environment provisioning, and user-facing workflow commands. It also uses `uv` for Python environment/package installation workflows. ([GitHub][8])

Current commands include:

```bash
arxpm init
arxpm config
arxpm install
arxpm add
arxpm build
arxpm compile
arxpm run
arxpm pack
arxpm publish
arxpm healthcheck
```

This is a big deal for usability. A language does not become comfortable only because the compiler works. It also needs a good project workflow. `arxpm` is the beginning of that story: a place where package management, builds, local dependencies, project configuration, and publishing can become consistent.

## vscode-arx: early editor support

There is also an early VS Code extension: `vscode-arx`.

For now, it is intentionally simple. It is a highlight-only extension with TextMate syntax highlighting for Arx files and basic language configuration, including line comments, brackets, auto-closing pairs, and surrounding pairs. It does not include a language server, commands, or runtime extension code yet. ([GitHub][9])

That is a good first step. Syntax highlighting already makes writing and reading `.x` files more pleasant, and keeping the extension small makes it easier to keep in sync with the language while the syntax is still changing.

## Douki: structured docstrings with YAML

Another project in the ecosystem is Douki, a docstring formatter and checker based on structured YAML docstrings.

Douki keeps docstrings synchronized with function signatures and validates them against a schema, without requiring a runtime dependency in the package using it. It supports commands such as `douki check` and `douki sync`, and it can also migrate existing NumPy-style docstrings. ([GitHub][10])

This fits naturally with Arx because Arx itself already uses YAML-like docstring blocks in examples and documentation. Having a dedicated tool for structured documentation helps keep APIs readable, consistent, and easier to validate automatically.

## arxlang-jupyter-kernel: first notebook experiments

The Arx ecosystem also has an early Jupyter kernel: `arxlang-jupyter-kernel`.

This first version works as a wrapper-style kernel. Each cell is compiled with the Arx CLI, executed as a native binary, and then stdout/stderr are returned to Jupyter. It keeps a session prelude with previously successful cells, so new cells compile as the previous successful source plus the current cell. ([GitHub][11])

This is very early, but it is an exciting direction. If Arx grows toward scientific computing, dataframes, tensors, Arrow integration, and ML workflows, then notebooks are a natural environment for experimentation, teaching, and demos.

## Where Arx could go next

The current work gives Arx a stronger base. The next steps can now be more ambitious.

Some ideas for the future include:

* Python bindings to use Arx libraries from Python
* Arx bindings to use Python libraries from Arx
* a scientific computing library for Arx, possibly `sciarx`
* a machine learning library for Arx
* deeper Apache Arrow integration, with more Arrow functions and tools available natively
* more builtin functionality for files, networking protocols, system interaction, and common runtime tasks

The Python interoperability story is especially interesting. Python already has a massive scientific and ML ecosystem. If Arx can interoperate well with Python, it could become easier to experiment with Arx without needing to rebuild the whole world from scratch.

At the same time, native Arx libraries for scientific computing and ML would help define what makes the language unique. The long-term vision is not only “a compiler that works,” but a language ecosystem that feels useful for real data-oriented projects.

## Final thoughts

Arx is still young, and many things are intentionally experimental. But the recent updates show a project that is becoming more organized and more ambitious.

The monorepo brings the compiler stack closer together. ArxPM starts to shape the developer workflow. VS Code support makes the language easier to write. Douki improves documentation discipline. The Jupyter kernel opens the door to interactive exploration. And inside the language itself, features like classes, typed functions, templates, lists, tensors, dataframes, imports, control flow, and builtins are gradually turning Arx into something much more concrete.

There is still a long road ahead, but the direction is exciting: a friendly, typed, data-oriented language with native compilation, Arrow-inspired abstractions, and an ecosystem designed to grow around real workflows.

Arx is not production-ready yet — and that is okay. This is the stage where the foundations are being shaped, the ideas are being tested, and the ecosystem is starting to take form.

And honestly, that is one of the most fun stages of a language project.

[1]: https://arxlang.org/ "ArxLang"
[2]: https://github.com/arxlang/arx "GitHub - arxlang/arx · GitHub"
[3]: https://arxlang.org/library/functions.html "functions – ArxLang"
[4]: https://arxlang.org/library/classes.html "classes – ArxLang"
[5]: https://arxlang.org/library/datatypes.html "datatypes – ArxLang"
[6]: https://arxlang.org/library/control-flow.html "control-flow – ArxLang"
[7]: https://arxlang.org/changelog/ "Changelog - ArxLang"
[8]: https://github.com/arxlang/arxpm "GitHub - arxlang/arxpm · GitHub"
[9]: https://github.com/arxlang/vscode-arx/ "GitHub - arxlang/vscode-arx · GitHub"
[10]: https://github.com/arxlang/douki "GitHub - arxlang/douki · GitHub"
[11]: https://github.com/arxlang/arxlang-jupyter-kernel "GitHub - arxlang/arxlang-jupyter-kernel · GitHub"
