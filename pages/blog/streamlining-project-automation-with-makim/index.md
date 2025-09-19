---
title: "Streamlining Project Automation with Makim"
slug: "streamlining-project-automation-with-makim"
date: 2024-03-18
authors: ["Ivan Ogasawara"]
tags: ["makim", "automation", "devops", "open-source"]
categories: ["devops", "automation", "python"]
description: |
  In software development, where efficiency, consistency, and reliability are paramount,
  automation tools play a crucial role. Makim, an innovative open-source tool, steps
  into the spotlight to improve automation workflows. It simplifies script execution,
  environment management, and task dependencies, positioning itself as a great asset in
  modern development environments.
  environment.
thumbnail: "/header.png"
template: "blog-post.html"
---
# Streamlining Project Automation with Makim

In software development, where efficiency, consistency, and reliability are paramount, automation tools play a crucial role. Makim, an innovative open-source tool, steps into the spotlight to improve automation workflows. It simplifies script execution, environment management, and task dependencies, positioning itself as a great asset in modern development environments.

## Introducing Makim

`Makim` elevates project automation by offering a structured, yet flexible approach to manage routine tasks, complex task dependencies, and environment configurations. Its design is centered around the `.makim.yaml` configuration file, allowing developers to orchestrate their workflows with precision and ease. Unlike traditional script execution tools, Makim's Python-based architecture and support for multiple programming languages and shells enhance its versatility and applicability across diverse projects.

Especially suited for DevOps Engineers and Software Developers, Makim eliminates redundancy in automation tasks. Its core functionality extends beyond simple script execution, encompassing:

- Argument definition for scripts
- Organization of tasks into groups
- Advanced dependency management between tasks
- Utilization of environment variables and custom variables
- Dynamic content generation with Jinja2 templates
- Specification of working directories for tasks
- Execution flexibility through support for multiple interpreters or shells

Despite its broad capabilities, Makim currently lacks support for Windows but plans to extend its compatibility in future versions.

## Getting Started with Makim

### Installation

Makim can be installed via `pip` or `conda`, catering to different setup preferences:

- To install `Makim` using `pip`, run:


```python
!pip install -q "makim==1.14.0"
```

- For those who prefer `conda`, execute:

  ```
  conda install "makim=1.14.0"
  ```

Given Makim's active development, pinning to a specific version is recommended to ensure consistency.

For this tutorial, we will disable the output color feature provided by typer, the command-line interface engine used by **Makim**.


```python
import os

os.environ["NO_COLOR"] = "1"
```

### Configuring `.makim.yaml`

The `.makim.yaml` file is the foundation of your Makim configuration. Here's how to start:

1. **Create the `.makim.yaml` File**: Place this file at the root of your project directory.
   
2. **Define Your Automation Tasks**: Configure your tasks, specifying actions, arguments, and dependencies. For example:


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

This setup demonstrates Makim's ability to manage tasks with conditional logic and dependencies.

### Exploring Makim's CLI

Makim's CLI provides insights into available commands, arguments, and configurations through the auto-generated help menu:


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
                                                                                
 Usage: makim [OPTIONS] COMMAND [ARGS]...                                       
                                                                                
Makim is a tool that helps you to organize and simplify your helper commands.

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --version             -v            Show the version and exit                │
│ --file                        TEXT  Makim config file [default: .makim.yaml] │
│ --dry-run                           Execute the command in dry mode          │
│ --verbose                           Execute the command in verbose mode      │
│ --install-completion                Install completion for the current       │
│                                     shell.                                   │
│ --show-completion                   Show completion for the current shell,   │
│                                     to copy it or customize the              │
│                                     installation.                            │
│ --help                              Show this message and exit.              │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ clean.tmp        Use this target to clean up temporary files                 │
│ tests.unit       Build the program                                           │
╰──────────────────────────────────────────────────────────────────────────────╯

If you have any problem, open an issue at:
https://github.com/osl-incubator/makim



</span></code>
</pre>
</div>

This feature facilitates easy access to Makim's functionalities, enhancing usability and understanding of the tool.

### Executing Your First Commands

With your `.makim.yaml` file set up, you can begin to use `makim`:


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

In the case you type your command wrong, **Makim** will suggest you some alternative:


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
Usage: makim [OPTIONS] COMMAND [ARGS]...
Try 'makim --help' for help.
╭─ Error ──────────────────────────────────────────────────────────────────────╮
│ No such command 'tests.unittest'.                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
Command tests.unittest not found. Did you mean tests.unit'?

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
bash completion installed in /home/xmn/.bash_completions/makim.sh
Completion will take effect once you restart the terminal

</span></code>
</pre>
</div>

After this command you will need to restart the terminal in order to use this auto-completion feature.

## Advanced Features and Examples

Makim's adaptability is showcased through various features and practical examples:

