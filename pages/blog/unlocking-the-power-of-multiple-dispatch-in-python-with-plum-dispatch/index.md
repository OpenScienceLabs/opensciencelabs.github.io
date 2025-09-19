---
title: "Unlocking the Power of Multiple Dispatch in Python with Plum-Dispatch"
slug:  unlocking-the-power-of-multiple-dispatch-in-python-with-plum-dispatch
date: 2024-01-05
authors: ["Ivan Ogasawara"]
tags: [open-source, multiple-dispatch, python]
categories: [python]
description: |
  Python, known for its simplicity and readability, sometimes requires a bit of
  creativity when it comes to implementing certain programming paradigms. One such
  paradigm is multiple dispatch (or multimethods), which allows functions to behave
  differently based on the type of their arguments. This is where plum-dispatch
  comes into play.
thumbnail: "/header.png"
template: "blog-post.html"
---
Python, known for its simplicity and readability, sometimes requires a bit of creativity when it comes to implementing certain programming paradigms. One such paradigm is multiple dispatch (or multimethods), which allows functions to behave differently based on the type of their arguments. While not natively supported in Python, this feature can be incredibly powerful, particularly in complex applications such as mathematical computations, data processing, or when working with abstract syntax trees (ASTs). This is where `plum-dispatch` comes into play.

## What is Multiple Dispatch?

Multiple dispatch is a feature where the function to be executed is determined by the types of multiple arguments. This is different from single dispatch (which Python supports natively via the `functools.singledispatch` decorator), where the function called depends only on the type of the first argument.

## Introducing Plum-Dispatch

`plum-dispatch` is a Python library that provides an efficient and easy-to-use implementation of multiple dispatch. It allows you to define multiple versions of a function, each tailored to different types of input arguments.

### Installation

First things first, let's install `plum-dispatch`:


```python
!pip install plum-dispatch -q
```

### Basic Usage

To demonstrate the basic usage of `plum-dispatch`, let's start with a simple example. Suppose we have a function that needs to behave differently when passed an integer versus when it's passed a string.


```python
from plum import dispatch


class Processor:
    @dispatch
    def process(self, data: int):
        return f"Processing integer: {data}"

    @dispatch
    def process(self, data: str):
        return f"Processing string: {data}"
```

In this example, `Processor` has two `process` methods, one for integers and one for strings. `plum-dispatch` takes care of determining which method to call based on the type of `data`.

### Advanced Example: Working with ASTs

`plum-dispatch` shines in more complex scenarios, such as when working with different types of nodes in an abstract syntax tree. Let's create a simple AST representation with different node types and a visitor class to process these nodes.


```python
class StringNode:
    def __init__(self, value):
        self.value = value

class NumberNode:
    def __init__(self, value):
        self.value = value

class BaseASTVisitor:
    @dispatch
    def visit(self, node: StringNode):
        raise Exception("Not implemented yet.")

    @dispatch
    def visit(self, node: NumberNode):
        raise Exception("Not implemented yet.")

class ASTVisitor(BaseASTVisitor):
    @dispatch
    def visit(self, node: StringNode):
        return f"Visited StringNode with value: {node.value}"

    @dispatch
    def visit(self, node: NumberNode):
        return f"Visited NumberNode with value: {node.value}"
```

With `plum-dispatch`, our `ASTVisitor` can have a single `visit` method that behaves differently depending on whether it's visiting a `StringNode` or a `NumberNode`.

### Putting It All Together
Now, let's see `plum-dispatch` in action:


```python
processor = Processor()
print(processor.process(123))  # "Processing integer: 123"
print(processor.process("abc"))  # "Processing string: abc"

visitor = ASTVisitor()
print(visitor.visit(StringNode("Hello")))  # "Visited StringNode with value: Hello"
print(visitor.visit(NumberNode(456)))  # "Visited NumberNode with value: 456"
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Processing integer: 123
Processing string: abc
Visited StringNode with value: Hello
Visited NumberNode with value: 456

</span></code>
</pre>
</div>

## Conclusion

`plum-dispatch` offers a neat and powerful way to implement multiple dispatch in Python, making your code more modular, readable, and elegant. Whether you're dealing with simple data types or complex structures like ASTs, `plum-dispatch` can help you write more efficient and maintainable code.

For more complex examples and advanced usage, check out the [plum-dispatch documentation](https://github.com/wesselb/plum).
