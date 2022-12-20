"""
Create a folder for each blog page (images/<blog page slug>) and move
inside all its images. 

extensions to move:
.png
.jpeg/jpg
.gif
.webp
.csv?

before:
test_files/blog/<blog page>/*images

after:
test_files/images/<blog page slug>/*images
"""

import logging
from pathlib import Path
import shutil
import re
from _config import gen_all_files_with_extension


def move(ROOT_DIR):
    for md_file in gen_all_files_with_extension(ROOT_DIR):
        move_images(md_file)


def move_images(md_file):

    images = _grep_imgs(md_file)
    imgs_dir = _create_dir(md_file)

    for image in images:
        if Path(imgs_dir / str(image).split('/')[-1]).exists():
            Path(image).unlink()

        else:
            shutil.move(image, imgs_dir)
            logging.warning(f'{str(image).split("/")[-1]} moved to {imgs_dir}')


def _extract_slug(md_file):

    content = Path(md_file).read_text()
    pattern = 'slug: [a-zA-z0-9-]+\n'
    extract_comment_tag = re.compile(pattern)
    result = extract_comment_tag.search(content)
    if result:
        slug = result.group().split('slug: ')[1]
        slug = slug.replace("'", "")
        slug = slug.replace("\n", "")
        slug = slug.replace("$", "")
        return slug
    
    else:
        logging.warning(f'Slug for {md_file} was not found')

    
def _create_dir(md_file):

    slug = _extract_slug(md_file)
    img_dir = Path(md_file).parent.parent.parent / 'images' / slug
    img_dir.mkdir(exist_ok=True, parents=True)

    return img_dir


def _grep_imgs(md_file):

    extensions = ['.png', '.jpeg', '.jpg', '.gif', '.webp', '.csv']
    md_dir = Path(md_file).parent

    images = []
    if md_dir.exists():
        for file in Path(md_dir).glob(r'**/*'):
            if file.suffix in extensions:
                images.append(file)

    return images


def main():
    from _config import BLOG_PATH
    move(BLOG_PATH)

if __name__ == "__main__":
    main()
