# Learn Finnish — public docs

User-facing pages for the **Learn Finnish** iOS app (privacy, terms, support, remote config).

## Published files (GitHub Pages root for this app)

| Path | Purpose |
|------|---------|
| [`index.html`](index.html) | Privacy policy, terms (summary), support contact |
| [`api.json`](api.json) | Remote config bootstrap (`apiBaseURL`, feature flags) for the iOS app |

Do **not** put internal engineering notes here — only what end users / App Store / the app binary need.

## URLs (after Pages is enabled on `app-docs`)

- Privacy / terms: `https://ammarisme.github.io/app-docs/learn-finnish/`
- Bootstrap config: `https://ammarisme.github.io/app-docs/learn-finnish/api.json`

The iOS client reads `api.json` via `RemoteConfigStore.pagesBootstrapURL`.
