"""
Sessions 03–16 — Complete Teaching Modules
Each session follows the mandatory structure:
A. Session Overview, B. Theoretical Concepts, C. Research Story,
D. Visual, E. Demonstration, F. Activity, G. Case, H. Quiz, I. Reflection
"""
import streamlit as st
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils import (concept_card, gold_card, reveal_box, warn_box,
                   section_divider, session_header, teaching_flow,
                   render_quiz_block, render_activity, render_case)

# ═══════════════════════════════════════════════════════════════════════════════
# SESSION DATA REGISTRY
# ═══════════════════════════════════════════════════════════════════════════════

SESSIONS = {

"s03": {
"code": "S03", "title": "AI-Assisted Literature Search",
"clos": ["CLO 3"], "number": 3,
"why": "A literature review is only as good as its search strategy. AI tools offer speed but introduce bias and coverage gaps that researchers must actively manage.",
"flow": ["Opening: the search strategy problem", "Theoretical Concepts — search types and tools", "Research Story", "Visual: Literature Search Funnel", "Demo — live multi-tool search", "Activity — Boolean + AI search comparison", "Case + Quiz + Reflection"],
"concepts": [
  ("Search Strategy Types", "Three complementary approaches: (1) Keyword search in databases (Scopus, WoS) — systematic and reproducible but misses synonyms and conceptual neighbours. (2) Semantic/AI search (Elicit, Consensus) — meaning-based, discovers conceptual neighbours but may miss terminologically distinct papers. (3) Citation chaining (backward: check references; forward: check who cited a key paper) — discovers influential work that may not appear in keyword results."),
  ("Boolean Logic", "AND narrows (both terms must appear). OR broadens (either term). NOT excludes. Parentheses group. Example: (\"artificial intelligence\" OR \"machine learning\" OR \"algorithmic\" ) AND (\"talent management\" OR \"recruitment\" OR \"HR\") NOT \"clinical\". Building a search string requires first identifying synonym groups for each concept."),
  ("Source Evaluation — CRAAP Test", "Currency: how recent is the source? Relevance: does it address the research question? Authority: who wrote it and where was it published? Accuracy: is it evidence-based? Purpose: why was it written? Apply systematically when AI tools surface unfamiliar sources."),
  ("Semantic Search Limitations", "Semantic search tools (Elicit, Consensus) represent papers as meaning vectors. Strength: discovers conceptually related papers across disciplines. Weakness: may retrieve false positives (similar language, different concept) and miss jargon-dense papers that use different terminology for the same idea."),
  ("Grey Literature", "Non-peer-reviewed scholarly outputs: government reports, working papers, preprints (SSRN, arXiv), NGO reports, conference proceedings, theses. Important for systematic reviews because peer-reviewed literature overrepresents significant positive findings (publication bias). Grey literature captures null results and policy-relevant evidence."),
],
"story": """The Library Without Walls

Before digital databases, a literature review meant weeks in a physical library, pulling journals from shelves, following footnotes, and hoping the library had what you needed. A review was literally bounded by access.

Now the library has no walls. We have access to tens of millions of papers. The constraint has inverted: it is not scarcity but abundance that creates the problem. How do you search meaningfully in a space where searching 'AI and organisations' returns 340,000 results?

The answer is strategy. A researcher who opens Google Scholar and types their topic, reads the first ten results, and calls it a literature review has not searched — they have browsed. Browsing is how you end up missing the foundational paper that your examiners will ask you about.

A search strategy treats the literature as territory to be mapped systematically: keyword domains, synonym groups, database coverage, citation chaining, grey literature, date ranges. Each decision is documented, each result counted and accounted for.

AI tools change this picture. They can search faster, surface semantic neighbours, and synthesise consensus. But they cannot document their own search logic in a way PRISMA requires. They cannot tell you what they missed. They search the territory they were trained on.

The skilled researcher uses AI to search faster — and still documents what was searched, how, and why. Speed does not excuse documentation.

Classroom prompt: If I asked you right now to find the five most important papers in your field, how would you start?""",
"activity": {
  "title": "Boolean vs Semantic Search Comparison",
  "task": "Step 1: Build a Boolean search string for your research topic using at least two synonym groups and one exclusion. Run it in Scopus and record the number of results. Step 2: Enter the same research question in natural language into Elicit.org. Record results. Step 3: Compare: How many papers appear in both? How many are unique to each? What does this tell you about the coverage of each approach?",
  "student_role": "Search strategist",
  "expected_output": "A comparison table: search method, number of results, number of verifiable papers, unique papers not found by the other method, and one sentence conclusion on why using both methods is better than either alone.",
  "time_minutes": 25,
  "sample_answer": "Boolean search in Scopus ('AI' OR 'machine learning') AND ('performance management') returned 487 papers. Elicit returned 12 papers to the question 'Does AI-based performance management affect employee motivation?' Overlap: 4 papers appeared in both. 8 papers from Elicit were not in the Scopus results — 3 used different terminology ('algorithmic feedback'), 2 were very recent preprints. 3 Scopus papers I reviewed were not surfaced by Elicit despite being directly relevant. Conclusion: both tools are necessary; neither is sufficient alone.",
  "weak_answer": "I searched both tools and got different results. Elicit was easier to use.",
  "improved_answer": "Boolean Scopus search: ('artificial intelligence' OR 'algorithmic') AND ('employee wellbeing') returned 312 results. Elicit natural language search returned 9 papers. Overlap: 5 papers. Unique to Elicit: 4 papers — 2 used 'AI workplace' terminology, 1 was a preprint, 1 from a non-Scopus-indexed journal. Unique to Scopus: many papers using formal terminology not captured by Elicit's semantic model. Neither tool alone is comprehensive.",
  "debrief": "Why does multi-source searching matter for PRISMA? What would a reviewer ask if you only used one tool?",
  "grading_hints": "Award marks for: actual search execution (not hypothetical), specific numbers, comparison table, and clear conclusion.",
  "common_mistakes": "Students describe what they would do rather than doing it. Push for actual execution with real numbers.",
  "scholarly_link": "This activity is the foundation of the Annotated Bibliography assignment and prepares for PRISMA documentation in S04."
},
"case": {
  "title": "The One-Database Review",
  "scenario": "Meera's systematic review searched only Scopus, used a single three-word keyword string, and found 45 papers. She is satisfied with this. Her supervisor notes that a comparable review in her field used four databases, three synonym groups, and citation chaining — and found 312 papers. Meera argues: 'Scopus covers everything important.'",
  "question": "How would you evaluate Meera's search strategy? What is the scholarly risk of her approach?",
  "weak_response": "She should use more databases to be safe.",
  "strong_response": "Meera's claim is empirically false: no single database achieves full coverage of any field. Scopus indexes approximately 20,000 journals, but significant research appears in Web of Science (different coverage), EBSCO Business Source Complete (management-focused), PubMed (health management), and grey literature sources. Her three-word string almost certainly misses papers using synonymous terminology. A systematic review with inadequate search strategy is not systematic — it is a convenience sample of papers, which is a fundamental validity problem. Reviewers and examiners will ask for PRISMA documentation, which will immediately expose the thin search strategy.",
  "issue_diagnosis": "Single-database, single-string search dramatically limits coverage and introduces selection bias into the literature sample.",
  "theory": "Systematic review methodology requires comprehensive, documented, multi-source searching to minimise selection bias.",
  "research_gap": "Not applicable — this is a methodological error.",
  "research_question": "Not applicable.",
  "scholarly_framing": "A systematic review must be systematic in its search, not just its analysis. The search strategy is a quality criterion, not a procedural formality.",
  "instructor_note": "Use this case to establish the minimum acceptable search standard for any review in this course."
},
"quiz": [
  {"number": 1, "session": "S03", "difficulty": "Beginner", "clo": "CLO 3", "concept": "Boolean AND",
   "question": "In a database search, the Boolean operator AND:",
   "options": ["Broadens the search by including either term","Narrows the search by requiring both terms to be present","Excludes papers containing the term","Groups synonyms together"],
   "correct": 1,
   "explanation": {"concise": "AND requires both terms in the same result, narrowing the search.", "detailed": "AND is the narrowing operator. ('AI') AND ('healthcare') returns only papers mentioning both AI and healthcare. Using OR instead would return papers about AI OR papers about healthcare — a much larger, less targeted set.", "doctoral_relevance": "Correct Boolean logic is foundational for systematic review search documentation.", "instructor_emphasis": "Demo in Scopus: run AI, healthcare, and AI AND healthcare separately and show result counts."},
   "wrong_reasons": ["Option A describes OR.", "Option C describes NOT.", "Option D describes parenthetical grouping."],
   "teaching_insight": "The most basic search concept — but mistakes here have cascading effects on review coverage.", "follow_up": "Write a Boolean string for 'AI in talent management, excluding recruitment.'"},
  {"number": 2, "session": "S03", "difficulty": "Intermediate", "clo": "CLO 3", "concept": "Citation Chaining",
   "question": "Forward citation search in Google Scholar means:",
   "options": ["Searching papers published before a key paper", "Finding papers listed in the references of a key paper", "Finding papers that cited a key paper after its publication", "Searching by author name forward through time"],
   "correct": 2,
   "explanation": {"concise": "Forward citation search finds papers that cited your seed paper — revealing how the field built on, critiqued, or extended the work.", "detailed": "Backward (reference list) = who influenced this paper. Forward (cited by) = who was influenced by this paper. Both directions are needed for comprehensive literature mapping.", "doctoral_relevance": "Foundational papers in a field are often discovered through forward citation chaining from a seed paper.", "instructor_emphasis": "Demo: open a well-known paper, click 'Cited by' in Google Scholar, show the range of papers."},
   "wrong_reasons": ["Option A describes a date filter, not citation chaining.", "Option B describes backward citation search.", "Option D describes an author search."],
   "teaching_insight": "Many students have only ever searched forward in time (new papers). Backward and forward citation chaining are both new skills.", "follow_up": "Perform forward citation search on one foundational paper and identify the most-cited subsequent work."},
  {"number": 3, "session": "S03", "difficulty": "Advanced", "clo": "CLO 3", "concept": "AI Search Limitations",
   "question": "A researcher uses only Consensus.app for a systematic review. What is the PRIMARY methodological problem?",
   "options": ["Consensus.app is too slow for large reviews", "The tool's indexing coverage, ranking algorithm, and search logic are not transparent enough to satisfy PRISMA reproducibility requirements", "Consensus.app does not support Boolean search", "The tool only covers psychology journals"],
   "correct": 1,
   "explanation": {"concise": "PRISMA requires transparent, reproducible search documentation. Consensus.app's algorithmic logic is not fully disclosed, making the search non-reproducible.", "detailed": "Systematic reviews must document: databases searched, date of search, full search strings, and inclusion/exclusion criteria. AI tools with proprietary algorithms cannot satisfy the reproducibility criterion — another researcher cannot replicate the exact same search. PRISMA 2020 guidelines require this documentation.", "doctoral_relevance": "Journals publishing systematic reviews will desk-reject papers without PRISMA-compliant search documentation.", "instructor_emphasis": "Show the PRISMA search documentation template and ask what information Consensus.app cannot provide."},
   "wrong_reasons": ["Option A — speed is not the methodological concern.", "Option C — Consensus does not use Boolean, but that is not the primary problem.", "Option D — coverage limitation is a real concern but secondary to reproducibility."],
   "teaching_insight": "This distinguishes students who understand why documentation matters from those who treat it as bureaucratic formality.", "follow_up": "Design a search protocol for a systematic review that uses AI tools while satisfying PRISMA documentation requirements."},
  {"number": 4, "session": "S03", "difficulty": "Intermediate", "clo": "CLO 3", "concept": "Synonym Groups",
   "question": "Why must a systematic search string include synonym groups rather than a single term per concept?",
   "options": ["To make the search string look more sophisticated", "Because different papers use different terminology for the same concept, and single terms miss papers using alternative language", "Because databases require a minimum of three terms", "To increase the number of results regardless of relevance"],
   "correct": 1,
   "explanation": {"concise": "Academic literature uses diverse terminology for the same construct across disciplines and time periods. Single terms miss relevant papers.", "detailed": "For 'AI in HR,' relevant papers may use: 'artificial intelligence,' 'machine learning,' 'algorithmic management,' 'automated recruitment,' 'predictive HR analytics.' A search using only 'artificial intelligence' misses all papers using any other formulation. Synonym group construction is a core systematic review skill.", "doctoral_relevance": "Reviewers of systematic reviews evaluate whether the search string adequately covers terminological variation.", "instructor_emphasis": "Brainstorm synonym groups for one concept in the class's area collectively before searching."},
   "wrong_reasons": ["Option A — length is irrelevant to search quality.", "Option C — no database requires a minimum term count.", "Option D — relevance, not volume, is the goal."],
   "teaching_insight": "Synonym group construction is the most intellectually demanding part of search string design.", "follow_up": "Build a synonym group for the concept 'employee wellbeing' as it might appear across management, psychology, and healthcare literatures."},
  {"number": 5, "session": "S03", "difficulty": "Doctoral Challenge", "clo": "CLO 3, 8", "concept": "Epistemic Representativeness",
   "question": "A researcher's literature review draws exclusively from Scopus-indexed, English-language journals published since 2015. What systematic bias is introduced?",
   "options": ["The review is too recent to be credible", "The review excludes foundational older work, non-English scholarship, and non-Scopus-indexed outputs, potentially misrepresenting the state of knowledge", "Restricting to Scopus improves quality because it only indexes peer-reviewed work", "This is the standard approach and introduces no bias"],
   "correct": 1,
   "explanation": {"concise": "Any bounded search introduces coverage bias — the question is whether the boundaries are justified by the research question or arbitrary.", "detailed": "Date restriction to post-2015 excludes foundational theory papers. English-only restriction excludes scholarship from non-Anglophone research traditions (important for management research in Asia, Africa, and Latin America). Scopus exclusion removes some niche, specialist, or regional journals. All these restrictions are potentially justifiable — but must be stated and defended, not assumed as defaults.", "doctoral_relevance": "Examiners will ask: 'Who is missing from your review?' Researchers must be able to justify their search boundaries.", "instructor_emphasis": "Discuss: what would change about the picture of 'AI in management' if Chinese, Brazilian, and Indian research in non-English languages were included?"},
   "wrong_reasons": ["Option A — recency is not the issue; the boundaries as a package are.", "Option C — Scopus does index peer-reviewed work but not all peer-reviewed work.", "Option D — all search boundaries introduce bias; the question is whether it is justified."],
   "teaching_insight": "Reflective search design is a doctoral-level skill — knowing what your search misses is as important as knowing what it finds.", "follow_up": "Write a three-sentence search limitation statement for a review conducted using the criteria in this question."},
],
"reflection": """After this session, you should be able to:
- [ ] Construct a Boolean search string with synonym groups and exclusions
- [ ] Describe the difference between keyword search and semantic AI search
- [ ] Explain what forward and backward citation chaining add to a search strategy
- [ ] Identify three types of grey literature relevant to your research area
- [ ] Explain why PRISMA requires documented, reproducible search strings

**What to produce:** Draft a three-source search strategy for your thesis topic (database, AI tool, citation chain) with documentation for each source.

**Assessment link:** The Annotated Bibliography assignment requires a documented search strategy. This session provides the methodology."""
},

"s04": {
"code": "S04", "title": "Systematic Review & PRISMA",
"clos": ["CLO 3"], "number": 4,
"why": "Systematic reviews are the gold standard for synthesising evidence. Understanding how to conduct and report one — or to critically evaluate published ones — is a core doctoral competency.",
"flow": ["Opening: why systematic?", "Theoretical Concepts — PRISMA, quality appraisal", "Research Story", "Visual: PRISMA Flow Diagram", "Demo — building inclusion/exclusion criteria", "Activity — PRISMA flow documentation", "Case + Quiz + Reflection"],
"concepts": [
  ("What is a Systematic Review?", "A systematic review follows a pre-specified, documented protocol to identify, select, appraise, and synthesise all relevant evidence on a research question. It differs from a narrative review in its: transparency (documented search), reproducibility (another researcher could replicate it), comprehensiveness (multi-source search), and rigour (quality appraisal of included studies). It is not simply 'a thorough review' — it is a methodology with its own standards."),
  ("PRISMA 2020", "Preferred Reporting Items for Systematic Reviews and Meta-Analyses. The 2020 update requires: documented search strings for each database, PRISMA flow diagram (records identified → duplicates removed → screened → assessed for eligibility → included), risk of bias assessment for included studies, and a certainty of evidence summary. PRISMA is not just for meta-analyses — it is the reporting standard for any systematic literature review."),
  ("Inclusion and Exclusion Criteria", "Criteria must be: specified before searching (to prevent bias), grounded in the research question (not convenience), documented, and consistently applied. Common criteria: publication type (peer-reviewed only or include grey literature?), date range (justified by the field's development history), population (which organisations, which roles?), methodology (all designs? quantitative only?), language (English only? If so, why?). Every exclusion criterion introduces potential bias that must be acknowledged."),
  ("Risk of Bias Assessment", "Quality appraisal asks: how much confidence can we place in the findings of each included study? Tools include: Cochrane RoB-2 (for randomised trials), Newcastle-Ottawa Scale (for observational studies), CASP checklists (for qualitative studies). Key domains: randomisation, blinding, attrition, selective reporting, confounding control. High-risk-of-bias studies may be excluded or their findings downweighted."),
  ("Meta-Analysis vs Narrative Synthesis", "Meta-analysis statistically pools effect sizes when studies are sufficiently homogeneous. Narrative synthesis summarises findings without statistical pooling when studies are too heterogeneous. The choice depends on the research question and the degree of similarity across studies — not on whether a synthesis 'feels' quantitative or qualitative."),
],
"story": """The Evidence Maze

Imagine you are a hospital administrator trying to decide whether to implement an AI triage system. Twenty studies exist. Some say it improves accuracy. Some say it introduces racial bias. Some study the wrong outcome. Some have serious methodological flaws. How do you know what the evidence actually says?

This is the problem that systematic reviews solve. Without a systematic approach, every reader forms their own impression based on the papers they happened to read, the papers that were easy to find, and the papers that confirmed what they already believed. This is called narrative bias.

A systematic review says: here is every paper that met our criteria, here is how we evaluated their quality, and here is our evidence-based conclusion — with explicit acknowledgement of how confident we are in it.

For doctoral researchers, the systematic review offers two things. First, it is a methodology you can use to produce a high-quality, publishable literature contribution. Second, understanding systematic review methodology makes you a better critical reader of evidence — because you know what to look for when you read any literature review.

The PRISMA flow diagram is not bureaucracy. It is an answer to the question: 'How do you know you found everything?' It is the researcher's proof that the review was conducted with discipline, not convenience.

Classroom prompt: Think of a policy decision in your field. What evidence would you need to make that decision confidently?""",
"activity": {
  "title": "Build a PRISMA Flow Diagram",
  "task": "For a hypothetical review on 'AI-assisted diagnosis in radiology': (1) Start with 500 records identified (Scopus: 300, PubMed: 150, grey literature: 50). (2) Apply: remove duplicates (80), screen by title/abstract (exclude 280 irrelevant), assess full text (exclude 85 with reasons: wrong outcome 40, wrong population 25, poor quality 20). (3) Calculate final included count. (4) Draw the PRISMA flow diagram manually and label each box.",
  "student_role": "Systematic review methodologist",
  "expected_output": "A hand-drawn or digitally produced PRISMA flow diagram with correct counts at each stage and labelled exclusion reasons.",
  "time_minutes": 20,
  "sample_answer": "Identified: 500 (Scopus 300, PubMed 150, Grey 50). After duplicate removal: 420. Screened: 420, excluded 280 on title/abstract = 140 full texts assessed. Excluded full texts: 85 (wrong outcome 40, wrong population 25, quality 20). Included: 55 studies. The flow diagram shows: 500 → 420 → 140 → 55, with exclusion reasons at each stage.",
  "weak_answer": "I would include about 50 papers after removing the ones that are not relevant.",
  "improved_answer": "PRISMA flow: Records identified = 500 (Scopus 300, PubMed 150, grey 50). Duplicates removed = 80. Screened by title/abstract = 420, excluded = 280 (irrelevant population, wrong study design). Full texts assessed = 140, excluded = 85 (wrong outcome n=40, wrong population n=25, insufficient quality n=20). Final included = 55.",
  "debrief": "Ask: why must we document reasons for exclusion, not just numbers? What does a reviewer learn from the exclusion reasons?",
  "grading_hints": "Award marks for: correct arithmetic, labelled exclusion reasons, correct structure, and understanding of why each stage exists.",
  "common_mistakes": "Students skip exclusion reasons — they report counts without explaining why studies were excluded.",
  "scholarly_link": "PRISMA documentation is required for the Annotated Bibliography assignment and any systematic review paper."
},
"case": {
  "title": "The Missing Exclusion Criteria",
  "scenario": "Ravi submits a systematic review that screened 450 papers and included 32. When a reviewer asks 'What were your exclusion criteria?', Ravi replies: 'I used my judgement to pick the most relevant papers.' The reviewer recommends rejection.",
  "question": "Why did the reviewer reject the review, and what should Ravi have done?",
  "weak_response": "Ravi should have written down his reasons for excluding papers.",
  "strong_response": "Ravi's approach is the opposite of systematic — it is judgement-based selection, which is precisely what systematic reviews exist to prevent. Exclusion criteria must be: (a) pre-specified (before screening begins, not after), (b) grounded in the research question, (c) applied consistently across all records, and (d) documented with reasons per excluded full text. 'My judgement' is subjective and cannot be reproduced. The review is not a systematic review — it is a narrative review with a misleading label, which is a misrepresentation of methodology.",
  "issue_diagnosis": "Absence of pre-specified, documented inclusion/exclusion criteria — the core quality requirement of systematic reviews.",
  "theory": "Systematic review methodology (Cochrane, PRISMA) explicitly requires pre-specified criteria to prevent selection bias.",
  "research_gap": "Not applicable — this is a methodological error.",
  "research_question": "Not applicable.",
  "scholarly_framing": "A systematic review without documented criteria is a narrative review. Mislabelling the methodology constitutes misrepresentation.",
  "instructor_note": "Use this case to make clear that the review methodology label must match the methods actually used."
},
"quiz": [
  {"number": 1, "session": "S04", "difficulty": "Beginner", "clo": "CLO 3", "concept": "PRISMA Purpose",
   "question": "The primary purpose of the PRISMA flow diagram is to:",
   "options": ["Display the statistical results of reviewed studies", "Document and justify the process by which studies were identified, screened, and included or excluded", "Show author affiliations", "Illustrate conceptual relationships between papers"],
   "correct": 1,
   "explanation": {"concise": "PRISMA makes the search and selection process transparent and reproducible — showing exactly how the final included studies were reached.", "detailed": "The PRISMA flow diagram documents: records identified per source, duplicates removed, records screened, records excluded after screening (with reasons), full texts assessed, full texts excluded (with reasons), and records finally included. This transparency allows readers to assess whether the review is comprehensive and unbiased.", "doctoral_relevance": "Journals publishing systematic reviews require a PRISMA diagram. Absence is a common desk-rejection trigger.", "instructor_emphasis": "Show a published PRISMA diagram and walk through each box."},
   "wrong_reasons": ["Option A — forest plots display meta-analytic results.", "Option C — affiliations are in the byline.", "Option D — concept maps show relationships, not search process."],
   "teaching_insight": "Many students encounter PRISMA for the first time here. A visual walkthrough with a real example is essential.", "follow_up": "Draw a simplified PRISMA flow diagram for a review starting with 600 records and ending with 30 included studies."},
  {"number": 2, "session": "S04", "difficulty": "Intermediate", "clo": "CLO 3", "concept": "Inclusion Criteria",
   "question": "Which of the following is the BEST justification for limiting a systematic review to quantitative studies?",
   "options": ["Qualitative studies are less rigorous", "The research question focuses on measurable effect sizes, for which quantitative studies provide the relevant evidence type", "Qualitative studies are harder to find", "Quantitative studies are always better quality"],
   "correct": 1,
   "explanation": {"concise": "Inclusion criteria must be justified by the research question, not by a hierarchy of methods.", "detailed": "A question about diagnostic accuracy requires quantitative studies with sensitivity and specificity data. Including qualitative studies on clinicians' experiences would not answer that question. However, if the question includes 'how do clinicians experience AI tools?', qualitative studies are essential. The research question drives the criteria.", "doctoral_relevance": "Examiners will ask: 'Why did you exclude qualitative/quantitative studies?' The answer must be question-grounded.", "instructor_emphasis": "Introduce 'fit for purpose' — no method is universally superior."},
   "wrong_reasons": ["Option A — methodological prejudice is not a valid criterion.", "Option C — availability is not a quality criterion.", "Option D — quantitative quality varies enormously."],
   "teaching_insight": "Students often default to quantitative-only without thinking it through. This question challenges that reflex.", "follow_up": "Write inclusion criteria for a review on 'patient experiences of AI in diagnosis.'"},
  {"number": 3, "session": "S04", "difficulty": "Advanced", "clo": "CLO 3", "concept": "Publication Bias",
   "question": "Publication bias in systematic reviews refers to:",
   "options": ["Journals favouring papers by famous institutions", "The tendency for journals to publish statistically significant positive findings more than null or negative results, distorting the evidence base", "Reviewers preferring quantitative papers", "Citing papers from your own country more often"],
   "correct": 1,
   "explanation": {"concise": "Publication bias inflates apparent evidence for an effect because null results are underrepresented in the published literature.", "detailed": "Studies that find no significant effect are much less likely to be submitted or accepted. Systematic reviews that include only published studies therefore see a biased sample — overrepresenting evidence for effects. Grey literature search and funnel plot analysis (in meta-analyses) are used to detect and account for publication bias.", "doctoral_relevance": "Systematic reviews must acknowledge potential publication bias. Failure to do so is a reviewer concern.", "instructor_emphasis": "Show a funnel plot from a published meta-analysis and explain asymmetry."},
   "wrong_reasons": ["Option A — institutional prestige bias is different from publication bias.", "Option C — methodological preference is reviewer bias, not publication bias.", "Option D — citation nationalism is a different concern."],
   "teaching_insight": "Publication bias explains why some systematic reviews reach more optimistic conclusions than the full evidence would support.", "follow_up": "How would you address potential publication bias in a systematic review on AI and employee creativity?"},
  {"number": 4, "session": "S04", "difficulty": "Intermediate", "clo": "CLO 3", "concept": "Quality Appraisal",
   "question": "Risk of bias assessment in systematic reviews is conducted to:",
   "options": ["Identify which studies support the researcher's hypothesis", "Evaluate methodological quality of included studies and flag limitations affecting confidence in findings", "Reduce included studies to a manageable number", "Determine which authors are most trustworthy"],
   "correct": 1,
   "explanation": {"concise": "Quality appraisal systematically evaluates how much confidence we can place in each study's findings.", "detailed": "Risk of bias tools (Cochrane RoB-2, Newcastle-Ottawa Scale, CASP) evaluate: randomisation quality, allocation concealment, blinding, attrition, selective reporting. Studies with high risk of bias produce less reliable findings. Reviews that pool high and low quality studies without distinction may mislead.", "doctoral_relevance": "PRISMA 2020 requires risk of bias assessment as a standard component. Reviewers check for it.", "instructor_emphasis": "Walk through one risk of bias tool (Newcastle-Ottawa Scale or CASP) for one study from the field."},
   "wrong_reasons": ["Option A — cherry-picking is exactly what bias assessment prevents.", "Option C — exclusion may follow quality assessment but is not its purpose.", "Option D — author trustworthiness is not a validity criterion."],
   "teaching_insight": "Students confuse high citation count with high quality. Frequently cited papers can have significant methodological limitations.", "follow_up": "Apply a three-criterion quality checklist to one paper in your research area."},
  {"number": 5, "session": "S04", "difficulty": "Doctoral Challenge", "clo": "CLO 3", "concept": "Narrative vs Meta-Analytic Synthesis",
   "question": "When is narrative synthesis MORE appropriate than meta-analysis?",
   "options": ["When pooling effect sizes statistically", "When studies are too heterogeneous in design, population, or outcome to justify statistical pooling", "When more than 50 studies are available", "When the research question is quantitative"],
   "correct": 1,
   "explanation": {"concise": "Narrative synthesis is appropriate when methodological or clinical heterogeneity makes statistical pooling invalid or misleading.", "detailed": "Meta-analysis is valid only when studies are sufficiently similar in design, population, intervention, and outcome. High I² (heterogeneity statistic) signals that studies are too diverse to pool meaningfully. Narrative synthesis instead summarises and interprets the pattern of findings without statistical combination.", "doctoral_relevance": "Choosing between synthesis methods must be justified methodologically, not made by default.", "instructor_emphasis": "Show a heterogeneity test (I²) from a published meta-analysis and explain what high heterogeneity implies."},
   "wrong_reasons": ["Option A — that is the rationale for meta-analysis, not narrative synthesis.", "Option C — number of studies does not determine the method.", "Option D — quantitative questions do not automatically require meta-analysis."],
   "teaching_insight": "Many students assume more data always means meta-analysis. Heterogeneity is the deciding criterion.", "follow_up": "Examine an I² statistic in a published meta-analysis in your field and interpret its implications."},
],
"reflection": """After this session, you should be able to:
- [ ] Explain what distinguishes a systematic review from a narrative review
- [ ] Draw a complete PRISMA flow diagram with correct labels and counts
- [ ] Write inclusion and exclusion criteria justified by a research question
- [ ] Describe what risk of bias assessment evaluates and name one tool
- [ ] Explain when narrative synthesis is preferred over meta-analysis

**What to produce:** Draft inclusion and exclusion criteria for a systematic review in your research area. Justify each criterion in one sentence.

**Assessment link:** The Annotated Bibliography assignment requires a documented search strategy consistent with systematic review standards."""
},

}  # end SESSIONS dict


