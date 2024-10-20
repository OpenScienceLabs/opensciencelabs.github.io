---
title: "Newsletter First Edition"
slug: "newsletter-first-edition"
date: 2024-10-19
authors: ["Mfonobong Uyah"]
tags: ["Newsletter", "OSL", "First Edition"]
categories: ["Newsletter"]
description: |
  The OSL newsletter is launching soon! Our first edition has been repurposed
  for this blog post, but you can subscribe to receive future releases directly
  in your inbox.
thumbnail: "/header.jpg"
template: "blog-post.html"
---

**Highlights:**

- **OSL Grant News**
- **PyOpenSci’s Upcoming Fall Festival Event**
- **OSL Projects Development Report**
- **Open Study Group**

## News: OSL Receives PSF Grant for MAKIM and ASTx Projects

We're thrilled to announce that the Python Software Foundation (PSF) has granted
funding to two of our key projects: **MAKIM** and **ASTx**. This support will
help accelerate development and enhance the capabilities of these tools. Read on
to learn more about these projects and the impact of the PSF grant.

### About the Python Software Foundation

Founded in March 2001, the Python Software Foundation (PSF) is a nonprofit
organization dedicated to advancing and promoting the Python programming
language. The PSF supports a wide range of open-source Python projects,
fostering a vibrant and inclusive community.

## Are You a Pythonista? Join the PyOpenSci Fall Festival 2024

Mark your calendars! Our partner is hosting a one-of-a-kind event. The
**PyOpenSci Fall Festival 2024** is an inaugural online meeting of Python, Open
Science, and Open Source enthusiasts set to take place from October 28 to
November 1, 2024.

The event promises to feature insightful talks, essential hands-on workshops,
and office hours with numerous industry experts exchanging ideas and sharing
experiences.
[Go here](https://www.pyopensci.org/events/pyopensci-2024-fall-festival.html) to
learn more.

## OSL Projects Development Report

### MAKIM Improvements

**MAKIM** is a YAML-based task automation tool inspired by Make. It offers
structured definitions for tasks and dependencies, supporting conditionals,
arguments, grouping, variables, Jinja2 templating, and environment file
integration.

Makim team has made several recent updates to the project, including the
addition of new features supported by the PSF grant.

- Added support for checking the .makim.yaml structure with a schema definition.
- Added support for matrix variables for tasks.
- Changed from dependencies support to hooks with pre and post run support.
- Fixed text problems and issues in the continuous integration jobs.
- Introduced support for interactive arguments, allowing for more dynamic user
  input.
- Refactored the attribute "shell" to "backend," improving code clarity.
- Updated the configuration for MyPy to ensure better type-checking practices.

Read more about MAKIM
[here](https://dev.to/opensciencelabs/streamlining-project-automation-with-makim-21nc).

### ASTx Improvements

**ASTx** is a language-agnostic expression structure designed primarily for the
ArxLang project. However, it can be utilized by any programming language or
parser to create high-level representations of Abstract Syntax Trees (AST).

ArxLang team has made several developmental improvements to ASTx, including the
addition of new features supported by the PSF grant:

- Added a new import statement feature for improved module management.
- Implemented runtime type checking using Typeguard.
- Enhanced type safety and reliability.
- Improved the development configuration structure, and dependencies.
- Added a transpiler from astx to python
- Added support to complex32 and complex64
- Added support to float16, and float64
- Added support to uint8, uint16, unit32, uint64, uint128

If you would like to read more on ASTx,
[go here](https://opensciencelabs.org/blog/console-based-representation-in-astx/).

### Sugar and SciCookie Both Have New Updates

**Sugar** and **SciCookie** are not the only projects receiving updates. The
latest PRs on the Sugar repository include:

- Added support for checking the .sugar.yaml structure with a schema definition.
- A fix for the Jinja2 template.
- A refactor of the interface for plugins/extensions that moves the main command
  to the compose group.

On the SciCookie project, SciCookie team has added some feature and
improvements:

- Improved tests and infrastructure.
- Added support to pixi with pyproject.
- Added support to circleci.

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

Join our Open Study Group! Everyone is welcome to participate in our dedicated
one-hour sessions designed to support your personal studies. Use this online
meeting space to focus on your work, ask questions, and share updates about your
progress. Whether you're tackling a new project, learning a new skill, or simply
seeking a quiet time to study, our study group provides a supportive and
collaborative environment to help you achieve your goals. Come connect with
fellow learners and make the most of your study time together!

Ask for more information on our [Discord](https://www.opensciencelabs.org/discord).
