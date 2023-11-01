---
title: "Google Summer of Code- Week 4th & 7th Midterm Evaluation"
slug: google-summer-of-code-week-4th-and-7th-midterm-evaluation
date: 2023-07-25
authors: ["Ankit Kumar"]
tags: [google summer of code, gsoc, open-source open-sciencelab]
categories: [open-source, gsoc]
description: |
  In this article, I will share the progress for Week 4th week to 7th week for my
  contribution to Open-science labs as a part of Google Summer of Code 2023.
thumbnail: "/GSoC-Vertical.png"
---

## Google Summer of Code- Week 4th & 7th Midterm Evaluation

In this article, I will share the progress for Week 4th week to 7th week for my
contribution to Open-science labs as a part of Google Summer of Code 2023.

 <img src="GSoC-Vertical.png" width="400">

As my Google Summer of Code journey continued, I found myself faced with an
exciting yet daunting task: implementing a whole new build-system as an option
for templates in the esteemed Open-Science Lab. This endeavor demanded
meticulous planning, unwavering dedication, and the exploration of various
build-systems, including Maturin, Hatchling, Scikit-build, and `pybuild11`.

In this period, I started working on to add support for `Maturin` build-system.

### Maturin

[**Maturin**]() was the first build-system I explored. Its unique approach of
building Python bindings for Rust libraries intrigued me, and I wondered if it
could provide a novel solution to the lab's needs. The seamless blending of
Python and Rust offered the potential for unparalleled performance and memory
efficiency in research projects. However, I faced a steep learning curve to
master the intricacies of Rust and its integration with Python. Overcoming these
challenges was a significant achievement, and I managed to create a functional
prototype that demonstrated Maturin's potential to revolutionize the
Open-Science Lab's workflow. My contribution to this issue is
[here](https://github.com/osl-incubator/scicookie/pull/152)

After merging this pull request, I started to add support for `Hatchling`
build-system.

### Hatchling

[**Hatchling**]() known for its user-friendly nature, was my next target. It
promised to simplify the build and deployment processes, which could be
particularly beneficial for newcomers to the lab and projects with
straightforward requirements. Integrating Hatchling into the lab's ecosystem
required thorough documentation and integration tests to ensure its smooth
adoption. Overcoming initial hurdles, I was elated to see the positive response
from the lab's community as they began adopting Hatchling for their projects. My
contribution to this issue is
[here](https://github.com/osl-incubator/scicookie/pull/144)

After completetion of this issue, I jumped to a task to add support for
`Scikit-Build-Core`.

### Scikit-build-core

[**Scikit-build-core**]() a cross-platform build-system, offered a robust option
for integrating CPython extensions. While challenging to implement, I recognized
its potential to support projects with complex native code dependencies. My
experience with Scikit-build exposed me to advanced build and packaging
concepts, and I was thrilled to see it complementing the existing build-systems
in the lab, catering to a broader range of projects. My contribution to this
issue is [here](https://github.com/osl-incubator/scicookie/pull/161)

### Conclusions

In conclusion, my Google Summer of Code experience with implementing new
build-systems for the Open-Science Lab was a transformative journey. Overcoming
hurdles with Maturin, embracing user-friendliness with Hatchling, exploring the
potential of Scikit-build.I realized the importance of innovation and
adaptability in the world of open-source development. This experience has not
only enriched my technical skills but also instilled in me a passion for
contributing to projects that drive positive change in the world of scientific
research. As I look to the future, I am excited to continue this journey,
collaborating with the open-source community to create solutions that empower
researchers and advance the boundaries of knowledge.

You can read my previous blog [here](https://medium.com/@ayeankit)

If want to connect with me on LinkedIn
[here](https://www.linkedin.com/in/ayeankit/). Github
[here](https://github.com/ayeankit).
