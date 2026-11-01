# Independent reviewer recruitment plan — Atlas of Biology

**Scope:** Biology atlas only  
**Canonical branch:** `workspace/biology`  
**Repository:** `Ajokendo/Atlas-of-Knowledge`  
**Purpose:** recruit qualified independent reviewers for G4 scientific review and G5 Russian/English editorial review.

## 1. Current status and boundaries

The reviewer documentation package is prepared. This plan operationalizes recruitment; it does not mean that reviewers have been contacted, accepted, or completed a review. No reviewer names, affiliations, availability, fees, or contact details are assumed.

The external review must use one immutable source snapshot and its matching rendered preview. Before sending invitations, record the exact branch-head commit SHA, archive/preview identifier, review scope, expected return date and maintainer in `INDEPENDENT_REVIEW_BUNDLE.md`. Do not send a moving branch link as the review baseline.

## 2. Reviewer roles

| ID | Review function | Required competence | Primary scope |
|---|---|---|---|
| G4-01 | General scientific coordinator | Biology degree or equivalent professional experience; experience in science education or scientific editing; able to assess evidence quality | All 13 pages at overview level; cross-page consistency; review coordination |
| G4-02 | Ichthyology / freshwater ecology | Fish taxonomy and freshwater survey methods; regional Central Asian knowledge is strongly preferred | Son-Kul and Suusamyr fish surveys; Kempir-Abad basin expedition; freshwater fauna and habitat claims |
| G4-03 | Mammalogy / conservation genetics | Mammal taxonomy, population monitoring and/or conservation genetics; competence reading genomic datasets and metadata | Argali genomic study and Dryad metadata; maral counts; snow leopard and other mammal claims |
| G4-04 | Ornithology | Bird identification, distribution and breeding evidence; familiarity with field-record standards | Tibetan Snowcock; Common Crane breeding record at Issyk-Kul; candidate Black-necked Crane record near Soek Pass |
| G4-05 | Herpetology | Reptile and amphibian taxonomy, checklist construction and regional distribution evidence | Reptile checklist snapshot; amphibian checklist; Bufotes taxonomic treatment |
| G4-06 | Botany / regional floristics | Plant taxonomy, floristic survey methods and Central Asian/Kyrgyzstan flora | Botany and Kyrgyzstan flora pages; nomenclature, endemism and regional distribution claims |
| G5-RU | Russian-language editor | Professional Russian editing; experience with educational/scientific texts and terminology control | Russian text across all 13 pages; terminology, grammar, clarity and parity |
| G5-EN | English-language editor | Professional English editing; experience with educational/scientific texts and terminology control | English text across all 13 pages; terminology, grammar, clarity and parity |

A reviewer may cover more than one scientific specialty only when their documented expertise genuinely supports both. The G4 scientific coordinator should not be the sole reviewer of specialist claims. G5-RU and G5-EN should be separate independent reviews; a bilingual editor may provide an additional parity pass but should not silently replace both independent language reviews.

## 3. Independence and eligibility checks

Before assignment, record privately:
- relevant qualifications, current role and subject-specific experience;
- publications, fieldwork, teaching or professional editing relevant to the assigned scope;
- any prior contribution to this atlas or close personal/professional relationship with its authors;
- any financial, institutional or other conflict that could reasonably affect impartiality;
- confirmation that the reviewer can assess the supplied language and evidence directly.

Do not publish private contact details, CVs or correspondence in the repository without explicit permission. If a conflict affects only part of the scope, document the exclusion and assign that part to another reviewer.

## 4. Invitation and assignment sequence

1. Identify potential candidates through universities, research institutes, professional societies, relevant journals and established expert networks. Search by specialty and geography; do not assume that institutional affiliation alone establishes competence.
2. Send a short invitation describing the educational purpose, open-source/free-use context, scope, expected workload, deadline and whether the work is voluntary or funded. Do not imply payment or institutional endorsement unless confirmed.
3. Ask the candidate to disclose relevant expertise and conflicts before sharing any private material.
4. Agree the exact pages/claims, review language, deliverables, deadline and permission to acknowledge the reviewer.
5. Freeze the review snapshot and share the matching read-only archive plus rendered preview.
6. Track acceptance, assignment, receipt, findings, author response and recheck in `INDEPENDENT_REVIEW_TRACKING_REGISTER.md`.
7. Close a review gate only after the signed report and required claim/page records are received and critical/major corrections have been rechecked.

