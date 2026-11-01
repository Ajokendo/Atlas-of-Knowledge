

### Reproducible browser-audit toolchain

The Chemistry CI workflow installs exact versions of its browser-audit dependencies rather than floating npm tags: Playwright `1.64.1` and axe-core `4.14.0`. It prints the resolved top-level dependency tree with `npm ls --depth=0` before installing Chromium, so CI logs retain evidence of the tool versions used for each run. These are test-only dependencies; the static Chemistry Atlas remains dependency-free for visitors. Update either pinned version deliberately, then review the release notes and require a fresh full CI run before accepting the change.
