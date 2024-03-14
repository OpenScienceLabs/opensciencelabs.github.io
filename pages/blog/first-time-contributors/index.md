---
title: "First Time Contributors"
slug: first-time-contributors
date: 2024-02-10
authors: ["Daniela Iglesias Rocabado"]
tags: [open-source, contributors, git, osl]
categories: [contributors]
description: |
  First Time Contributors" refers to individuals making their initial foray into contributing to open-source projects within scientific laboratories. These newcomers bring diverse skills and fresh perspectives, enriching the collaborative environment. Embracing inclusivity and providing guidance fosters their engagement, leading to innovative solutions in open science.
thumbnail: "/header.jpeg"
template: "blog-post.html"
---
Diving into project development can be overwhelming for beginners. A first-timers guide is key to navigate this unfamiliar terrain. From understanding basics to mastering tools, it'll help you contribute effectively. Join us as we explore how to get started in a development project!

## Git for Beginners: Avoiding Issues in Your First Contributions

The world of open-source programming project development is a vibrant and collaborative space, but it can also be daunting for those venturing in for the first time. We've noticed that new contributors often face significant challenges when taking their first steps in this environment. That's why we've created this first-timers guide.

Our aim is to provide a comprehensive resource that helps newcomers overcome initial barriers and start contributing effectively right from the get-go. By offering a guide that covers everything from the basics to best practices in open-source project development, we hope to streamline the onboarding process and foster a more inclusive and productive collaborative environment.

This guide will not only be beneficial for those starting their journey in open-source projects but will also serve as the primary reference for all affiliated projects and projects under the OSL Incubator Program. By standardizing practices and promoting a common understanding of the processes involved, we aim to enhance the experience for all contributors and promote more efficient and high-quality development in our open-source projects.

## Getting Started

In this guide, we'll tackle the common challenges that newcomers encounter in open-source projects. These include navigating Git and establishing your development environment. We'll provide step-by-step instructions on Git fundamentals and setting up your virtual workspace seamlessly.

Additionally, we will offer further advice for the contributor to start with a solid initial structure, thus ensuring that their project is well-organized from the outset. From the initial setup to active contribution in the project, this guide aims to provide contributors with the tools and knowledge needed to effectively contribute to open-source programming projects.

# GIT

## What is Git?
Git is a widely used distributed version control system in software development. It allows project collaborators to work collaboratively on the same set of files, recording changes, merging contributions, and maintaining a detailed history of all modifications made to the source code.

## How to install Git?
To install Git, you can follow these steps:

