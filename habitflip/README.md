# HabitFlip

Public source lives in `habitflip/public/`; store preparation lives in `habitflip/publishing/`.

The GitHub Pages source is `main` → `/docs`. Run `python3 habitflip/publishing/prepare_site.py` to prepare `docs/habitflip/`, then commit and push. The script copies only public HTML, CSS, and image assets. Existing Finnish Pro pages remain in place.

Public base: https://ammarisme.github.io/app-docs/habitflip/

Validate with `python3 habitflip/publishing/validate.py`. Preview with `python3 -m http.server 8874 --directory docs --bind 127.0.0.1`, then open `http://127.0.0.1:8874/habitflip/`.
