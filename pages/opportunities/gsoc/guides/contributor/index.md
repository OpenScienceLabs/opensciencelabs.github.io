# Google Summer of Code (GSoC) Contributor Guide

These are Open Science Labs' (OSL) general recommendations for projects and
sub-organizations participating in Google Summer of Code (GSoC) under the OSL
umbrella. Maintainers can use, adapt, or incorporate these recommendations
partially or completely into their own project guidelines. Contributors: also
read the guidelines of the project you are contributing to. Official GSoC rules
and applicable codes of conduct still apply.

This guide covers applications, initial contributions, collaboration, and
[suggested practices for mentors and sub-organizations](#suggested-practices-for-mentors-and-sub-organizations).
See also the [Contribution Guidelines](../../../guides/contribution/index.md)
and [Coding Tips](../../../guides/coding-tips/index.md).

## Candidates' Guide

Use the following steps to prepare your application.

### How to Apply

#### Selecting a Sub-Organization/Project

Review the available sub-organizations and their projects. Choose a project that
aligns with your interests, skills, and learning goals.

#### Initiating Contact with Projects and Mentors

Introduce yourself to mentors in the designated communication channel. Explain
your interest and ask initial questions about the project or mentoring process.
Mentors: publish the contact channel and expected response times alongside the
project idea.

#### Making an Initial Contribution

Before opening a pull request, try a small, documented workflow and write a
short blog post or newcomer experience report covering:

- The project's mission, main objectives, and intended users.
- How to install or access it and complete one useful example, with reproducible
  instructions for other newcomers.
- What works well, what was confusing, and any setup or documentation obstacles.
- Constructive suggestions for improvement and what you learned.

Mentors: use this report as an initial selection criterion and announce the
task, expected effort, deadline, submission channel, and assessment criteria in
advance. Accept a Markdown document or draft shared with the team without
requiring a personal blog or a pull request. If setup fails, document the steps
tried and the blocker so mentors can assess your approach and help resolve the
problem.

Then agree on a small follow-up contribution with your mentor, such as improving
onboarding documentation, adding a test, or fixing a bug. Focus on useful work
and responding to feedback rather than maximizing the number of pull requests.

#### Crafting a Proposal with Mentor Support

Develop a detailed proposal with mentor feedback that outlines:

- **Milestones and Timeline:** Specific tasks and expected outcomes within the
  program period.
- **Contribution Impact:** How the work will further the project’s goals.
- **Language and Style:** Clear, informative, and objective language; concise
  and focused content without unnecessary filler or marketing-style phrasing.

Follow the published AI-use policy, disclose assistance as required, and verify
everything you submit. Write a proposal that reflects your own understanding and
be prepared to explain your choices. Mentors: assess understanding through the
work and discussion; writing style alone is not evidence of AI use.

Include a short "Newcomer insight" section describing an onboarding obstacle and
one suggested improvement. Use it to demonstrate what you learned from trying
the project and your attention to the proposal instructions.

Review the [contributor rules](https://summerofcode.withgoogle.com/rules) for
the program and follow the proposal template provided
[here](/opportunities/gsoc/templates/contributor-proposal).

## Review Process

Mentors: publish a selection checklist with minimum criteria and a separate
scoring rubric. Cover the introductory report, required proposal sections,
AI-policy compliance, agreed availability, and evidence of engagement.
Distinguish requirements that exclude an application from preferences used to
compare suitable candidates. Candidates: read both before applying.

Assess engagement through thoughtful questions, responses to feedback, progress
updates, support for peers, and follow-through on agreed tasks. Prioritize
quality and reliability over message counts or constant online presence. Give
**50% of the assessment to community engagement and 50% to technical
understanding and project planning**.

Provide clear feedback on proposals and discuss alternatives when another
project is a better fit. Candidates: notify mentors in the designated channel
when your proposal is ready for review. Keep general technical discussions
public and allow time for replies as mentors manage messages, issues, pull
requests, and reviews.

## Approved Contributors

For accepted candidates, the following guidelines serve as a roadmap for
successful collaboration during the GSoC program with Open Science Labs.

### Effective Workflow and Proactivity

- **Establish a Regular Workflow:** Work closely with your mentor to set clear
  weekly objectives.
- **Proactive Engagement:** Actively seek tasks, ask clarifying questions, and
  schedule regular check-ins to monitor progress.

### Communication Best Practices

- **Timely Updates:** Keep mentors informed about progress, challenges, and any
  required assistance.
- **Use Designated Channels:** Communicate via the project’s preferred platforms
  to ensure transparency and prompt feedback.

Send a brief daily status report to your mentor on agreed working days. Agree on
the channel and delivery window, accounting for time zones and planned absences.
Use a shared thread or project log so other mentors can also help. Include:

- **Progress:** What I worked on or learned, with links where relevant.
- **Next:** What I plan to do next.
- **Blockers:** What is preventing progress and what help I need.

Report blockers even when no code was completed. Mentors: review updates and
respond to requests for help. Respect agreed working days and absences. During
selection, announce any reporting exercise in advance and limit it to a short,
defined activity.

### Programming Best Practices

For practical suggestions on code readability, focused pull requests, testing,
and AI-assisted work, see OSL's
[Coding Tips](../../../guides/coding-tips/index.md).

- **Adherence to Standards:** Follow the coding standards and best practices
  outlined by your mentor and project guidelines.
- **Maintainable Code:** Write clean, well-documented, and maintainable code.
- **Constructive Feedback:** Embrace code reviews as opportunities to learn and
  improve your technical skills.

## Suggested Practices for Mentors and Sub-Organizations

Publish selection criteria and contributor expectations **before the selection
period begins**. Confirm the working agreement with selected contributors during
community bonding, including any agreed adjustments.

### Publish a Selection Checklist

Separate minimum requirements from scored preferences. For each minimum, state
what evidence is expected, the deadline, whether clarification or correction is
possible, and when failure to meet it excludes an application. For example:

- [ ] The applicant meets the current official GSoC eligibility requirements.
- [ ] The introductory project-use report meets the published criteria.
- [ ] The proposal includes the requested sections and demonstrates
      understanding of the project's goals.
- [ ] The candidate follows the published AI-use and disclosure policy.
- [ ] The candidate shows meaningful engagement and responds within agreed
      communication windows.
- [ ] Availability and proposed scope are realistic for the project.

Use the same published criteria consistently, document selection reasons, and
allow agreed accessibility or scheduling accommodations. Meeting the checklist
does not guarantee a slot. Additional project criteria are separate from
[Google's official rules](https://summerofcode.withgoogle.com/rules).

### Check That Instructions Were Read

Include a small, explicit, project-relevant instruction to check that candidates
read the guidance. Request a "Newcomer insight" section with one observation
from trying the project. Include it in the proposal instructions and checklist,
and explain how omissions are handled. Prefer a useful task over an unrelated
secret phrase or personal trivia; it gives mentors evidence they can discuss
with the candidate.

### Make the AI Policy Specific

Explain permitted and prohibited uses separately for proposals, introductory
reports, code, tests, and documentation. State whether editing, translation,
brainstorming, or code generation is allowed; what tools or data restrictions
apply; and how assistance should be disclosed. Describe how suspected violations
will be reviewed and let candidates explain their work. Link the policy from the
project idea, proposal instructions, and contribution guide.

### Give Community Engagement Explicit Weight

Assign **50% of the internal assessment to community engagement**. Use the
remaining 50% to assess technical understanding and planning during selection,
and agreed deliverables and code quality during the program. Publish the rubric,
evidence, and any minimum thresholds for both areas. For example:

| Area                                       | Weight | Evidence to consider                                                                                       |
| ------------------------------------------ | ------ | ---------------------------------------------------------------------------------------------------------- |
| Communication and reliability              | 20%    | Useful updates, timely replies within agreed windows, and early notice of blockers or absences.            |
| Collaboration and response to feedback     | 20%    | Constructive discussion, follow-through on review, and support for peers where opportunities arise.        |
| Learning and sharing project understanding | 10%    | Newcomer insights, documentation, or explanations that help others learn.                                  |
| Technical understanding and project work   | 50%    | A feasible proposal during selection; tested, documented progress against agreed goals during the program. |

Assess observable behavior rather than personality, English fluency, message
volume, or constant availability. Give newcomers a reasonable opportunity to
demonstrate each criterion. A strong engagement score does not remove the need
to meet agreed technical goals. Use this rubric for internal assessment
alongside the official GSoC evaluation requirements.

### Set Expectations and Address Problems Early

Share a contributor checklist before selection covering deliverables, reporting
frequency, response windows, check-ins, AI policy, review participation, and
evaluation criteria. Explain what happens when expectations are repeatedly
unmet. Also state mentor responsibilities, including availability, review
turnaround, and a backup contact. Keep a shared record of agreed changes.

If progress or engagement falls short, discuss specific examples privately,
identify blockers and any gaps in mentoring support, and agree on concrete next
steps and a review date. Distinguish persistent failure to follow through from
an agreed absence or a technical obstacle raised promptly.

Decline candidates who do not meet published selection criteria. During the
program, give an honest failing evaluation when agreed expectations remain
unmet; passing someone solely to avoid a difficult conversation helps neither
the contributor nor the project. Coordinate with OSL's organization
administrators, document the basis for the decision, and follow the current GSoC
evaluation process. Communicate concerns early and provide feedback before the
evaluation.

For official mentoring guidance, see
[Setting Expectations](https://google.github.io/gsocguides/mentor/setting-expectations),
[Selecting a Contributor](https://google.github.io/gsocguides/mentor/selecting-a-student),
and [Evaluations](https://google.github.io/gsocguides/mentor/evaluations).

## Proposal Resources

Consult the [GSoC Student Guide](https://google.github.io/gsocguides/student/)
for comprehensive details on the application process and proposal preparation.
Read Google's
[advice for contributors](https://developers.google.com/open-source/gsoc/help/student-advice)
and use the
[proposal template](/opportunities/gsoc/templates/contributor-proposal).