- **Conditional Dependencies and Arguments**: Define complex task dependencies with conditional execution based on passed arguments.
- **Dynamic Configuration with Jinja2**: Leverage Jinja2 templates for advanced scripting and dynamic content generation.
- **Environment and Custom Variable Management**: Organize and utilize variables effectively across different scopes of your project.
- **Specifying Working Directories**: Control the execution context of your tasks by setting working directories.

These examples underscore Makim's capability to accommodate intricate automation scenarios, streamlining development workflows.

## Exploring Makim Through Examples

### Utilizing Various Interpreters

Makim extends its functionality beyond conventional script execution by supporting various interpreters and shell languages, facilitating a versatile development environment. While **xonsh** is the default interpreter - blending the capabilities of Bash and Python for an enriched command-line experience - Makim's architecture allows for seamless integration with other environments. For developers seeking to leverage this feature, a foundational understanding of **xonsh** can be beneficial. Comprehensive details and usage guidelines are available in the [official xonsh documentation](https://xon.sh/).

This section demonstrates executing straightforward commands across multiple interpreters, showcasing Makim's adaptability to diverse programming contexts.


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
                                                                                
 Usage: makim [OPTIONS] COMMAND [ARGS]...                                       
                                                                                
Makim is a tool that helps you to organize and simplify your helper commands.

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --version             -v            Show the version and exit                │
│ --file                        TEXT  Makim config file [default: .makim.yaml] │
│ --dry-run                           Execute the command in dry mode          │
│ --verbose                           Execute the command in verbose mode      │
│ --install-completion                Install completion for the current       │
│                                     shell.                                   │
│ --show-completion                   Show completion for the current shell,   │
│                                     to copy it or customize the              │
│                                     installation.                            │
│ --help                              Show this message and exit.              │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ tests.node             Test using nodejs                                     │
│ tests.perl             Test using perl                                       │
│ tests.python           Test using php                                        │
│ tests.r                Test using R                                          │
│ tests.run-all          Run tests for all the other targets                   │
│ tests.sh               Test using sh                                         │
╰──────────────────────────────────────────────────────────────────────────────╯

If you have any problem, open an issue at:
https://github.com/osl-incubator/makim



</span></code>
</pre>
</div>

Prior to executing these targets, it is necessary to install the required dependencies:


```python
!mamba install -q -y perl nodejs r-base sh 
```

Proceed to execute all defined targets by invoking the run-all target, which encapsulates all other targets as its dependencies for a sequential execution process:


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
(node:1634785) Warning: The 'NO_COLOR' env is ignored due to the 'FORCE_COLOR' env being set.
(Use `node --trace-warnings ...` to show where the warning was created)
Running Makim: Hello, World, from Perl!
Running Makim: Hello, World, from Python!
[1] "Running Makim: Hello, World, from R!"
Running Makim: Hello, World, from sh!

</span></code>
</pre>
</div>

In scenarios where your chosen interpreter supports debugging - such as Python or Xonsh through the use of `breakpoint()` - you can introduce a breakpoint within your code. This enables the debugging of your **Makim** target, allowing for an interactive examination of the execution flow and variable states.

### Using Variables (vars)

**Makim** facilitates the definition of variables within the `.makim.yaml` configuration, supporting all the **YAML** data types, including strings, lists, and dictionaries. This feature enhances script configurability and reusability across different tasks and environments.

Consider reviewing the provided example to understand how to effectively leverage variables in your **Makim** configurations:


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

Now, let's proceed to create users within the staging environment:


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

**Makim** enhances script flexibility by allowing the use of arguments. It enables not only the definition of arguments for tasks but also the passing of arguments to dependencies and the specification of conditions for those dependencies.

Explore this functionality through this example:


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

### Utilizing Environment Variables

The previous sections demonstrated the use of environment variables. Here, we'll delve into their application in more detail.

**Makim** permits the incorporation of environment variables from `.env` files or directly within the `.makim.yaml` file, applicable at global, group, and target levels.

Examine an example to understand the implementation:


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

### Specifying the Working Directory

Makim provides the capability to set a specific working directory for tasks at any scope: global, group, or target.

Review a straightforward example to learn how to apply this feature:


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

This tutorial concludes with a showcase of Makim's key features. While this overview covers the essentials, diving deeper into **Makim** will reveal more advanced and intriguing ways to leverage its capabilities.

## Contributing to Makim

Makim's growth is propelled by its community. Contributions, whether through code, documentation, or feedback, are welcome. Explore the [GitHub repository](https://github.com/osl-incubator/makim) and consider contributing to foster Makim's development.

## Conclusion

Makim stands out as a transformative tool in project automation, bridging the gap between simplicity and complexity. Its comprehensive feature set, coupled with the flexibility of its configuration, makes Makim a quintessential tool for developers and DevOps engineers alike. As you incorporate Makim into your projects, its impact on enhancing productivity and consistency will become evident, marking it as an indispensable part of your development toolkit.

Dive deeper into Makim's functionalities by visiting the [official documentation](https://github.com/osl-incubator/makim). Try it and let us know your thoughts about it!
