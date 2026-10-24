# Huan Ning Academic Website

An independent, low-maintenance website for Huan Ning's research and writing.

- Website: Hugo (pinned to version 0.136.5)
- Hosting: GitHub Pages with the GitHub Actions workflow in `.github/workflows/publish.yaml`
- Content storage: versioned Markdown files in this repository
- Editorial UI: [Pages CMS](https://app.pagescms.org/), configured by `.pages.yml`
- Search: Pagefind static index generated during build, version 1.5.2

**No database, paid web server, remote theme module, JavaScript framework, or runtime service required.**

## Structure

| Section | Folder |
|---|---|
| News | `content/news` |
| Research Articles | `content/articles` |
| Blog | `content/post` |
| Research Projects | `content/project` |
| Publications | `content/publication` |
| Biography | `content/about.md` |

The homepage assembles the latest News, Blog, Articles, Projects, and Publications automatically and links to independently hosted interactive research applications from project pages.

## Interactive projects: external links only

The main personal site contains project descriptions and links, not embedded applications. A project may set `demo_url`, `paper_url`, `repo_url`, and `data_url` in its front matter. Project pages show simple links labelled **Interactive Demo**, **Paper**, **Code Repository**, and **Dataset** only when those URLs are provided. The homepage project card shows the interactive demo URL when available.

Each interactive app is maintained and hosted separately in its own repository. If a demo is offline, the academic site's text and other research pages will continue to work. Other optional related resources can be added as ordinary Markdown links to publications, code, and datasets. Do not put API keys or private data in the website repository.

The U.S. Hourly Population Explorer is a currently linked example: https://gladcolor.github.io/hourly_population/

## Publishing

1. Merge the review branch after the pull request build check succeeds.
2. Under GitHub repository **Settings > Pages**, set **Build and deployment > Source** to **GitHub Actions**. A preview branch has already deployed successfully; its public address is https://gladcolor.github.io/huanning/.
3. Publish at `https://gladcolor.github.io/huanning/` and verify the homepage, internal links, articles, projects, and search.
4. Sign in to [Pages CMS](https://app.pagescms.org/) with GitHub, grant access only to `gladcolor/huanning`, and open the repository. **While the prototype branch is the live deployed website, select `website-prototype-2026-10`, not `main`.** After final review, merge the PR into `main` and switch the editor to `main` only when deployment is configured for that branch. The CMS reads `.pages.yml` on the selected branch.
5. Use News, Blog, Articles, Projects, and Publications in Pages CMS. Saving an entry commits a Markdown file; GitHub Actions rebuilds the website.

**Do not change the DNS for huanning.me until the GitHub Pages test site has been checked.** When ready, configure the custom domain under Settings > Pages, then update the domain's DNS records. Update `.pages.yml` media output from `/huanning/media` to `/media` at that time.

## Content migration status

This branch includes a verified biography, research-project pages, selected publications, an initial news feed, and short archive entries for the WordPress weblog. Archive entries link to the complete original posts.

**All 11 public WordPress posts returned by the REST API have been imported as independent Markdown pages with local images and original HTML backed up; four Google Sites source pages have been archived, the full bibliography restored, and research projects and figures migrated.** Private posts, drafts, restricted attachments, external video/iframe assets, and content accessible only through signed-in administrator exports are not covered. Before redirecting the domain or deleting the old blog:

1. Export WordPress.com via Tools > Export (XML).
2. Download media files separately.
3. Convert posts preserving original dates, content, embeds and source URLs.
4. Import media under `static/media/` and check image paths.
5. Compare every imported post with its original, then preserve redirects and backups.

The original sites should remain online until the content and links are verified.

## Longevity / maintenance

- Keep the theme as plain Hugo templates and CSS under `layouts/` and `static/css/`; there are no external theme modules to update.
- Card and list thumbnails come from the optional `image` front-matter field (Pages CMS: **Card image**), otherwise from the first image in the body. Hugo resizes local images to small WebP files at build time.
- The Hugo version and Pagefind version are pinned in GitHub Actions.
- Use GitHub's **Download ZIP** or `git clone` periodically for local offsite backups, and retain the WordPress XML and media archive.
- Update the GitHub Actions versions periodically when needed for security/support compatibility. 'Low maintenance' does not imply no maintenance forever.
- Keep original research figures and large binaries out of the site repository if they exceed GitHub Pages limits. Link to archived datasets, scholarly repositories, or GitHub releases.
- Existing historic content stays readable without a CMS login.

## Design references

- [DataHealth Lab](https://datahealthlab.org/): research and latest news hierarchy
- [Urban Demographics](https://www.urbandemographics.org/): research writing and publications
- [Penn State GIScience](https://giscience.psu.edu/): news, blog, and research navigation
- [W3C Web Accessibility Initiative](https://www.w3.org/WAI/tips/designing/): contrast, navigation and mobile layouts

This is an original design inspired by established academic website patterns, not a copy of another site's code or branding.

## Adding content through Pages CMS

1. Open https://app.pagescms.org/ and sign in to GitHub as gladcolor.
2. Authorize only the huanning repository, then select branch `website-prototype-2026-10` while it powers the preview.
3. Select News, Research Articles, Blog, Projects, Publications, or About. Click New for a new entry or open an existing entry to edit.
4. Fill Title, Date, Summary, and the rich-text Body. Optional links in Projects are Interactive Demo URL, Paper URL, Code Repository URL, and Dataset URL.
5. Click Save. Pages CMS writes a Markdown file to the chosen branch, where the GitHub Pages workflow rebuilds the website.
6. Verify the published URL. New News automatically appears in Latest News; recent Blog/Articles appear in Research & Writing.

The CMS is configured to preserve existing frontmatter not explicitly shown in its form, including historical tags and reference metadata. This avoids accidental metadata loss when editing older posts.

**Important:** A CMS draft is an item with `draft: true`. Hugo does not publish drafts by default. Set it to false when ready. The current site preview uses the prototype branch, not main.


## Public archive migration verification

Read `MIGRATION_STATUS.md`, `migration-report.json`, and the raw source files under `archive/google-sites/` and `archive/wordpress/`. The original Google Sites publications page is preserved in `archive/google-sites/publications.md`, and the public WordPress article bodies are independent Markdown pages with locally stored images under `static/media/wordpress/`. Media downloaded from the public Google Sites pages is under `static/media/google-sites/`. Compare article layouts and image placement against the original sites before switching domain names.

## CMS editing note

A published WordPress article with `wordpress_id` is self-contained, and no "Read the original WordPress version" box is shown on the new website. The original source URL is retained in the Markdown front matter and full API backups for verification only.

## Website editorial policy

All migrated WordPress articles are self-contained; the public site must not display links back to the old WordPress site as substitutes for article bodies. Retain the old URLs only as source metadata and in the migration archive. News articles derived from WordPress must include the complete relevant content, not merely a link. Legacy WordPress originals remain preserved for offline audit, not navigation. To prevent duplicate summary entries, the original Gemma 4 placeholder was removed and its URL redirected to the complete migrated post.
