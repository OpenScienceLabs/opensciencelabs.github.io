# Google Summer of Code (GSoC) Guide

These are Open Science Labs' (OSL) general recommendations for projects and
sub-organizations participating in Google Summer of Code (GSoC) under the OSL
umbrella. Organization admins and maintainers can use, adapt, or incorporate
these recommendations partially or completely into their own project guidelines.
Contributors: also read the guidelines of the project you are contributing to.
Official GSoC rules and applicable codes of conduct still apply.

Find the recommendations for your role:

- [Organization Admins](#organization-admins): coordinate participation, mentor
  capacity, selection, and evaluation across projects.
- [Mentors](#mentors): prepare project guidance, assess candidates, and support
  contributors throughout the program.
- [Contributor Candidates](#contributor-candidates): get to know the community,
  use the software, prepare an application, and collaborate after selection.

See also the [Contribution Guidelines](../../../guides/contribution/index.md)
and [Coding Tips](../../../guides/coding-tips/index.md).

## Organization Admins

### Coordinate Participation and Mentor Capacity

Confirm which affiliated projects intend to participate in the upcoming GSoC
edition and which project ideas they plan to submit. Distinguish planned
participation from confirmed participation when communicating with candidates.
Keep project ideas, contacts, and participation updates easy to find.

Confirm mentor availability and backup coverage before offering project ideas.
Balance contributor allocations across projects and mentors, and keep the scope
within the mentoring capacity available. Do not promise candidates a place
before selection and slot allocation are complete.

Publish the organization contact channel, selection timeline, and escalation
route for candidates and mentors. Use OSL's coordination channels for matters
across projects and each project's preferred community channel for its work.

### Publish the Selection Framework

Publish common selection criteria, the assessment rubric, and evaluation
expectations **before the selection period begins**. Coordinate with mentors to
make project-specific criteria equally clear. Separate minimum requirements that
exclude an application from scored preferences used to compare suitable
candidates.

For each minimum requirement, state the evidence, deadline, whether correction
or clarification is possible, and how unmet criteria affect selection. Use the
same published criteria consistently, record selection reasons, and account for
agreed accessibility or scheduling accommodations. Meeting the checklist does
not guarantee a slot. Review the current
[official GSoC rules](https://summerofcode.withgoogle.com/rules) when defining
eligibility and selection procedures.

### Give Community Engagement Explicit Weight

Assign **50% of the internal assessment to community engagement**. Use the
remaining 50% to assess technical understanding and planning during selection,
and agreed deliverables and code quality during the program. Publish the rubric,
evidence, and minimum thresholds for both areas. For example:

| Area                                       | Weight | Evidence to consider                                                                                       |
| ------------------------------------------ | ------ | ---------------------------------------------------------------------------------------------------------- |
| Communication and reliability              | 20%    | Useful updates, timely replies within agreed windows, and early notice of blockers or absences.            |
| Collaboration and response to feedback     | 20%    | Constructive discussion, follow-through on review, and support for peers where opportunities arise.        |
| Learning and sharing project understanding | 10%    | User experience reports, documentation, or explanations that help others learn.                            |
| Technical understanding and project work   | 50%    | A feasible proposal during selection; tested, documented progress against agreed goals during the program. |

Assess observable behavior rather than personality, English fluency, message
volume, or constant availability. Give newcomers a reasonable opportunity to
demonstrate each criterion. A strong engagement score does not remove the need
to meet agreed technical goals. Use this rubric for internal assessment
alongside the official GSoC evaluation requirements.

### Support Consistent Decisions and Resolve Problems

Check that mentors publish their expectations before selection, provide timely
feedback, and have enough capacity to support their contributors. Arrange backup
support when a mentor is unavailable.

Review concerns and evaluation decisions with mentors, including evidence of
missed expectations, support provided, and feedback shared with the contributor.
Address gaps in mentoring support as well as contributor engagement. Follow the
current GSoC evaluation process and communicate decisions clearly.

<a id="suggested-practices-for-mentors-and-sub-organizations"></a>

## Mentors

### Prepare the Project and Welcome Candidates

Publish the preferred community app or communication channel, contact details,
and expected response times alongside the project idea. Explain the project's
mission, intended users, main workflows, and development setup. State which
ideas are planned for the upcoming GSoC edition and update candidates when plans
change.

Provide a manageable starting workflow and examples of helpful contributions,
including documentation, tests, and bug fixes. Encourage candidates to spend
several days using the software before rushing into a pull request. For a tool
or library, suggest different use cases and realistic tasks so candidates can
understand both its strengths and its limitations.

### Use a Project Experience Report as the First Contribution

Ask candidates to write a blog post or newcomer experience report from a user's
perspective. Use it as an initial selection criterion and announce the expected
effort, deadline, submission channel, and assessment criteria in advance.

Assess what the candidate tried, how clearly they explain the software, what
they learned, and the usefulness of their observations. Value reproducible
examples and constructive suggestions. Accept a Markdown document or draft
shared with the team without requiring a personal blog or a pull request. If
setup fails, review the steps attempted and the blocker, and help the candidate
move forward.

Keep the task manageable and give candidates time to explore. Do not require a
long history of contributions; use the activity to help newcomers develop and
demonstrate understanding.

### Publish a Project Selection Checklist

Align project criteria with the organization's selection framework. For example:

- [ ] The applicant meets the current official GSoC eligibility requirements.
- [ ] The project experience report meets the published criteria.
- [ ] The proposal explains the project's goals and includes the requested
      sections.
- [ ] The candidate follows the published AI-use and disclosure policy.
- [ ] The candidate shows meaningful engagement and responds within agreed
      windows.
- [ ] Availability and proposed scope are realistic for the project.

Include a small, explicit, project-relevant instruction to check that candidates
read the guidance. Request a "Newcomer insight" proposal section with one
observation from trying the software. Include it in the instructions and
checklist, and explain how omissions are handled. Use the response to discuss
the candidate's experience and understanding.

### Make the AI Policy Specific

Explain permitted and prohibited uses separately for proposals, experience
reports, code, tests, and documentation. State whether editing, translation,
brainstorming, or code generation is allowed; what tools or data restrictions
apply; and how assistance must be disclosed. Link the policy from the project
idea, proposal instructions, and contribution guide.

Assess understanding through the work and discussion. Describe how suspected
violations will be reviewed and let candidates explain their work. Writing style
alone is not evidence of AI use.

### Review Proposals and Agree on Expectations

Assess proposals using the published checklist and rubric. Provide clear
feedback and discuss alternatives when another project is a better fit. Look for
thoughtful questions, responses to feedback, useful observations from using the
software, and follow-through on agreed tasks.

Share a contributor checklist before selection covering deliverables, reporting
frequency, response windows, check-ins, AI policy, review participation, and
evaluation criteria. State your own availability, review turnaround, and backup
contact. Explain what happens when expectations are repeatedly unmet.

Confirm the working agreement during community bonding, including time zones,
planned absences, and any adjustments. Keep a shared record of changes.

### Support Progress and Address Problems Early

Set clear weekly objectives, hold regular check-ins, and review daily status
reports on agreed working days. Respond to requests for help and give actionable
feedback. During selection, announce any reporting exercise in advance and limit
it to a short, defined activity.

If progress or engagement falls short, discuss specific examples privately,
identify blockers and gaps in mentoring support, and agree on next steps and a
review date. Distinguish persistent failure to follow through from an agreed
absence or a technical obstacle raised promptly.

Decline candidates who do not meet published selection criteria. During the
program, give an honest failing evaluation when agreed expectations remain
unmet; passing someone solely to avoid a difficult conversation helps neither
the contributor nor the project. Coordinate with organization admins, document
the basis for the decision, and follow the current GSoC evaluation process.
Communicate concerns early and provide feedback before the evaluation.

For official mentoring guidance, see
[Setting Expectations](https://google.github.io/gsocguides/mentor/setting-expectations),
[Selecting a Contributor](https://google.github.io/gsocguides/mentor/selecting-a-student),
and [Evaluations](https://google.github.io/gsocguides/mentor/evaluations).

<a id="candidates-guide"></a>

## Contributor Candidates

### Start in the Community's Preferred Channel

Find the project's preferred community app or channel and use it for your first
contact. Introduce yourself, explain your interests, and ask:

- Does the organization intend to participate in the upcoming GSoC edition?
- Which of its projects or project ideas are planned to participate?
- Where can I find the relevant documentation and discuss getting started?

Ask about the team's plans for the upcoming GSoC edition rather than assuming
participation based on a previous year. Choose a project that aligns with your
interests, skills, and learning goals. Allow time for replies and keep technical
questions in the community channel so others can learn and help.

### Spend Time Using the Software

Use the software as a user before rushing to change its code. Spend several days
exploring it, follow the documentation, and try it on a real task or a need you
understand. For a tool or library, test different contexts and use cases rather
than stopping after one quick-start example.

Discuss your experience with colleagues, other users, and the community. Ask
questions, compare approaches, and understand why existing workflows work as
they do. Keep notes about examples, strengths, confusing steps, and limitations.
Hands-on experience helps you identify useful improvements and explain why they
matter to users.

### Write About Your Experience as a User

Before opening a pull request, write a blog post or newcomer experience report
covering:

- The project's mission, main objectives, and intended users.
- What you used it for, why you chose those tasks, and the contexts you
  explored.
- How to install or access it, with reproducible examples for other newcomers.
- What works well and which features or workflows you found useful.
- What was confusing, what could work better, and any setup or documentation
  obstacles.
- Constructive suggestions, questions discussed with others, and what you
  learned.

Take time to develop observations from actual use. Write an honest account with
specific examples. Follow the announced submission process; a draft or Markdown
document shared with the team is enough when public publication is not
requested. If setup fails, document what you tried and where you became blocked.

Then agree on a small follow-up contribution with a mentor, such as improving
onboarding documentation, adding a test, or fixing a bug. Focus on useful work
and responding to feedback rather than maximizing the number of pull requests.

### Prepare Your Proposal

Develop a detailed proposal with mentor feedback that explains:

- **Impact:** How the work advances the project's goals and helps its users.
- **Plan:** Specific tasks, deliverables, milestones, timeline, and risks.
- **Availability:** Time commitments and planned absences.
- **Newcomer Insight:** An observation from using the software and a suggested
  improvement.

Use clear, concise language. Follow the published AI-use policy, disclose
assistance as required, and verify everything you submit. Write a proposal that
reflects your own understanding and be prepared to explain your choices.

Review the [official rules](https://summerofcode.withgoogle.com/rules), the
selection checklist, and the assessment rubric before applying. Use the
[proposal template](../../templates/contributor-proposal.md).

### Review Process

Notify mentors in the designated channel when your proposal is ready for review.
Respond to feedback, ask clarifying questions, and allow time for replies. Show
engagement through thoughtful discussion, useful progress updates, support for
peers, and follow-through on agreed tasks. The recommended internal rubric gives
community engagement 50% of the assessment and technical understanding and
planning the other 50%.

<a id="approved-contributors"></a>

### After Selection: Work with Your Mentor

Agree on weekly objectives, check-in times, reporting channels, response
windows, and planned absences. Send a brief daily status report on agreed
working days using a shared thread or project log. Include:

- **Progress:** What I worked on or learned, with links where relevant.
- **Next:** What I plan to do next.
- **Blockers:** What is preventing progress and what help I need.

Report blockers even when no code was completed, and give early notice of
changes in availability. Ask for help, respond to reviews, and use feedback to
improve your work. Follow the
[Coding Tips](../../../guides/coding-tips/index.md) for readable code, focused
pull requests, testing, and documentation.

Consult the [GSoC Student Guide](https://google.github.io/gsocguides/student/)
and Google's
[advice for contributors](https://developers.google.com/open-source/gsoc/help/student-advice)
for further application guidance.