1. **Windows Operating System:** You can download the Git installer from the [official Git website](https://gitforwindows.org/). Once downloaded, run the installer and follow the installation wizard instructions.

2. **macOS Operating System:** Git is usually pre-installed on macOS. However, if it's not installed or you want to update it, you can do so through the command line or using package management tools like Homebrew.

3. **Linux Operating System:** In most Linux distributions, Git is available in the default package repositories. You can install it using the package manager specific to your distribution, such as apt for Ubuntu or yum for CentOS.

For more detailed material on Git, we recommend using the Software Carpentry material, which is more focused on people who already have basic knowledge of Git but still face difficulties. You can access the material at the following link: [Software Carpentry - Git Novice](https://swcarpentry.github.io/git-novice/)

## First Steps to Collaborating on a Project

### Understanding Repository Forking
When embarking on a collaborative project, the first step often involves forking a repository. Forking is a fundamental aspect of version control systems like Git, enabling individuals or teams to create their own copy of a project's repository. This copy acts as a sandbox where contributors can freely experiment, make changes, and propose improvements without affecting the original project.

#### Steps to Forking a Repository
1. **Navigate to the Repository:** Visit the project's repository on the hosting platform, such as GitHub, GitLab, or Bitbucket.

2. **Locate the Fork Button:** Look for the "Fork" button on the repository's page. This button is usually located in the top-right corner. Clicking it will initiate the forking process.

3. **Choose Destination:** When prompted, select where you want to fork the repository. You can fork it to your personal account or to an organization you're a part of.

4. **Wait for Forking to Complete:** The platform will create a copy of the repository in your account or organization. Depending on the size of the repository and the platform's load, this process may take a few seconds to complete.

5. **Clone Your Forked Repository:** Once the forking process is finished, clone the forked repository to your local machine using Git. This will create a local copy of the repository that you can work on.

#### Benefits of Forking a Repository
- **Independence:** Forking gives you complete control over your copy of the project. You can modify it as you see fit without impacting the original.

- **Experimentation:** Forking provides a safe environment for experimenting with changes. You can try out new features, fix bugs, or test ideas without risking the stability of the main project.

- **Collaboration:** Forking facilitates collaboration by enabling contributors to work on different aspects of the project simultaneously. Once you've made improvements or fixes in your fork, you can propose them to the original project through a pull request.


### What is a Pull Request and why is it important?

A Pull Request (PR) is a proposed change that a collaborator makes to a code repository managed by a version control system such as Git. It's essentially a request for the changes made in one branch of a repository to be incorporated into another branch, usually the main branch. Pull Requests are essential in the collaborative workflow of software development, as they allow teams to review, discuss, and approve changes before they are merged into the codebase. This facilitates collaboration, improves code quality, and helps maintain a clear history of modifications made to the project.

### Steps for creating a good Pull Request:

1. **Create a feature branch:** Before starting to make changes to the code, create a new branch in the repository that clearly describes the purpose of the changes you plan to make. This helps keep the development organized and makes code review easier.

2. **Make necessary changes:** Once you're on your feature branch, make the changes to the code as planned. Make sure to follow the project's coding conventions and write unit tests if necessary.

3. **Update documentation if necessary:** If your changes affect existing functionality or introduce new features, it's important to update the corresponding documentation, such as code comments or user documentation.

4. **Create the Pull Request:** Once you've completed your changes and are ready to request review, create a Pull Request. Provide a clear and concise description of the purpose of your changes, as well as any relevant context to facilitate review by your team members.

5. **Request review:** After creating the Pull Request, assign relevant reviewers to examine your changes. This may include other developers on the team, technical leads, or anyone with expertise in the area affected by your modifications.

6. **Respond to comments and make adjustments if necessary:** Once reviewers have provided feedback on your Pull Request, take the time to respond to their questions and make any necessary adjustments to your code. It's important to collaborate constructively during this process to ensure that the proposed changes are of the highest possible quality.

By following these steps, you can effectively contribute to a project's development through Pull Requests that are easy to review, approve, and merge, ultimately leading to stronger code and more efficient teamwork.


# Why Creating Virtual Environments is Important

Creating virtual environments is crucial for several reasons:

- **Isolation:** Virtual environments allow you to isolate project dependencies, preventing conflicts between different projects that may require different versions of the same packages. This ensures that your projects remain stable and reproducible.

- **Dependency Management:** By creating separate environments for each project, you can manage dependencies more effectively. You can install specific versions of packages for each project without affecting other projects or the system-wide installation.

- **Experimentation:** Virtual environments provide a safe space for experimentation. You can try out new packages or versions without worrying about breaking existing projects or the system environment.

- **Collaboration:** Virtual environments make it easier to collaborate with others on projects. You can share environment configuration files (e.g., `environment.yml`) to ensure that all collaborators are working with the same dependencies and versions.

By following these steps and understanding the importance of virtual environments, you'll be able to create, manage, and work in isolated environments with Conda efficiently.


Here's a basic guide to creating virtual environments with Conda:

1. **Install Conda:**
   If you don't have Conda installed yet, you can download and install Miniconda or Anaconda according to your needs from the official Anaconda website.

2. **Create a new virtual environment:**
   Open your terminal or console and run the following command to create a new virtual environment. Replace `environment_name` with the name you want for your environment.

$ conda create --name environment_name
3. **Activate the virtual environment:**
To start working in your virtual environment, you need to activate it. You can do this with the following command:
$ conda activate environment_name
4. **Deactivate the virtual environment:**
When you're done working in your virtual environment and want to return to the base Conda environment, you can deactivate it with the following command:
$ conda deactivate