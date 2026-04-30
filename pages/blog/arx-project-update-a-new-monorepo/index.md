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

# Arx Project Update: A New Monorepo, Arrow-Backed Data Containers, and a Growing Ecosystem

The Arx project has been moving fast lately, and this feels like a good moment to share where things are today.

Arx is still an early-stage programming language and compiler project, but the direction is becoming much clearer: a language focused on data-oriented computing, native collection abstractions, and a compiler pipeline designed to work naturally with modern data systems.

One of the most important parts of this direction is Apache Arrow. Arrow data types are already first-class citizens inside Arx. Today, that support covers a small but important fraction of Arrow-backed containers, especially `Tensor` and `Table`. The plan is to expand this foundation with more Arrow data types and Arrow compute functions over time.

This makes Arx especially interesting for people working with data science, analytics, numerical computing, dataframe workflows, columnar memory, and high-performance data processing. If you are already familiar with Apache Arrow, PyArrow, pandas, Polars, NumPy, or scientific Python workflows, Arx is exploring a space that should feel very relevant.

## The Arx monorepo

One of the biggest recent changes is that Arx is now organized as a monorepo.

The main repository now brings together the three core packages of the compiler stack:

* `packages/astx` — ASTx, the abstract syntax tree foundation
* `packages/irx` — IRx, the intermediate representation, semantic/lowering layer, backend, and runtime integration
* `packages/arx` — Arx, the language frontend and user-facing compiler tooling

They are lockstep-released ecosystem packages, with one shared release workflow across `astx`, `pyirx`, and `arxlang`.

That matters because language features usually do not live in only one place. A new syntax feature in Arx may need AST support in ASTx, semantic or lowering support in IRx, and user-facing compiler behavior in Arx. Keeping these packages together makes it easier to evolve the compiler pipeline coherently.

In practice, this should make development simpler, reviews more focused, and cross-package refactors easier to manage.

## A language for data-oriented computing

Arx has a Python-like feel, with indentation-based blocks and familiar control-flow syntax, while also taking inspiration from languages such as C++, Rust, Java, Go, and JavaScript.

The goal is not to copy any single language. The goal is to combine readable syntax, explicit types, native compilation, and data-oriented abstractions.

Arx uses LLVM for native code generation and provides support for tensors, dataframes, and series backed by Arrow C++ data containers.

That combination is the core of the project’s identity: Arx is not only trying to be a general-purpose compiler experiment. It is moving toward a language where data containers, Arrow interoperability, and native execution are part of the foundation.

## What Arx supports today

Arx is still a prototype, but it already has several important language pieces in place.

### Functions and typed signatures

Arx functions are defined with `fn`, typed parameters, and explicit return types.

```arx
fn add(x: i32, y: i32) -> i32:
  return x + y
```

The language also supports function calls, default parameter values, extern prototypes, and template-style functions with bounded type parameters.

```arx
@<T: i32 | f64>
fn add(x: T, y: T) -> T:
  return x + y
```

This is an important step toward writing reusable code while still keeping the compiler pipeline explicit and type-aware.

### Classes

Class support has also been added. Arx supports class declarations with fields and methods, giving the language a clearer path for organizing larger programs.

```arx
class Counter:
  value: i32 = 0

  fn get(self) -> i32:
    return self.value
```

This is still early, but it establishes a foundation for object-oriented patterns inside Arx.

### Lists, tensors, dataframes, and Arrow-backed containers

Arx exposes `list[...]` and `tensor[...]` as distinct public collection forms. It supports fixed-shape tensors such as `tensor[i32, 2, 2]`, runtime-shaped tensor parameters such as `tensor[i32, ...]`, and fixed-width numeric tensor element types such as `i8`, `i16`, `i32`, `i64`, `f32`, and `f64`.

```arx
fn pick(grid: tensor[i32, 2, 2]) -> i32:
  return grid[1, 0]
```

