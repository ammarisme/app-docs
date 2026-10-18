# app-docs

Public documentation and GitHub Pages content for Ammar’s apps.

GitHub Pages source: **`main` branch → `/docs` folder**.

## Live URLs

| Path | Purpose |
|------|---------|
| [`docs/index.html`](docs/index.html) | **Finnish Pro** landing page (App Store: https://apps.apple.com/us/app/finnish-pro/id6815337238) |
| [`docs/learn-finnish/`](docs/learn-finnish/) | Privacy, terms, support, remote config |

- Landing: https://ammarisme.github.io/app-docs/
- Privacy / terms: https://ammarisme.github.io/app-docs/learn-finnish/
- Support: https://ammarisme.github.io/app-docs/learn-finnish/support.html
- Bootstrap config: https://ammarisme.github.io/app-docs/learn-finnish/api.json

## App directories

Each app owns its own directory. The existing Finnish Pro site remains in `docs/`. HabitFlip is published in its own `docs/habitflip/` subdirectory.

| Directory | App | Contents |
| --- | --- | --- |
| `docs/` | Finnish Pro | Existing public site and documentation |
| [`habitflip/`](habitflip/README.md) | HabitFlip | Public pages, assets, and publishing materials |

HabitFlip’s public files live in `habitflip/public/`; submission materials live in `habitflip/publishing/`. Run `python3 habitflip/publishing/prepare_site.py` to copy only HabitFlip public assets into `docs/habitflip/`, then commit and push to `main`. Publishing notes are excluded.