# ═══════════════════════════════════════════════════════════════════════════════
# STUB DATA FOR SESSIONS 5–16 (complete content per session)
# ═══════════════════════════════════════════════════════════════════════════════

STUB_SESSIONS = {
"s05": {"code":"S05","title":"Research Questions & Hypotheses","clos":["CLO 2","CLO 5"],"number":5,"why":"Precision in framing questions and hypotheses determines the entire study design. Vague questions produce vague findings."},
"s06": {"code":"S06","title":"Theoretical Frameworks","clos":["CLO 4"],"number":6,"why":"Theory is not decoration — it is the explanatory engine of a study. Without it, findings cannot be interpreted or generalised."},
"s07": {"code":"S07","title":"Quantitative Methods with AI","clos":["CLO 5"],"number":7,"why":"AI is changing what quantitative research can do — and what biases it can introduce. Scholars must understand both."},
"s08": {"code":"S08","title":"Qualitative Methods with AI","clos":["CLO 5"],"number":8,"why":"AI tools are entering qualitative analysis — from transcription to coding. Rigour requires knowing what is gained and what is lost."},
"s09": {"code":"S09","title":"Mixed Methods & AI Integration","clos":["CLO 5"],"number":9,"why":"Mixed methods done well is more than two studies stapled together. Integration is the intellectual core."},
"s10": {"code":"S10","title":"AI for Data Collection","clos":["CLO 6"],"number":10,"why":"From AI-generated survey items to chatbot interviews, data collection is changing fast — with significant ethical implications."},
"s11": {"code":"S11","title":"AI-Assisted Analysis & Interpretation","clos":["CLO 6"],"number":11,"why":"Interpreting AI output is not the same as reading a statistical table. Critical evaluation of algorithmic findings is a new scholarly skill."},
"s12": {"code":"S12","title":"Academic Writing with AI","clos":["CLO 7"],"number":12,"why":"AI can accelerate writing, but the researcher's voice, argument, and accountability cannot be outsourced."},
"s13": {"code":"S13","title":"Citation, Plagiarism & Research Ethics","clos":["CLO 7","CLO 8"],"number":13,"why":"In the AI era, the boundaries of plagiarism, self-plagiarism, and fabrication require fresh examination."},
"s14": {"code":"S14","title":"Peer Review & Revision","clos":["CLO 7"],"number":14,"why":"Responding to peer review is one of the most important and least taught academic skills."},
"s15": {"code":"S15","title":"Dissemination & Publication Strategy","clos":["CLO 7","CLO 8"],"number":15,"why":"Getting research read matters as much as conducting it well. Strategic dissemination is a scholarly responsibility."},
"s16": {"code":"S16","title":"Capstone & the Future of AI Research","clos":["CLO 1","CLO 8"],"number":16,"why":"This session synthesises the course and asks: what does it mean to be a researcher in an AI-enabled world?"},
}

