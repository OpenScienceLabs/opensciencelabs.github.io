---
title: "Console-based representation in ASTx"
slug: "console-based-representation-in-astx"
date: 2024-08-08
authors: ["Ana Krelling", "Ivan Ogasawara"]
tags: ["abstract syntax tree", "ascii", "console"]
categories: ["abstract syntax tree", "console"]
description: |
    Recently, console-based AST representation was included in the ASTx framework. Such feature can enhance the debugging and analysis capabilities of ASTx, particularly in environments such as a pdb session. In this tutorial, we'll explore this new feature as well as the ASTx Graphviz visualization.
thumbnail: "/header.png"
template: "blog-post.html"
---
# Introduction

The ASTx library is an agnostic framework for constructing and representing Abstract Syntax Trees (ASTs). Its primary objective is to provide a versatile and language-independent structure for ASTs, with the flexibility to be utilized across various programming languages and parsing tools. ASTx doesn't aim to be a lexer or a parser, although it could be used by any programming language or parser written in Python in order to provide a high level representation of the AST.

Many kinds of nodes (classes) are currently supported. Below is a list with just some examples:

##### Statements:
* Function
* Function Prototype
* FunctionReturn
* ForRangeLoop 
* VarDecl

##### Operators:
* BinaryOp
* UnaryOp

##### Data types:
* Boolean
* Literal 
* Variable 


The ASTx project is still under development, so new classes may be added to the ones above at any time.

Below are installation instructions and an example, so you can have an overview of how you can leverage the ASTx library for your needs.

# Installation
The first step is to install ASTx. You can do it simply by running the command below in your terminal:\
`$ pip install astx`\
If you need more information on installation, you can get it in the [ASTx installation page](https://github.com/arxlang/astx/blob/main/docs/installation.md).
After that, you can just open a Jupyter Notebook instance and start writing your first AST.


# Example: an AST of a series of mathematical operations
Here we will present a quick example of an AST of the expression \
`basic_op = lit_1 + b - a * c / a + (b - a / a)`, in which \
$~~~~$ `lit_1` is a defined integer, and \
$~~~~$ `a`, `b`, and `c` are variables.\
The first thing to do is, in your Jupyter Notebook instance, import `display`, which will allow you to have a basic visualization of the AST, and the astx library itself. 


```python
# import display for AST visualization
import astx

from astx.viz import graph_to_ascii, traverse_ast_ascii
```

Then we create an instance of the Module class, and this instance will be the first node of the tree, or the root node. After that, we declare the variables and literal that will be part of the basic operation that we will parse into an AST.


```python
# Create module
module = astx.Module()

# Declare variables
decl_a = astx.VariableDeclaration(name="a", type_=astx.Int32, value=astx.LiteralInt32(1))
decl_b = astx.VariableDeclaration(name="b", type_=astx.Int32, value=astx.LiteralInt32(2))
decl_c = astx.VariableDeclaration(name="c", type_=astx.Int32, value=astx.LiteralInt32(4))

a = astx.Variable(name="a")
b = astx.Variable(name="b")
c = astx.Variable(name="c")

# Declare literal
lit_1 = astx.LiteralInt32(1)

# State the expression
basic_op = lit_1 + b - a * c / a + (b - a / a)
```

After the basic expression is stated, we create an instance of the Function class. As mentioned in the API documentation, each instance of the Function class must have a prototype and a body, so we'll create those first.

The body is made of a block that is created and the variables, as well as the basic operation, are appended to it afterwards.


```python
# Create FunctionPrototype
main_proto = astx.FunctionPrototype(
    name="main", args=astx.Arguments(), return_type=astx.Int32
)

# Create FunctionReturn
main_block = astx.Block()
main_block.append(decl_a)
main_block.append(decl_b)
main_block.append(decl_c)
main_block.append(astx.FunctionReturn(basic_op))

# Create Function
main_fn = astx.Function(prototype=main_proto, body=main_block)

# Append function to module
module.block.append(main_fn)
```

After this, the module is complete. We can get its AST structure as a dictionary, as well as a PNG representation.


```python
# Create dictionary representation
module.get_struct()
```




<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
{'MODULE[main]': {'content': [{'FUNCTION[main]': {'content': {'args': {'Arguments(0)': {'content': [],
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.GenericKind: -100>}}},
'body': {'BLOCK': {'content': [{'VariableDeclaration[a, Int32]': {'content': {'Literal[Int32]: 1': {'content': 1,
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': 'c4848732a3c542f1b3818bc799dc0b26',
'kind': <ASTKind.GenericKind: -100>}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.VarDeclKind: -203>}}},
{'VariableDeclaration[b, Int32]': {'content': {'Literal[Int32]: 2': {'content': 2,
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': 'b63f0bf700194bb7abbdf99d8cc20336',
'kind': <ASTKind.GenericKind: -100>}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.VarDeclKind: -203>}}},
{'VariableDeclaration[c, Int32]': {'content': {'Literal[Int32]: 4': {'content': 4,
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '0c0686b5f12a45bd9ff1a20da82702a0',
'kind': <ASTKind.GenericKind: -100>}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.VarDeclKind: -203>}}},
{'RETURN': {'content': {'BINARY[+]': {'content': {'lhs': {'BINARY[-]': {'content': {'lhs': {'BINARY[+]': {'content': {'lhs': {'Literal[Int32]: 1': {'content': 1,
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '8d5d86d52b98484a8e5947ae4e6556f1',
'kind': <ASTKind.GenericKind: -100>}}},
'rhs': {'Variable[b]': {'content': 'b',
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.GenericKind: -100>}}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.BinaryOpKind: -301>}}},
'rhs': {'BINARY[/]': {'content': {'lhs': {'BINARY[*]': {'content': {'lhs': {'Variable[a]': {'content': 'a',
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.GenericKind: -100>}}},
'rhs': {'Variable[c]': {'content': 'c',
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.GenericKind: -100>}}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.BinaryOpKind: -301>}}},
'rhs': {'Variable[a]': {'content': 'a',
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.GenericKind: -100>}}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.BinaryOpKind: -301>}}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.BinaryOpKind: -301>}}},
'rhs': {'BINARY[-]': {'content': {'lhs': {'Variable[b]': {'content': 'b',
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.GenericKind: -100>}}},
'rhs': {'BINARY[/]': {'content': {'lhs': {'Variable[a]': {'content': 'a',
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.GenericKind: -100>}}},
'rhs': {'Variable[a]': {'content': 'a',
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.GenericKind: -100>}}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.BinaryOpKind: -301>}}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.BinaryOpKind: -301>}}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.BinaryOpKind: -301>}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.ReturnKind: -403>}}}],
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.GenericKind: -100>}}}},
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.FunctionKind: -401>}}}],
'metadata': {'loc': {line: -1, col: -1},
'comment': '',
'ref': '',
'kind': <ASTKind.ModuleKind: -101>}}}
</span></code>
</pre>
</div>




