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


## 11. Public institutional routes researched (candidate sources, not endorsements)

The following are publicly documented institutional routes relevant to the review scope. They are **potential channels for requesting nominations**, not confirmed reviewer acceptances. A listed staff member should be approached only after checking current role, relevant publications, availability and conflicts of interest. In particular, anyone involved in producing a source record under review should not independently validate that same record without a separate conflict assessment.

| Route | Publicly documented relevance | Possible review assignment / next action | Public route |
|---|---|---|---|
| Institute of Biology, National Academy of Sciences of the Kyrgyz Republic — Laboratory of Ichthyology and Hydrobiology | Researches Kyrgyzstan's aquatic biodiversity, fish fauna, hydrobionts, lakes and rivers. The institutional page names laboratory head Шайгул Асылбаева and lists staff. | First contact route for G4-02. Ask the institute to nominate an independent fish taxonomist; check whether the candidate authored or participated in any Son-Kul, Suusamyr or Kempir-Abad source being reviewed. | https://ibnaskr.org/laboratoriya-ikhtiologii-i-gidrobiologii/ ; public lab email shown on the page: asylbaeva76@gmail.com |
| Institute of Biology, NAS KR — Laboratory of Vertebrate Zoology | Official page documents research on Kyrgyzstan's birds and mammals, population monitoring, rare species, field surveys and conservation. It names laboratory head Аскар Давлетбаков. | Nomination route for G4-03, G4-04 and G4-05 (mammals, birds, herpetology). Request separate specialists where needed; screen conflicts carefully if staff contributed to cited datasets or checklist records. | https://ibnaskr.org/laboratoriya-zoologii-pozvonochnykh-zhivotnykh/ ; general institute contact: ibnaskr@mail.ru, +996 559 355 308 |
| Institute of Biology, NAS KR — Laboratory of Flora and related plant research units | The institute lists a Laboratory of Flora and a geobotany/ecosystem-restoration laboratory among its research units. | Nomination route for G4-06. Request a plant taxonomist/florist with Kyrgyzstan or Central Asian flora expertise, not simply a general horticulture reviewer. | https://ibnaskr.org/ ; general institute contact above |
| J. Balasagyn Kyrgyz National University — Faculty of Biology | Official faculty page lists Botany and Plant Physiology, Zoology/Human and Animal Physiology, and General Biology/Ecology departments. | Potential academic nominations for botany, zoology, ecology and general biology. Ask faculty administration to route the request to a researcher with recent relevant publications. | https://www.knu.kg/ky/en/faculties |
| Kyrgyz-Turkish Manas University — Department of Biology / Faculty of Sciences | Official research page lists biochemistry, animal science, wild animals, cytogenetics, ecology, evolution, biodiversity, plant science, microbial biology, molecular genomics and bioinformatics. | Potential independent reviewers for general biology, genetics/genomics, ecology, botany and zoology; assess exact specialist fit and language of review. | https://manas.edu.kg/en/natural_sciences/biology/research ; public university contact: info@manas.edu.kg, +996 (312) 54 19 41-47 |
| E. Gareev Botanical Garden | Official institutional information describes it as a base for botanical field practice for several Kyrgyz universities. | Additional nomination route for flora/taxonomy and plant identification; prioritize a research botanist/florist rather than relying on horticultural expertise alone. | https://botanica.kg/field_practices/ ; official contact details are published by the garden and should be reconfirmed before use. |
| Ilbirs Foundation | Its public profile describes field research and conservation work involving snow leopards, marmots, flora and fauna; it is a conservation organization, not an academic peer-review body. | Possible referral route for mammal/conservation practitioners and independent field specialists; use only as a source of nominations, not as a substitute for academic taxonomic review. | https://ilbirs.org/english/about-us ; public contact page: https://ilbirs.org/english/contact |
| National Academy of Sciences / Institute of Biology institutional directory | Official Academy directory lists the Institute of Biology, its director and public institutional contact details. | Formal institutional route if direct lab outreach is not appropriate; request independent external nominations and clarify that the atlas authors are seeking review, not institutional endorsement. | https://kruia.gov.kg/content_list/show/56/ru ; ibnaskr@mail.ru, +996 559 355 308 |

### Recruitment assessment after source mapping

- **Strongest first route:** Institute of Biology NAS KR, because its publicly described laboratory structure directly matches the atlas's regional fish, vertebrate, bird, mammal, herpetology and flora review needs.
- **Academic cross-check routes:** KNU Faculty of Biology and Manas University Biology Department, to seek reviewers outside the source-producing unit and to obtain subject-specific nominations.
- **Specialist supplementary routes:** E. Gareev Botanical Garden for plant identification/floristics; Ilbirs for conservation-practitioner referrals, not independent academic approval.
- **Language-editor recruitment:** approach university language/philology departments and professional editors separately. The biology departments above are not evidence of professional Russian or English editing competence.
- **No named person is yet marked as a confirmed candidate or contacted reviewer.** Publicly named laboratory heads are institutional contact points only; suitability and independence must be established before assignment.