STUB_QUIZ_TEMPLATE = [
    {"number":i,"difficulty":d,"clo":"CLO 1","concept":"Core concept",
     "question":f"Sample question {i} — replace with session-specific content.",
     "options":["Option A","Option B","Option C","Option D"],"correct":1,
     "explanation":{"concise":"See quiz bank for full questions.","detailed":"Full questions available in the Quiz Bank section with complete explanations.","doctoral_relevance":"All questions have doctoral relevance noted in the Quiz Bank.","instructor_emphasis":"Use the Quiz Bank to access 5+ questions per session."},
     "wrong_reasons":["See Quiz Bank for full explanations of wrong options."]*3,
     "teaching_insight":"Full quiz questions for this session are in the Quiz Bank — filter by session code.",
     "follow_up":"Check the Quiz Bank for follow-up discussion questions."}
    for i,d in enumerate(["Beginner","Intermediate","Advanced","Doctoral Challenge","Intermediate"],1)
]


def render_full_session(key):
    """Render a fully authored session (s03, s04)."""
    data = SESSIONS[key]

    session_header(
        code=data["code"], title=data["title"],
        clos=data["clos"], why=data["why"]
    )
    teaching_flow(data["flow"])
    section_divider()

    # A. Theoretical Concepts
    st.markdown("## 📖 A. Theoretical Concepts")
    for cname, cbody in data["concepts"]:
        with st.expander(cname, expanded=False):
            concept_card(cname, cbody)

    section_divider()

    # B. Story
    st.markdown("## 📖 B. Tell Me the Research Story")
    if st.button("🎭 Tell Me the Research Story", key=f"{key}_story"):
        st.markdown(f'<div class="gold-card">{data["story"]}</div>', unsafe_allow_html=True)

    section_divider()

    # C. Visual placeholder (session-specific diagrams would be added here)
    st.markdown("## 📊 C. Visual Explanation")
    if key == "s03":
        render_s03_funnel()
    elif key == "s04":
        render_s04_prisma()

    section_divider()

    # D. Activity
    st.markdown("## 🏋️ D. Classroom Activity")
    render_activity(data["activity"], key=f"{key}_act")

    section_divider()

    # E. Case
    st.markdown("## 📋 E. Mini Case")
    render_case(data["case"], key=f"{key}_case")

    section_divider()

    # F. Quiz
    st.markdown("## 📝 F. Session Quiz")
    render_quiz_block(data["quiz"], key_prefix=key, title=f"{data['code']} — Five Questions")

    section_divider()

    # G. Reflection
    st.markdown("## ✅ G. Reflection & Output")
    st.markdown(data["reflection"])


def render_stub_session(key):
    """Render a stub session with core concepts and quiz bank pointer."""
    data = STUB_SESSIONS[key]
    session_number = data["number"]

    session_header(
        code=data["code"], title=data["title"],
        clos=data["clos"], why=data["why"]
    )

    st.info(f"📚 **Full session content for {data['code']} is available below.** Scroll through each section.")

    # Teaching flow
    teaching_flow([
        "Opening and framing",
        "Theoretical Concepts",
        "Research Story",
        "Visual Explanation",
        "Instructor Demonstration",
        "Classroom Activity",
        "Mini Case + Quiz + Reflection"
    ])
    section_divider()

    # Render session-specific content
    if key == "s05": render_s05_content()
    elif key == "s06": render_s06_content()
    elif key == "s07": render_s07_content()
    elif key == "s08": render_s08_content()
    elif key == "s09": render_s09_content()
    elif key == "s10": render_s10_content()
    elif key == "s11": render_s11_content()
    elif key == "s12": render_s12_content()
    elif key == "s13": render_s13_content()
    elif key == "s14": render_s14_content()
    elif key == "s15": render_s15_content()
    elif key == "s16": render_s16_content()

    section_divider()
    st.markdown("### 📝 Session Quiz")
    st.info("Navigate to **📚 Quiz Bank** in the sidebar, filter by this session code, for the full set of questions with reveal-based answers.")


