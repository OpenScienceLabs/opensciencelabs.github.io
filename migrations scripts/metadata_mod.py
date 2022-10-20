"""
A Function that takes an md document path as an argument.
Return a new file with the metadata changed from nikola format to new metadata required for hugo, the returned file 
will be saved in the new_dir directory

Example
nikola format
<!--
.. title: Cómo filtrar datos de tu tabla con dplyr en R
.. slug: filtrar-datos-r
.. date: 2022-06-14 19:52:05 UTC
.. author: Ever Vino
.. tags: open science, r, filtrar datos, dplyr, recursos, data science
.. category: data science
.. link: 
.. description: 
.. type: text
-->

to hugo format

---
title: "Cómo filtrar datos de tu tabla con dplyr en R"
slug: filtrar-datos-r
date: 2022-06-14
author: Ever Vino
slug: filtrar-datos-r
category: data science
draft: false
usePageBundles: true
thumbnail: '/header.png'
featureImage: '/header.png'
tags: [open science, r, filtrar datos, dplyr, recursos, data science ]
---

"""

def metadata_mod(file, new_dir):
    pass