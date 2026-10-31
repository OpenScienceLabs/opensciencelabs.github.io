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

Open Science Labs (OSL) shares these recommendations with affiliated projects,
including sub-organizations participating in GSoC with us. Projects may follow
them completely, select the parts that help, or adapt them to their language,
tooling, and community. Contributors should follow the practices their project
has adopted and ask maintainers when something is unclear.

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
  Projects can document or automate these commands to make onboarding easier;
  adopting a particular automation tool is optional.

## Keep Changes Small and Focused

- Aim for one clear purpose per pull request. Separate unrelated cleanup,
  formatting, dependency updates, and new features when practical.
- Discuss large features or refactoring with maintainers before implementation.
  Agree on smaller steps that can each be reviewed and checked.
- If a project chooses a pull request size guideline, treat it as a review aid
  and explain exceptions. Generated files and related tests may affect the size;
  line count alone does not determine whether a change is manageable.
- Follow the project's preferred way of updating branches, whether that is a
  merge or a rebase. Coordinate before rewriting a branch others use.

## Write Readable Code

- Use descriptive names and keep functions focused on a clear responsibility.
  Prefer straightforward code over unnecessary abstractions.
- Reduce deep nesting where it helps readability, for example with guard clauses
  or small helper functions. Around four levels can be a useful prompt to
  reconsider the structure, rather than a universal limit.
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

Use the project's installation instructions first. These commands apply to
projects with a `pre-commit` configuration; other projects may provide different
checks. Inspect any automatic changes and include only those relevant to your
contribution.

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

Projects can decide whether AI-assisted contributions are allowed and under
which conditions. Maintainers can publish that policy in their contribution
guide, including any disclosure expectations.

Where use is allowed, understand and verify every submitted change. Check APIs,
dependencies, tests, and explanations rather than assuming generated output is
correct. Remove irrelevant code and comments, respect confidentiality and
licensing obligations, and follow the project's disclosure policy. Contributors
remain responsible for explaining and maintaining their work. Review the
substance of a contribution; writing style or emojis alone do not establish
whether AI was used.

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
