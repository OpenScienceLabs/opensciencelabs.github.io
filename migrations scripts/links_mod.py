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
from _config import gen_all_files_with_extension

def replace(ROOT_DIR):
    for md_file in gen_all_files_with_extension(ROOT_DIR):
        replace_header_links(md_file)
        replace_links(md_file)


def replace_header_links(md_file):

    content = Path(md_file).read_text()

    pattern = "(!\[[a-zA-Z ]+\]\()[\.\.\/]+\/images\/blog\/[a-zA-Z-]+\/(header\.png\))"
    #subst = r"\1../../\2"
    subst = ""

    output = open(md_file,"w")
    output.write(re.sub(pattern, subst, content, 0, re.MULTILINE))
    output.close()

    logging.warning(f'{md_file} updated.')

def replace_links(md_file):
    #"![header](../../../images/blog/visualiza-tus-datos-en-r-con-ggplot-y-gganimate/header.png)"
    content = Path(md_file).read_text()
    #"![Mapa de](../../../images/blog/dibuja-shapefile/grafica3.png)"
    #"![Meme GOT](../../../../images/blog/ethereum-merge/meme-summer.jpeg)"
    pattern = "(!\[[a-zA-Z\s : ]+\]\()[\.\.\/]+\/images\/blog\/[a-zA-Z-]+\/([a-zA-Z0-9.-_]+\))"
    subst = r"\1\2"
    
    
    output = open(md_file,"w")
    output.write(re.sub(pattern, subst, content, 0, re.MULTILINE))
    output.close()

    logging.warning(f'{md_file} updated.')

def main():
    from _config import BLOG_PATH
    replace(BLOG_PATH)

if __name__ == "__main__":
    main()
