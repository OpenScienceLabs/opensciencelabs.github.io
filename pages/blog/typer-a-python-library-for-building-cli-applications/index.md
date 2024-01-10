---
title: "Typer: A Python Library for Building CLI Applications"
slug: typer-a-python-library-for-building-cli-applications
date: 2024-01-11
authors: ["Ivan Ogasawara"]
tags: [open-source, cli, python]
categories: [python]
description: |
  Typer is an exciting library for Python developers, designed to make the creation of
  command-line interface (CLI) applications not just easier, but also more enjoyable.
  Built on top of the well-known Click library, Typer leverages Python 3.6+ features,
  like type hints, to define CLI commands in a straightforward and intuitive way.
thumbnail: "/header.svg"
template: "blog-post.html"
---
# Typer: A Python Library for Building CLI Applications

## What is Typer?

Typer is an exciting library for Python developers, designed to make the creation of command-line interface (CLI) applications not just easier, but also more enjoyable. Built on top of the well-known Click library, Typer leverages Python 3.6+ features, like type hints, to define CLI commands in a straightforward and intuitive way.

## Why Choose Typer?

- **Simplicity**: With Typer, you can create powerful CLI applications using minimal code.
- **Type Hints**: Leverages Python's type hints for parameter declaration, reducing errors and improving code clarity.
- **Automatic Help**: Generates help text and error messages based on your code.
- **Subcommands**: Supports nested commands, allowing complex CLI applications.

## Getting Started with Typer

### Installation

To begin using Typer, you first need to install it. You can easily do this using pip:


```python
!pip install typer -q
```

### Creating Your First Typer Application

Let's start with a simple example. We'll create an application that greets a user.

First, import Typer and create an instance of it:


```python
import typer

app = typer.Typer()
```

Now, define a function that will act as your command. Use type hints for function arguments:


```python
@app.command()
def greet(
    name: str = typer.Option(
        "--name",
        "-n",
        help="The name of the person to greet."
    )
) -> None:
    """Greets the user by name."""
    typer.echo(f"Hello {name}!")
```

To run this application, use the following code block at the end of your script:

```python
if __name__ == "__main__":
    app()
```

### Running the Application

Save the script as `greet.py` and run it from the command line:


```python
%%writefile greet.py

import typer

app = typer.Typer()

@app.command()
def greet(
    name: str = typer.Option(
        ..., 
        "--name",
        help="The name of the person to greet."
    )
) -> None:
    """Greets the user by name."""
    typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting greet.py

</span></code>
</pre>
</div>


```python
!python greet.py --name Alice
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Hello Alice!

</span></code>
</pre>
</div>

### Help Documentation

Typer automatically generates help documentation for your application. Try running:


```python
!python greet.py --help
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Usage: greet.py [OPTIONS]

Greets the user by name.

Options:
--name TEXT                     The name of the person to greet.  [required]
--install-completion [bash|zsh|fish|powershell|pwsh]
Install completion for the specified shell.
--show-completion [bash|zsh|fish|powershell|pwsh]
Show completion for the specified shell, to
copy it or customize the installation.
--help                          Show this message and exit.

</span></code>
</pre>
</div>

You'll get a detailed description of how to use the command, including available options.

## Working with Subcommands

Typer supports subcommands, allowing you to build more complex applications. In the following example, the script is structured around a main Typer application (app) and two sub-applications (app_user and app_product). This hierarchical structure is a hallmark of Typer, allowing for the organization of commands into distinct categories – in this case, user-related and product-related operations. Such an approach not only enhances the readability and maintainability of the code but also provides a more intuitive interface for the end users. They can easily navigate through the different functionalities of the application, whether it's creating or updating users, or handling product information.


```python
%%writefile ecommerce.py
import typer

from typer import Context, Option


app = typer.Typer(help="Operations for e-commerce.")
app_user = typer.Typer(help="Operations for user model.")
app_product = typer.Typer(help="Operations for product model.")

app.add_typer(app_user, name="user")
app.add_typer(app_product, name="product")

@app.callback(invoke_without_command=True)
def main(
    ctx: Context,
    version: bool = Option(
        None,
        "--version",
        "-v",
        is_flag=True,
        help="Show the version and exit.",
    ),
) -> None:
    """Process envers for specific flags, otherwise show the help menu."""
    if version:
        __version__ = "0.1.0"
        typer.echo(f"Version: {__version__}")
        raise typer.Exit()

    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit(0)

@app_user.command("create")
def user_create(name: str = typer.Argument(..., help="Name of the user to create.")) -> None:
    """Create a new user with the given name."""
    print(f"Creating user: {name} - Done")


@app_user.command("update")
def user_update(name: str = typer.Argument(..., help="Name of the user to update.")) -> None:
    """Update user data with the given name."""
    print(f"Updating user: {name} - Done")

@app_product.command("create")
def product_create(name: str = typer.Argument(..., help="Name of the product to create.")) -> None:
    """Create a new product with the given name."""
    print(f"Creating product: {name} - Done")


@app_product.command("update")
def product_update(name: str = typer.Argument(..., help="Name of the product to update.")) -> None:
    """Update a product with the given name."""
    print(f"Updating product: {name} - Done")


if __name__ == "__main__":
    app()
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting ecommerce.py

</span></code>
</pre>
</div>

A key feature demonstrated in the script is the use of the callback function with the invoke_without_command=True parameter. This setup enables the execution of specific code (like displaying the version or help text) before any subcommands are processed. It's a powerful tool for handling pre-command logic or global options that apply to the entire CLI application.

Moreover, the script showcases the simplicity and elegance of defining commands in Typer. Each operation, such as creating or updating users and products, is defined as a function, with parameters automatically translated into command-line options or arguments. This approach not only makes the code more readable but also leverages Python's type hints to ensure that the command-line arguments are correctly interpreted, providing a seamless and error-free user experience.

In the following lines, there are some examples of the CLI call with different parameters.


```python
!python ecommerce.py --help
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Usage: ecommerce.py [OPTIONS] COMMAND [ARGS]...

Operations for e-commerce.

Options:
-v, --version                   Show the version and exit.
--install-completion [bash|zsh|fish|powershell|pwsh]
Install completion for the specified shell.
--show-completion [bash|zsh|fish|powershell|pwsh]
Show completion for the specified shell, to
copy it or customize the installation.
--help                          Show this message and exit.

Commands:
product  Operations for product model.
user     Operations for user model.

</span></code>
</pre>
</div>


```python
!python ecommerce.py --version
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Version: 0.1.0

</span></code>
</pre>
</div>


```python
!python ecommerce.py user --help
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Usage: ecommerce.py user [OPTIONS] COMMAND [ARGS]...

Operations for user model.

Options:
--help  Show this message and exit.

Commands:
create  Create a new user with the given name.
update  Update user data with the given name.

</span></code>
</pre>
</div>


```python
!python ecommerce.py user create --help
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Usage: ecommerce.py user create [OPTIONS] NAME

Create a new user with the given name.

Arguments:
NAME  Name of the user to create.  [required]

Options:
--help  Show this message and exit.

</span></code>
</pre>
</div>


```python
!python ecommerce.py product --help
```

## Conclusion

Typer is a powerful yet straightforward tool for building CLI applications in Python. By leveraging Python's type hints, it offers an intuitive way to define commands and parameters, automatically handles help documentation, and supports complex command structures with subcommands. Whether you're a beginner or an experienced Python developer, Typer can significantly enhance your productivity in CLI development.

Happy coding with Typer! 🐍✨
