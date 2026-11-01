# Atlas of Knowledge — Feedback and Public Review Standard

**Pilot subject:** Biology  
**Canonical branch:** `workspace/biology`  
**Scope:** reusable product and editorial standard for the whole Atlas of Knowledge portal. This file is stored in the Biology work area as the first pilot specification; it does not authorize edits to other subject folders or shared portal files.

## 1. Purpose

Provide readers with a simple, free way to report factual errors, unclear explanations, translation issues, accessibility barriers, technical faults, and ideas for improvement. Feedback is an editorial input, not an automatic scientific verdict and not a substitute for formal peer review.

## 2. Two entry points

### Portal-wide feedback

Use for:
- comments about the Atlas of Knowledge portal as a whole;
- navigation, search, accessibility, and cross-subject problems;
- proposals for new subjects or shared features.

The portal entry point should identify the portal as the target and allow an optional subject selection.

### Subject-atlas feedback

Every subject atlas should expose:
- **Review this atlas** — general feedback about the subject atlas;
- **Comment on this chapter** — feedback tied to the current chapter;
- **Report a specific issue** — an optional anchor to a section, figure, table, interactive tool, or claim.

When a reader opens the form from a chapter or a specific content block, the subject, language, page path, and content anchor should be prefilled. The reader must still be able to correct them.

## 3. Feedback categories

Use the same category vocabulary across all subjects:
1. Scientific / factual correction
2. Source, citation, or data concern
3. Explanation or structure
4. Russian/English translation or terminology
5. Illustration, chart, map, or table
6. Interactive feature or technical problem
7. Accessibility or mobile display
8. Suggestion / general comment

Do not use public star ratings as a proxy for scientific quality. A rating can reward popularity rather than accuracy and is not needed for this project.

## 4. Minimum submission fields

Required:
- category;
- comment or description;
- target (portal, subject atlas, chapter, or specific content anchor).

Optional:
- name or pseudonym;
- email for a reply;
- organization / professional affiliation;
- source or evidence link;
- preferred response language.

Do not require registration or an email address for an ordinary submission. Do not ask for sensitive personal data. Explain that an anonymous submission cannot receive a personal reply.

## 5. Review workflow and public status

All incoming submissions enter a private moderation queue first. Suggested states:
- **Received** — submission recorded;
- **Under review** — editor is checking it;
- **Confirmed** — the issue is supported by evidence;
- **Correction in progress** — an update is being prepared;
- **Fixed** — correction is published and linked to a version/commit;
- **Not confirmed** — evidence does not support the proposed correction;
- **Deferred** — valid suggestion, scheduled for later;
- **Duplicate** — already reported elsewhere.

A public status page may show the issue summary, status, date, and resolution. Do not publish the submitter's email, private correspondence, or identity without explicit consent. Do not publish abusive, promotional, defamatory, or personally identifying content.

## 6. Scientific integrity

- A submission is a claim to investigate, not proof that the atlas is wrong.
- Scientific changes require checking primary or authoritative sources and recording the editorial decision.
- For material scientific corrections, retain the old and new wording, evidence, date, and responsible editor in the change log.
- If evidence is inconclusive, label the issue unresolved or deferred; do not silently rewrite the claim.
- A reader may optionally provide credentials, but self-declared credentials must not be displayed as verified.
- Do not call a user comment an expert review or peer review unless a separately documented review process actually took place.
- A person must not approve their own contribution or their own publication/data as independent evidence.

## 7. Privacy, safety, and moderation

- Keep contact details separate from public feedback text.
- Collect the minimum data needed to process the submission.
- Publish a short privacy notice beside the form: purpose, optional contact field, publication/consent choice, retention period, and contact route for privacy requests.
- Obtain explicit opt-in before publishing a named review or quoting a person.
- Provide an abuse-reporting and moderation path.
- Use server-side validation, rate limiting, spam controls, and safe output encoding. Never trust client-side validation alone.
- Do not expose internal moderation notes or submitter contact details in the public repository.

## 8. Technical architecture

The site is currently a static HTML atlas. A visible HTML form alone cannot safely store submissions, moderate them, send notifications, or provide anonymous intake. Do not ship a fake submit button or imply that feedback has been received when no endpoint exists.

Recommended architecture:
1. Shared feedback form component with bilingual labels and accessible validation.
2. A configured HTTPS submission endpoint (or a vetted form service selected by the project owner).
3. Private storage / moderation queue with restricted access.
4. Optional public, sanitized issue-status feed.
5. Editorial workflow that links confirmed fixes to a commit or release.

The endpoint and storage provider must be selected and configured before enabling submission. Keep secrets out of HTML, JavaScript, and the public repository. A free service may have limits, data-processing terms, or account requirements; verify those before choosing it.

## 9. Accessibility and bilingual behaviour

- Full keyboard operation, visible focus, programmatic labels, and clear error messages.
- Do not rely on colour alone for status.
- Support Russian and English labels and confirmation messages.
- Preserve the reader's selected language when opening the form.
- Ensure the form works on narrow mobile screens and with screen readers.
- Use plain language and explain what happens after submission.

## 10. Release checklist

- [ ] Portal-wide and subject-level entry points have distinct target scopes.
- [ ] Chapter/content anchor is prefilled correctly and editable.
- [ ] No account or email is required for an ordinary submission.
- [ ] Privacy notice and consent for public attribution are present.
- [ ] Endpoint, storage, access control, rate limiting, and spam controls are configured.
- [ ] Form success is shown only after the server confirms receipt.
- [ ] Moderation statuses and public/private fields are tested.
- [ ] Keyboard, screen-reader, contrast, mobile, and bilingual tests pass.
- [ ] A confirmed correction can be traced to evidence and a published commit.

**Current pilot status:** policy and architecture specified. No live feedback endpoint or moderation database is configured by this document. Do not describe the form as operational until the complete submission path is tested.


## Reusable interface template
- `FEEDBACK_WIDGET_TEMPLATE.html` provides a bilingual accessible form template for the Biology pilot and later subject reuse.
- The endpoint is intentionally unconfigured and the submit control stays disabled. The template is not a live submission channel until an approved HTTPS endpoint and private moderation queue are configured and tested.
