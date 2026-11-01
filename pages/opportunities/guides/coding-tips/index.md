---
title: "Coding Tips"
description:
  "Practical coding recommendations that OSL-affiliated projects and GSoC
  sub-organizations can adopt or adapt."
date: "2026-10-31"
authors: ["OSL Team"]
template: single-sidebar.html
---

# Coding Tips

These are Open Science Labs' (OSL) general coding recommendations for affiliated
projects, including sub-organizations participating in GSoC under the OSL
umbrella. Maintainers can use, adapt, or incorporate these recommendations
partially or completely into their own project guidelines. Contributors: also
read the guidelines of the project you are contributing to.

For collaboration and mentoring suggestions, see our
[Contribution Guidelines](../contribution/index.md). This page focuses on the
technical side of a contribution.

## Start with the Project's Workflow

- Read `CONTRIBUTING.md`, the development documentation, and nearby code before
  editing. Use the project's existing patterns and tools.
- Set up the documented development environment and install dependencies using
  the project's configuration or lock files. An isolated environment helps avoid
  conflicts with other projects and makes problems easier to reproduce.
- Run the relevant checks before changing code so you can distinguish existing
  failures from those introduced by your work.
- Reuse the project's commands for testing, formatting, and documentation.
  Document and automate recurring commands to make onboarding easier.

## Keep Changes Small and Focused

- Aim for one clear purpose per pull request. Separate unrelated cleanup,
  formatting, dependency updates, and new features when practical.
- Discuss large features or refactoring with maintainers before implementation.
  Agree on smaller steps that can each be reviewed and checked.
- Use pull request size guidelines as a review aid and explain exceptions.
  Account for generated files and related tests when assessing size; consider
  complexity and scope alongside line count.
- Follow the project's preferred way of updating branches, whether that is a
  merge or a rebase. Coordinate before rewriting a branch others use.

## Write Readable Code

- Use descriptive names and keep functions focused on a clear responsibility.
  Prefer straightforward code over unnecessary abstractions.
- Reduce deep nesting where it helps readability, for example with guard clauses
  or small helper functions. At around four levels, review the structure for
  opportunities to simplify it.
- Keep comments that explain intent, constraints, scientific assumptions, or
  non-obvious decisions. Remove outdated comments and those that only repeat the
  code. Clear comments and documentation are valuable even when code is
  readable.
- Keep comments professional and consistent with project style; avoid decorative
  emojis unless the project uses them for a specific purpose.
- Use the project's formatter and whitespace conventions. End text files with a
  newline; this does not require adding an extra blank line.

## Use Automated Checks Where Available

If the project uses `pre-commit`, install its configured hooks in your local
checkout and run them before requesting review:

```bash
pre-commit install
pre-commit run --all-files
```

Install the development dependencies first. These commands use the repository's
`pre-commit` configuration. Inspect automatic changes and include only those
relevant to your contribution.

Run the checks appropriate to the change, such as formatting, linting, type
checking, or documentation builds. Review continuous integration (CI) results
and investigate failures. If a check cannot run locally, explain the limitation
in the pull request so reviewers know what remains unverified.

## Test Behavior and Update Documentation

- For a bug fix, add a regression test that demonstrates the problem and passes
  with the fix when practical.
- For new behavior, cover expected use, relevant edge cases, and failure cases.
  Use the project's existing testing framework and conventions.
- Keep tests reproducible. Use small fixtures and control randomness, external
  services, or other sources of variability where appropriate.
- Update examples, API documentation, or setup instructions when the change
  affects them. For scientific code, document assumptions and validate results
  against suitable reference cases.
- Describe how you checked the change, including commands and results, in the
  pull request. Passing CI supports review but does not replace understanding
  the code or checking that it solves the intended problem.

## Use AI Tools Responsibly

Maintainers: publish an AI-use policy in the contribution guide. State which
activities allow AI assistance, which uses are prohibited, and what disclosure
is expected.

Contributors: follow the AI-use policy and understand and verify every submitted
change. Check APIs, dependencies, tests, and explanations rather than assuming
generated output is correct. Remove irrelevant code and comments, respect
confidentiality and licensing obligations, and follow the project's disclosure
policy. Contributors remain responsible for explaining and maintaining their
work. Review the substance of a contribution; writing style or emojis alone do
not establish whether AI was used.

## Before Requesting Review

- Read your own diff and remove accidental or unrelated changes.
- Summarize the problem, approach, and any tradeoffs; link related issues.
- Include test results, documentation updates, and any known limitations.
- Keep unfinished work in draft when the platform supports it, and use the
  project's agreed channel when it is ready for review.

## Learn More from the OSL Blog

- [First Time Contributors](../../../blog/first-time-contributors/index.md):
  development environments, documentation, testing, and contribution workflows.
- [Three Years with Google Summer of Code: What I've Learned](../../../blog/three-years-with-google-summer-of-code-what-ive-learned/index.md):
  small pull requests, early design discussions, and learning through mentoring.
- [Streamlining Project Automation with Makim](../../../blog/streamlining-project-automation-with-makim/index.md):
  an example of organizing repeatable project tasks. Follow your project's
  current setup instructions when applying ideas from older tutorials.