def render_s03_funnel():
    st.markdown("### Literature Search Funnel")
    try:
        import plotly.graph_objects as go
        stages = ["All potential records<br>(Topic-level)", "Database search<br>(Keyword + Boolean)", "AI semantic search<br>(Elicit, Consensus)", "Citation chaining<br>(Forward + Backward)", "Grey literature<br>(Reports, preprints)", "Screened by title/abstract", "Full text assessed", "Final included studies"]
        sizes = [10000, 500, 200, 150, 80, 120, 60, 30]
        colors = ["#1a3a6e","#2a5298","#3a72c8","#4a8ad8","#c8a951","#d4b861","#1a7a4a","#1a9a5a"]
        fig = go.Figure(go.Funnel(y=stages, x=sizes, textinfo="value+percent initial",
                                   marker=dict(color=colors)))
        fig.update_layout(title="Literature Search Funnel — Narrowing to Included Studies",
                          title_font=dict(size=14, color="#1a3a6e"), height=450,
                          margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig, use_container_width=True)
    except ImportError:
        st.info("Install plotly for the interactive funnel diagram.")

    with st.expander("🔍 How to Interpret This Funnel"):
        st.markdown("""
**Reading the funnel:** Each stage narrows the universe of potential records to a manageable, relevant set.

**Why it looks like a funnel:** Most records are eliminated early (by scope, language, date). Full text assessment is more thorough but applied to fewer records.

**What each stage means:**
- Top: The conceptual universe of all potentially relevant work
- Database search: Systematic, documented, reproducible
- AI semantic search: Complementary — finds synonymous work databases miss
- Citation chaining: Finds influential work not captured by keyword search
- Grey literature: Reduces publication bias by including non-peer-reviewed work
- Screening: Applying inclusion/exclusion criteria systematically
- Full text: Detailed eligibility assessment
- Included: The evidence base for the review

**CLO connection:** CLO 3 — conducting systematic literature reviews with AI search tools.

**Instructor note:** Ask students to estimate how many papers they think exist on their topic before showing the funnel. The gap between expectation and reality is educational.
        """)


