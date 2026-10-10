# Mindful Lock

All Mindful Lock documentation and publishing materials live in this app-specific directory. `/docs` belongs to the existing Finnish Pro app.

```text
mindful-lock/
├── public/       # Landing, support, privacy, terms, credits, web assets
└── publishing/   # Store copy, review notes, screenshot plan, release checklist
```

- [Public site](public/index.html)
- [Publishing package](publishing/README.md)
- [Release checklist](publishing/release-checklist.md)

From the repository root:

```sh
python3 mindful-lock/publishing/validate.py
python3 -m http.server 8874 --directory mindful-lock/public --bind 127.0.0.1
```

Preview: `http://127.0.0.1:8874/`.

The existing GitHub Pages source (`main` → `/docs`) serves Finnish Pro. Mindful Lock requires deployment configuration for its own public directory; the current proposed store URLs are not live. Deploy only `public/`, preserving the other app and excluding submission notes.
