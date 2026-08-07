# Dummy Test Files (Intentionally Buggy)

These files are just for testing your Git/GitHub push workflow. They are **not meant to run correctly** — each one has intentional errors.

## Files

- **buggy_calculator.py** — missing colon, typo (`retrun`), divide-by-zero, `=` instead of `==`, undefined variable
- **buggy_app.js** — missing comma in object, off-by-one loop bug, call to a function that doesn't exist
- **buggy_page.html** — unclosed tags, wrong DOM method name (`getElementByID` instead of `getElementById`), reference to a missing variable

## Purpose

Push this folder to GitHub to confirm your `git init` / `git add` / `git commit` / `git push` flow works end-to-end. Since Git only tracks files (it doesn't run them), these will push and appear on GitHub just fine even though the code itself is broken.