def render_s04_prisma():
    st.markdown("### PRISMA 2020 Flow Diagram Structure")

    import streamlit.components.v1 as components

    prisma_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'DM Sans', 'Segoe UI', sans-serif; background: #fff; padding: 16px; }
  .diagram {
    display: flex; gap: 16px; align-items: flex-start;
    max-width: 860px; margin: 0 auto;
  }
  /* Stage labels column */
  .stages {
    display: flex; flex-direction: column;
    gap: 0; width: 80px; flex-shrink: 0; padding-top: 4px;
  }
  .stage-label {
    font-size: 9px; font-weight: 700; text-transform: uppercase;
    letter-spacing: .08em; color: #9aabcc;
    display: flex; align-items: center; justify-content: flex-end;
    padding-right: 8px; text-align: right; line-height: 1.3;
  }
  /* Main flow column */
  .main-flow {
    display: flex; flex-direction: column; align-items: center;
    flex: 1; gap: 0;
  }
  /* Box styles */
  .box {
    width: 100%; border-radius: 9px; padding: 10px 14px;
    text-align: center; position: relative;
  }
  .box-main {
    background: #eef3fb; border: 2px solid #1a3a6e;
  }
  .box-included {
    background: #edfaf3; border: 2px solid #0d6e3f;
  }
  .box-label {
    font-size: 12px; font-weight: 600; color: #1a3a6e; margin-bottom: 2px;
  }
  .box-sub {
    font-size: 10px; color: #4a6090; margin-bottom: 3px;
  }
  .box-n {
    font-size: 16px; font-weight: 800; color: #0f2147;
  }
  .box-included .box-label { color: #0d6e3f; }
  .box-included .box-n { color: #0d6e3f; font-size: 20px; }
  .box-included .box-sub { color: #2d8a5a; }
  /* Arrows between boxes */
  .arrow-down {
    width: 2px; height: 24px; background: #1a3a6e;
    position: relative; margin: 0 auto;
  }
  .arrow-down::after {
    content: '';
    position: absolute; bottom: -7px; left: 50%;
    transform: translateX(-50%);
    border-left: 7px solid transparent;
    border-right: 7px solid transparent;
    border-top: 8px solid #1a3a6e;
  }
  /* Row with main box + exclusion box side by side */
  .row { display: flex; align-items: center; gap: 0; width: 100%; }
  .row-main { flex: 1; }
  /* Exclusion connector */
  .excl-connector {
    display: flex; align-items: center; flex-shrink: 0;
    width: 48px;
  }
  .excl-line {
    height: 2px; flex: 1;
    border-top: 2px dashed #c8a951;
  }
  .excl-arrow {
    width: 0; height: 0;
    border-top: 6px solid transparent;
    border-bottom: 6px solid transparent;
    border-left: 8px solid #c8a951;
  }
  /* Exclusion box */
  .excl-col { width: 190px; flex-shrink: 0; }
  .box-excl {
    background: #fff8e6; border: 2px solid #c8a951;
    border-radius: 9px; padding: 9px 11px; text-align: center;
  }
  .excl-label {
    font-size: 10px; font-weight: 700; color: #8a5a00; margin-bottom: 2px;
  }
  .excl-n { font-size: 16px; font-weight: 800; color: #8a5a00; }
  .excl-detail { font-size: 9px; color: #a06820; margin-top: 3px; line-height: 1.5; }
  /* Spacer boxes for rows without exclusions */
  .excl-spacer { width: 238px; flex-shrink: 0; } /* 48 + 190 */
  /* Legend */
  .legend {
    display: flex; gap: 20px; justify-content: center;
    margin-top: 18px; padding-top: 14px;
    border-top: 1px solid #e8eef8; flex-wrap: wrap;
  }
  .legend-item { display: flex; align-items: center; gap: 6px; font-size: 10px; color: #666; }
  .legend-swatch {
    width: 14px; height: 14px; border-radius: 4px; flex-shrink: 0;
  }
  /* Stage height matching */
  .sh-id   { height: 68px; }
  .sh-dup  { height: 52px; }
  .sh-scr  { height: 52px; }
  .sh-elig { height: 52px; }
  .sh-inc  { height: 72px; }
  .sa-id   { height: 68px; display: flex; align-items: center; }
  .sa-dup  { height: 76px; display: flex; align-items: center; }
  .sa-scr  { height: 76px; display: flex; align-items: center; }
  .sa-elig { height: 76px; display: flex; align-items: center; }
  .sa-inc  { height: 72px; display: flex; align-items: center; }
</style>
</head>
<body>

<div class="diagram">

  <!-- Stage labels -->
  <div class="stages">
    <div class="stage-label sa-id">Identification</div>
    <div class="stage-label sa-dup">Deduplication</div>
    <div class="stage-label sa-scr">Screening</div>
    <div class="stage-label sa-elig">Eligibility</div>
    <div class="stage-label sa-inc">Included</div>
  </div>

  <!-- Main flow -->
  <div class="main-flow">

    <!-- Row 1: Identification -->
    <div class="row">
      <div class="row-main">
        <div class="box box-main sh-id">
          <div class="box-label">Records identified</div>
          <div class="box-sub">Scopus + PubMed + Grey literature</div>
          <div class="box-n">n = 500</div>
        </div>
      </div>
      <div class="excl-spacer"></div>
    </div>

    <div class="arrow-down"></div>

    <!-- Row 2: Deduplication -->
    <div class="row">
      <div class="row-main">
        <div class="box box-main sh-dup">
          <div class="box-label">After duplicates removed</div>
          <div class="box-n">n = 420</div>
        </div>
      </div>
      <div class="excl-spacer"></div>
    </div>

    <div class="arrow-down"></div>

    <!-- Row 3: Screening + Exclusion A -->
    <div class="row">
      <div class="row-main">
        <div class="box box-main sh-scr">
          <div class="box-label">Records screened</div>
          <div class="box-sub">Title + abstract review</div>
          <div class="box-n">n = 420</div>
        </div>
      </div>
      <div class="excl-connector">
        <div class="excl-line"></div>
        <div class="excl-arrow"></div>
      </div>
      <div class="excl-col">
        <div class="box-excl">
          <div class="excl-label">Excluded after screening</div>
          <div class="excl-n">n = 280</div>
          <div class="excl-detail">Irrelevant topic<br>Wrong population<br>Wrong study design</div>
        </div>
      </div>
    </div>

    <div class="arrow-down"></div>

    <!-- Row 4: Eligibility + Exclusion B -->
    <div class="row">
      <div class="row-main">
        <div class="box box-main sh-elig">
          <div class="box-label">Full texts assessed</div>
          <div class="box-sub">Eligibility review</div>
          <div class="box-n">n = 140</div>
        </div>
      </div>
      <div class="excl-connector">
        <div class="excl-line"></div>
        <div class="excl-arrow"></div>
      </div>
      <div class="excl-col">
        <div class="box-excl">
          <div class="excl-label">Full texts excluded</div>
          <div class="excl-n">n = 85</div>
          <div class="excl-detail">Wrong outcome: 40<br>Wrong population: 25<br>Poor quality: 20</div>
        </div>
      </div>
    </div>

    <div class="arrow-down"></div>

    <!-- Row 5: Included -->
    <div class="row">
      <div class="row-main">
        <div class="box box-included sh-inc">
          <div class="box-label">✓ Studies included in review</div>
          <div class="box-n">n = 55</div>
          <div class="box-sub">Final evidence base</div>
        </div>
      </div>
      <div class="excl-spacer"></div>
    </div>

  </div><!-- /main-flow -->
</div><!-- /diagram -->

<!-- Legend -->
<div class="legend">
  <div class="legend-item">
    <div class="legend-swatch" style="background:#eef3fb;border:2px solid #1a3a6e"></div>
    Main screening flow
  </div>
  <div class="legend-item">
    <div class="legend-swatch" style="background:#fff8e6;border:2px solid #c8a951"></div>
    Exclusions (with reasons)
  </div>
  <div class="legend-item">
    <div class="legend-swatch" style="background:#edfaf3;border:2px solid #0d6e3f"></div>
    Final included studies
  </div>
</div>

</body>
</html>
"""
    components.html(prisma_html, height=520, scrolling=False)

    with st.expander("🔍 How to Interpret the PRISMA Diagram"):
        st.markdown("""
**Each box represents a decision stage with a documented count.**

**The left column** shows the narrowing funnel: identified → deduplicated → screened → full text assessed → included.

**The right column** shows what was excluded and WHY. Exclusion reasons are as important as the counts — they tell reviewers how criteria were applied.

**What reviewers check:**
- Do the numbers add up correctly?
- Are exclusion reasons specific and consistent?
- Does the included count match what is reported in the results?

**PRISMA is not optional:** Most systematic review journals require this diagram. Many reject papers without it at desk review.

**Instructor teaching note:** Ask students to regenerate this diagram for their own hypothetical review, starting with a plausible number of initial records.
        """)


# ── Session 05: Research Questions & Hypotheses ──────────────────────────────
def render_s05_content():
    st.markdown("## 📖 A. Theoretical Concepts")

    with st.expander("1. Research Questions vs Hypotheses"):
        concept_card("Research Question", "Open-ended inquiry: How, What, To what extent, Why. Used in exploratory, explanatory, and descriptive studies. Example: 'How does AI-assisted scheduling affect nurse autonomy?'")
        concept_card("Hypothesis", "Directional, testable prediction derived from theory. Example: 'AI-assisted scheduling reduces perceived autonomy among nurses compared to manual scheduling.' Used in confirmatory, theory-testing studies.")
        concept_card("Null Hypothesis (H₀)", "The 'no effect' baseline: 'There is no difference in perceived autonomy between AI-scheduled and manually scheduled nurses.' Statistical tests evaluate whether data is inconsistent with H₀.")
        warn_box("Common error: writing a hypothesis for a qualitative study, or a research question where a testable prediction is required.")

    with st.expander("2. The PICO Framework for Health Research"):
        st.markdown("""
**P** — Population: Who? (e.g., emergency department nurses in tertiary hospitals)
**I** — Intervention: What? (e.g., AI triage algorithm)
**C** — Comparison: Compared to what? (e.g., conventional nurse-led triage)
**O** — Outcome: What is measured? (e.g., patient waiting time, diagnostic accuracy)

**Example PICO question:** In emergency department nurses (P), does AI-assisted triage (I) compared to nurse-led triage (C) reduce patient waiting times (O)?

**Why C matters:** Without a comparison, there is no counterfactual — you cannot determine whether AI made a difference.
        """)

    with st.expander("3. Scope and Operationalisation"):
        concept_card("Scope", "The boundaries of the study: which population, which context, which time period, which level of analysis. A well-scoped question is answerable with specific methods in a bounded time.")
        concept_card("Operationalisation", "Translating abstract constructs into concrete, measurable indicators. 'Employee engagement' → UWES scale items. 'AI readiness' → validated instrument measuring capability, motivation, and infrastructure.")
        st.markdown("**Weak:** 'Does AI affect employees?'")
        st.markdown("**Strong:** 'Does AI-assisted performance feedback (measured by manager AI system usage frequency) improve employee goal clarity (measured by SMART goal adherence rate) among mid-level managers in Indian IT firms over 12 weeks?'")

    with st.expander("4. AI-Assisted Research Question Refinement"):
        concept_card("Using AI to Test Question Precision", "Enter your research question into Elicit or Consensus. If the AI cannot return relevant papers, your question may be too narrow, too broad, or using terminology different from the literature. Use the results to calibrate.")
        warn_box("AI-refined questions are starting points. The final question must reflect your theoretical and contextual judgements, not just what the AI found.")

    section_divider()
    st.markdown("## 📖 B. Tell Me the Research Story")
    if st.button("🎭 Research Story — S05", key="s05_story"):
        st.markdown("""<div class="gold-card">
<strong>The Question That Changed Everything</strong><br><br>
Frederick Taylor, in the early 20th century, walked into a factory and asked a question no one had asked seriously before: 'How long does this task actually take?' Not an average, not an estimate, but a measured, timed observation. That question — precise, bounded, operationalised — gave rise to scientific management.

Fifty years later, Herbert Simon walked into a boardroom and asked: 'How do managers actually make decisions?' Not how they should, but how they do. That question — changed from normative to descriptive — opened behavioural decision theory.

Every significant research tradition begins with a question that is precisely different from what anyone asked before. Not completely different — those questions come out of existing conversations. But precisely different: a boundary condition shifted, a population changed, a construct redefined.

The art of the research question is the art of precision. Not 'does AI affect organisations?' but 'does AI-assisted performance feedback change goal-setting behaviour among mid-level managers in Indian IT firms in a post-pandemic hybrid work context?' Every word carries weight. Every word is a choice.

The question you write determines the study you can do, the theory you will engage, the findings you can claim, and the contribution you can make. Spend more time on the question than on anything else.

<em>Class activity: write your current research question on paper. Now count the words doing actual analytical work. How many are there?</em>
</div>""", unsafe_allow_html=True)

    section_divider()
    st.markdown("## 📊 C. Visual: Research Question Refinement Path")
    st.markdown("""
| Stage | Example | Problem |
|---|---|---|
| Topic | AI in organisations | Not a question |
| Broad question | Does AI affect employees? | Too vague — what AI? which employees? what effect? |
| Narrowed question | Does AI performance management affect engagement? | Missing context and population |
| Scoped question | Does AI performance feedback affect engagement in hybrid workers in Indian IT? | Approaching workable scope |
| Operationalised question | Does AI performance feedback frequency (>3x/week) predict UWES engagement scores in hybrid IT workers in Bengaluru firms after 12 weeks? | Doctoral-level precision |
    """)

    section_divider()
    st.markdown("## 🏋️ D. Activity — Refine Your Research Question")
    act = {
        "title": "Research Question Ladder",
        "task": "Start with your broadest possible research interest (one topic word). Apply the refinement ladder: add phenomenon, then outcome, then population, then context, then time dimension. Write the question at each stage. Evaluate which level is right for your study.",
        "student_role": "Research question architect",
        "expected_output": "Five increasingly specific versions of your research question, with one sentence explaining why you chose one level over the others.",
        "time_minutes": 20,
        "sample_answer": "Level 1: AI. Level 2: Does AI affect healthcare? Level 3: Does AI affect nurse decision-making? Level 4: Does AI clinical decision support affect nursing autonomy in ICU settings? Level 5: Does AI clinical decision support tool use frequency predict perceived nursing autonomy (measured by NAS scale) in ICU nurses in Mumbai public hospitals over 6 months? I would work at Level 4–5 for a doctoral study, with Level 5 as my operational research question.",
        "weak_answer": "My research question is about AI and healthcare. I made it more specific.",
        "improved_answer": "Starting point: 'AI in healthcare.' Refined through five stages to: 'Does the implementation of AI-assisted triage systems predict patient waiting time reduction in emergency departments of tier-2 Indian government hospitals?' Selected this level because it is bounded (triage systems, emergency departments, tier-2 govt hospitals), outcome-specified (waiting time), and answerable with a quasi-experimental or longitudinal design.",
        "debrief": "Peer review: swap questions with a classmate. Can they tell what the study is about from the question alone? Can they identify the method the question implies?",
        "grading_hints": "Award marks for: five distinct levels of specificity, clear progression, justified choice, and methodological awareness.",
        "common_mistakes": "Students jump to Level 5 without showing the progression, missing the skill of iterative refinement.",
        "scholarly_link": "This exercise feeds directly into the Research Questions section of the Research Proposal."
    }
    render_activity(act, key="s05_act")

    section_divider()
    st.markdown("## 📋 E. Mini Case — The Hypothesis That Could Not Be Tested")
    case = {
        "title": "The Untestable Hypothesis",
        "scenario": "Deepa writes: 'H1: AI is good for organisations.' Her supervisor returns it with 'This is not a hypothesis — it is an opinion.' Deepa is confused: she believes the hypothesis to be true.",
        "question": "What is wrong with Deepa's hypothesis, and how should it be rewritten?",
        "weak_response": "It should be more specific about what AI does.",
        "strong_response": "Deepa's statement fails three hypothesis criteria: (a) it is not directional — 'good' is not a measurable direction; (b) it is not operationalised — 'AI' and 'organisations' are undefined; (c) it cannot be falsified — what evidence would prove it wrong? A testable hypothesis would be: 'AI-assisted performance management (measured by algorithm-generated feedback frequency) positively predicts employee task performance (measured by OKR achievement rate) in mid-level managers in Indian technology firms.' This specifies: the intervention, the mechanism, the outcome, the direction, and the population.",
        "issue_diagnosis": "Hypothesis is normative and non-operationalised. It is an opinion, not a scientific prediction.",
        "theory": "Popper's falsifiability criterion: a scientific hypothesis must be capable of being proven wrong by evidence.",
        "research_gap": "N/A — this is a hypothesis formulation error.",
        "research_question": "Does AI-assisted performance feedback increase task performance in mid-level IT managers?",
        "scholarly_framing": "A hypothesis is a precise, theory-derived, falsifiable prediction about a specific relationship between operationalised constructs.",
        "instructor_note": "Use Deepa's hypothesis to practice hypothesis rewriting as a class exercise."
    }
    render_case(case, key="s05_case")

    section_divider()
    st.markdown("## ✅ F. Reflection & Output")
    st.markdown("""
**After this session:**
- [ ] Distinguish research questions from hypotheses and null hypotheses
- [ ] Apply the PICO framework to a health management research question
- [ ] Operationalise two constructs from your research area
- [ ] Write a question at doctoral-level specificity

**Assessment link:** Research questions and hypotheses are the core of Section 2 of the Research Proposal.
    """)


# ── Session 06: Theoretical Frameworks ───────────────────────────────────────
def render_s06_content():
    st.markdown("## 📖 A. Theoretical Concepts")

    with st.expander("1. What is a Theoretical Framework?"):
        concept_card("Function", "A theoretical framework provides the explanatory mechanism: WHY are X and Y expected to be related? It is not a literature review section — it is the logical engine of the study.")
        concept_card("Grand vs Middle-Range Theory", "Grand theories (systems theory, structuration) explain broadly but cannot generate specific testable predictions. Middle-range theories (Social Exchange Theory, TAM, RBV) specify mechanisms in bounded domains — far more useful for empirical study.")
        st.markdown("**Weak use of theory:** 'Social Exchange Theory has been used in management research (citations).'")
        st.markdown("**Strong use of theory:** 'Social Exchange Theory predicts that when AI systems provide consistent, fair performance feedback (benefit), employees will reciprocate with increased organisational citizenship behaviour (reciprocity norm). This mechanism explains our prediction that AI feedback frequency positively relates to OCB.'")

    with st.expander("2. Theory-Method-Context Triangle"):
        concept_card("Theory → Method → Context", "Theory determines what relationships to test. Method determines how to test them. Context determines where the test is valid. All three must align. A mismatch (e.g., constructivist theory with positivist methods) is an epistemological inconsistency.")
        gold_card("Alignment Check", "Ask: Does my theory specify a relationship? Does my method allow me to test that relationship? Does my context justify applying this theory here?")

    with st.expander("3. Applying a Theory to a New Context"):
        st.markdown("""
When using a theory developed in one context for another, you must argue:
1. What are the theory's core constructs and mechanisms?
2. Are these constructs present in the new context?
3. Are the mechanisms expected to operate similarly in the new context?
4. Are there contextual features that modify or constrain the theory's predictions?

**Example:** Applying Technology Acceptance Model (developed in Western corporate settings) to AI adoption in Indian public hospitals requires arguing: (a) perceived usefulness and ease of use are relevant constructs in this context, (b) the adoption decision process is similar (though potentially modified by hierarchical authority and resource constraints), (c) the TAM prediction may be moderated by power distance culture and institutional constraints.
        """)

    with st.expander("4. AI for Theory Discovery"):
        concept_card("Connected Papers for Theory Mapping", "Enter a foundational theory paper (e.g., Blau 1964 on Social Exchange) into Connected Papers. The resulting graph shows how the theory has been applied, extended, and contested across fields.")
        concept_card("Elicit for Theory Evaluation", "Search 'Does Social Exchange Theory explain AI adoption' in Elicit to see how other researchers have applied and evaluated the theory in your area.")
        warn_box("AI tools surface how others have used a theory. They cannot tell you whether the theory applies to your specific context — that is your theoretical contribution.")

    section_divider()
    st.markdown("## 📖 B. Tell Me the Research Story")
    if st.button("🎭 Research Story — S06", key="s06_story"):
        st.markdown("""<div class="gold-card">
<strong>The Flashlight and the Room</strong><br><br>
Imagine you walk into a completely dark room. You do not know what is in it. You could fumble around with your hands — eventually you would find something, but you would miss most of the room and might trip over what is in the centre.

Now you have a flashlight. The flashlight does not change the room. The same objects are in the same positions. But the flashlight lets you see, systematically, what is there — provided you point it in the right direction.

Theory is the flashlight. It does not change the phenomenon you are studying. Organisations behave the same way whether or not you apply Social Exchange Theory to them. But the theory tells you where to look, what to expect, and how to interpret what you find.

Here is the catch: the flashlight only illuminates what it points at. A researcher using only Resource-Based View will see resources, capabilities, and competitive advantage everywhere — and will miss power dynamics, identity, and emotion. A researcher using only Institutional Theory will see norms and legitimacy — and will miss individual agency and strategic choice.

The choice of theory is not neutral. It is a decision about what matters, what is visible, and what gets left in the dark. Doctoral researchers must choose deliberately — and acknowledge what their chosen flashlight does not illuminate.

<em>Classroom prompt: Point your theoretical flashlight at your research area. What does it illuminate? What does it leave in the dark?</em>
</div>""", unsafe_allow_html=True)

    section_divider()
    st.markdown("## 📊 C. Theory Comparison Table")
    st.markdown("""
| Theory | Origin | Core Mechanism | Best For | Limitation |
|---|---|---|---|---|
| Social Exchange Theory | Blau (1964) | Reciprocity of benefits | Trust, commitment, citizenship behaviour | Assumes rational calculation of exchanges |
| Technology Acceptance Model | Davis (1989) | Perceived usefulness + ease → adoption | Technology adoption | Ignores social pressure, culture |
| Institutional Theory | DiMaggio & Powell (1983) | Mimetic, coercive, normative isomorphism | Organisational change, policy adoption | Limited individual agency |
| Resource-Based View | Barney (1991) | Rare, valuable, inimitable resources → advantage | Firm performance, strategy | Static; difficult to operationalise |
| Conservation of Resources | Hobfoll (1989) | Resource loss threat drives stress | Burnout, wellbeing, stress | Primarily individual-level |
| Signalling Theory | Spence (1973) | Observable signals reduce information asymmetry | Hiring, credentialing, AI transparency | Assumes signal interpretability |
    """)

    section_divider()
    st.markdown("## 🏋️ D. Activity — Justify Your Theory")
    act = {
        "title": "Theory Application Argument",
        "task": "Choose one theory from the table above or from your own reading. Apply it to your research topic. Write three paragraphs: (1) Explain the theory's core mechanism. (2) Map its constructs to your study's variables. (3) Argue why it applies in your specific context.",
        "student_role": "Theoretical analyst",
        "expected_output": "Three structured paragraphs demonstrating theory application and contextual justification.",
        "time_minutes": 25,
        "sample_answer": "Social Exchange Theory (Blau, 1964) proposes that relationships are governed by reciprocity norms: when one party provides a benefit, the other feels obligated to reciprocate. In the context of AI-assisted performance management, the theory predicts that employees who receive consistent, fair AI feedback (benefit from the organisation) will reciprocate with increased in-role performance and citizenship behaviour. In Indian IT firms — which typically feature high power distance and collectivist norms — the reciprocity dynamic may operate through team-level rather than individual-level exchange, which represents an important contextual modification of the original Western theory.",
        "weak_answer": "Social Exchange Theory is relevant to my research. Many papers use it in management research.",
        "improved_answer": "SET (Blau, 1964) specifies that reciprocal exchange of benefits creates trust and obligation. I apply this to AI performance management: AI feedback = organisational benefit; increased employee performance = reciprocation. In Indian hybrid work contexts, this mechanism may be moderated by perceived AI fairness — consistent with Cropanzano & Mitchell's (2005) extension of SET to organisational justice.",
        "debrief": "Peer review: read a classmate's three paragraphs. Can you identify: (1) the mechanism, (2) the variable mapping, (3) the contextual justification? What is missing?",
        "grading_hints": "Award marks for: mechanism clarity, variable mapping, contextual argument, and citation of theory source.",
        "common_mistakes": "Students describe the theory without applying it — or apply it without arguing for contextual fit.",
        "scholarly_link": "This three-paragraph structure is the core of the Theoretical Framework section in the Research Proposal."
    }
    render_activity(act, key="s06_act")

    section_divider()
    st.markdown("## ✅ E. Reflection & Output")
    st.markdown("""
**After this session:**
- [ ] Explain the difference between a theoretical framework and a literature review
- [ ] Distinguish grand theory from middle-range theory
- [ ] Map a theory's constructs to study variables with explicit reasoning
- [ ] Argue for a theory's applicability in a specific context

**Assessment link:** Theoretical Framework is Section 3 of the Research Proposal.""")


# ── Session 07: Quantitative Methods with AI ─────────────────────────────────
def render_s07_content():
    st.markdown("## 📖 A. Theoretical Concepts")

    with st.expander("1. Quantitative Research Design Types"):
        concept_card("Cross-Sectional Survey", "Data collected at one time point. Describes relationships but cannot establish temporal precedence. Most common in management research. Vulnerable to common method bias.")
        concept_card("Longitudinal Panel Design", "Data collected at multiple time points from the same participants. Establishes temporal precedence. Reduces common method bias. More expensive.")
        concept_card("Quasi-Experimental", "Intervention with pre/post measurement and a comparison group. Tests causal claims without full randomisation. Appropriate for organisational interventions.")
        concept_card("Experimental (Lab/Field)", "Random assignment to conditions. Strongest causal inference. Rare in management research due to ethical and practical constraints.")

    with st.expander("2. Measurement Validity and Reliability"):
        st.markdown("""
**Content validity:** Items cover the full domain of the construct (assessed by expert panel)
**Construct validity:** The measure captures the intended construct, not something else
- Convergent validity: items from the same construct correlate strongly
- Discriminant validity: items from different constructs do NOT correlate strongly
**Reliability:** Internal consistency — Cronbach's alpha ≥ 0.70 is the conventional threshold
**EFA → CFA sequence:** First explore structure (Exploratory Factor Analysis), then confirm it (Confirmatory Factor Analysis) on a separate sample.
        """)

    with st.expander("3. Common Method Bias (CMB)"):
        concept_card("What is CMB?", "When both predictor and outcome are measured from the same source in the same instrument at the same time, correlations may be artificially inflated by shared measurement context (mood, social desirability, consistency motive).")
        concept_card("Diagnosis", "Harman's single-factor test (common but limited). More robust: Unmeasured Latent Method Construct (ULMC) in SEM. Variance Inflation Factor in regression.")
        concept_card("Prevention", "Time-lagged design (IV and DV measured at different time points). Multiple informants (manager rates performance; employee rates wellbeing). Procedural separation (physical or temporal distance between scale sections).")

    with st.expander("4. AI in Quantitative Research"):
        concept_card("AI-Assisted Scale Development", "AI generates candidate items rapidly. Still requires: expert content validation (CVR/CVI), pilot testing, EFA, CFA. AI speed ≠ AI validity.")
        concept_card("AI Statistical Interpretation", "Tools like Julius AI can narrate SPSS/R output. Researchers must still understand what the statistics mean and whether the interpretations are valid.")
        concept_card("Machine Learning vs SEM", "ML optimises prediction; SEM tests theoretical relationships. These are different goals. Using ML to 'test a theory' misunderstands both ML and theory testing.")

    section_divider()
    st.markdown("## 📖 B. Tell Me the Research Story")
    if st.button("🎭 Research Story — S07", key="s07_story"):
        st.markdown("""<div class="gold-card">
<strong>Numbers That Lie</strong><br><br>
In 2011, a paper was published in Science claiming that people in power feel physically taller. The study was real. The statistics were correct. The p-values were below 0.05. And the finding was, most likely, an artefact of flexible methodology — running multiple analyses until something significant appeared, then reporting only that analysis.

This is not fraud. This is called p-hacking, or researcher degrees of freedom. It is entirely possible to produce statistically significant results from random noise if you analyse the data long enough and in enough ways.

AI tools make this easier, not harder. With AI-assisted analysis, a researcher can run dozens of models, test dozens of moderators, and generate hundreds of outputs in the time it used to take to set up SPSS. The probability of finding something significant by chance goes up, not down, as analytical power increases.

The antidote is pre-registration: committing to your hypotheses, variables, and analytical approach before seeing the data. It is the quantitative equivalent of showing your work before the exam. AI can help you analyse faster. Pre-registration ensures that speed does not become a license for fishing.

Numbers can lie when the questions that produced them are not honest. Statistical rigour begins before the data is collected.

<em>Class prompt: What is the difference between exploring data and testing a hypothesis? Why does this distinction matter?</em>
</div>""", unsafe_allow_html=True)

    section_divider()
    st.markdown("## ✅ C. Reflection & Output")
    st.markdown("""
**After this session:**
- [ ] Match a quantitative design to a given research question
- [ ] Explain internal vs external vs construct validity
- [ ] Describe common method bias and two strategies to prevent it
- [ ] Distinguish exploratory from confirmatory factor analysis
- [ ] Explain why ML optimises prediction while SEM tests relationships

**Assessment link:** Quantitative methods inform the Methodology section of the Research Proposal.""")


# ── Session 08: Qualitative Methods with AI ──────────────────────────────────
def render_s08_content():
    st.markdown("## 📖 A. Theoretical Concepts")

    with st.expander("1. Qualitative Research Paradigm"):
        concept_card("Epistemological Foundation", "Qualitative research sits within an interpretivist or constructivist paradigm: reality is socially constructed, meanings are context-dependent, and the researcher's perspective shapes the research.")
        concept_card("When to Use Qualitative Methods", "When the phenomenon is poorly understood, when context is central to meaning, when the research question asks 'how' or 'why' rather than 'how much', when participants' own interpretive frames matter.")
        concept_card("Rigour Criteria", "Lincoln & Guba's (1985) criteria replace internal/external validity: Credibility (analogue to internal validity), Transferability (analogue to external validity), Dependability (analogue to reliability), Confirmability (analogue to objectivity).")

    with st.expander("2. Thematic Analysis — Braun & Clarke"):
        st.markdown("""
**Six phases (Braun & Clarke, 2006):**
1. Familiarisation with data (reading, notes)
2. Generating initial codes (data-level labels)
3. Searching for themes (patterns across codes)
4. Reviewing themes (does each theme work?)
5. Defining and naming themes (what is the theme about?)
6. Writing up (analytical narrative)

**Code vs Theme:**
- Code = data label ('mentioned workload concern')
- Theme = interpretive claim ('Workload concerns are amplified by algorithmic unpredictability')

**Reflexive TA (Braun & Clarke 2019 update):** Themes are not found in data — they are constructed by the researcher through an interpretive process. Researcher reflexivity is therefore essential, not optional.
        """)

    with st.expander("3. AI in Qualitative Analysis"):
        concept_card("AI Transcription", "Tools like Otter.ai, Whisper (OpenAI) produce rapid transcripts. Quality varies — technical jargon and accents reduce accuracy. Always check against recording before analysis.")
        concept_card("AI-Assisted Coding", "NLP tools (Atlas.ti AI, NVivo AI coding) can suggest initial codes. These are pattern-matched labels, not interpretive codes. Researcher must review, refine, and reinterpret every code.")
        concept_card("AI Theme Generation", "LLMs can generate 'themes' from text, but these are statistical clusters, not interpretive constructs. A theme generated by AI has not been through the iterative, interpretive process that gives themes analytical validity.")
        warn_box("AI-generated codes and themes require human interpretive validation before they can be used in analysis. Presenting AI-generated themes as analytical findings is a methodological misrepresentation.")

    with st.expander("4. Purposive Sampling and Saturation"):
        concept_card("Purposive Sampling", "Select participants based on specific characteristics relevant to the phenomenon. Not random — deliberately targeted. In a study of AI resistance in hospitals: nurses, IT leads, administrators, senior doctors each add a different perspective.")
        concept_card("Theoretical Saturation", "Continue collecting data until new data no longer generates new conceptual insights. This is a theoretical criterion, not a number. Typical qualitative studies: 12–30 participants, depending on topic complexity and data richness.")

    section_divider()
    st.markdown("## 📖 B. Tell Me the Research Story")
    if st.button("🎭 Research Story — S08", key="s08_story"):
        st.markdown("""<div class="gold-card">
<strong>What the Numbers Could Not Say</strong><br><br>
A large hospital system implemented an AI clinical decision support tool. Survey data showed 72% of nurses reported 'satisfaction' with the system. Management declared it a success.

A qualitative researcher then interviewed 20 nurses. What emerged was more complicated. Yes, nurses were 'satisfied' in the sense of not actively resisting the system. But underneath that satisfaction: anxiety about professional deskilling ('I used to know what I was seeing — now I wait for the machine to confirm it'), uncertainty about responsibility ('If the AI is wrong and I followed it, who is accountable?'), and a quiet solidarity around workarounds ('We all know which AI alerts to ignore').

None of this was visible in the 72% satisfaction figure. It was not that the survey was wrong — it asked what it asked and found what it found. But the meaning behind the numbers was a different story.

Qualitative research gives voice to the complexity that quantitative measures necessarily compress. It does not tell you what percentage of nurses feel a certain way — it tells you what feeling that certain way actually means to them. For research on AI in healthcare, where implementation success depends on adoption, adaptation, and trust, that meaning is not optional background detail. It is the finding.

<em>Class prompt: Think of a quantitative finding in your field. What qualitative question would you need to ask to understand why it looks the way it does?</em>
</div>""", unsafe_allow_html=True)

    section_divider()
    st.markdown("## ✅ C. Reflection & Output")
    st.markdown("""
**After this session:**
- [ ] Explain three qualitative rigour criteria (Lincoln & Guba)
- [ ] Describe the six phases of Braun & Clarke's thematic analysis
- [ ] Distinguish code from theme with an example
- [ ] Evaluate the role and limits of AI in qualitative coding
- [ ] Design a purposive sampling strategy for a qualitative study

**Assessment link:** Qualitative methods inform the Methodology section of the Research Proposal.""")


# ── Sessions 09–16: Complete teaching content ────────────────────────────────
def render_s09_content():
    st.markdown("## 📖 A. Theoretical Concepts")
    with st.expander("1. Mixed Methods Logic"):
        concept_card("Why Mix?", "Use mixed methods when one paradigm alone cannot answer the research question. The combination is justified by the question, not by desire for comprehensiveness.")
        concept_card("Three Major Designs", "Convergent parallel: both strands simultaneously, integrate at interpretation. Explanatory sequential: quant → qual (qual explains quant). Exploratory sequential: qual → quant (qual informs quant instrument).")
        concept_card("Integration", "True integration happens at the level of interpretation (meta-inference), not just data collection. A joint display places quantitative and qualitative findings side by side to enable comparison.")
    with st.expander("2. Triangulation — What It Actually Means"):
        st.markdown("""
Triangulation (Denzin, 1978): using multiple methods, sources, or investigators to cross-validate.
- **Data triangulation:** Multiple sources (interviews + observations + documents)
- **Investigator triangulation:** Multiple researchers code/analyse
- **Methodological triangulation:** Quantitative + qualitative on the same phenomenon
- **Theory triangulation:** Multiple theoretical lenses

Triangulation does not guarantee agreement — divergence between strands is itself a finding that reveals complexity.
        """)
    with st.expander("3. Joint Display"):
        concept_card("Definition", "A table or figure placing quantitative and qualitative data side by side to enable meta-inference.")
        st.markdown("**Example:** Survey shows 65% of managers resist AI adoption. Interview data shows resistance stems from accountability fears ('if AI decides and it's wrong, I'm blamed'). Joint display: resistance percentage alongside representative quote, enabling the inference that resistance is structural (accountability architecture), not attitudinal.")
    st.markdown("---")
    st.markdown("## 📖 B. Research Story")
    if st.button("🎭 Research Story — S09", key="s09_story"):
        st.markdown("""<div class="gold-card"><strong>Two Blind Researchers and the Elephant</strong><br><br>The parable of blind scholars and the elephant is well-worn but underused in methodology teaching. The researcher who measures only the trunk describes a flexible cylinder. The researcher who only interviews describes a creature with a trunk 'like a snake' and legs 'like tree trunks.' Neither is wrong. Both are incomplete. Mixed methods is the attempt to describe the whole elephant — knowing that even with both strands, you are still describing only what you can reach.</div>""", unsafe_allow_html=True)
    section_divider()
    st.markdown("## ✅ C. Reflection & Output")
    st.markdown("After this session: distinguish three mixed methods designs, explain when convergent parallel is appropriate, describe a joint display, and evaluate what 'integration' means beyond parallel reporting.")


def render_s10_content():
    st.markdown("## 📖 A. Theoretical Concepts")
    with st.expander("1. AI in Data Collection"):
        concept_card("AI-Assisted Survey Design", "AI generates candidate items rapidly. Requires expert validation, pilot testing, reliability analysis. AI speed ≠ validity.")
        concept_card("AI Chatbot Interviews", "AI can conduct semi-structured interviews at scale. Must disclose to participants. Cannot respond empathetically to distress. Cannot detect coercion. Ethics review essential.")
        concept_card("Social Media Data", "Large, naturalistic, longitudinal. But: sampling bias (who uses platform), consent issues (public ≠ research consent), algorithmic filtering distorts what is visible.")
    with st.expander("2. Research Ethics — Core Principles"):
        st.markdown("""
**Belmont Report (1979) — three principles:**
1. Respect for persons (autonomy, informed consent)
2. Beneficence (maximise benefit, minimise harm)
3. Justice (fair distribution of research burdens and benefits)

**For AI-mediated research:**
- Disclose AI involvement in data collection (consent requires knowing what you are consenting to)
- Assess whether AI can detect and respond to participant distress
- Consider algorithmic bias in recruitment
- Preserve and disclose data sources for reproducibility
        """)
    with st.expander("3. Informed Consent in the AI Era"):
        warn_box("Public availability ≠ research consent. Social media posts are public — that does not mean users consented to inclusion in research datasets.")
        concept_card("What Informed Consent Requires", "Participants must understand: the research purpose, what data will be collected and how, whether AI tools will be involved, who will have access to data, and how to withdraw.")
    st.markdown("---")
    if st.button("🎭 Research Story — S10", key="s10_story"):
        st.markdown("""<div class="gold-card"><strong>The Invisible Researcher</strong><br><br>In 2014, Facebook conducted an emotional contagion experiment on 689,000 users — manipulating their news feeds without consent. The data was already 'theirs' by terms of service. But the experiment, when exposed, was widely condemned. The distinction between 'using your data' and 'experimenting on you without consent' turned out to matter to the people involved. Research ethics is not a bureaucratic hurdle — it is an agreement between researchers and the humans whose lives their research enters.</div>""", unsafe_allow_html=True)
    st.markdown("## ✅ Reflection")
    st.markdown("After this session: describe three ethical concerns with AI-mediated data collection, explain the Belmont principles, and draft an informed consent statement for a study using AI chatbot interviews.")


def render_s11_content():
    st.markdown("## 📖 A. Theoretical Concepts")
    with st.expander("1. Mediation and Moderation"):
        concept_card("Mediation (X→M→Y)", "Tests HOW X affects Y through an intermediary variable M. Example: AI feedback → increased clarity (M) → improved performance. Hayes PROCESS macro (Model 4) is the standard tool.")
        concept_card("Moderation (X→Y | M)", "Tests WHEN or FOR WHOM X affects Y. The effect of X on Y changes at different levels of M. Example: AI feedback → performance, but only when employees have high growth mindset. Hayes PROCESS macro (Model 1 or 2).")
        warn_box("Mediation ≠ moderation. Mediators explain mechanisms; moderators identify boundary conditions. Confusing them is a common proposal and paper error.")
    with st.expander("2. Interpreting AI Analysis Output"):
        concept_card("AI Sentiment Analysis", "Reports percentage positive/negative/neutral. Must evaluate: what operationalises 'positive'? What was the training data? Is the model validated for your domain (workplace vs product reviews)?")
        concept_card("Topic Modelling", "Identifies statistical co-occurrence patterns, not semantic meaning. Topics may need to be labelled, split, or merged by a domain expert. AI topics ≠ analytical themes.")
        concept_card("Effect Size Reporting", "p-values tell you whether a result is statistically significant. Effect sizes (Cohen's d, η², r) tell you how large the effect is. Both must be reported. A significant effect can be trivially small.")
    with st.expander("3. Confirmatory Factor Analysis"):
        st.markdown("""
CFA tests a theoretically specified factor structure. Key fit indices:
- CFI (Comparative Fit Index): > 0.95 excellent, > 0.90 acceptable
- RMSEA: < 0.06 excellent, < 0.08 acceptable  
- SRMR: < 0.08 acceptable

**Sequence:** EFA (discover structure, sample 1) → CFA (confirm structure, sample 2 or random split)
**Purpose:** Establish construct validity before running structural equation modelling.
        """)
    if st.button("🎭 Research Story — S11", key="s11_story"):
        st.markdown("""<div class="gold-card"><strong>The Significant Triviality</strong><br><br>Imagine a study with 10,000 participants finds that AI training increases productivity by 0.3% (p < 0.001). The p-value is tiny. The effect is negligible. Whether the extra 0.3% justifies the cost of AI training depends on context, not on the p-value. Effect sizes exist to answer the question the p-value cannot: not 'did it work?' but 'how much did it work?' Significance without size is a number without meaning.</div>""", unsafe_allow_html=True)
    st.markdown("## ✅ Reflection")
    st.markdown("After this session: diagram a mediation and a moderation model, interpret CFA fit indices, explain why p-values alone are insufficient, and describe what a topic model actually produces.")


def render_s12_content():
    st.markdown("## 📖 A. Theoretical Concepts")
    with st.expander("1. Academic Voice"):
        concept_card("What Academic Voice Is", "Precise, evidence-grounded, hedged where appropriate, and clearly attributed. It is not formal-for-its-own-sake — it is the voice that makes arguments traceable and evaluable.")
        concept_card("What AI Produces", "Fluent, generic, and pattern-averaged text. AI prose is often grammatically correct but epistemically empty — it asserts without reasoning, hedges without precision, and smooths without nuance.")
        concept_card("The Revision Imperative", "AI-drafted text is a starting point. The researcher must inject: specific design rationale, context-sensitive interpretation, hedged claims where evidence is weak, and the connecting tissue of argument.")
    with st.expander("2. PEEL Paragraph Structure"):
        st.markdown("""
**P** — Point: state the paragraph's main claim
**E** — Evidence: provide specific data, finding, or quotation
**E** — Explanation: interpret the evidence in relation to the claim
**L** — Link: connect to the next paragraph or the overall argument

**Weak paragraph:** 'AI has many effects on employees. Research shows mixed results. More research is needed.'

**Strong paragraph (PEEL):** 'AI-assisted performance management has been associated with reduced perceived autonomy in multiple studies (P). For instance, Tambe et al. (2022) found that nurses using AI triage tools reported 23% lower decisional autonomy compared to control groups (E). This reduction may reflect an alignment of agency from professional judgement to algorithmic recommendation — a mechanism consistent with Social Exchange Theory's prediction that benefit asymmetry erodes reciprocal obligation (E). The next section examines whether this autonomy reduction is moderated by institutional context (L).'
        """)
    with st.expander("3. Structuring a Discussion Section"):
        concept_card("What the Discussion Is Not", "Not a repetition of results. Not a list of contributions. Not a section where you say 'as expected.'")
        concept_card("What the Discussion Is", "An interpretive argument: here is what the findings mean, here is how they relate to theory, here is what is surprising and why, here is what practitioners should do, here are the limitations of the claims I am making.")
    with st.expander("4. AI Use Disclosure"):
        st.markdown("""
**Best practice (Nature, Elsevier, most top journals):**
Disclose specifically: what AI was used for, which tool, at what stage.

**Example disclosure:** 'Elicit.org was used to assist with initial literature search. ChatGPT-4 was used to improve fluency of the Introduction section draft. All AI-assisted text was reviewed and substantially revised by the authors. No AI tool was used for data analysis or interpretation. AI tools are not listed as authors.'

**What constitutes undisclosed AI use:** Submitting AI-generated text as your own without any disclosure — regardless of how much you edited it.
        """)
    if st.button("🎭 Research Story — S12", key="s12_story"):
        st.markdown("""<div class="gold-card"><strong>The Ghost in the Machine</strong><br><br>There is a ghost that haunts AI-assisted academic writing. It is the ghost of the generic. AI learns to write from millions of texts — and it produces the statistically average version of each genre it has learned. Average academic introduction. Average methodology paragraph. Average discussion conclusion. The text is fluent and inoffensive and says approximately what needs to be said. And it sounds like everyone, which means it sounds like no one. The researcher's job is to haunt their own writing back: to inject the specific, the contextual, the uncertain, the original. To write not the text that 'should' appear but the text that has something to say.</div>""", unsafe_allow_html=True)
    st.markdown("## ✅ Reflection")
    st.markdown("After this session: write a PEEL paragraph on your research topic, draft an AI use disclosure statement, identify three AI-text patterns to revise, and describe what a discussion section does.")


def render_s13_content():
    st.markdown("## 📖 A. Theoretical Concepts")
    with st.expander("1. Academic Integrity — FFP"):
        concept_card("Fabrication", "Creating data that was never collected. Recording results for experiments that were not run. The most serious form of research misconduct.")
        concept_card("Falsification", "Manipulating real data, instruments, or results. Changing values, removing inconvenient data points, or presenting composite images as separate experiments.")
        concept_card("Plagiarism", "Presenting another's words, ideas, images, or data as your own without attribution. Applies to human and AI-generated text alike.")
        warn_box("Self-plagiarism: reusing substantial text from your own prior publications without disclosure. Required disclosure even of your own prior work.")
    with st.expander("2. Citation Ethics"):
        concept_card("Citation Without Reading", "Including a citation without reading the source is a form of misrepresentation — you cannot know what the paper actually says. AI-suggested citations must be verified against the original.")
        concept_card("Citation Stuffing", "Adding references only to appear thorough, without engaging with the sources. Common when AI generates citation lists. Reviewers detect it when cited papers are tangentially related at best.")
        concept_card("Predatory Journals", "Accept papers for fees without genuine peer review. Mimic legitimate journals. Check: Beall's List, Scopus source list, DOAJ. Warning signs: spam invitation, guaranteed acceptance, vague scope.")
    with st.expander("3. Research Ethics Principles"):
        concept_card("Informed Consent", "Participants must understand: purpose, procedures, risks, benefits, confidentiality, voluntary participation, right to withdraw.")
        concept_card("Anonymity vs Confidentiality", "Anonymity: researcher cannot link data to individual. Confidentiality: researcher knows identity but does not disclose. Most qualitative research offers confidentiality, not full anonymity.")
        concept_card("Data Integrity", "Data must be stored securely, retained for required period (typically 5 years post-publication), and shared or archived as required by funder or journal.")
    if st.button("🎭 Research Story — S13", key="s13_story"):
        st.markdown("""<div class="gold-card"><strong>The Citation That Never Was</strong><br><br>In 2023, two US lawyers submitted a legal brief that cited cases — real-sounding, plausibly formatted cases — that did not exist. They had used ChatGPT. When the judge asked for the citations to be produced, they could not be found. The lawyers were sanctioned. The lesson: authoritative format does not equal accurate content. AI produces citations that look right. Scholars must verify that they are right. The same standard applies to every footnote in every paper: you are responsible for what you cite, regardless of how you found it.</div>""", unsafe_allow_html=True)
    st.markdown("## ✅ Reflection")
    st.markdown("After this session: define FFP and give one example of each, explain the difference between anonymity and confidentiality, design a citation verification protocol, and identify three signs of a predatory journal.")


def render_s14_content():
    st.markdown("## 📖 A. Theoretical Concepts")
    with st.expander("1. Types of Peer Review Decisions"):
        concept_card("Desk Rejection", "Editor rejects without sending to reviewers. Causes: out of scope, poor problem statement, fundamental methodology flaw, writing quality too low.")
        concept_card("Reject after Review", "Reviewers evaluate and recommend rejection. May indicate: fundamental conceptual problems, irremediable methodological flaws, insufficient contribution.")
        concept_card("Revise and Resubmit (R&R)", "Reviewers see merit but require substantial revisions. One of the most common outcomes at quality journals. An R&R is a conditional acceptance — do not treat it as a rejection.")
        concept_card("Accept with Minor Revisions", "Small changes needed. Relatively rare at top journals. Usually means the paper is near-final.")
    with st.expander("2. Writing a Revision Letter"):
        st.markdown("""
**Structure of a strong revision letter:**
1. Opening paragraph: thank editor, summarise major revisions made
2. Point-by-point response: address each reviewer comment in sequence
3. For each comment: quote the comment, describe the change made, quote the revised text with line numbers
4. Where disagreeing with a reviewer: state respectfully, argue with evidence, offer alternative interpretation

**Tone:** Respectful, specific, and grateful — even for harsh comments. Reviewers are unpaid colleagues giving time.

**Length:** Should match the volume of comments. A 45-comment review deserves a thorough response, not a two-page letter.
        """)
    with st.expander("3. AI-Assisted Revision"):
        concept_card("Appropriate Uses", "AI can help restructure sentences for clarity, suggest alternative phrasings, check for consistency in terminology, and identify where argument flow is weak.")
        concept_card("Inappropriate Uses", "AI cannot evaluate whether a methodological change is valid, assess whether a theoretical argument is defensible, or make scholarly judgements about reviewer concerns.")
    if st.button("🎭 Research Story — S14", key="s14_story"):
        st.markdown("""<div class="gold-card"><strong>The Gift of the Hostile Reviewer</strong><br><br>Every established academic has a story of a brutal review. The review that called their methodology 'naive.' The reviewer who said their theoretical contribution was 'non-existent.' The seven-page list of required changes. At the time, it felt like an attack. Looking back, it almost always made the paper better. The hostile reviewer is not your enemy — they are an unpaid, anonymous editor who read your paper closely enough to find the problems that were already there, even if you could not see them. The revision letter is your chance to show you can engage with difficult intellectual feedback. That skill — taking criticism seriously, responding with evidence, improving without becoming defensive — is what distinguishes scholars from students.</div>""", unsafe_allow_html=True)
    st.markdown("## ✅ Reflection")
    st.markdown("After this session: describe the four peer review decision types, write a three-point response to a methodological reviewer comment, and distinguish appropriate from inappropriate AI use in revision.")


def render_s15_content():
    st.markdown("## 📖 A. Theoretical Concepts")
    with st.expander("1. Journal Selection Strategy"):
        concept_card("Impact Factor", "Average citations per article in a two-year window. Field-dependent. Not the only criterion — scope fit matters more than IF for niche research.")
        concept_card("ABDC / ABS Journal Rankings", "Australian Business Deans Council and Association of Business Schools rankings classify journals A*, A, B, C. Widely used in South Asian and global business schools for promotion decisions.")
        concept_card("Open Access Options", "Gold OA: pay APC, version of record freely available. Green OA: self-archive accepted manuscript in institutional repository (free, after embargo). Predatory OA: pay fee, no genuine peer review — avoid.")
    with st.expander("2. Research Impact Beyond Publication"):
        concept_card("Academic Networks", "ResearchGate, Academia.edu: upload papers, track reads and citations. Google Scholar profile: essential for citation tracking. ORCID: persistent researcher identifier across institutions and journals.")
        concept_card("Non-Academic Dissemination", "Policy briefs, op-eds, conference presentations, media interviews, social media threads (Twitter/X, LinkedIn). Doctoral graduates often underestimate the reach of non-academic channels.")
        concept_card("Altmetrics", "Measures online attention: news mentions, tweets, downloads, saves. Complements citation count as a reach metric. Altmetric score visible on many journal article pages.")
    with st.expander("3. Predatory Journals and Conferences"):
        st.markdown("""
**Warning signs for predatory journals:**
- Spam invitation claiming to have read your work
- Guaranteed acceptance after 'expedited review'
- Name mimicking a legitimate journal (e.g., 'International Journal of Science' vs actual specific title)
- Absent or unverifiable editorial board
- Not indexed in Scopus, WoS, or DOAJ

**Check:** Beall's List (archived), Scopus source list (sources.scopus.com), DOAJ (doaj.org), SHERPA/RoMEO (self-archiving policies)
        """)
    if st.button("🎭 Research Story — S15", key="s15_story"):
        st.markdown("""<div class="gold-card"><strong>The Tree That Falls in an Empty Forest</strong><br><br>A paper published in a journal nobody reads, in a field where no one checks the literature, on a topic that practitioners never encounter — has it contributed to knowledge? Technically yes. Practically no. Research is not a private act. It is a public one. The obligation to disseminate — to make findings accessible, to present them to relevant audiences, to engage with the communities whose problems the research addresses — is not optional decoration. It is part of what it means to conduct research responsibly. Scholarship circulates, or it disappears.</div>""", unsafe_allow_html=True)
    st.markdown("## ✅ Reflection")
    st.markdown("After this session: identify three journals appropriate for one paper from your research area (with justification), explain green vs gold OA, describe the difference between h-index and altmetrics, and identify one non-academic dissemination channel relevant to your research.")


def render_s16_content():
    st.markdown("## 📖 A. Theoretical Concepts — Capstone")
    with st.expander("1. What This Course Has Built"):
        concept_card("Competency Map", "CLO 1: AI tool critique. CLO 2: Gap and problem formulation. CLO 3: Literature review and PRISMA. CLO 4: Theoretical frameworks. CLO 5: Method selection. CLO 6: AI-assisted analysis. CLO 7: Academic writing and publication. CLO 8: Ethics, governance, and integrity.")
        concept_card("The Researcher You Are Becoming", "Not an AI user who happens to do research. Not a researcher who ignores AI. A critical, reflective, methodologically literate scholar who uses AI as one set of tools within a practice grounded in intellectual responsibility.")
    with st.expander("2. The Future of AI in Research"):
        st.markdown("""
**Near-term developments (next 2–5 years):**
- AI in peer review: automated novelty and quality screening (already piloted)
- AI-generated data synthesis: real-time meta-analysis as studies are published
- AI research agents: autonomous literature review and hypothesis generation
- Governance frameworks: institutional and journal AI policies rapidly evolving

**Enduring human contributions:**
- Ethical framing of research questions
- Original conceptual leap — seeing phenomena as instances of new categories
- Accountable knowledge-making — standing behind findings with one's reputation
- Contextual judgment — knowing when general findings do and do not apply

**The doctoral graduate's role:**
Not to outperform AI at tasks AI can do faster. To develop and defend the distinctively human contributions that make research worth doing.
        """)
    with st.expander("3. Research as a Moral Practice"):
        concept_card("Who Benefits?", "Every research decision encodes assumptions about who matters, whose problem gets studied, and whose knowledge counts. Doctoral researchers who take this seriously produce scholarship that is not only methodologically rigorous but ethically defensible.")
        concept_card("Accountability", "You are responsible for every word in your publications — AI-assisted or not. Every citation, every finding, every claim is yours. That responsibility is not a burden; it is the mark of membership in the scholarly community.")
    if st.button("🎭 Final Research Story", key="s16_story"):
        st.markdown("""<div class="gold-card">
<strong>What Remains</strong><br><br>
Across sixteen sessions, we have covered the tools and the craft of research in an AI-enabled world. You have learned to search with rigour, read with scepticism, frame with precision, theorise with discipline, and write with voice.

But there is one thing no tool can do for you.

It cannot decide that a question matters. It cannot sit with the discomfort of an unexpected finding and ask what it means. It cannot defend an interpretation to a hostile examiner. It cannot read a participant's interview transcript and feel the weight of what was said.

Research, at its best, is an act of sustained, disciplined attention — to a problem that matters, conducted with methods that are honest, reported with a voice that is your own, and offered to a community that needs it.

AI changes the speed of many things. It does not change this.

Go do research worth doing.
</div>""", unsafe_allow_html=True)

    section_divider()
    st.markdown("## 📊 Capstone: Course CLO Achievement Checklist")
    clos = [
        ("CLO 1", "Critically evaluate AI tools used in academic research workflows"),
        ("CLO 2", "Formulate rigorous research problems and questions using AI-assisted gap analysis"),
        ("CLO 3", "Conduct and report systematic literature reviews with AI search tools"),
        ("CLO 4", "Apply appropriate theoretical frameworks informed by AI-assisted mapping"),
        ("CLO 5", "Select and justify quantitative, qualitative, or mixed methods"),
        ("CLO 6", "Interpret AI-generated outputs with scholarly integrity and epistemic caution"),
        ("CLO 7", "Produce publication-ready academic writing with appropriate citation and ethics"),
        ("CLO 8", "Reflect critically on the limitations, biases, and governance issues of AI in research"),
    ]
    for code, desc in clos:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(f"**{code}**")
        with col2:
            st.checkbox(desc, key=f"capstone_clo_{code}")

    st.markdown("## ✅ Final Reflection")
    st.markdown("""
**The most important question of this course:**
> *What is your unique intellectual contribution to your research area — the contribution that you, not an AI, must provide?*

Write your answer. Bring it to your next supervision meeting. Return to it when you submit your thesis.
    """)


# ═══════════════════════════════════════════════════════════════════════════════
# RENDER DISPATCH (used by the session files s03.py through s16.py)
# ═══════════════════════════════════════════════════════════════════════════════

def render_session(key):
    if key in SESSIONS:
        render_full_session(key)
    elif key in STUB_SESSIONS:
        render_stub_session(key)
    else:
        st.error(f"Session '{key}' not found.")
