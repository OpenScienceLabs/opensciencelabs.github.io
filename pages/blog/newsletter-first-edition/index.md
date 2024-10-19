---
title: "OSL Newsletter First Edition"
slug: "osl-newsletter-first-edition"
date: 2024-10-19
authors: ["Mfonobong Uyah"]
tags: ["Newsletter", "OSL", "First Edition"]
categories: ["Newsletter"]
description: "The OSL newsletter is getting ready to launch. Our first release has been repurposed for this blog post but you can catch the next release right in your mail."
thumbnail: "/header.jpg"
template: "blog-post.html"
---

**Highlights:**

- OSL grant news 
- A little about the Python Software Foundation
- MAKIM development report
- ASTx development report
- Sugar development report 
- SciCookie development report 
- PyOpenSci’s Upcoming Fall Festival Event


## News: OSL receives PSF grant for its MAKIM and ASTx Projects

The Python Software Foundation (PSF) has agreed to fund two projects under the OSL umbrella. The projects are MAKIM and ASTx. Find out more about these projects and the ongoing PSF grant work in the following sections. 

## About the Python Software Foundation

The Python Software Foundation (PSF) is a nonprofit organisation dedicated to supporting the development of open-source projects linked to the Python language. Founded in March 2001, the PSF has grown to become an impactful and outstanding organisation sponsoring some of the most reputable Python-based open-source programs.

## MAKIM Improvements

Makim is a YAML-based task automation tool inspired by Make, offering structured definitions for tasks and dependencies with support for conditionals, arguments, grouping, variables, Jinja2 templating, and environment file integration. 

Our in-house team has made many recent updates to the project. A missing single quote was added to address an error related to a wrong command, enhancing command functionality. Support for interactive arguments was introduced, allowing for more dynamic user input. Dependency management was updated, specifically with the paginate library, while also resolving a CI installation issue to streamline the build process. Additionally, the attribute "shell" was refactored to "backend," improving code clarity. Finally, the configuration for MyPy was updated to ensure better type-checking practices.

Read more about MAKIM <a href="https://dev.to/opensciencelabs/streamlining-project-automation-with-makim-21nc">here</a>.
 
## ASTx Improvements

ASTx is a language-agnostic expression structure designed primarily for the ArxLang project, although it can be utilised by any programming language or parser to create a high-level representation of Abstract Syntax Trees (AST). It does not function as a lexer or parser. Its features include modular AST blocks, control flow structures (like if/else statements and for loops), integer data types (Int8 to Int64), binary and unary operators, object visibility (public and private), scope management (global and local), a symbol table organised by scope, and function declarations and calls. 

Our team has made several developmental improvements to ASTx, which include the addition of a new import statement feature allowing for improved module management, implementation of runtime type checking using Typeguard, enhancement of type safety and reliability, and update on the Prettier configuration as well as the MAKIM and CI steps to streamline the development and integration processes.

If you would like to read more on ASTx, <a href="https://opensciencelabs.org/blog/console-based-representation-in-astx/">go here</a>. 

## EXTRA: Sugar and SciCookie Both Have New Updates

MAKIM and ASTx are not the only projects getting new updates. The latest PRs on the Sugar repository have seen a fix for the Jinja2 template, another that refractors the interface for plugins/extensions and moves the main command to the compose group, and another that refractor and fixes the classes and CLI. On the SciCookie project, our team has added a smoke test for pyenv. 

Love to become a contributor? Jump on any open issues or make a PR for a new feature, fix, or test. 


<p>
    <img src=./study.jpeg alt ="Study Group">
</p>
<a href="https://discord.gg/Z7uqu82A">Jump to OSL Discord Group</a>
 

## Are you a Pythonista? Join the PyOpenSci Fall Festival 2024

Mark your calendars! Our partner is hosting a one-of-a-kind event. The PyOpenSci Fall Festival 2024 is an inaugural online meeting of Python, Open Science, and Open Source enthusiasts set to take place from October 28 to November 1, 2024. 

The event promises to feature big talks, essential hands-on workshops, and office hours with lots of industry experts exchanging ideas and sharing experiences. Go <a href="https://www.pyopensci.org/events/pyopensci-2024-fall-festival.html">here</a> to learn more.

## What Next? How To Get Started Learning About OSL Products and Activities

- Tour our website: Jump on the OSL website to explore information about our mission, vision, contribution guidelines, and much more. Visit our website now by simply clicking this link.  
 
- Become a member: Join the OSL Discord server. This is recommended if you have a technical background, especially regarding software development. But we also welcome new talents and enthusiasts. If you also want to contribute through server moderation or critical decision-making, our Discord server is the place to be. Come onboard using this link.
 
- Become one of our important connections: The OSL LinkedIn and X accounts are active. Here, you can get updates about published articles and events before they hit your email.  
 
- Explore our products and ideas: Visit our YouTube channel. There are already 12 insightful videos to watch on our channel with a lot more rolling out soon. See how to install and use our most popular tools and pick up new knowledge on programming languages, coding best practices, and past events.

<a align="center" href="https://www.youtube.com/@opensciencelabs/videos">Jump to Our YouTube Channel</a>. 

