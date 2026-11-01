# Reuse guide — Feedback module for other Atlas subjects

**Source specification:** `FEEDBACK_SYSTEM_STANDARD.md`  
**Pilot:** Atlas of Biology  
**Purpose:** give every subject developer a consistent, copy-ready implementation instruction.

## What to copy into each subject folder

1. Copy `FEEDBACK_SYSTEM_STANDARD.md` into the subject folder (or link to the canonical project-level standard once the shared documentation location is approved).
2. Add a subject-specific implementation note with the subject name, branch, chapter list, and local content anchors.
3. Add the same two entry points to the subject landing page and chapter pages:
   - review the whole subject atlas;
   - comment on this chapter / report a specific issue.
4. Prefill subject, page path, language, and optional section/figure/tool anchor.
5. Use the shared categories, moderation statuses, privacy rules, and accessibility requirements without inventing subject-specific rating scales.
6. Record accepted corrections in that subject's own change log and cite the commit that contains the fix.

## Copy-ready task for a subject developer

> Implement the Atlas of Knowledge feedback standard in this subject only. Read the shared Feedback and Public Review Standard first. Add bilingual, accessible entry points on the subject landing page and each chapter page. A reader must be able to review the whole atlas or report an issue tied to the current chapter or a specific content anchor. Prefill subject, page, language, and anchor where possible. Use the shared feedback categories and moderation states. Do not require registration or email for an ordinary submission. Do not publish personal data or named reviews without explicit consent. Do not create public star ratings or label comments as peer review. Do not enable a submit button until the configured HTTPS endpoint and private moderation queue have been tested end to end. Do not modify other subjects, the shared portal, or publishing configuration without separate authorization. Record all changed paths, tests, and commit SHAs.

## Subject-specific fields

Only add optional fields where they materially help the discipline. Examples:
- Biology: species / scientific name, geographic area, source or observation record.
- Geography: place name, map layer, dataset, date of observation.
- Chemistry: formula, reaction, unit, experimental condition.
- Physics: chapter, equation, laboratory, measured quantity.

These fields must remain optional unless essential to identify the reported issue. Do not require users to disclose personal or sensitive information.

## Integration dependency — do not conceal it

A static website cannot accept and securely retain submissions by itself. Before enabling the form, the project owner must choose and configure one shared endpoint and private moderation store (or a vetted form provider). The same endpoint may serve all subjects if it stores the subject and page metadata reliably. Never place API secrets in public client-side code.

Until the endpoint exists and end-to-end tests pass, show only a clearly labelled “feedback channel is being prepared” state or keep the submit control disabled with an explanation. Do not simulate successful submission.

## Suggested rollout

1. Approve the shared endpoint/provider and privacy terms.
2. Implement and test the component in Biology as the pilot.
3. Validate anonymous submission, moderation, privacy, and bilingual/accessibility behaviour.
4. Freeze the component contract and copy it to each subject branch/folder.
5. Add the portal-wide entry point only when the shared portal owner authorizes changes to the portal files.
6. Track adoption subject by subject; never edit another subject's branch as part of the Biology pilot.
