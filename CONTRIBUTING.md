# Contributing Guide for Open Science Labs Blog

## Getting Started

To contribute to the Open Science Labs blog, you should first fork the
repository and clone it locally. Follow these steps to set up your local
development environment:

```bash
# Clone your fork of the repository
$ git clone https://github.com/MY-USER-NAME/opensciencelabs.github.io
$ cd opensciencelabs.github.io

# Add the original project as an upstream remote
$ git remote add upstream https://github.com/opensciencelabs/opensciencelabs.github.io
$ git fetch --all
```

_Note: Replace `MY-USER-NAME` with your GitHub username._

## Setting Up the Environment

Set up the Conda environment to manage the dependencies for the blog:

```bash
# Create and activate the Conda environment
$ mamba env create --file conda/dev.yaml
$ conda activate osl-web
```

This will create a new Conda environment named `osl-web` with all necessary
dependencies and activate it.

## Developing Blog Posts

### Development Commands

- **Previewing Changes:** Use `makim pages.preview` to run a local server for
  previewing the blog and other pages.
- **Building the Site:** Before pushing changes to GitHub, build the site using
  `makim pages.build` to ensure everything is compiled correctly.

### Creating a New Blog Post

1. **Prepare the Blog Post:**

   - Navigate to `pages/blog` and create a new folder with a slugified version
     of your blog post's title. Use
     [https://slugify.online/](https://slugify.online/) to generate a slug.
   - Inside this folder, create your blog post file:
     - For Markdown: `index.md`
     - For Jupyter Notebooks: `index.ipynb` (use Jupyter Lab to create this
       directly)

2. **Include a Header Image:**
   - Place a header image (either `header.png` or `header.jpg`) in your blog
     post folder. Make sure the image is under a free license.

### Metadata and Formatting

- **Markdown Posts:** Add a metadata block at the beginning of your `index.md`
  file:

  ```markdown
  ---
  title: "Title of Your Blog Post"
  slug: "slug-of-your-blog-post"
  date: YYYY-MM-DD
  authors: ["Author Name"]
  tags: ["tag1", "tag2"]
  categories: ["category1", "category2"]
  description: "Short description of the blog post."
  thumbnail: "/path/to/header.jpg"
  template: "blog-post.html"
  ---
  ```

- **Jupyter Notebook Posts:** The first cell of your `index.ipynb` should be in
  `raw` mode containing the same metadata as above.

3. **Building and Viewing:**
   - If using a Jupyter Notebook, run `makim pages.build` to convert the
     notebook into a Markdown file (`index.md`).
   - Add the generated `index.md` to your repository as it will be used to
     render the webpage.

## Final Steps

Before submitting your blog post:

- Ensure all files are added to your repository.
- Submit a pull request to the main `opensciencelabs.github.io` repository for
  review.

Thank you for contributing to the Open Science Labs blog!
