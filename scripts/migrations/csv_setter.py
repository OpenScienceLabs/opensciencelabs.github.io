"""
From a csv file and the files directory path as arguments, modify the metadata according the new metadata assigned from 
the csv file.

Example
if the file exist in the csv file modify its metadata according to

filename, slug, author, date, tags, category
...
filtrar-datos-r.md, filtrar-datos-r, John Vino, 2022-09-25, "Word Cloud, r, DataViz", ciencia de datos https://opensciencelabs.org/blog/filtrar-datos-r/filtrar-datos-r/
...

filename=filtrar-datos-r.md
---
title: "Crea tu nube de palabras en R a partir de un documento de texto"
author: John Vino
slug: filtrar-datos-r
category: ciencia de datos
date: 2022-09-25
draft: false
usePageBundles: true
thumbnail: '/header.png'
featureImage: '/header.png' 
tags: ["Word Cloud, r, DataViz"]
alias: ["https://opensciencelabs.org/blog/filtrar-datos-r/filtrar-datos-r/"]
---
Note that in the alias key in the metadata is equal to a list containing the url 
"""

def csv_setter_fun(csv_file, files_dir):
    pass
