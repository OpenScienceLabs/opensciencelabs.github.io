---
title: "funding.json"
description: "Open Science Labs, sharing knowledge"
date: "2019-02-28"
authors: ["OSL Team"]
---

## Here's the OSL funding.json manifest

```
{ "version": "v1.0.0",
  "entity": {
    "type": "organisation",
    "role": "owner",
    "name": "Open Science Labs",
    "email": "team@opensciencelabs.org",
    "phone": "",
    "description": "Open Science Labs (OSL) is a non-profit organisation dedication to creating innovative FOSS.",
    "webpageurl": {
      "url": "https://www.opensciencelabs.org",
      "wellKnown": ""
    }
  },
  "projects": [
    {
      "guid": "astx",
      "name": "ASTx",
      "description": "ASTx is a groundbreaking library designed to encapsulate language components in an agnostic and pythonic way. It provides a comprehensive set of classes and functionalities, allowing developers to articulate the core elements of any programming language.",
      "webpageUrl": {
        "url": "https://astx.arxlang.org"

      },
      "repositoryUrl": {
        "url": "https://github.com/arxlang/astx",
        "wellKnown": "https://github.com/opensciencelabs/opensciencelabs.github.io/tree/main/.well-known/funding-manifest-urls"
      }
    },

      {
      "guid": "sugar",
      "name": "Sugar",
      "description": "Sugar is a tool that helps users organize their stack of containers and any additional scripts. ",
      "webpageUrl": {
        "url": "https://osl-incubator.github.io/sugar"

      },
      "repositoryUrl": {
        "url": "https://github.com/osl-incubator/sugar",
        "wellKnown": "https://github.com/opensciencelabs/opensciencelabs.github.io/tree/main/.well-known/funding-manifest-urls"
      }

    },

    {
      "guid": "makim",
      "name": "Makim",
      "description": "Makim is a YAML-based task automation tool offering structures for the definition for tasks and dependencies, with  support for conditionals.",
      "webpageUrl": {
        "url": "https://osl-incubator.github.io/makim"

      },
      "repositoryUrl": {
        "url": "https://github.com/osl-incubator/makim",
        "wellKnown": "https://github.com/opensciencelabs/opensciencelabs.github.io/tree/main/.well-known/funding-manifest-urls"
      }

    },

    {
      "guid": "scicookie",
      "name": "SciCookie",
      "description": "Scicookie is a template which creates projects from project templates and is based on Cookiecutter. It serves as an initial structure to simply project creation processes.",
      "webpageUrl": {
        "url": "https://osl-incubator.github.io/scicookie"

      },
      "repositoryUrl": {
        "url": "https://github.com/osl-incubator/scicookie",
        "wellKnown": "https://github.com/opensciencelabs/opensciencelabs.github.io/tree/main/.well-known/funding-manifest-urls"
      }

    },

    {
      "guid": "artbox",
      "name": "ArtBox",
      "description": "Artbox is a tool that handles multimedia files processing, such as conversion from speech to text and vice versa.",
      "webpageUrl": {
        "url": "https://osl-incubator.github.io/artbox"

      },
      "repositoryUrl": {
        "url": "https://github.com/osl-incubator/artbox",
        "wellKnown": "https://github.com/opensciencelabs/opensciencelabs.github.io/tree/main/.well-known/funding-manifest-urls"
      }

    }
  ],

  "funding": {
    "channels": [
      {
        "guid": "opencollective",
        "type": "payment-provider",
        "address": "https://opencollective.com/osl",
        "description": "We use Open Collective for receiving funds."
      }
    ],
    "plans": [
      {
        "guid": "hosting-monthly",
        "status": "active",
        "name": "hosting suppport",
        "description": "This will cover the cost of proposed server hosting for OSL projects.",
        "amount": 0,
        "currency": "USD",
        "frequency": "monthly",
        "channels": ["opencollective"]
      },
      {
        "guid": "developer-time",
        "status": "active",
        "name": "developer-support",
        "description": "This will cover the cost of one developer working part-time on the projects.",
        "amount": 0,
        "currency": "USD",
        "frequency": "monthly",
        "channels": ["opencollective"]
      },
      {
        "guid": "angel-plan",
        "status": "active",
        "name": "goodwill plan",
        "description": "Pay anything you wish to show your goodwill for our projects.",
        "amount": 0,
        "currency": "USD",
        "frequency": "one-time",
        "channels": ["opencollective"]
      },
      {
        "history": []
      }
    ]
  }
}
```
