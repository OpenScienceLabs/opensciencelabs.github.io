"""
Mutual configuration for python scripts
"""

from pathlib import Path

BLOG_PATH = Path(Path(__file__).parent / 'test_files' / 'blog')

def gen_all_files_with_extension(ROOT_DIR, EXTENSIONS=['.md']):
    if Path(ROOT_DIR).exists():
        for path in Path(ROOT_DIR).glob(r'**/*'):
            if path.suffix in EXTENSIONS:
                yield path
    else:
        raise Exception(f"{ROOT_DIR} not found")
