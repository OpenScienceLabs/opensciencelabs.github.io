---
title: "Open Science Labs Project Governance"
date: 2019-09-14
author: Ivan Ogasawara
draft: false
usePageBundles: false
tags: ["gobernance"]
aliases: ["/governance/"]
---


The objectives of this document include formalizing the governance of the Open Science Labs (OSL) project. In both common and uncommon situations, outlining the decision-making procedure and the interactions between the various members of our community, including the relationship between work that may be supported by for-profit or nonprofit organizations and open source collaborative development.

## Summary

OSL is a community-owned and community-run project. To the maximum extent possible, decisions about project direction are made by community consensus (but note that "consensus" here has a somewhat technical meaning that might not match everyone's expectations -- see below). Some members of the community additionally contribute by serving on the OSL (Eunice Rodas, Ever Vino, Ivan Ogasawara, Luis Casas), where they are responsible for facilitating the establishment of community consensus, for stewarding project resources, and -- in extreme cases -- for making project decisions if the normal community-based process breaks down.

Commonly, everyone is responsible for specific areas or tasks and, if there is anything that needs to be decided by the group, this person brings this topic to one of our contributor's meetings and we can discuss and decide that together. The main criteria we have that should be respected is that the content should be related to an "open" topic (private technologies are not allowed, for example), and the access to that information should also be open (references to private content is not allowed neither). So, we try to have an open space for everyone to bring their ideas and have also the space to implement that idea as well, the steering council first main goal is to help contributors to share their ideas before to put it in practice.

## The project

Open Science Labs (OSL) is a community that aims to join people from all parts of the world, specially from Latin America countries and create an open space for teaching, learning and sharing topics around open science and open computational tools.

OSL also motivates initiatives about English language because it increases the possibilities of collaboration in open projects across the world.

The software developed by OSL initiatives are released under some OSI approved license (such as BSD, Apache 2.0, or MIT), built openly and hosted on public GitHub repositories under the OpenScienceLabs organization.

The Project is conducted by a distributed team of contributors, who are individuals that have collaborated with code, documentation, graphical design or other kind of work to the Project. Anyone can be a Contributor. Contributors can be affiliated with any legal entity or none. Contributors participate in the project by submitting, reviewing and discussing GitHub pull requests and issues and participating in open and public Project discussions on GitHub, discord, among other channels. The basis of project participation is openness and transparency.

The Project Community consists of all Contributors and Users of the Project. Contributors work on behalf of and are responsible to the larger Project Community and we strive to keep the barrier between Contributors and Users as low as possible.

In order to improve transparency and a better fiscal workflow, OSL is currently looking for a fiscal sponsor to help our project to grow.


## Governance

This section describes the governance and leadership model of The Project.

The principles of Project governance are:

    Openness & Transparency
    Active Contribution
    Institutional Neutrality
    Diversity, Equity and Inclusion
    Education

### Consensus-based decision making by the community

In general, all project decisions will be made by consensus of all interested Contributors. The primary goal of this approach is to ensure that the people who are most affected by and involved in any given change can contribute their knowledge in the confidence that their voices will be heard, because thoughtful review from a broad community is the best mechanism we know of for creating high-quality software.

The mechanism we use to accomplish this goal may be unfamiliar for those who are not experienced with the cultural norms around free/open-source software development. We provide a summary here, and highly recommend that all Contributors additionally read Chapter 4: Social and Political Infrastructure of Karl Fogel's classic Producing Open Source Software, and in particular the section on Consensus-based Democracy, for a more detailed discussion.

In this context, consensus does NOT require:

* that we wait to solicit everybody's opinion on every  change,
* that we ever hold a vote on anything, or
* that everybody is happy or agrees with every decision.

For us, what consensus means is that we entrust everyone with the right to veto any change if they feel it necessary. While this may sound like a recipe for obstruction and pain, this is not what happens. Instead, we find that most people take this responsibility seriously, and only invoke their veto when they judge that a serious problem is being ignored, and that their veto is necessary to protect the project. And in practice, it turns out that such vetoes are almost never formally invoked, because their mere possibility ensures that Contributors are motivated from the start to find some solution that everyone can live with -- thus accomplishing our goal of ensuring that all interested perspectives are taken into account.

How do we know when consensus has been achieved? First of all, this is rather difficult since consensus is defined by the absence of vetos, which requires us to somehow prove a negative. In practice, we use a combination of our best judgement (e.g., a simple and uncontroversial bug fix posted on GitHub and reviewed by a core developer is probably fine) and best efforts (e.g., all substantive API changes must be posted to a github issue or a discussion on discord in order to give the broader community a chance to catch any problems and suggest improvements; we assume that anyone who cares enough about OSL to invoke their veto right should be on the github OSL repositories or discord). OSL, is a small group, and aims for quick and transparent communication, so the common channels for communication are the github issues and the discord channels. So, all people involved can have a quick and transparent communication about any specific problem and we can react very quick.

If one does need to invoke a formal veto, then the process should consist of:

* an unambiguous statement that a veto is being invoked,
* an explanation of why it is being invoked, and
* a description of what conditions (if any) would convince the vetoer to withdraw their veto.

If all proposals for resolving some issue are vetoed, then the status quo wins by default.

In the worst case, if a Contributor is genuinely misusing their veto obstructively to the detriment of the project, then they can be ejected from the project by consensus of the Steering Council -- see below.


### Steering Council

The Project will have a Steering Council that consists of Project Contributors who have produced contributions that are substantial in quality and quantity, and sustained over at least one year. The overall role of the Council is to ensure, with input from the Community, the long-term well-being of the project, both technically and as a community.

During the everyday project activities, council members participate in all discussions, code review and other project activities as peers with all other Contributors and the Community. In these everyday activities, Council Members do not have any special power or privilege through their membership on the Council. However, it is expected that because of the quality and quantity of their contributions and their expert knowledge of the Project Software and Services that Council Members will provide useful guidance, both technical and in terms of project direction, to potentially less experienced contributors.

The Steering Council and its Members play a special role in certain situations. In particular, the Council may, if necessary:

* Make decisions about the overall scope, vision and direction of the project.
* Make decisions about strategic collaborations with other organizations or individuals.
* Make decisions about specific technical issues, features, bugs and pull requests. They are the primary mechanism of guiding the code review process and merging pull requests.
* Make decisions about the Services that are run by The Project and manage those Services for the benefit of the Project and Community.
* Update policy documents such as this one.
* Make decisions when regular community discussion doesn’t produce consensus on an issue in a reasonable time frame.

However, the Council's primary responsibility is to facilitate the ordinary community-based decision making procedure described above. If we ever have to step in and formally override the community for the health of the Project, then we will do so, but we will consider reaching this point to indicate a failure in our leadership.

#### Council decision making

If it becomes necessary for the Steering Council to produce a formal decision, then they will use a form of the Apache Foundation voting process. This is a formalized version of consensus, in which +1 votes indicate agreement, -1 votes are vetoes (and must be accompanied with a rationale, as above), and one can also vote fractionally (e.g. -0.5, +0.5) if one wishes to express an opinion without registering a full veto. These numeric votes are also often used informally as a way of getting a general sense of people's feelings on some issue, and should not normally be taken as formal votes. A formal vote only occurs if explicitly declared, and if this does occur then the vote should be held open for long enough to give all interested Council Members a chance to respond -- at least one week.

In practice, we anticipate that for most Steering Council decisions (e.g., voting in new members) a more informal process will suffice.

#### Council membership

A list of current Steering Council Members is maintained at the page About.

To become eligible to join the Steering Council, an individual must be a Project Contributor who has produced contributions that are substantial in quality and quantity, and sustained over at least six month. Potential Council Members are nominated by existing Council members, and become members following consensus of the existing Council members, and confirmation that the potential Member is interested and willing to serve in that capacity. The Council will be initially formed from the set of existing Core Developers who, as of late 2015, have been significantly active over the last year.

When considering potential Members, the Council will look at candidates with a comprehensive view of their contributions. This will include but is not limited to code, code review, infrastructure work, mailing list and chat participation, community help/building, education and outreach, design work, etc. We are deliberately not setting arbitrary quantitative metrics (like “100 commits in this repo”) to avoid encouraging behavior that plays to the metrics rather than the project’s overall well-being. We want to encourage a diverse array of backgrounds, viewpoints and talents in our team, which is why we explicitly do not define code as the sole metric on which council membership will be evaluated.

If a Council member becomes inactive in the project for a period of six month, they will be considered for removal from the Council. Before removal, inactive Member will be approached to see if they plan on returning to active participation. If not they will be removed immediately upon a Council vote. If they plan on returning to active participation soon, they will be given a grace period of one month. If they don’t return to active participation within that time period they will be removed by vote of the Council without further grace period. All former Council members can be considered for membership again at any time in the future, like any other Project Contributor. Retired Council members will be listed on the project website, acknowledging the period during which they were active in the Council.

The Council reserves the right to eject current Members, if they are deemed to be actively harmful to the project’s well-being, and attempts at communication and conflict resolution have failed. This requires the consensus of the remaining Members.

#### Conflict of interest

It is expected that the Council Members will be employed at a wide range of companies, universities and non-profit organizations. Because of this, it is possible that Members will have conflict of interests, such ones include, but are not limited to:

* Financial interests, such as investments, employment or contracting work, outside of The Project that may influence their work on The Project.
* Access to proprietary information of their employer that could potentially leak into their work with the Project.

All members of the Council shall disclose to the rest of the Council any conflict of interest they may have. Members with a conflict of interest in a particular issue may participate in Council discussions on that issue, but must recuse themselves from voting on the issue.

#### Private communications of the Council

To the maximum extent possible, Council discussions and activities will be public and done in collaboration and discussion with the Project Contributors and Community. The Council will have a private channel on discord that will be used sparingly and only when a specific matter requires privacy. When private communications and decisions are needed, the Council will do its best to summarize those to the Community after eliding personal/private/sensitive information that should not be posted to the public internet.

#### Subcommittees

The Council can create subcommittees that provide leadership and guidance for specific aspects of the project. Like the Council as a whole, subcommittees should conduct their business in an open and public manner unless privacy is specifically called for. Private subcommittee communications should happen on the main private discord channel of the Council unless specifically called for.


## Institutional Partners and Funding

The Steering Council are the primary leadership for the project. No outside institution, individual or legal entity has the ability to own, control, usurp or influence the project other than by participating in the Project as Contributors and Council Members. However, because institutions can be an important funding mechanism for the project, it is important to formally acknowledge institutional participation in the project. These are Institutional Partners.

An Institutional Contributor is any individual Project Contributor who contributes to the project as part of their official duties at an Institutional Partner. Likewise, an Institutional Council Member is any Project Steering Council Member who contributes to the project as part of their official duties at an Institutional Partner.

Institutions become eligible to become an Institutional Partner when they share same values of Open Science Labs and are available to collaborate to the project in any of these ways:

- publicizing open science labs in their social network
- allocate one or more contributors to help Open Science Labs projects or other affiliated projects
- funding Open Science Labs activities
- offering mentoring for Open Science Labs Contributors when contributing to their projects (defined by the Partner).
- offering opportunties for contracting Open Science Labs Conbributors who have contributed to their projects (defined by the Partner)

If at some point an existing Institutional Partner doesn't accomplish with these points mentioned above, then six month grace period begins. If at the end of this six months period they continue not to have any contribution, then their Institutional Partnership will lapse, and resuming it will require going through the normal process for new Partnerships.

Funding acquired by Institutional Partners to work on The Project is called Institutional Funding. However, no funding obtained by an Institutional Partner can override the Steering Council. If a Partner has funding to do Open Science work and the Council decides to not pursue that work as a project, the Partner is free to pursue it on their own. However in this situation, that part of the Partner’s work will not be under the Open Science Labs umbrella and cannot use the Project trademarks in a way that suggests a formal relationship.

Institutional Partner benefits are:

* Acknowledgement on the Open Science Labs websites and in talks.
* Ability to influence the project through the participation of their Council Member.
* Council Members invited to Open Science Labs Developer Meetings.

A list of current Institutional Partners is maintained at the page About Us.

## Document history

* [https://github.com/opensciencelabs/opensciencelabs.github.io](https://github.com/opensciencelabs/opensciencelabs.github.io)

## Acknowledgements

Substantial portions of this document were adapted from the NumPy project governance and decision-making document https://github.com/numpy/numpy/commits/main/doc/source/dev/governance/governance.rst.

## License

CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/
