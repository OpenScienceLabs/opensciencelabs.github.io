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

import re
from pathlib import Path
import logging


def replace(ROOT_DIR):
    """
    This function will recursively replace metadata in all
    markdown files (also in children directories).
    Be careful.

    Usage example:

        replace('/home/user/opensciencelabs.github.io')
    """

    for md_file in _gen_all_files_with_extension(ROOT_DIR):
        _replace_metadata(md_file)


def _replace_metadata(md_file):

    content = Path(md_file).read_text()
    pattern = "<!--[^>]*-->"
    extract_comment_tag = re.compile(pattern)
    result = extract_comment_tag.findall(content)

    if result:
        new_content = result[0]

        new_content = new_content.replace("<!--", "")
        new_content = new_content.replace("-->", "")
        new_content = new_content.replace(".. ", "")
        new_content = re.sub("title: (.*)", r'title: "\1"', new_content)
        new_content = re.sub("date: ([0-9]+-[0-9]+-[0-9]+) .*", r"date: \1", new_content)
        new_content = re.sub("tags: (.*)", r"tags: [\1]", new_content)
        new_content = re.sub("category: (.*)", r"category: [\1]", new_content)
        new_content = re.sub("(link:.*|description:.*)", "", new_content)
        new_content = re.sub("\n\s+\n", "\n", new_content, re.MULTILINE)
        new_content += 'draft: false\n'
        new_content += 'usePageBundles: true\n'
        new_content += 'thumbnail: \n'
        new_content += 'featureImage: \n'
        new_content = f"---{new_content}---\n"

        output = open(md_file,"w")
        output.write(content.replace(result[0], new_content))
        output.close()
        
        logging.warning(f'{md_file} updated.')

def _gen_all_files_with_extension(ROOT_DIR, EXTENSIONS=['.md']):
    for path in Path(ROOT_DIR).glob(r'**/*'):
        if path.suffix in EXTENSIONS:
            yield path

