"""
Takes a files directory, where md file exists. 
From every md file, create a row inside a csv file where you specify separated in columns: the file name, slug, author, 
date, tags, category, url
Example 
from a file which has the following metadata

filename=filtrar-datos-r.md
---
title: "Crea tu nube de palabras en R a partir de un documento de texto"
author: Ever Vino
slug: filtrar-datos-r
category: data science
date: 2022-09-25
draft: false
usePageBundles: true
thumbnail: '/header.png'
featureImage: '/header.png' 
tags: [nube de palabras, r, visualización de datos]
---

create a new row inside a new csv file 

filename, slug, author, date, tags, category, url
...
filtrar-datos-r.md, filtrar-datos-r, Ever Vino, 2022-09-25, "nube de palabras, r, visualización de datos", data science, https://opensciencelabs.org/blog/filtrar-datos-r/filtrar-datos-r/
...

This should return a csv file in the path indicated as argument
"""

def csv_creator_fun(files_dir, path_where):
    pass