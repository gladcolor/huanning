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
| Interactive Applications | `content/demos` |
| Publications | `content/publication` |
| Biography | `content/about.md` |

The homepage assembles the latest News, Blog, Articles, Projects, and Publications automatically and highlights one verified live interactive research application.

## Interactive research: long-term architecture

Treat the academic website as a stable **discovery hub**, not the hosting environment for every large research application:

- Add each interactive result to `content/demos/` with `demo_status`, `demo_url`, project URL, source code, and optional publication link.
- Add `demo_url` to related project pages so visitors can launch working software directly from research summaries.
- Client-side applications using JavaScript, HTML, WebGL, or map libraries can be hosted on GitHub Pages in their own repositories, or kept as standalone static assets. They do not require a server-side database.
- Expensive model inference, private credentials, restricted geodata, and large datasets should be hosted separately from the public static website. Do not commit API keys or confidential datasets.
- Keep each demo independently deployable and exportable, using versioned code and data snapshots when licenses permit. Even if a demo becomes unavailable, its research page, description, screenshots, code links and publications can remain intact.
- Prefer explicit **Launch interactive demo** links. Do not assume an outside application permits framing. Add a preview embed only after testing permissions, accessibility, and mobile behavior.
- Do not make all projects wait on the least stable demo: applications should be modular, and failures must not affect the homepage.

The currently verified live app is the [2022 U.S. Hourly Population Map](https://gladcolor.github.io/hourly_population/), with 2D/3D exploration. The website does not claim that all research projects are deployed interactive applications.

## Publishing

1. Merge the review branch after the pull request build check succeeds.
2. Under GitHub repository **Settings > Pages**, set **Build and deployment > Source** to **GitHub Actions**.
3. Publish at `https://gladcolor.github.io/huanning/` and verify the homepage, internal links, articles, projects, and search.
4. Sign in to [Pages CMS](https://app.pagescms.org/) with GitHub, grant access to `gladcolor/huanning`, and select the main branch. The CMS sees the repository's `.pages.yml`.
5. Use News, Blog, Articles, Projects, Interactive Demos, and Publications in Pages CMS. Saving an entry commits a Markdown file; GitHub Actions rebuilds the website.

**Do not change the DNS for huanning.me until the GitHub Pages test site has been checked.** When ready, configure the custom domain under Settings > Pages, then update the domain's DNS records. Update `.pages.yml` media output from `/huanning/media` to `/media` at that time.

## Content migration status

This branch includes a verified biography, research-project pages, selected publications, an initial news feed, and short archive entries for the WordPress weblog. Archive entries link to the complete original posts.

**WordPress articles, original images, comments, and attachments have NOT been fully imported.** Before redirecting the domain or deleting the old blog:

1. Export WordPress.com via Tools > Export (XML).
2. Download media files separately.
3. Convert posts preserving original dates, content, embeds and source URLs.
4. Import media under `static/media/` and check image paths.
5. Compare every imported post with its original, then preserve redirects and backups.

The original sites should remain online until the content and links are verified.

## Longevity / maintenance

- Keep the theme as plain Hugo templates and CSS under `layouts/` and `static/css/`; there are no external theme modules to update.
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
