# Validation record

Verified 10 October 2026 during package preparation.

- `python3 mindful-lock/publishing/validate.py`: **154 static checks passed** after correcting the subtitle to 30 characters. Name 12/30, subtitle 30/30, promotional text 135/170, description 1,963/4,000, keywords 98/100 UTF-8 bytes.
- Validated five HTML pages, local targets and fragments, image alt attributes, basic document metadata, PNG dimensions, metadata/text consistency, and six ordered screenshot scenes.
- Adjacent app `python3 qa/audit-local-privacy.py`: passed its static source guard. This is not a traffic capture or a release-device test.
- Local landing preview returned HTTP 200. Browser review covered landing at 1200px and 390px widths and support navigation plus an FAQ expansion. Fixed responsive image aspect ratio after observing distortion. This is focused visual review, not comprehensive accessibility certification.
- Existing Finnish Pro pages and assets were not modified; only the root README gained Mindful Lock pointers.
- No app build, device suite, live deployment, submission, entitlement approval, or final screenshot capture was performed as part of this package.

The preview server is local and temporary. Reopen it using the package README command when needed.

## Directory correction

Moved all Mindful Lock files into the top-level `mindful-lock/` app directory, with `public/` and `publishing/` subdirectories. Updated validator paths, local preview commands, links, and deployment instructions. `/docs` is restored to the existing app only. Revalidated after moving; no page layout or feature changes.