## 12. Preliminary named reviewer leads — evidence and conflict screening (75% preparation milestone)

The people below are **potential leads for nomination or an exploratory invitation**, not confirmed candidates, contacted reviewers, accepted reviewers or institutional endorsements. Their public profiles establish a plausible subject match only. Current availability, willingness, independence, language capability and conflicts must still be checked privately before any assignment.

| Review area | Potential lead | Public evidence for subject fit | Independence / conflict screen required | Status |
|---|---|---|---|---|
| G4-02 Ichthyology / freshwater ecology | Шайгул Мокешовна Асылбаева | The Institute of Biology NAS KR profile identifies her as head of its Ichthyology and Hydrobiology Laboratory and describes expertise in fish fauna, fish parasites, aquaculture, rare fish and aquatic monitoring. https://ibnaskr.org/laboratoriya-ikhtiologii-i-gidrobiologii/ | Establish whether she or her laboratory produced, collected or analysed any Son-Kul, Suusamyr or Kempir-Abad records in the atlas. If so, exclude those records from her independent review and seek an external reviewer for them. | Potential lead; not contacted; availability unknown. |
| G4-04 Ornithology | Сергей Викторович Кулагин | A public expert profile describes a PhD-level zoology qualification, research on passerine birds in the Issyk-Kul basin, bird monitoring and ornithological work; it identifies him as a researcher at the Institute of Biology NAS KR. https://map.kg/ru/jeksperty/66-kulagin-sergej-viktorovich.html | Verify current institutional role and recent publications. Check any contribution to the atlas's cited bird observations, checklists or datasets; exclude self-authored records from independent adjudication. | Potential lead; profile requires current-status confirmation; not contacted. |
| G4-03 Mammalogy / conservation genetics; G4-04 birds | Аскар Темирбекович Давлетбаков | The Institute of Biology NAS KR identifies him as head of the Vertebrate Zoology Laboratory, with research on birds, mammals, rare species and monitoring. The page also lists the 2026 argali SNP paper among the laboratory's publications. https://ibnaskr.org/laboratoriya-zoologii-pozvonochnykh-zhivotnykh/ | **Known publication conflict for the argali genomic claim:** he is a co-author of the cited 2026 argali SNP paper. Do not assign independent review of that paper, its dataset or conclusions. A separate bird/mammal scope may be considered only after checking all cited sources and field records for direct involvement. His expertise alone does not establish independent genetics-review eligibility. | Potential lead for a restricted scope only; conflict recorded; not contacted. |
| G4-06 Botany / regional floristics | Георгий Анатольевич Лазьков | The Institute of Biology NAS KR identifies him as Doctor of Biological Sciences and head of the Flora Laboratory, with expertise in Kyrgyzstan flora, taxonomy, rare and endemic plants. https://ibnaskr.org/laboratoriya-flory/ | **Known publication conflict for the alien-plant inventory:** he co-authored the 2024 paper on alien plants of Kyrgyzstan listed on the institutional profile. Do not ask him to independently adjudicate that paper or claims derived directly from it. Check other chapter sources for authorship, specimen or project involvement before assigning any remaining scope. | Potential lead for a restricted scope only; conflict recorded; not contacted. |
| G5-RU Russian-language editor | No individual identified yet | Manas University publicly documents Russian Language and Literature within its Department of Philology; Bishkek State University lists a Faculty of Russian Philology and an Academic Writing course. https://www.manas.edu.kg/en/humanities/philology ; https://bsu.kg/ru/fakultet-russkoj-filologii/ | Request nominations for an independent professional editor experienced in scientific/educational Russian. Verify editing samples, terminology practice and conflicts. A department or faculty is a nomination route, not a reviewer. | Institutional routes identified; no individual lead verified. |
| G5-EN English-language editor | No individual identified yet | Manas University publicly documents an English Language and Literature programme within its Department of Philology. https://www.manas.edu.kg/en/humanities/philology | Request nominations for an independent professional English editor with science/education experience. Verify native-level or equivalent editing competence, samples and conflicts. | Institutional route identified; no individual lead verified. |

### Specialist gaps still requiring nominations

