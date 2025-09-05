---
title: "Packaging a VS Code Extension Using pnpm and VSCE"
slug: "packaging-a-vs-code-extension-using-pnpm-and-vsce"
date: 2025-08-31
authors: ["Ansh Arora"]
tags: ["Makim", "Automation", "VSCode", "pnpm", "esbuild"]
categories: ["Packaging", "Node", "Extensions"]
description: |
  A step-by-step guide to packaging and publishing VS Code extensions with pnpm and vsce, 
  covering how to avoid dependency resolution issues.
thumbnail: "/header.png"
template: "blog-post.html"
---

# Packaging a VS Code Extension Using pnpm and VSCE

VS Code’s `vsce` tool doesn't play nicely with `pnpm` out of the box; here’s a
proven workaround using bundling and the `--no-dependencies` flag to get things
running smoothly.

---

## Why pnpm + vsce can be problematic

`vsce` relies on `npm list --production --parseable --depth=99999`, which fails
under pnpm's symlink-based dependency management, often throwing
`npm ERR! missing:` errors.  
([github.com](https://github.com/microsoft/vscode-vsce/issues/421),
[daydreamer-riri.me](https://daydreamer-riri.me/posts/compatibility-issues-between-vsce-and-pnpm/))

---

## Solution Overview

1. **Bundle your extension** using a bundler such as **esbuild** or **Webpack**
2. **Use `--no-dependencies`** when running `vsce package` and `vsce publish`

Because all dependencies are bundled, `vsce` no longer needs to resolve them
from `node_modules`.

---

## Step-by-Step Setup

### 1. Install Tools

```bash
pnpm add -D @vscode/vsce esbuild
```

@vscode/vsce` is the CLI for packaging and publishing VSCode extensions. Recent
versions (e.g., v3.6.0) support npm (≥6) and Yarn (1.x), but don't officially
support pnpm.

### 2\. Configure `package.json`

Scripts Add build and packaging commands: jsonc Copy code

```json
{
  "scripts": {
    "vscode:prepublish": "pnpm run bundle",
    "bundle": "esbuild ./src/extension.ts --bundle --outfile=out/main.js --external:vscode --format=cjs --platform=node --minify",
    "package": "pnpm vsce package --no-dependencies",
    "publish": "pnpm vsce publish --no-dependencies"
  }
}
```

- `vscode:prepublish`: runs before packaging; bundles source using esbuild
- `bundle`: compiles `extension.ts` into `out/main.js` and excludes the `vscode`
  module
- `package` / `publish`: calls VSCE via pnpm, skipping dependency resolution

### 3\. Why It Works

By bundling dependencies manually, `vsce` doesn’t need to resolve them during
packaging or publishing. The `--no-dependencies` option avoids pnpm’s symlink
issues entirely.

## Sample `package.json` Snippet

```json
{
  "devDependencies": {
    "@vscode/vsce": "^3.6.0",
    "esbuild": "^0.XX.X"
  },
  "scripts": {
    "vscode:prepublish": "pnpm run bundle",
    "bundle": "esbuild ./src/extension.ts --bundle --outfile=out/main.js --external:vscode --format=cjs --platform=node --minify",
    "package": "pnpm vsce package --no-dependencies",
    "publish": "pnpm vsce publish --no-dependencies"
  }
}
```

### **Wrap-Up**

Using **pnpm** with VS Code extensions involves a few extra steps because `vsce`
doesn’t support pnpm’s dependency structure directly. The ideal workflow: _
**Bundle your extension first**, then _ **Use `--no-dependencies`** to package
and publish safely.