The important detail is that Arx is not treating these containers as simple syntax sugar. Some of them are backed by Apache Arrow C++ data types. Today, this support is still limited to a small fraction of Arrow’s world, especially `Tensor` and `Table`, but the direction is already clear: Arrow data types are first-class citizens in Arx, and support will expand to more Arrow data types and functions.

For people coming from data science or data infrastructure, this is one of the most exciting parts of the project. Arx has the opportunity to make Arrow-native data structures feel natural at the language level, instead of only being accessed through external libraries.

### Control flow

Arx supports familiar control flow such as `if`/`else`, `while`, and `for` loops.

```arx
fn sum_values() -> i32:
  var total: i32 = 0

  for value in [1, 2, 3]:
    total = total + value

  return total
```

The project also has builtin support for `range(...)`, and for-in loops can iterate over list-valued expressions such as ranges, list literals, and list variables.

### Builtins and standard library direction

Arx now ships a bundled pure-Arx standard library under the reserved `stdlib` namespace. Compiler-provided builtins are kept separate from the public standard library, and builtin functions such as `range(...)` are available automatically.

```arx
import math from stdlib

fn main() -> i32:
  return math.square(4)
```

This separation is important. Builtins are compiler-provided, while `stdlib` should be imported.

### Testing support

Arx also has an `arx test` subcommand. The runner searches for test files, discovers zero-argument `test_*` functions returning `none`, and executes each test in its own compiled subprocess.

```bash
arx test
arx test -k square
arx test --list
```

For a young language, this is a very practical feature. It makes it easier to write examples, regression tests, compiler tests, and library tests using the language itself.

## IRx and Arrow runtime support

A lot of the data-oriented foundation lives in IRx.

IRx lowers ASTx nodes to LLVM IR using `llvmlite`, provides a visitor-based code generation pipeline, and can produce runnable executables through `clang`. Its supports arithmetic, variables, functions, returns, structured control flow, fatal assertions, and system-level expressions.

Alongside an one-dimensional array substrate, IRx exposes an initial internal `Tensor` layer for homogeneous N-dimensional values, backed by Arrow C++ `arrow::Tensor`. The current tensor support is focused on fixed-width numeric element types and readonly Arrow C++ backed storage.

This is still early, but it is also one of the strongest signals about where Arx is going: a language where data containers and Arrow-backed runtime support are part of the compiler architecture, not an afterthought.

## arxpm: project management for Arx

Another important piece of the ecosystem is `arxpm`.

`arxpm` is the Arx project manager and workspace tool. It owns `.arxproject.toml` rendering, project layout inference and validation, default target selection, Python environment provisioning via `uv`, and user-facing workflow commands.

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

This is a big deal for usability. A language does not become comfortable only because the compiler works. It also needs a good project workflow.

`arxpm` is the beginning of that story: a place where package management, builds, local dependencies, project configuration, and publishing can become consistent.

## vscode-arx: early editor support

There is also an early VS Code extension: `vscode-arx`.

For now, it is intentionally simple. It is a highlight-only extension with TextMate syntax highlighting for Arx files and basic language configuration, including line comments, brackets, auto-closing pairs, and surrounding pairs. The README explicitly says it has no language server, commands, or runtime extension code yet.

That is a good first step. Syntax highlighting already makes writing and reading Arx code more pleasant, and keeping the extension small makes it easier to keep in sync while the language is still evolving.

## Douki: structured docstrings with YAML

Another project in the ecosystem is Douki.

Douki is a developer tool for structured YAML docstrings. It keeps docstrings synchronized with function signatures and validates them against a schema, without adding a runtime dependency to the package using it. For now, douki just supports Python, but soon it will supports arx source files as well.

It supports workflows such as:

```bash
douki check src/
douki sync src/
```

This fits naturally with the Arx ecosystem because documentation discipline matters a lot in fast-moving compiler and language projects. Having a dedicated tool for structured documentation helps keep APIs readable, consistent, and easier to validate automatically.

