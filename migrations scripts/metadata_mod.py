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

Usage:

`python migrations\ scripts/metadata_mod.py`

"""

import re
import logging

from pathlib import Path
from _config import gen_all_files_with_extension

def replace(ROOT_DIR):
    for md_file in gen_all_files_with_extension(ROOT_DIR):
        replace_metadata(md_file)


def replace_metadata(md_file):

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
        new_content += 'thumbnail: "/header.png"\n'
        new_content += 'featureImage: "/header.png"\n'
        new_content = f"---{new_content}---\n"

        output = open(md_file,"w")
        output.write(content.replace(result[0], new_content))
        output.close()
        
        logging.warning(f'{md_file} updated.')


def main():
    from _config import BLOG_PATH
    replace(BLOG_PATH)

if __name__ == "__main__":
    main()
