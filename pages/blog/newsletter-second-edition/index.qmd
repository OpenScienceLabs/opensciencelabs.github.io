---
title: "Newsletter Second Edition"
slug: "newsletter-second-edition"
date: 2024-12-11
authors: ["Mfonobong Uyah"]
tags: ["Newsletter", "OSL", "Second Edition"]
categories: ["Newsletter"]
description: |
  The second edition of the OSL newsletter is here. Catch up on the latest updates from within and outside our organisation. Don't forget to share this resource with your network. 
thumbnail: "/header.jpg"
template: "blog-post.html"
---

**Highlights:**

- **Review of pyOpenSci Fall Festival 2024**
- **ArxLang/ASTx talk at PyConLadies2024**
- **Did You Know?**
- **What’s New in Software Development?**
- **More on MAKIM and ArxLang/ASTx Developments**
- **Open Study Group**

## Review: pyOpenSci Fall Festival 2024 in A Few Sentences

Our partner, pyOpenSci, just concluded the maiden edition of its Fall Festival. The highly anticipated event ran from October 28 to November 1, 2024, exposing participants to coding best practices, exciting sample projects, new tools and products, and games like Roast My Repo. The entire event was hosted on Spatial Chat.

If you were unable to attend this event, we got you covered. Here’s a brief summary of each day’s activities:

- Day 1: Keynote talks from Eric Ma, Melissa Medoca, and Rowan Cockett. These experts spoke on Open Science in Relation to biomedicine and LLMs, the impact of Open Source on Open Science, and how Markdown catalyses scientific computations through MySTMd.

- Day 2: A three-part session on formatting code, modularising code, and finally, testing code.

- Day 3: Insightful package creation tutorial using a template designed and owned by the pyOpenSci community.

- Day 4: Tips and tricks to effectively sharing a code. How to publish your package on TestPyPI, and add a DOI to your GitHub repo using Zenodo.

- Day 5: Reproducible reports with Quarto (interactive Python and R in your browser). Speech by George Stagg and demo by James Balamuta.

## News: ArxLang/ASTx talk at PyConLadies2024

Ana Krelling, an impeccable contributor to the OSL community, gave a talk tiled “ASTx: Empowering Language Processing Through Custom Abstract Syntax Trees” at the recently concluded PyConLadies 2024 event.

You can watch Ana's insightful session [here](https://www.youtube.com/watch?v=azVNQTFmuhA).

## Did You Know?

You can convert a Jupyter notebook to a script in the terminal
Once you have the terminal open, you can use it to run Jupyter notebooks as scripts by running:

```jupyter nbconvert --to script <notebook_name>.ipynb```

This converts the notebook into a Python script, which can then be executed directly from the terminal. You can also replace 'script' with any of the following; 'asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'slides', or 'webpdf'.

## What’s New in Software Development

**Linux Kernel 6.12 Has Been Released.**
The new update is intended to receive Long-Term Support (LTS), up until 2026. It reportedly comes packed with features such as real-time computing with PREEMPT_RT, hardware enhancements for AMD, Intel, and NVIDIA, and network improvements for DMTCP, IPv6 IOAM6, and PTP Timestamps.

Other pecks of the Linux Kernel 6.12 are driver updates, thermal core testing, file-backed mount support, guest PMU support, ARM permission overlay support, android guest support, and more. You can read more on this [here](https://www.developer-tech.com/news/linux-kernel-6-12-real-time-capabilities-hardware-boosts-and-more/).

## Updates: Recent Implementations from the Makim and ArxLang/ASTx teams

### Makim team

The updates introduce support for SSH-based command execution, along with a fix for the validate_config function name. It also includes the addition of initial infrastructure for SSH-related tests and a fix for the xonsh version. On the continuous integration (CI) side, the linter job was fixed, and a matrix strategy was added to improve testing coverage.

### ArxLang/ASTx team

The update adds the IfExpr and WhileExpr classes, while also fixing the argument type in the FunctionCall class. Additionally, the output for the ForRangeLoopExpr was improved, and support for boolean operators was added to the transpiler. The linter issues were also addressed and fixed.

## What’s Next? How to Get Started Learning About OSL Projects and Activities

- **Tour Our Website:** Explore our mission, vision, contribution guidelines,
  and more on the [OSL website](https://www.opensciencelabs.org).
- **Become a Member:** Join our
  [OSL Discord server](https://www.opensciencelabs.org/discord) to connect with
  like-minded individuals, contribute to discussions, and collaborate to project
  under OSL umbrella. Whether you have a technical background or are a new
  enthusiast, everyone is welcome!

- **Stay Connected:** Follow us on
  [LinkedIn](https://www.linkedin.com/company/opensciencelabs) and
  [X](https://twitter.com/opensciencelabs) to get updates about published
  articles and events before they hit your email.

- **Explore Our Projects and Ideas:** Visit our
  [YouTube channel](https://www.youtube.com/@opensciencelabs/videos). With 12
  insightful videos already available and many more rolling out soon, you can
  learn how to install and use our most popular tools, as well as gain knowledge
  on programming languages, coding best practices, and past events.

### Open Study Group

Join our Open Study Group! Everyone is welcome to participate in our dedicated one-hour sessions designed to support your personal studies. Use this online meeting space to focus on your work, ask questions, and share updates about your progress. Whether you're tackling a new project, learning a new skill, or simply seeking a quiet time to study, our study group provides a supportive and collaborative environment to help you achieve your goals. Come connect with fellow learners and make the most of your study time together!

This study group is sponsored by [LiteRev](https://literev.unige.ch/)!

Ask for more information on our [Discord](https://www.opensciencelabs.org/discord).
