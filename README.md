# lm-ai.nz

Website for [LensenMcGavin AI](https://lm-ai.nz), an artificial intelligence consultancy focused on responsible AI adoption in Aotearoa New Zealand.

Built with [Jekyll](https://jekyllrb.com/) (based on the [Reverie](https://github.com/amitmerchant1990/reverie) theme) and deployed via GitHub Pages.

## Structure

- `_pages/` — site pages (home, about, media, writing, CPD, contact)
- `_posts/` — op-eds and articles, listed automatically at [/writing/](https://lm-ai.nz/writing/)
- `_includes/inline_style.scss` — the site stylesheet (inlined into every page)
- `_config.yml` — site configuration

## Adding an op-ed

Create `_posts/YYYY-MM-DD-slug.md`:

```yaml
---
layout: post
title: "Title here"
date: YYYY-MM-DD
published_in: RNZ            # optional: outlet that first published it
published_url: https://...   # optional: link to the published version
---
```

The post appears at `lm-ai.nz/slug/` and is listed on the Writing page automatically.