```python
# Create ascii representation
dot_graph = traverse_ast_ascii(module.get_struct(simplified=True))
graph = graph_to_ascii(dot_graph) 
print(graph)
```

![non-funky_ascii_tree.png](index_files/0d8393a6-fb00-4364-8f2f-319295075948.png)


```python
# Create PNG representation
module
```


    
![png](index_files/index_11_0.png)
    





<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>

</span></code>
</pre>
</div>



We can also get the PNG representation of parts of the AST, such as `basic_op` and the variable `a`:


```python
# Create PNG representation
basic_op
```


    
![png](index_files/index_13_0.png)
    





<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>

</span></code>
</pre>
</div>




```python
# Create PNG representation
a
```


    
![png](index_files/index_14_0.png)
    





<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>

</span></code>
</pre>
</div>



## Custom shapes

It is also possible to use custom shapes for the output using the function `viz.visualize`. The Default shape is `box`, but  `diamond`, `ellipse`, and `circle` are also avaiable options. 


```python
# Import visualization module
from astx import viz

# Create PNG representation with diamond shape
viz.visualize(a.get_struct(), shape="diamond")
```


    
![png](index_files/index_16_0.png)
    



```python
# Create PNG representation with circle shape
viz.visualize(a.get_struct(), shape="circle")
```


    
![png](index_files/index_17_0.png)
    



```python
# Create PNG representation with ellipse shape
viz.visualize(a.get_struct(), shape="ellipse")
```


    
![png](index_files/index_18_0.png)
    


# Conclusion

This guide provides clear instructions and a simple example for you to start using the ASTx library. But this is just the beginning of your journey. Make sure to check out the other tutorials available, such as the one for [variables](https://github.com/arxlang/astx/blob/main/docs/tutorials/variables.ipynb) and the one for [functions](https://github.com/arxlang/astx/blob/main/docs/tutorials/functions.ipynb).
