#!/usr/bin/env python3
"""Copy HabitFlip public assets into the existing GitHub Pages source."""
from pathlib import Path
import shutil
app = Path(__file__).resolve().parents[1]
source = app / "public"
dest = app.parent / "docs" / "habitflip"
allowed = {".html", ".css", ".png", ".svg", ".ico", ".webp"}
for path in sorted(source.rglob("*")):
    if path.is_file() and path.suffix in allowed:
        target = dest / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
print(f"Prepared {dest}; publishing materials excluded.")
