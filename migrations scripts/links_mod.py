"""
Takes as input a md file path and changes its contained links.
According to the following example

Erase the next image link
![hoja de datos](../../../images/blog/filtrar-datos-r/header.png)

Change the link
![hoja de datos](../../../images/blog/filtrar-datos-r/header.png)
to
![hoja de datos](../../header.png)

Usage:

`python migrations\ scripts/links_mod.py`
"""
import re
import logging

from pathlib import Path
from _config import _gen_all_files_with_extension

def replace(ROOT_DIR):
    for md_file in _gen_all_files_with_extension(ROOT_DIR):
        _replace_header_links(md_file)


def _replace_header_links(md_file):

    content = Path(md_file).read_text()

    regex = "(!\[[a-zA-Z ]+\]\()[\.\.\/]+\/images\/blog\/[a-zA-Z-]+\/(header\.png\))"
    subst = r"\1../../\2"

    output = open(md_file,"w")
    output.write(re.sub(regex, subst, content, 0, re.MULTILINE))
    output.close()

    logging.warning(f'{md_file} updated.')


def main():
    from _config import BLOG_PATH
    replace(BLOG_PATH)

if __name__ == "__main__":
    main()
