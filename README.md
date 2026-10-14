# Huan Ning: Academic Website Prototype

This is a research-oriented website built with **Hugo and HugoBlox** for GitHub Pages.

## Sections

- **News**: Research announcements and updates at `content/news/`.
- **Articles**: Research essays and explainers at `content/articles/`.
- **Blog**: Personal research notes at `content/post/`.
- **Projects**: Independent research project pages at `content/project/`.
- **Publications**: Selected research papers at `content/publication/`.
- **About**: Biography at `content/about.md`.

The homepage automatically lists the latest content for these sections. All content remains Markdown in GitHub for portable backups.

## Publishing with GitHub Pages

1. Review and merge the website prototype pull request into `main`.
2. Open **Settings → Pages** in this repository.
3. Set **Build and deployment → Source** to **GitHub Actions**.
4. The existing workflow at `.github/workflows/publish.yaml` builds and deploys the site when `main` changes.
5. The initial test address will be `https://gladcolor.github.io/huanning/` if Pages deployment is enabled and succeeds.

**Do not add a CNAME or update huanning.me DNS until the test website has been verified.**

## Browser-based editing

The repository includes `.pages.yml` for [Pages CMS](https://app.pagescms.org/).

1. Sign in to Pages CMS with GitHub.
2. Grant the Pages CMS GitHub App access to `gladcolor/huanning`.
3. Select the repository and the appropriate branch.
4. Create or edit entries under News, Articles, Blog, Projects, or Publications.
5. Saving commits a Markdown file. A push to `main` automatically triggers the GitHub Pages workflow.

Editor uploads initially use `/huanning/media`, which is appropriate for the trial URL. Update this media URL when switching to a custom root domain.

## Content migration

The content in this prototype consists of **short summaries and direct links** to original pages at [huanning.me](https://www.huanning.me) and [gladcolor.wordpress.com](https://gladcolor.wordpress.com). It does **not** claim to have imported your complete WordPress archive, attachments, or comments.

For full migration, export WordPress content, verify media copies, and plan redirects for old post URLs.

## Long-term backups

Clone or download this repository periodically. Keep your WordPress XML and image exports separately until full migration is confirmed.

## Template credit

Originally based on the open-source [Hugo Academic CV theme by HugoBlox](https://github.com/HugoBlox/theme-academic-cv). See `LICENSE.md`.
