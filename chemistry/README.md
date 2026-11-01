

### Reproducible browser-audit toolchain

The Chemistry CI workflow installs exact versions of its browser-audit dependencies rather than floating npm tags: Playwright `1.64.1` and axe-core `4.14.0`. It prints the resolved top-level dependency tree with `npm ls --depth=0` before installing Chromium, so CI logs retain evidence of the tool versions used for each run. These are test-only dependencies; the static Chemistry Atlas remains dependency-free for visitors. Update either pinned version deliberately, then review the release notes and require a fresh full CI run before accepting the change.


### Verification checkpoint — 2026-11-01

- [x] Pinned-toolchain commit `d203edc1e79207df727b480a199fbb747225e2f0`: Chemistry Actions run [41321214353](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41321214353) completed successfully.
- [x] Documentation commit `f3fe2b96c0a0f7db25ce6f2408116c9403a279e9`: Chemistry Actions run [41321221712](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41321221712) completed successfully.
- [x] Both runs completed the repository validation, pinned browser-tool installation, local server startup, and Chromium tests across the Chemistry pages.
- [x] The latest recorded automated accessibility gate covers all 21 Chemistry pages in Russian and English (42 axe-core scans), with no serious or critical findings in the final CI run.
- [ ] Physical-device, screen-reader, and independent scientific reviews remain external pending gates; CI success does not satisfy them.
