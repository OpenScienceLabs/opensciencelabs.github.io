# Simplifying Build Automation with Makim

In today’s fast-paced software development environment, the efficiency of build automation and dependency management can significantly impact project timelines and developer productivity. Enter `Makim`, a modern tool designed to simplify and enhance these processes. This guide offers a deep dive into `Makim`, providing a step-by-step tutorial to help you integrate it into your workflow seamlessly.

## Introduction

`Makim` stands as a progressive iteration of the traditional `make` utility, adopting a `.makim.yaml` format over the classic `Makefile`. It focuses on improving how targets and dependencies are defined, with additional control options like conditional execution. By leveraging YAML, `Makim` offers an intuitive, readable way to configure build processes, making it an excellent choice for developers looking for a powerful yet straightforward automation tool.

Makim is a Python-based automation tool designed for effortless project management, and supports various programming languages. With an intuitive CLI, users can specify interpreters, debug code, and define dependencies seamlessly.

Catering to DevOps Engineers and Software Developers, Makim streamlines tasks without redundancy. Its versatile language support makes automation and project management easy. By minimizing setup complexities, Makim frees users to focus on coding.

Makim supports multiple backends for executing code, enabling the use of various programming languages within the Makim configuration file, including Python. By default, Makim employs Xonsh - a shell language and command-line interface that augments Python 3.6+ by integrating shell primitives from Bash and IPython, thus offering a robust scripting environment. Compatible with key operating systems like Linux, macOS, and Windows, Xonsh is tailored to streamline shell commands and scripting using Python's syntax. It strives to offer a flexible interface to accommodate users of all skill levels, from novices to experts, facilitating a broad spectrum of daily computing activities.

**NOTE**: Makim doesn't have support for Windows machines yet, but it is already planned to have.

## Getting Started with Makim

### Installation

Before diving into the intricacies of `Makim`, you'll need to install it. `Makim` is available through both `pip` and `conda`, accommodating various environments and preferences:

- To install `Makim` using `pip`, run:


```python
!pip install -q "makim==1.14.0"
```

- For those who prefer `conda`, execute:

  ```
  conda install "makim=1.14.0"
  ```

These commands install `Makim` on your system. Please, note that makim is still in constantly development, and until it reaches the version 2, it will be changing by a lot, so we recommend to pin it to a specific version.

### Setting Up Your First `.makim.yaml` File

At the heart of `Makim` is the `.makim.yaml` file, which houses all your project's automation configuration. Here's how to create a basic `.makim.yaml`:

1. **Navigate to Your Project Root**: The `.makim.yaml` file should be located at the root of your project directory.
   
2. **Create Your `.makim.yaml`**: Start with a simple text editor or IDE of your choice and create a new file named `.makim.yaml`.

3. **Define Your Configuration**: Insert the basic structure of your automation setup. For instance, you might want to define a simple build and clean process as follows:


