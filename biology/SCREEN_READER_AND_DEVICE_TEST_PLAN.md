# Biology Atlas — screen-reader and real-device test plan

**Status / Статус:** prepared; all hands-on tests below are **Pending**.  
**Branch / Ветка:** `workspace/biology`  
**Scope / Объём:** 13 Biology HTML pages, Russian and English modes, interactive models, tables and navigation.

This document is a test protocol, not evidence that assistive-technology or physical-device testing has already been performed. Automated Chromium and axe-core results are recorded in `PROGRESS_CHECKPOINT.md`.

## 1. Test environments / Среды тестирования

Record the exact versions and date for every test session.

| Environment | Required coverage | Status |
|---|---|---|
| Windows 11 + NVDA + Firefox | Full chapter navigation, headings, landmarks, buttons, live announcements | Pending |
| Windows 11 + NVDA + Chrome | Repeat critical interactions and dynamic announcements | Pending |
| Android + TalkBack + Chrome | Touch exploration, swipe navigation, language switch, interactive models and tables | Pending |
| iOS + VoiceOver + Safari | Rotor/headings/landmarks, touch exploration, controls and tables | Pending |
| Physical mobile browser without screen reader | Layout, zoom, overflow, focus visibility, touch target and orientation checks | Pending |

If a listed device or assistive technology is unavailable, record it as **Not tested / Не проверено**. Do not infer a pass from another platform.

## 2. Common checks on every page / Общие проверки каждой страницы

- [ ] Page title identifies the subject/chapter and language.
- [ ] The skip link is reachable first by keyboard and moves focus to the main content.
- [ ] Header, navigation, main content and footer are announced in a logical order.
- [ ] Heading navigation follows a meaningful hierarchy; no heading level is used only for visual styling.
- [ ] Links have understandable names out of context; external links open safely.
- [ ] All visible buttons and controls have useful names that include their visible labels.
- [ ] Language switch announces the destination language and updates the document language.
- [ ] The active language is understandable; hidden-language text is not announced.
- [ ] Focus is visible and follows a logical order; no keyboard trap occurs.
- [ ] At 200% and 400% zoom, content remains usable without loss of essential information.
- [ ] Text spacing and reflow do not hide controls or content.
- [ ] No unintended horizontal page scrolling at mobile width; horizontally scrollable tables remain independently reachable.

## 3. Interactive model checks / Интерактивные модели

For each interaction, test both languages and record the exact control, announced result and any delay.

| Page / Страница | Critical interaction | Expected announcement / Ожидаемое объявление |
|---|---|---|
| Landing page | Six SVG organelles; Tab, Enter, Space | Organelles have names; selected organelle description is announced |
| Botany | Organ, condition and quiz controls | Selected state and explanatory/quiz feedback are announced |
| Zoology | Animal-group selector and quiz | Selected group and updated description are announced |
| Cell biology | Organelle, transport and mitosis controls | Selected state and model output are announced |
| Anatomy | Organ-system selector and quiz | Selected system and updated description are announced |
| Genetics | DNA template, codon and mutation controls | Updated sequence/result is announced |
| Microbiology | Organism group, shape and growth phase | Selected state and output are announced |
| Ecology | Food-chain, carbon, nitrogen and pressure controls | Each selected process and its explanation are announced |
| Evolution | Selection, mechanism, homology and timeline controls | Updated model output is announced |
| Biochemistry | Enzyme, factor, ATP and respiration controls | Updated explanation is announced |
| Systematics | Rank, domain, species name and key controls | Selected state and dynamic species-name output are announced |
| Kyrgyzstan flora | Navigation, source lists, evidence key and tables | Lists are announced as lists; tables expose row/column context |
| Kyrgyzstan fauna | Navigation, source lists, evidence key and tables | Lists are announced as lists; tables expose row/column context |

For native buttons, verify Enter and Space activation. For the custom SVG organelle controls, verify both keys and confirm focus does not disappear. For toggle buttons, verify the announced pressed/not-pressed state matches the visible state.

## 4. Table and navigation checks / Таблицы и навигация

- [ ] Focus each horizontally scrollable table region.
- [ ] Use ArrowLeft and ArrowRight to scroll the table without moving the whole page unexpectedly.
- [ ] Confirm the screen reader announces the region's purpose and table headers/cell associations.
- [ ] Verify the table can be exited with Tab and that focus continues in a predictable order.
- [ ] Confirm no content is available only by hover or pointer.
- [ ] Test portrait and landscape orientations on mobile.

## 5. Defect recording / Регистрация дефектов

For each finding, record:

1. Date and tester.
2. Device, OS, browser and exact assistive-technology version.
3. Page URL/path and language.
4. Steps to reproduce, including keyboard/touch actions.
5. Expected result and actual announcement/behaviour.
6. Impact: Critical / Serious / Moderate / Minor.
7. Screenshot or short recording where appropriate, avoiding personal data.
8. Fix commit, retest result and closure date.

Do not mark a platform or page as passed until every critical/serious finding is fixed or explicitly documented as an accepted limitation by the project owner.

## 6. Release interpretation / Интерпретация готовности

- Automated axe-core and Chromium checks are **automated evidence only**.
- A pass on NVDA does not certify TalkBack or VoiceOver, and vice versa.
- A successful responsive viewport test is not a physical-device test.
- The manual tests above remain Pending until performed on the named environments and recorded.
- This plan does not change the controlled Biology readiness score by itself.