## 5. Minimum deliverables

### G4 scientific
- Signed report identifying reviewer, qualifications, scope, snapshot SHA and date.
- Disposition for each of the 10 priority claims (six P1, four P2): accept, correct, reject, or unresolved, with rationale and evidence.
- Page-level records for assigned pages and decisions for relevant cross-page checks.
- Explicit list of limitations, uncertain claims and items that cannot be verified.
- Recheck confirmation for all critical/major findings after corrections.

### G5 Russian and English
- Separate signed report for each language.
- Page-level review coverage for all 13 pages, or an agreed division of work that collectively covers every page.
- Exact correction proposals with file/page and location, suggested replacement, and reason.
- Terminology decisions and a short style sheet for recurring scientific terms.
- Explicit parity findings where the two language versions differ in meaning, scope, units, names or qualifications.
- Recheck confirmation after accepted corrections.

## 6. Decision and severity rules

- **Critical:** potentially dangerous or materially false scientific information, serious misidentification, or a fundamental error that invalidates a key explanation. Must be resolved before publication.
- **Major:** substantial factual, evidential, taxonomic, translation or interpretation problem. Must be corrected or explicitly resolved before the relevant gate closes.
- **Minor:** local wording, grammar, formatting or non-material clarification. Record and resolve according to editorial policy.
- **Suggestion:** optional improvement that does not indicate an error. May be accepted or declined with a brief rationale.

A reviewer disagreement must remain visible in the issue log until resolved; do not convert an unresolved disagreement into approval by averaging opinions.

## 7. Draft invitation — scientific reviewer

**Subject:** Invitation to independently review the Atlas of Biology (scientific accuracy)

Dear [Name],

We are preparing a free, bilingual Russian-English educational Atlas of Biology, with a dedicated section on the biodiversity of Kyrgyzstan. We would like to invite you to provide an independent scientific review of [assigned subject/pages/claims], particularly [specific topic].

The review is intended to assess scientific accuracy, strength and traceability of evidence, taxonomic and quantitative claims, and whether explanations are appropriate for a school-level educational resource. We will provide a fixed, read-only snapshot, its matching rendered preview, a page-by-page review matrix and a structured claims register.

If you are interested, could you let us know whether the proposed scope matches your expertise, your availability, and whether any conflict of interest would affect your review? We would agree the schedule and acknowledgement arrangements before sharing the review package.

The atlas is intended to remain free to use. No institutional endorsement or payment is implied by this invitation; any compensation, if applicable, would need to be agreed explicitly in advance.

Thank you for considering the invitation.

Kind regards,  
[Sender / project contact]

## 8. Draft invitation — language editor

**Subject:** Invitation to independently edit the [Russian/English] Atlas of Biology

Dear [Name],

We are preparing a free, bilingual Russian-English educational Atlas of Biology and are seeking an independent professional editor for its [Russian/English] version.

The assignment covers 13 pages and focuses on accuracy of meaning, natural and accessible educational language, consistent scientific terminology, grammar and style, and parity with the corresponding second-language version. We will provide a fixed read-only snapshot, a page-level editorial matrix and a structured correction template.

If you are interested, please let us know about your relevant editing experience, availability, any potential conflict of interest and whether the proposed scope is feasible. We would agree the schedule, deliverables and acknowledgement arrangements before the review begins.

Thank you for considering the invitation.

Kind regards,  
[Sender / project contact]

## 9. Recruitment tracker fields

Keep candidate identity and contact information in a private working record, not in this public repository file. The public review register should contain only reviewer IDs or consented acknowledgements, assigned scope, status, snapshot SHA, report reference and gate disposition.

Suggested private tracker fields:
- Reviewer ID; specialty/language; candidate source; qualifications checked;
- conflict-of-interest declaration received; invitation date; response;
- accepted scope; agreed deadline; snapshot SHA sent;
- report received; outstanding questions; corrections assigned;
- recheck received; gate decision; acknowledgement permission.

## 10. Release-gate separation

Recruitment and review do not replace the other open release gates. The 52 planned illustrations remain deferred until assets are produced and checked. Screen-reader testing, measured contrast verification, keyboard operation and physical-device testing must be recorded separately. No publication-ready claim should be made until all applicable gates have evidence and sign-off.
