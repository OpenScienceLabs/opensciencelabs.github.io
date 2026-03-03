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

1. **Prepare the Blog Post (Quarto-first workflow):**

   - Navigate to `pages/blog` and create a new folder with a slugified version
     of your blog post's title. Use
     [https://slugify.online/](https://slugify.online/) to generate a slug.
   - Inside this folder, create your blog post as a **Quarto document**:
     - `index.qmd`

2. **Include a Header Image:**
   - Place a header image (either `header.png` or `header.jpg`) in your blog
     post folder. Make sure the image is under a free license.

### Authoring images (performance and accessibility)

- **Alt text:** Always add descriptive `alt` text for images (e.g. in Markdown:
  `![Description of the image](image.png)`). This helps accessibility and SEO.
- **Dimensions:** Prefer images with reasonable dimensions (e.g. 1200px wide for
  in-content screenshots). The theme applies responsive sizing and lazy-loading
  to blog content images; very large originals will still be downscaled by the
  browser but use more bandwidth.
- **Format:** PNG or JPEG is fine. For very large images, consider providing
  WebP versions where the build or CMS supports it; the theme can use
  `<picture>` / `srcset` for fallbacks.

### Metadata and Formatting

- **Quarto (`.qmd`) Posts:** Add a metadata block at the beginning of your
  `index.qmd` file:

  ```markdown
  ---
  title: "Title of Your Blog Post"
  slug: "slug-of-your-blog-post"
  date: YYYY-MM-DD
  authors: ["Author Name"]
  tags: ["tag1", "tag2"]
  categories: ["category1", "category2"]
  description: "Short description of the blog post."
  thumbnail: "/header.jpg"
  template: "blog-post.html"
  ---
  ```

  The body of the file uses standard Markdown plus any Quarto features you need
  (code chunks, figures, etc.). During the build, `makim pages.build` will
  render `index.qmd` to `index.md` using Quarto so that MkDocs can consume the
  generated Markdown.

3. **Building and Viewing:**
   - Run `makim pages.build` to render `index.qmd` to `index.md` and build the
     site. The generated `index.md` is used to render the webpage.

### Regenerating blog Markdown (for CI)

CI expects the rendered `index.md` files under `pages/blog/*/` to be committed.
If you change `.qmd` content or metadata, regenerate and push the markdown:

```bash
# From repo root with conda env active (e.g. on WSL or Linux)
$ makim pages.pre-build
$ git add pages/blog/*/index.md
$ git commit -m "chore: sync rendered blog index.md from qmd"
$ git push
```

On Windows, use WSL or a Linux environment so `makim pages.pre-build` (Quarto) runs correctly.

### Commit messages

Keep commit messages professional and descriptive. Do not add tool or editor tags
(e.g. "Made-with: Cursor") to commit messages.

To fix existing commits that contain such a line (e.g. before pushing a PR):

```bash
# Rebase the last N commits (replace 3 with how many need fixing)
$ git rebase -i HEAD~3
# In the editor, change 'pick' to 'reword' for each commit whose message you want to fix. Save and close.
# For each chosen commit, Git will open the message: remove the "Made-with: ..." line, save and close.
# Then force-push your branch (only for your own PR branch):
$ git push --force-with-lease
```

## Final Steps

Before submitting your blog post:

- Ensure all files are added to your repository.
- For new or migrated posts, confirm that `index.qmd` exists and that
  `makim pages.build` successfully generates the corresponding `index.md`.
- Submit a pull request to the main `opensciencelabs.github.io` repository for
  review.

Thank you for contributing to the Open Science Labs blog!
