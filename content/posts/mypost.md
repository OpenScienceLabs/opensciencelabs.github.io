---
title: 'Using Hugo page bundles'
description: 'Page bundles are an optional way to organize content within Hugo.'
summary: "Page bundles are an optional way to organize page resources within Hugo. You can opt-in to using page bundles in Hugo Clarity with `usePageBundles` in your site configuration --- or in a page's front matter." # For the post in lists.
date: '2022-03-24'
aliases:
  - hugo-page-bundles
author: 'Hugo Authors'
usePageBundles: true
thumbnail: '/home-banner.svg'

featureImage: '/home-banner.svg' # Top image on post.
# featureImageAlt: 'Description of image' # Alternative text for featured image.
# featureImageCap: 'This is the featured image.' # Caption (optional).
# thumbnail: 'thumbnail.jpg' # Image in lists of posts.
# shareImage: 'share.jpg' # For SEO and social media snippets.

categories:
  - syntax
tags:
  - Hugo
series:
  - Themes Guide
---

[Page bundles](https://gohugo.io/content-management/page-bundles/) are an optional way to [organize page resources](https://gohugo.io/content-management/page-resources/) within Hugo.

You can opt-in to using page bundles in Hugo Clarity with `usePageBundles` in your site configuration or in a page's front matter. [Read more about `usePageBundles`.](https://github.com/chipzoller/hugo-clarity#organizing-page-resources)

With page bundles, resources for a page or section, like images or attached files, live **in the same directory as the content itself** rather than in your `static` directory.

Hugo Clarity supports the use of [leaf bundles](https://gohugo.io/content-management/page-bundles/#leaf-bundles), which are any directories within the `content` directory that contain an `index.md` file. Hugo's documentation gives this example:

<!-- ---
title: "First post"
date: 2022-09-24T21:26:16-04:00
draft: false
usePageBundles: true
featureImage: 'https://images.unsplash.com/photo-1447069387593-a5de0862481e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1169&q=80'

---

# Título grande

## Some code

En este post demostramos la posibilidad de usar este buen generador de sitios

```py
def factorial(n):
    if n<2:
        return n*factorial(n-1)
```

> Este es un mensaje de la tipo frase famosa

$$
y = x^2
$$ -->
