---
title: "Three Years with Google Summer of Code: What I've Learned"
slug: three-years-with-google-summer-of-code-what-ive-learned
date: 2025-11-02
authors: ["Ivan Ogasawara"]
tags: [open-source, gsoc, mentoring]
categories: [gsoc]
description: |
  Three years in GSoC taught us one thing: mentoring matters more than code.
  As a 2025 mentoring org (with AlphaOneLabs, Extralit, Makim, Sugar), our 
  playbook is simple—balance mentors, set explicit contribution rules, meet 
  regularly; and for contributors: communicate publicly and ship small, 
  tested PRs.
thumbnail: "/header.png"
template: "blog-post.html"
---

# Three Years with Google Summer of Code: What I've Learned

Mentoring is at the heart of Open Science Labs (OSL). It's why we joined Google
Summer of Code (GSoC) in the first place. We started as a sub-organization under
the NumFOCUS umbrella for two years, and in 2025 we were accepted as a
**Mentoring Organization**. Huge thanks to **Anavelyz Pérez** for keeping us on
track. We’re pleased to have secured four contributor slots for 2025 with
**AlphaOneLabs**, **Extralit**, **Makim**, and **Sugar**.

We're incredibly proud of the contributors and mentors who made GSoC 2025 a
success. We were also, honestly, a bit heartbroken—many strong applicants did
real work and still didn't get in. On a personal note, attending the **GSoC
Summit** was a highlight: I met inspiring people and learned a lot from their
experiences.

Below are the lessons that stood out across these three years and practical
recommendations for organizers, mentors, and contributors.

---

## The Big Lesson

**GSoC isn't just about code—it's about mentoring.** Code is the artifact;
mentoring is the engine. The best summers happen when we design for learning,
clarity, and care. Everything else follows.

---

## Recommendations for Organizers

- **Confirm your slot count early.** The number of slots you _realistically_
  expect should shape how many projects you onboard and how you scope them.

- **Balance mentors as well as projects.** When allocating slots, distribute
  contributors across both projects _and_ mentors. Avoid situations where one
  mentor has two contributors while another has none—burnout and uneven support
  help no one.

---

## Recommendations for Mentors

- **Limit the number of projects per mentor.** The pre-selection phase is
  intense. If you're stretched across multiple proposals, candidates won't get
  the guidance they deserve. One well-mentored project beats three
  under-mentored ones.

- **Codify contribution rules up front.** Document expectations clearly and link
  them everywhere:

  - Max PR size (e.g., “prefer ≤300 lines; split larger changes”).
  - Stale PR policy (e.g., “no updates for 10 days → close or draft”).
  - Code style, linting, and formatting rules.
  - Clear stance on AI-generated code (allowed or not, and under what
    conditions).

- **Keep your CONTRIBUTING.md and PR template current.** Treat them as living
  documents. If you change the rules mid-summer, call it out in a pinned
  message.

- **Equip contributors to grow.** Share starter issues, architecture diagrams,
  walkthrough videos, and links to docs or talks. Provide “good first PR”
  examples.

- **Meet regularly.** Short weekly 1:1s or cohort calls work wonders. Use
  agendas. End with explicit next steps.

- **Nurture community, not competition.** Encourage contributors to help each
  other, co-review PRs, and pair on debugging. A supportive, respectful culture
  is non-negotiable.

- **Have a Plan B for great applicants who aren't selected.** If you have
  bandwidth, offer an internship track, micro-grants, or
  “fellows-without-funding” with mentorship and recognition. It keeps momentum
  and grows your contributor base.

---

## Recommendations for Contributors

- **Default to public communication.** Ask questions in the project's public
  channels. It helps others learn and shows the team how you collaborate.

- **If a mentor is unresponsive, switch projects.** They're likely overloaded;
  repeated pings won't help. Find a project with responsive maintainers and
  bandwidth for new contributors.

- **Avoid giant PRs.** Huge changes are hard to review and often get stuck. Ship
  small, focused PRs that follow the project's style and tests.

- **Show you understand the project's culture.** Read the docs. Match coding
  style. Follow the templates. Keep commits scoped and messages clear.

- **Be careful with AI-generated code.** Don't paste blindly. Understand the
  problem, explain your choices, remove unnecessary comments, and **never**
  include emojis in code comments.

- **Discuss big changes before you implement them.** Don't refactor core
  components or alter architecture without buy-in. Open an issue, propose a
  design, gather feedback.

- **Ship tests and pass CI.** If you fix a bug or add a feature, include tests.
  Make sure CI is green before asking for review.

- **Write a crisp proposal.** Be clear, specific, and concise (≤10 pages).
  Demonstrate understanding of the project and outline concrete steps,
  milestones, and risks. Ask maintainers for early feedback so you have time to
  refine.

---

## Looking Ahead

I'm excited to keep participating in GSoC in the coming years and to keep
welcoming new contributors into open-source communities. Thank you to the GSoC
team for running this program year after year—it raises the visibility of
projects, gives newcomers a safe place to learn from experts, and strengthens
the open-source ecosystem. For hundreds of students and first-time contributors,
GSoC isn't just a summer; it's a beginning.
