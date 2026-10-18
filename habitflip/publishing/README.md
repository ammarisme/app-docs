# HabitFlip publishing package

Prepared 10 October 2026 from the adjacent HabitFlip source checkout and the app-docs repository's existing docs. This package is **prepared, not published or App Store submission-ready**. All public-facing files live in `habitflip/public/`; internal preparation lives here, beside the public site within the app’s own directory.

## Contents

- [App Store fields](app-store/metadata.json) and paste-ready [English copy](app-store/en-US/description.txt).
- [Review notes](app-review-notes.md): physical-device walkthrough and permission details.
- [Family Controls request brief](family-controls-brief.md).
- [Privacy answers and code evidence](privacy-assessment.md).
- [Screenshot storyboard](screenshots.csv) and [capture guide](screenshot-guide.md).
- [TestFlight copy and acceptance](testflight.md).
- [Launch copy](launch-copy.md).
- [Release checklist](release-checklist.md): specific open items, including signing, entitlements, in-app policy link, device evidence, and captures.
- [Source references](sources.md), [validation script](validate.py), and [verification record](validation-report.md).

## Planned public URLs

| App Store field | URL |
| --- | --- |
| Marketing | https://ammarisme.github.io/app-docs/habitflip/ |
| Support | https://ammarisme.github.io/app-docs/habitflip/support.html |
| Privacy | https://ammarisme.github.io/app-docs/habitflip/privacy.html |
| Terms summary | https://ammarisme.github.io/app-docs/habitflip/terms.html |
| Audio credits | https://ammarisme.github.io/app-docs/habitflip/credits.html |

The public route is `/app-docs/habitflip/`. Prepare it with `python3 habitflip/publishing/prepare_site.py`, which copies only `habitflip/public/` into `docs/habitflip/` for the existing main → /docs Pages deployment. Publishing notes are excluded; existing Finnish Pro hosting is preserved.

## Preview and validate

From the app-docs root:

```sh
python3 habitflip/publishing/validate.py
python3 -m http.server 8874 --directory habitflip/public --bind 127.0.0.1
```

Open `http://127.0.0.1:8874/`. The existing `/docs` directory belongs to Finnish Pro and is not used by HabitFlip.

## Decisions still needed

Confirm seller/copyright name, support email ownership, pricing, distribution regions, age-rating answers, review contact name/phone, and final Apple App ID. Draft category: Health & Fitness, with Productivity secondary. Existing Xcode settings support iPhone and iPad; retain both only after testing and preparing the required screenshots. No price, rating, approval, or availability has been invented.

The landing page deliberately says “Preparing for the App Store.” After approval, add the verified App Store URL and official badge, replace that message, and optionally add an Apple Smart App Banner with the real ID.

## Scope

This is a local artifact package in the cloned app-docs repository. No app source changes, App Store submission, GitHub push, or deployment were performed. The original app-docs landing page and Learn Finnish pages are preserved.