- **G4-05 Herpetology:** no sufficiently verified individual specialist has been identified. The Vertebrate Zoology Laboratory is a nomination route only; request a named reptile/amphibian taxonomist with recent regional checklist or field-publication evidence.
- **G4-03 Independent population genetics:** the publicly identified laboratory head has a direct co-authorship conflict for the argali genomic source. Seek a population geneticist outside that source team, preferably with experience reviewing sample provenance and genomic metadata.
- **G4-01 General scientific coordinator:** no individual candidate has yet been verified against the required cross-disciplinary science-education and evidence-review criteria.
- **G5-RU / G5-EN:** university departments are routes to nominations, not evidence that any named person has accepted or is qualified for this particular assignment.

### 75% recruitment-preparation assessment

Candidate-level evidence is now documented for several scientific areas, and known source-authorship conflicts have been made explicit. The shortlist is intentionally partial: unresolved specialist gaps remain, and no candidate has been contacted or confirmed. This milestone measures preparation of a defensible recruitment shortlist only; it does not measure completion of G4/G5 reviews or increase the atlas's controlled editorial-readiness score.


### 12.1 Additional specialist and language-editor leads identified after the 75% checkpoint

The following leads extend the shortlist. They remain uncontacted and unconfirmed. A public staff profile or publication record is evidence of a plausible fit, not proof of availability or independence.

| Review area | Potential lead | Public evidence for subject fit | Independence / conflict screen required | Status |
|---|---|---|---|---|
| G4-05 Herpetology | Татьяна Николаевна Дуйсебаева (Institute of Zoology, Kazakhstan) | The Institute of Zoology's official profile identifies her as a herpetology specialist working on amphibian and reptile systematics, ecology, phylogeny and Central Asian herpetofauna. Her listed work includes a 2023 report on new *Bufotes pewzowi* records in southern Kyrgyzstan and a 2024 paper on reptile communities in southeastern Kazakhstan. https://zool.kz/sotrudniki-laboratorii-ornitologii-i-gerpetologii/dujsebaeva-tatyana-nikolaevna/ ; https://old-sg.sgu.ru/en/articles/reptile-communities-of-desert-landscapes-and-analysis-of-the-herpetofauna-of-southeastern | Strong regional subject match. Before assignment, compare her publications and field records with every amphibian/reptile claim in the atlas. Exclude her own 2023 *Bufotes* record and any other source she co-authored from independent adjudication; ask her to disclose field-team and checklist involvement. | Strong potential lead for a restricted scope; not contacted; availability unknown. |
| G5-EN English-language editor | Ольга Юрьевна Шубина (Kyrgyz-Russian Slavic University) | The official KRSU page identifies her as head of the Department of English Theory and Practice and Intercultural Communication, Candidate of Philological Sciences and associate professor. https://www.krsu.kg/obrazovanie/kafedry/kafedra-teorii-i-praktiki-anglijskogo-yazyka-i-mezhkulturnoj-kommunikacii/ | Verify professional editing experience in scientific/educational English through a sample edit and references; confirm that she can edit the full scope and is independent of atlas authors. Teaching credentials alone do not establish copy-editing capacity. | Potential nomination/invitation lead; not contacted. |
| G5-RU Russian-language editor | Айнура Ракымбергеновна Абдыкасымова (Bishkek State University) | The official Faculty of Russian Philology page lists her as head of the Department of General and Russian Linguistics. https://bsu.kg/ru/fakultet-russkoj-filologii/ | Verify current position, editing portfolio and experience with scientific/educational texts; request a short paid or unpaid sample only after terms are agreed. Check independence from atlas authors. | Potential nomination/invitation lead; not contacted. |

### 12.2 Updated recruitment gaps and assignment safeguards

- **Herpetology:** a strong regional specialist lead is now identified outside Kyrgyzstan. Her prior co-authorship of a 2023 *Bufotes pewzowi* record involving southern Kyrgyzstan means that particular record, and any other source she co-authored, must be excluded from her independent adjudication.
- **Population genetics:** no suitable independent reviewer for the argali genomic claim has yet been verified. A general genetics or plant-population-genetics profile is not an adequate substitute for mammalian conservation genomics and sample-provenance review. Continue seeking an expert with relevant animal genomic datasets who did not author the cited argali paper or dataset.
- **General scientific coordinator:** still requires a person with demonstrated science-education/scientific-editing coordination and broad biological literacy; do not assign this role solely on seniority or institutional title.
- **Russian and English editing:** named academic leads are now available for exploratory nomination, but editing samples, workload, language competence, independence and terms remain to be checked.
- No invitations have been sent and no reviewer has accepted. The 75% recruitment-preparation milestone remains the latest completed milestone until the remaining specialist gaps and outreach-readiness checks are resolved.
