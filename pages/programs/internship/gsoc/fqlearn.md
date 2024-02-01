---
title: "GSoC - fqlearn Project Ideas"
description: "GSoC - fqlearn Project Ideas"
date: "2024-01-29"
authors: ["OSL Team"]
---

[&lt;&lt; Back](/programs/internship/gsoc)

# fqlearn

## Project Idea 1: Improve SteamTable module

### Abstract

SteamTable is a module to display and extract thermodynamic data on the state of
water.

### License

https://github.com/osl-pocs/fqlearn/blob/main/LICENSE

### Code of Conduct

https://github.com/osl-pocs/fqlearn/blob/main/CODE_OF_CONDUCT.md

### Current State

It is currently implemented, but a review and verification needs to be carried
out to see if the data shown is correct.

### Tasks

- Verify the correctness of data.
- Create Test for the module
- Improve Plotting

### Expected Outcomes

- Test against correct data
- Improved plotting with more explanatory text or plotted text.

### Details

- Prerequisites:
    - Python
    - Numerical Analysis
    - Knowledge in thermodynamics
- Expected Time: 350 hours
- Potential Mentor: Ever Vino

### References

- https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html
- https://www.thermopedia.com/content/1150/

---

## Project Idea 2: Add three component graphical solver

### Abstract

The three-component module will include the possibility of solving
three-component systems in liquid-liquid and solid-liquid extraction processes.

### License

https://github.com/osl-pocs/fqlearn/blob/main/LICENSE

### Code of Conduct

https://github.com/osl-pocs/fqlearn/blob/main/CODE_OF_CONDUCT.md

### Current State

Not implement

### Tasks

- Search experimental data for the most used three-components systems in the
  industry.
- Search methods to solve those systems
- Implement a module to allows solve graphically the three-component system.

### Expected Outcomes

- Experimental data inside the module as csv or posgres data
- A class called three component system to solve graphically three-system
  problems
- Unit tests for the module

### Details

- Prerequisites:
    - Python
    - Numerical Analysis
    - Basic knowledge in mass transfer
- Expected Time: 350 hours
- Potential Mentor: Ever Vino

### References

- https://www.jyoungpharm.org/sites/default/files/JYoungPharm_10_2_132_1.pdf
- https://www.theengineersperspectives.com/how-does-liquid-liquid-extraction-work/

[&lt;&lt; Back](/programs/internship/gsoc)