```python
%%writefile .makim.yaml
version: 1.0.0
groups:
  clean:
    env-file: .env
    targets:
      tmp:
        help: Use this target to clean up temporary files
        run: |
          echo "Cleaning up..."
  tests:
    targets:
     unit:
       help: Build the program
       args:
         clean:
           type: bool
           action: store_true
           help: if not set, the clean dependency will not be triggered.
       dependencies:
         - target: clean.tmp
           if: ${{ args.clean == true }}
       run: |
         echo "Runnint unit tests..."
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting .makim.yaml

</span></code>
</pre>
</div>

This configuration outlines two primary actions: `clean` and `build`, with the latter dependent on the former based on a conditional argument.

### Understanding the Help Menu

One of `Makim`'s standout features is its auto-generated help menu, which provides a comprehensive overview of available commands and their purposes. To access it, run:


```python
!makim --help
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
[1m                                                                                [0m
[1m [0m[1;33mUsage: [0m[1mmakim [OPTIONS] COMMAND [ARGS]...[0m[1m                                      [0m[1m [0m
[1m                                                                                [0m
Makim is a tool that helps you to organize and simplify your helper commands.

[2m╭─[0m[2m Options [0m[2m───────────────────────────────────────────────────────────────────[0m[2m─╮[0m
[2m│[0m [1;36m-[0m[1;36m-version[0m             [1;32m-v[0m      [1;33m    [0m  Show the version and exit                [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-file[0m                        [1;33mTEXT[0m  Makim config file [2m[default: .makim.yaml][0m [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-dry[0m[1;36m-run[0m                     [1;33m    [0m  Execute the command in dry mode          [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-verbose[0m                     [1;33m    [0m  Execute the command in verbose mode      [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-install[0m[1;36m-completion[0m          [1;33m    [0m  Install completion for the current       [2m│[0m
[2m│[0m                                     shell.                                   [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-show[0m[1;36m-completion[0m             [1;33m    [0m  Show completion for the current shell,   [2m│[0m
[2m│[0m                                     to copy it or customize the              [2m│[0m
[2m│[0m                                     installation.                            [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-help[0m                        [1;33m    [0m  Show this message and exit.              [2m│[0m
[2m╰──────────────────────────────────────────────────────────────────────────────╯[0m
[2m╭─[0m[2m Commands [0m[2m──────────────────────────────────────────────────────────────────[0m[2m─╮[0m
[2m│[0m [1;36mclean.tmp      [0m[1;36m [0m Use this target to clean up temporary files                 [2m│[0m
[2m│[0m [1;36mtests.unit     [0m[1;36m [0m Build the program                                           [2m│[0m
[2m╰──────────────────────────────────────────────────────────────────────────────╯[0m

If you have any problem, open an issue at:
https://github.com/osl-incubator/makim



</span></code>
</pre>
</div>

This command displays all the targets defined in your `.makim.yaml` file, along with their descriptions and available arguments, making it easier to understand and utilize your configurations.

### Executing Your First Commands

With your `.makim.yaml` file set up, you can begin to automate your tasks. Here are some examples:

- **Clean Temporary Files**: Simply run `makim clean.tmp` to execute the clean process.
  
- **Run unit tests**: Use `makim unit.tests` to start the build process. If you need to ensure a clean state before building, you can pass the `--clean` flag as such: `makim tests.unit --clean`.


```python
!makim clean.tmp
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml
Cleaning up...

</span></code>
</pre>
</div>


```python
!makim tests.unit
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml
Runnint unit tests...

</span></code>
</pre>
</div>

In the case you time your command wrong, **Makim** will suggest you some alternative:


```python
!makim tests.unittest
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
[33mUsage: [0mmakim [OPTIONS] COMMAND [ARGS]...
[2mTry [0m[2;34m'makim [0m[1;2;34m-[0m[1;2;34m-help[0m[2;34m'[0m[2m for help.[0m
[31m╭─[0m[31m Error [0m[31m─────────────────────────────────────────────────────────────────────[0m[31m─╮[0m
[31m│[0m No such command 'tests.unittest'.                                            [31m│[0m
[31m╰──────────────────────────────────────────────────────────────────────────────╯[0m
[31mCommand tests.unittest not found. Did you mean tests.unit'?[0m

</span></code>
</pre>
</div>

**Makim** CLI is empowered by **Typer**, and it allows us to have auto-completion for Makim groups and targets! If you want to install, you can run the following command:


```python
!makim --install-completion 
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
[32mbash completion installed in /home/xmn/.bash_completions/makim.sh[0m
Completion will take effect once you restart the terminal

</span></code>
</pre>
</div>

After this command you will need to restart the terminal in order to use this auto-completion feature.

## Advanced Configuration

As you become more familiar with `Makim`, you might want to explore advanced features, such as:

- **Defining Complex Dependencies**: `Makim` allows for sophisticated dependency management, including conditional dependencies based on arguments passed to targets.

- **Organizing Targets into Groups**: For larger projects, organizing targets into groups can enhance readability and maintainability.

- **Environment Variable Integration**: Utilize `env` and `env-file` configurations to manage environment variables across different scopes (global, group, and target).

- **Template Support with Jinja2**: The switch to `${{ some_variable }}` for Jinja2 template delimiters avoids conflicts with formatting tools like `prettier`, allowing for dynamic insertion of variables and arguments in your commands.

## Let's play with different Examples!

### Interpreters

As mentioned before, **Makim** can run code with different interpreters/shell languages. By default, it uses **xonsh**. If you are not familiarized with xonsh, please take a look into its official documentation: <https://xon.sh/>.

In this example,  we will run simple commands with different interpreters/shell languages.


```python
%%writefile .env
MSG_PREFIX="Running Makim: Hello, World,"
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
%%writefile .makim.yaml
version: 1.0
env-file: .env
groups:
  tests:
    targets:
      node:
        help: Test using nodejs
        shell: node
        run: console.log("${{ env.MSG_PREFIX }} from NodeJS!");
      perl:
        help: Test using perl
        shell: perl
        run: print "${{ env.MSG_PREFIX }} from Perl!\n";

      python:
        help: Test using php
        shell: python
        run: print("${{ env.MSG_PREFIX }} from Python!")

      r:
        help: Test using R
        shell: Rscript
        run: print("${{ env.MSG_PREFIX }} from R!")

      sh:
        help: Test using sh
        shell: sh
        run: echo "${{ env.MSG_PREFIX }} from sh!"

      run-all:
        help: Run tests for all the other targets
        dependencies:
          - target: node
          - target: perl
          - target: python
          - target: r
          - target: sh
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting .makim.yaml

</span></code>
</pre>
</div>


```python
!makim --help
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
[1m                                                                                [0m
[1m [0m[1;33mUsage: [0m[1mmakim [OPTIONS] COMMAND [ARGS]...[0m[1m                                      [0m[1m [0m
[1m                                                                                [0m
Makim is a tool that helps you to organize and simplify your helper commands.

[2m╭─[0m[2m Options [0m[2m───────────────────────────────────────────────────────────────────[0m[2m─╮[0m
[2m│[0m [1;36m-[0m[1;36m-version[0m             [1;32m-v[0m      [1;33m    [0m  Show the version and exit                [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-file[0m                        [1;33mTEXT[0m  Makim config file [2m[default: .makim.yaml][0m [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-dry[0m[1;36m-run[0m                     [1;33m    [0m  Execute the command in dry mode          [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-verbose[0m                     [1;33m    [0m  Execute the command in verbose mode      [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-install[0m[1;36m-completion[0m          [1;33m    [0m  Install completion for the current       [2m│[0m
[2m│[0m                                     shell.                                   [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-show[0m[1;36m-completion[0m             [1;33m    [0m  Show completion for the current shell,   [2m│[0m
[2m│[0m                                     to copy it or customize the              [2m│[0m
[2m│[0m                                     installation.                            [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-help[0m                        [1;33m    [0m  Show this message and exit.              [2m│[0m
[2m╰──────────────────────────────────────────────────────────────────────────────╯[0m
[2m╭─[0m[2m Commands [0m[2m──────────────────────────────────────────────────────────────────[0m[2m─╮[0m
[2m│[0m [1;36mtests.node           [0m[1;36m [0m Test using nodejs                                     [2m│[0m
[2m│[0m [1;36mtests.perl           [0m[1;36m [0m Test using perl                                       [2m│[0m
[2m│[0m [1;36mtests.python         [0m[1;36m [0m Test using php                                        [2m│[0m
[2m│[0m [1;36mtests.r              [0m[1;36m [0m Test using R                                          [2m│[0m
[2m│[0m [1;36mtests.run-all        [0m[1;36m [0m Run tests for all the other targets                   [2m│[0m
[2m│[0m [1;36mtests.sh             [0m[1;36m [0m Test using sh                                         [2m│[0m
[2m╰──────────────────────────────────────────────────────────────────────────────╯[0m

If you have any problem, open an issue at:
https://github.com/osl-incubator/makim



</span></code>
</pre>
</div>

Before we run these targets, we will need to install these dependences first:


```python
!mamba install -q -y perl nodejs r-base sh 
```

Now, let's run all the targets using `run-all` that defines all the other targets as dependencies:


```python
!makim tests.run-all
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml
Running Makim: Hello, World, from NodeJS!
Running Makim: Hello, World, from Perl!
Running Makim: Hello, World, from Python!
[1] "Running Makim: Hello, World, from R!"
Running Makim: Hello, World, from sh!

</span></code>
</pre>
</div>

If your interpreter allows you to debug, for example with Python or Xonsh with `breakpoint()`, you can add a breakpoint in your code, and you will be to debug your **Makim** target.

### Using vars


```python
%%writefile .makim.yaml
version: 1.0

vars:
  project-name: "my-project"
  dependencies:
    "dep1": "v1"
    "dep2": "v1.1"
    "dep3": "v2.3"
  authorized-users:
    - admin1
    - admin2
    - admin3

groups:
  staging:
    vars:
      env-name: "staging"
      staging-dependencies:
        "dep4": "v4.3"
        "dep5": "v1.1.1"
      staging-authorized-users:
        - staging1
        - staging2
        - staging3
    targets:
      create-users:
        help: Create users for staging, this example uses jinja2 for loop.
        # each target can also specify their `vars`, but it will not be used in this example
        run: |
          def create_user(username):
              print(f">>> creating user: {username} ... DONE!")
                                                                
          print("create admin users:")
          {% for user in vars.authorized_users %}
          create_user("${{ user }}")
          {% endfor %}

          print("\ncreate staging users:")
          {% for user in vars.staging_authorized_users %}
          create_user("${{ user }}")
          {% endfor %}

      install:
        help: install deps for staging using native xonsh `for` loop (it could work with Python as well)
        # each target can also specify their `vars`, but it will not be used in this example
        run: |
          def install(package, version):
              print(f">>> installing: {package}@{version} ... DONE!")
                                            
          print("install global dependencies:")
          for package, version in ${{ vars.dependencies | safe }}.items():
              install(package, version)

          print("\ninstall staging dependencies:")
          for package, version in ${{ vars.staging_dependencies | safe }}.items():
              install(package, version)
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting .makim.yaml

</span></code>
</pre>
</div>

Now, let's create the users for the staging environment:


```python
!makim staging.create-users
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml
create admin users:
>>> creating user: admin1 ... DONE!
>>> creating user: admin2 ... DONE!
>>> creating user: admin3 ... DONE!

create staging users:
>>> creating user: staging1 ... DONE!
>>> creating user: staging2 ... DONE!
>>> creating user: staging3 ... DONE!

</span></code>
</pre>
</div>

Last but not least, let's run the install target:


```python
!makim staging.install
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml
install global dependencies:
>>> installing: dep1@v1 ... DONE!
>>> installing: dep2@v1.1 ... DONE!
>>> installing: dep3@v2.3 ... DONE!

install staging dependencies:
>>> installing: dep4@v4.3 ... DONE!
>>> installing: dep5@v1.1.1 ... DONE!

</span></code>
</pre>
</div>

### Defining Arguments

As we saw in the first example, **Makim** also allow us to use arguments. But we are not just able to define arguments, but we can also call dependencies with arguments and define a pre-conditional for that dependency as well.

Let's see how it works in practice:


```python
%%writefile .makim.yaml
version: 1.0.0
groups:
  print:
    env-file: .env
    targets:
      name:
        help: Print given name
        args:
          name:
            type: str
            required: true
        run: print("${{ args.name }}")
      list:
        help: Build the program
        args:
          i-am-sure:
            type: bool
        dependencies:
          - target: print.name
            if: ${{ args.i_am_sure == true }}
            args:
              name: Mary
          - target: print.name
            if: ${{ args.i_am_sure == true }}
            args:
              name: John
          - target: print.name
            if: ${{ args.i_am_sure == true }}
            args:
              name: Ellen
          - target: print.name
            if: ${{ args.i_am_sure == true }}
            args:
              name: Marc
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting .makim.yaml

</span></code>
</pre>
</div>


```python
!makim print.list
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml

</span></code>
</pre>
</div>


```python
!makim print.list --i-am-sure
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml
Mary
John
Ellen
Marc

</span></code>
</pre>
</div>

### Using environment variables

In the examples above, we have seem some usage of environment variables. In this section, we will have a quick overview about how to use it.

**Makim** allows us to use environment variables from environment files (.env) or directly inside the **Makim** configuration file in all three scopes: global, group and/or target.

Let's take a look into how it would look like:


```python
%%writefile .env
ENV=dev
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
%%writefile .makim.yaml
version: 1.0
env-file: .env
env:
  GLOBAL_VAR: "1"
groups:
  global-scope:
    env:
      GROUP_VAR: "2"
    targets:
      test-var-env-file:
        help: Test env variable defined in the global scope from env-file
        run: |
          import os
          assert str(os.getenv("ENV")) == "dev"

      test-var-env:
        help: Test env variable defined in the global scope in `env` section
        env:
          TARGET_VAR: "3"
        run: |
          import os
          # you can get an environment variable directly with xonsh/python
          assert str(os.getenv("GLOBAL_VAR")) == "1"
          # or you can get an environment variable using jinja2 tag
          assert "${{ env.GROUP_VAR }}" == "2"
          assert "${{ env.get("TARGET_VAR") }}" == "3"
          assert "${{ env.get("UNKNOWN_TARGET_VAR", "4") }}" == "4"
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting .makim.yaml

</span></code>
</pre>
</div>


```python
!makim global-scope.test-var-env-file
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml

</span></code>
</pre>
</div>


```python
!makim global-scope.test-var-env
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml

</span></code>
</pre>
</div>

### Using working-directory

**Makim** allows users to define specific working directory for any of the scopes: global, group, and/or target.

Let's see a simple example about how to use that:


```python
%%writefile .makim.yaml
version: 1.0
working-directory: "/tmp"

groups:
  check-wd:
    targets:
      is-tmp:
        help: Test if working directory is `tmp`
        run: |
          import os
          print(os.getcwd())
          assert os.getcwd() == "/tmp"
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Overwriting .makim.yaml

</span></code>
</pre>
</div>


```python
!makim check-wd.is-tmp
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Makim file: .makim.yaml
/tmp

</span></code>
</pre>
</div>

With these examples, we conclude this tutorial. This cover almost all the features, but of course, if you start to explore **Makim** you will find more interest ways to use the features presented here.

## How to Contribute

If you liked **Makim**, consider to contribute to the project! It will help us to move forward faster and help more people!

You can take a look into the project in our GitHub repo: https://github.com/osl-incubator/makim

For more information about how to contribute, please take a look into its [**Contributing Guide**](https://osl-incubator.github.io/makim/contributing/).

If you have any feedback about the tool, such as how we could improve the features and the user experience, please open an [issue](https://github.com/osl-incubator/makim/issues).
Any input and insights would be very appreciated!

## Conclusion

`Makim` represents a significant leap forward in build automation and dependency task management, combining the robust functionality of `make` with the clarity and simplicity of YAML. By following this guide, you should now have a solid foundation to start utilizing **Makim**.