## arxlang-jupyter-kernel: first notebook experiments

The Arx ecosystem also has an early Jupyter kernel: `arxlang-jupyter-kernel`.

This first version is a wrapper-style Jupyter kernel. Each cell is compiled with the Arx CLI, executed as a native binary, and then stdout/stderr are returned to Jupyter.

This is very early, but it is an exciting direction. If Arx grows toward scientific computing, dataframes, tensors, Arrow integration, and machine learning workflows, notebooks are a natural environment for experimentation, teaching, demos, and data exploration.

## Why this matters for data science users

Arx is not trying to replace Python. Python has a massive ecosystem, and tools like NumPy, pandas, PyArrow, Polars, scikit-learn, Jupyter, and PyTorch are already deeply established.

Instead, Arx explores a different point in the design space: a language with native Arrow-backed data containers, compiler-aware data operations, and future Python bindings so Arx libraries can be used from existing Python workflows.

What would it look like to have a language where Arrow data types are first-class? What would it look like to have tensors, tables, and dataframes represented directly in the language and compiler pipeline? What would it look like to combine readable syntax, native compilation, and Arrow-backed runtime structures from the beginning?

That is the interesting space Arx is moving into.

For data science and data infrastructure people, this means Arx may become a place to experiment with ideas around:

* Arrow-native data containers
* dataframe and table abstractions
* tensor-oriented computation
* scientific computing workflows
* native execution
* Python interoperability
* compiler-aware data operations

The project is still young, but the foundation is becoming much more concrete.

## Where Arx could go next

The current work gives Arx a stronger base. The next steps can now be more ambitious, especially around data science, Apache Arrow, and interoperability with the broader Python ecosystem.

Some ideas for the future include:

* Python bindings to use Arx libraries from Python
* Arx bindings to use Python libraries from Arx
* a scientific computing library for Arx (`sciarx`)
* a machine learning library for Arx
* expanded support for Apache Arrow data types
* expanded support for Arrow compute functions
* more native support for Arrow-backed containers, including tensors, tables, arrays, schemas, and related tools
* more builtin functionality for files, networking protocols, system interaction, and common runtime tasks

The Python interoperability story is especially important. Python already has a huge scientific and machine learning ecosystem. If Arx can interoperate well with Python while also providing native Arrow-backed data structures, it could become easier to experiment with Arx inside existing data workflows.

At the same time, native Arx libraries for scientific computing and machine learning would help define what makes the language unique. The long-term vision is not only “a compiler that works,” but a language ecosystem where data containers, Arrow memory, native execution, and high-level syntax work together naturally.

## Final thoughts

Arx is still young, and many things are intentionally experimental. But the recent updates show a project that is becoming more organized, more ambitious, and more relevant for people working with data science and data infrastructure.

The monorepo brings the compiler stack closer together. ArxPM starts to shape the developer workflow. VS Code support makes the language easier to write. Douki improves documentation discipline. The Jupyter kernel opens the door to interactive exploration.

And inside the language itself, features like typed functions, classes, templates, lists, tensors, tables, dataframes, imports, control flow, builtins, tests, and Arrow-backed containers are gradually turning Arx into something much more concrete.

There is still a long road ahead, but the direction is exciting: a friendly, typed, data-oriented language with native compilation, Apache Arrow as a core foundation, and an ecosystem designed to grow around real scientific and analytical workflows.

Arx is not production-ready yet, and that is okay. This is the stage where the foundations are being shaped, the ideas are being tested, and the ecosystem is starting to take form.

And honestly, that is one of the most fun stages of a language project.

For more information, checkout the official repositories:

* https://github.com/arxlang/arx
* https://github.com/arxlang/arxpm
* https://github.com/arxlang/vscode-arx
* https://github.com/arxlang/douki
* https://github.com/arxlang/arxlang-jupyter-kernel
