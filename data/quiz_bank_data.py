"""
Quiz Bank — 100+ questions across all 16 sessions.
"""

QUIZ_BANK = [

# ── Session 1: AI & Research Landscape ──────────────────────────────────────
{
"number": 1, "session": "S01", "difficulty": "Beginner", "clo": "CLO 1",
"concept": "Role of AI in Research",
"question": "Which of the following BEST describes the current role of AI tools in academic research?",
"options": [
    "AI replaces human judgment in designing research studies",
    "AI assists researchers by automating repetitive tasks and surfacing patterns, while scholars retain interpretive authority",
    "AI produces research findings that can be published without scholarly review",
    "AI is primarily useful for formatting and typesetting manuscripts"
],
"correct": 1,
"explanation": {
    "concise": "AI augments scholarly work; it does not replace the researcher's epistemic responsibility.",
    "detailed": "Current AI tools — from semantic search engines to large language models — accelerate literature discovery, suggest methodological patterns, and help structure writing. However, the interpretation of findings, the ethical framing of questions, and the validity judgments remain firmly with the human researcher. This distinction matters both practically and institutionally.",
    "doctoral_relevance": "Doctoral scholars must be able to articulate where AI ends and their original intellectual contribution begins — a distinction increasingly required by journals and ethics committees.",
    "instructor_emphasis": "Ask students: 'If AI found your research gap, does that gap belong to you?' Use this to open a discussion on intellectual ownership."
},
"wrong_reasons": [
    "Option A overstates AI capability. Current AI cannot design rigorous studies — it can suggest designs, but cannot assess their suitability for a specific context.",
    "Option C is factually incorrect. AI outputs require human validation; no journal accepts AI as an author or sole analytical engine.",
    "Option D severely understates AI's role. While AI can assist with formatting, its research applications span literature synthesis, hypothesis generation, and data analysis."
],
"teaching_insight": "Students often hold either extreme: AI is magic or AI is useless. This question surfaces the nuanced middle ground.",
"follow_up": "Name one research task where AI involvement raises an ethical question, and explain why."
},

{
"number": 2, "session": "S01", "difficulty": "Intermediate", "clo": "CLO 1",
"concept": "Epistemic Authority",
"question": "A doctoral student uses an AI tool to generate a literature review summary. Which concern is MOST legitimate from a scholarly standpoint?",
"options": [
    "The summary may be too well-written for the student's level",
    "The AI may fabricate citations or misrepresent source arguments, compromising the review's accuracy",
    "Using AI makes the literature review too long",
    "AI summaries are always accurate because they draw on large training datasets"
],
"correct": 1,
"explanation": {
    "concise": "AI language models hallucinate — they generate plausible-sounding but sometimes factually incorrect citations and summaries.",
    "detailed": "Large language models (LLMs) produce outputs by predicting statistically likely text, not by retrieving verified facts. This means they can invent journal names, volume numbers, and even entire papers. For literature reviews, this is a serious risk — a fabricated citation that makes it into a published paper constitutes academic misconduct, even if unintentional.",
    "doctoral_relevance": "Every AI-assisted literature output must be cross-checked against the original source. This is not optional; it is a basic scholarly standard.",
    "instructor_emphasis": "Demonstrate this live: ask ChatGPT for five citations on a topic, then verify each one in Google Scholar. Expect at least one to be wrong."
},
"wrong_reasons": [
    "Option A is not a scholarly concern — writing quality is not an integrity issue in this context.",
    "Option C is irrelevant; length is not the problem.",
    "Option D is false. AI accuracy depends heavily on the task and the model. Citation accuracy is particularly poor in generative AI."
],
"teaching_insight": "Running a live hallucination demo is one of the most effective teaching moments in this course.",
"follow_up": "What verification steps should a researcher take before citing any AI-suggested source?"
},

{
"number": 3, "session": "S01", "difficulty": "Advanced", "clo": "CLO 1, 8",
"concept": "AI Bias in Research",
"question": "A management researcher uses an AI tool trained primarily on English-language, Western-context publications to map the literature on organisational trust. What is the MOST significant methodological concern?",
"options": [
    "The tool may not support PDF upload",
    "The researcher should have used a different search engine",
    "The AI may systematically exclude non-English and Global South scholarship, skewing the conceptual map",
    "The literature on organisational trust is too large for AI to process"
],
"correct": 2,
"explanation": {
    "concise": "AI trained on biased corpora reproduces those biases — English-language dominance in training data excludes significant non-Western scholarship.",
    "detailed": "Most large language models and semantic search tools are trained predominantly on English-language, Western academic outputs. When used for conceptual mapping, they may surface a geographically and linguistically narrow slice of the literature. For topics like trust, leadership, or ethics — where cultural context is central — this bias is not merely technical; it shapes the researcher's understanding of the phenomenon.",
    "doctoral_relevance": "Doctoral scholars must evaluate AI tools not only for accuracy but for representational coverage. A systematic review that uses AI must account for the tool's training data limitations.",
    "instructor_emphasis": "Ask: 'Who is missing from your AI-generated literature map?' This connects to debates about epistemic justice in research."
},
"wrong_reasons": [
    "Option A is a technical issue, not a methodological concern.",
    "Option B is vague and does not address the real problem.",
    "Option D is incorrect — AI tools can handle very large corpora; the issue is corpus composition, not size."
],
"teaching_insight": "This question opens a productive discussion on whose knowledge gets included in 'global' research.",
"follow_up": "How would you supplement an AI literature search to ensure adequate coverage of non-English scholarship?"
},

{
"number": 4, "session": "S01", "difficulty": "Doctoral Challenge", "clo": "CLO 1, 8",
"concept": "AI and Research Epistemology",
"question": "From a philosophy of science perspective, which critique of AI-assisted research is MOST epistemologically grounded?",
"options": [
    "AI tools are too expensive for most universities",
    "AI cannot process qualitative data effectively",
    "AI encodes the epistemic assumptions of its training data and may naturalise particular ways of knowing, marginalising alternative epistemologies",
    "AI tools produce too much output for a researcher to read"
],
"correct": 2,
"explanation": {
    "concise": "AI is not epistemically neutral — it encodes and reproduces the assumptions embedded in its training corpus.",
    "detailed": "Every training corpus reflects choices: which journals to include, which languages to index, which forms of knowledge count as 'evidence'. When AI tools are used unreflectively, they can reinforce positivist, Western, and quantitative epistemological frameworks at the expense of interpretivist, indigenous, or decolonial ways of knowing. This is not just a fairness issue — it can fundamentally shape what research questions get asked and which findings get legitimated.",
    "doctoral_relevance": "Doctoral scholars working in critical management studies, postcolonial research, or any non-mainstream tradition must be particularly alert to how AI tools position their epistemological standpoint.",
    "instructor_emphasis": "Connect this to Haraway's 'situated knowledge' — no tool is god-trick objective. AI is a situated technology."
},
"wrong_reasons": [
    "Option A is a resource issue, not an epistemological critique.",
    "Option B is empirically contestable — AI does process qualitative data (NLP, thematic analysis) — and misses the philosophical point.",
    "Option D is a practical inconvenience, not an epistemic critique."
],
"teaching_insight": "This question differentiates students who understand research philosophy from those who think of methods as neutral techniques.",
"follow_up": "How might a researcher using an interpretivist epistemology adapt their use of AI tools to remain epistemologically consistent?"
},

{
"number": 5, "session": "S01", "difficulty": "Intermediate", "clo": "CLO 1",
"concept": "Misconception — AI as Author",
"question": "A student submits a literature review section entirely generated by an AI and lists themselves as the sole author. Which statement BEST characterises this situation?",
"options": [
    "This is acceptable if the AI output is grammatically correct",
    "This is a form of academic misconduct equivalent to ghost-writing, and potentially constitutes plagiarism depending on institutional policy",
    "This is fine because AI tools do not hold copyright",
    "This is acceptable as long as the student reads the output before submitting"
],
"correct": 1,
"explanation": {
    "concise": "Submitting AI-generated work without disclosure is academic misconduct at most institutions.",
    "detailed": "Most universities have updated their academic integrity policies to require disclosure of substantive AI use. Even where policies are still evolving, submitting a section the student did not write — regardless of whether the 'author' is a human or a machine — misrepresents the student's intellectual contribution. The question of copyright is separate from the question of academic integrity.",
    "doctoral_relevance": "Journals now routinely require AI use statements. Doctoral students must understand what constitutes appropriate use versus misrepresentation.",
    "instructor_emphasis": "Share your institution's current AI policy and any relevant journal policies (e.g., Nature, Elsevier) before this question."
},
"wrong_reasons": [
    "Option A confuses technical quality with integrity — grammatical correctness has no bearing on academic honesty.",
    "Option C conflates copyright (a legal concept) with academic integrity (an ethical concept). They are different.",
    "Option D is insufficient — reading output before submission does not constitute intellectual authorship."
],
"teaching_insight": "Students often confuse 'using AI' with 'submitting AI work'. This question clarifies the boundary.",
"follow_up": "Draft a two-sentence AI use disclosure statement for a research paper that used AI for literature search and initial drafting."
},

# ── Session 2: Research Problem & Gap ───────────────────────────────────────
{
"number": 6, "session": "S02", "difficulty": "Beginner", "clo": "CLO 2",
"concept": "Research Gap",
"question": "A research gap is BEST defined as:",
"options": [
    "A topic that has not been studied by anyone, anywhere",
    "An inconsistency, unexplored context, or unanswered question that existing literature leaves open",
    "A difference in findings between two papers on the same topic",
    "A mistake in a published study that the researcher wants to correct"
],
"correct": 1,
"explanation": {
    "concise": "A research gap is an unexplored dimension, contested finding, or undertheorised context — not necessarily a completely unstudied topic.",
    "detailed": "Most strong research gaps are not blank slates. They are places where (a) existing findings conflict and need reconciliation, (b) a phenomenon has been studied in one context but not another, (c) a methodology has not been applied to a topic, or (d) theory has not been tested empirically, or vice versa. Students who look for gaps by searching for 'topics no one has written about' will almost always fail to find a legitimate gap.",
    "doctoral_relevance": "Reviewers evaluate whether the gap is genuine and significant. Stating 'no one has studied X' without evidence is a common rejection reason.",
    "instructor_emphasis": "Show the four types of gaps (empirical, theoretical, methodological, contextual) as a 2x2 matrix."
},
"wrong_reasons": [
    "Option A is too restrictive — most topics have some coverage. The gap is in depth, context, or approach.",
    "Option C describes a contradiction or inconsistency — useful for identifying gaps, but not the definition itself.",
    "Option D describes replication or error correction — a different kind of scholarly contribution."
],
"teaching_insight": "Drawing the 'research gap vs research topic' distinction early prevents superficial literature reviews.",
"follow_up": "Identify one gap type (empirical, theoretical, methodological, contextual) in a study you have read, and explain why it qualifies as that type."
},

{
"number": 7, "session": "S02", "difficulty": "Intermediate", "clo": "CLO 2",
"concept": "Problem Statement Construction",
"question": "Which problem statement is MOST suitable for a doctoral research proposal?",
"options": [
    "Employee engagement is important for organisations.",
    "Although AI-based performance management has been adopted widely, its effects on employee trust in hybrid work settings remain understudied, particularly in emerging economy firms.",
    "Many companies use AI and it affects employees in various ways.",
    "Research on AI in HR is growing and more studies are needed."
],
"correct": 1,
"explanation": {
    "concise": "A strong problem statement identifies the phenomenon, the gap, the context, and the significance.",
    "detailed": "Option B does four things well: it names the phenomenon (AI-based performance management), acknowledges existing work ('adopted widely'), specifies the gap (effects on employee trust in hybrid work settings remain understudied), and adds contextual precision (emerging economy firms). This gives a reviewer a clear picture of where the study fits and why it is needed.",
    "doctoral_relevance": "Journal reviewers and thesis examiners evaluate the problem statement first. A vague problem statement signals an unfocused study.",
    "instructor_emphasis": "Annotate Option B on the board: circle the phenomenon, underline the gap, box the context."
},
"wrong_reasons": [
    "Option A is a general claim with no gap, no specificity, and no research direction.",
    "Option C is too vague — 'various ways' does not define a researchable problem.",
    "Option D is a justification for more research in general, not a specific problem statement."
],
"teaching_insight": "Have students rewrite Option A using the four-element structure from Option B.",
"follow_up": "Write a two-sentence problem statement for a study on AI adoption in rural healthcare settings."
},

{
"number": 8, "session": "S02", "difficulty": "Advanced", "clo": "CLO 2",
"concept": "AI-Assisted Gap Discovery",
"question": "A researcher uses Elicit.org to identify research gaps. The tool returns papers with broadly similar findings. What should the researcher do NEXT?",
"options": [
    "Conclude there is no gap and choose a different topic",
    "Trust the consensus and proceed to design a replication study",
    "Search for variation: different contexts, methods, populations, or time periods not covered by the consensus studies",
    "Increase the number of papers and hope a gap appears"
],
"correct": 2,
"explanation": {
    "concise": "Consensus in the literature is not the absence of a gap — it is an invitation to probe the boundaries of that consensus.",
    "detailed": "When AI tools surface consistent findings, scholars should probe whether that consistency holds in: (a) different industry sectors or national contexts, (b) different time periods (pre/post a major disruption), (c) different organisational sizes or demographic groups, or (d) with different methodologies. Consensus in Western/large-firm studies, for instance, does not guarantee applicability in SMEs or in Indian or African contexts.",
    "doctoral_relevance": "Examiners expect candidates to show that they looked beyond agreement in the literature to find the specific site of their contribution.",
    "instructor_emphasis": "Introduce the concept of 'boundary conditions' — where does a well-supported finding NOT hold?"
},
"wrong_reasons": [
    "Option A is premature. Consensus in the literature does not exhaust all possible gaps.",
    "Option B could be a valid contribution but is not the 'next step' in gap analysis — it is a design choice made after the gap is confirmed.",
    "Option D is unstrategic — adding volume without changing the search strategy will yield similar results."
],
"teaching_insight": "Students who find consensus often feel defeated. Reframe consensus as the starting point for boundary condition analysis.",
"follow_up": "Name three 'boundary conditions' that might limit the generalisability of a finding on AI adoption in HR."
},

{
"number": 9, "session": "S02", "difficulty": "Doctoral Challenge", "clo": "CLO 2",
"concept": "Significance vs Novelty",
"question": "A dissertation committee member argues that a proposed study is 'novel but not significant.' What does this critique MOST likely mean?",
"options": [
    "The study uses a method no one has used before, which the committee dislikes",
    "The study addresses an unstudied question, but the answer would not advance theory, policy, or practice in a meaningful way",
    "The study is too original to be understood by reviewers",
    "The study has been done before, making it insignificant"
],
"correct": 1,
"explanation": {
    "concise": "Novelty (originality) and significance (contribution value) are separate criteria. A study can be new without being important.",
    "detailed": "A study of, say, personality traits of left-handed accountants in Fiji might be genuinely unstudied — but it offers no clear path to advancing accounting theory, improving practice, or informing policy. Significance requires that the answer to the research question matters: to scholars building theory, to practitioners making decisions, or to policymakers designing interventions.",
    "doctoral_relevance": "Doctoral candidates must be able to articulate the 'so what' of their research — not just 'no one has done this' but 'here is why the answer matters.'",
    "instructor_emphasis": "Ask students to answer 'so what?' for their proposed research in 30 seconds. If they struggle, the significance case is weak."
},
"wrong_reasons": [
    "Option A misinterprets the criticism — using a novel method is generally valued, not criticised.",
    "Option C is not a real academic concern. Reviewers do not reject work for being too original.",
    "Option D is the opposite of the critique — 'novel but not significant' means new, not replicated."
],
"teaching_insight": "This question helps students see that their pitch to reviewers must address both dimensions independently.",
"follow_up": "For your own research area, write one sentence on its novelty and one sentence on its significance — without using the same argument for both."
},

{
"number": 10, "session": "S02", "difficulty": "Intermediate", "clo": "CLO 2, 8",
"concept": "Ethics of Problem Selection",
"question": "A researcher wants to study 'why women fail in leadership roles.' A colleague suggests reframing this as 'what organisational conditions constrain women's leadership advancement.' What does the reframe achieve?",
"options": [
    "It makes the study easier to get funded",
    "It shifts the unit of analysis from individual deficit to structural constraint, which is epistemologically and ethically more defensible",
    "It makes the research question longer and more academic-sounding",
    "It avoids the need for female participants"
],
"correct": 1,
"explanation": {
    "concise": "The reframe moves from a deficit model (locating the problem in individuals) to a structural model (locating the problem in institutions), which is both more accurate and more ethical.",
    "detailed": "The original framing naturalises failure as something women do, implicitly treating leadership norms as neutral. The reframe recognises that leadership definitions, evaluation criteria, and promotion systems are socially constructed and may systematically disadvantage women. This is not political correctness — it is better theory construction, aligned with decades of feminist organisational theory.",
    "doctoral_relevance": "Research framing is not neutral. The way a question is posed shapes the kinds of answers that become thinkable, and has downstream implications for what gets published and cited.",
    "instructor_emphasis": "Connect to Merton's concept of 'opportunity structures' and Acker's 'gendered organisations' — the reframe is theoretically grounded."
},
"wrong_reasons": [
    "Option A may be incidentally true but is not the reason for the reframe.",
    "Option C is superficial — longer does not mean better.",
    "Option D is incorrect — structural analysis still requires data from and about women."
],
"teaching_insight": "This question surfaces how research framing encodes assumptions about causality and responsibility.",
"follow_up": "Identify a research question in your field that might benefit from a similar structural reframe, and explain what the reframe reveals."
},

# ── Session 3: AI Literature Search ─────────────────────────────────────────
{
"number": 11, "session": "S03", "difficulty": "Beginner", "clo": "CLO 3",
"concept": "AI Search Tools",
"question": "Which of the following AI-assisted tools is PRIMARILY designed to surface conceptual connections and citation networks rather than ranked keyword matches?",
"options": [
    "Google Scholar",
    "Scopus keyword search",
    "Connected Papers",
    "PubMed"
],
"correct": 2,
"explanation": {
    "concise": "Connected Papers builds a visual graph of papers related to a seed paper, revealing intellectual lineage rather than keyword matches.",
    "detailed": "Traditional search engines rank results by keyword frequency and citation count. Connected Papers uses co-citation and bibliographic coupling to build a graph where closeness indicates conceptual relationship. This helps researchers discover foundational papers they might not have found through keyword search, and identify clusters of work that represent distinct schools of thought.",
    "doctoral_relevance": "Doctoral literature reviews benefit from both keyword-driven depth (Scopus) and network-driven breadth (Connected Papers). Using only one type leads to blind spots.",
    "instructor_emphasis": "Do a live demo: enter a well-known paper in your field and walk through the resulting graph."
},
"wrong_reasons": [
    "Option A uses keyword and citation ranking, not network visualisation.",
    "Option B is a keyword-based system — sophisticated but not network-based.",
    "Option D is domain-specific to biomedical research and uses keyword/MeSH term matching."
],
"teaching_insight": "Many students have only ever used Google Scholar. This question introduces them to a fundamentally different search paradigm.",
"follow_up": "Enter a paper from your research area into Connected Papers and describe two findings from the graph that surprised you."
},

{
"number": 12, "session": "S03", "difficulty": "Intermediate", "clo": "CLO 3",
"concept": "Search String Design",
"question": "A researcher building a systematic search string for a review on AI in talent management includes only the term 'artificial intelligence.' What is the MAIN limitation of this approach?",
"options": [
    "The term is too technical for most databases",
    "It excludes synonymous and related terms (e.g., 'machine learning', 'algorithmic screening', 'automated recruitment') that appear in relevant papers",
    "Boolean operators will not work with this term",
    "The term 'artificial intelligence' has only been used in research since 2020"
],
"correct": 1,
"explanation": {
    "concise": "A single-term search misses synonymous terminology used across different disciplines and time periods.",
    "detailed": "The literature on AI in talent management uses a range of terms: 'machine learning', 'natural language processing', 'algorithmic hiring', 'automated screening', 'predictive HR analytics', and more. A search limited to 'artificial intelligence' misses papers using any other framing. This is a critical validity concern in systematic reviews, where comprehensiveness is a quality criterion.",
    "doctoral_relevance": "PRISMA guidelines require documentation of search strings. A narrow string without synonyms will be flagged by reviewers as incomplete.",
    "instructor_emphasis": "Walk through building a PICO or PEO-based search string from a simple term, adding synonyms at each step."
},
"wrong_reasons": [
    "Option A is false — 'artificial intelligence' is standard academic terminology in most databases.",
    "Option C is false — Boolean operators work with any search term.",
    "Option D is false — AI research dates to the 1950s; the term appeared in academic literature decades ago."
],
"teaching_insight": "Have students brainstorm synonyms for their own research topic before searching — then compare results.",
"follow_up": "Build a Boolean search string for a review on 'AI and employee wellbeing' using at least three synonym groups."
},

{
"number": 13, "session": "S03", "difficulty": "Advanced", "clo": "CLO 3",
"concept": "Source Evaluation",
"question": "A student finds a highly relevant paper on ResearchGate that is not indexed in Scopus or Web of Science. How should the student treat this source?",
"options": [
    "Automatically exclude it because it is not in a major database",
    "Include it without further evaluation since ResearchGate is an academic platform",
    "Evaluate it carefully: check the publication venue, peer-review status, author credentials, and citation record before including it",
    "Use it only in the appendix, never in the main review"
],
"correct": 2,
"explanation": {
    "concise": "Source platform does not determine scholarly quality — the paper's venue, peer-review status, and reception in the field do.",
    "detailed": "ResearchGate hosts preprints, working papers, conference papers, and peer-reviewed journal articles. The platform itself does not confer quality. A paper should be evaluated on: the journal or conference it was published in (indexed? predatory?), whether it underwent peer review, the authors' institutional affiliations and citation track record, and how it has been cited by other scholars.",
    "doctoral_relevance": "Systematic reviews must justify inclusion/exclusion criteria. 'Not in Scopus' can be an exclusion criterion, but it must be stated and justified — not assumed.",
    "instructor_emphasis": "Introduce the concept of 'grey literature' and when it is appropriate to include."
},
"wrong_reasons": [
    "Option A is overly rigid — some high-quality papers in emerging fields or non-Western scholarship are not indexed.",
    "Option B is uncritical — platform affiliation is not a quality guarantee.",
    "Option D is arbitrary — main vs appendix placement should depend on quality, not platform."
],
"teaching_insight": "Critical source evaluation is a skill that distinguishes doctoral-level from undergraduate literature use.",
"follow_up": "Design a simple three-criterion checklist for evaluating sources found outside major databases."
},

{
"number": 14, "session": "S03", "difficulty": "Intermediate", "clo": "CLO 3, 8",
"concept": "Misconception — AI Search is Comprehensive",
"question": "A student uses Consensus.app for 20 minutes and concludes 'the literature is clear.' What assumption does this reflect, and why is it problematic?",
"options": [
    "The student has used the tool correctly and the conclusion is valid",
    "The student assumes that AI search output is comprehensive, which it is not — AI tools surface a sample of relevant work, not the complete literature",
    "The student should have used a different AI tool to confirm the finding",
    "The student spent too little time, so a 40-minute search would solve the problem"
],
"correct": 1,
"explanation": {
    "concise": "AI search tools surface a probabilistically relevant sample — they cannot guarantee comprehensiveness or represent all scholarly positions.",
    "detailed": "Consensus.app and similar tools rank papers by semantic relevance and consensus signal. They do not index all journals, all languages, or all time periods equally. A 20-minute AI search may surface the dominant narrative in a field while missing dissenting voices, non-English scholarship, or newer preprints. 'The literature is clear' is a strong claim that requires a systematic, documented search, not a single AI session.",
    "doctoral_relevance": "Reviewers routinely ask: 'How do you know you have found the relevant literature?' A documented, multi-source search is the only defensible answer.",
    "instructor_emphasis": "Ask: 'How would you know if an important paper was missing from your review?' Lead students to see that you cannot know without multiple search strategies."
},
"wrong_reasons": [
    "Option A validates an unjustified conclusion — the tool may have been used correctly, but the claim it produces certainty is not.",
    "Option C misidentifies the problem as tool choice rather than the assumption of comprehensiveness.",
    "Option D is partly true (time matters) but misses the structural issue — more time on one tool still leaves the coverage problem."
],
"teaching_insight": "The 'I Googled it' mentality transferred to AI tools is one of the most common doctoral-level mistakes.",
"follow_up": "Design a three-source search strategy for a review on remote work and mental health, explaining why each source adds unique coverage."
},

{
"number": 15, "session": "S03", "difficulty": "Doctoral Challenge", "clo": "CLO 3",
"concept": "Semantic vs Keyword Search",
"question": "Semantic search tools like Elicit use embedding-based similarity rather than exact keyword matching. What is the MOST important implication for researchers using these tools?",
"options": [
    "Semantic tools always find more papers than keyword search",
    "Researchers may retrieve conceptually relevant papers that use different terminology, but may miss papers using the searched terms in a different conceptual sense",
    "Semantic search eliminates the need for inclusion and exclusion criteria",
    "Keyword search is obsolete and should be replaced entirely by semantic search"
],
"correct": 1,
"explanation": {
    "concise": "Semantic search finds conceptual neighbours but may retrieve false positives and miss terminologically distinct but contextually identical work.",
    "detailed": "Semantic embedding-based search represents papers as vectors in a high-dimensional space and retrieves papers whose meaning is close to the query. This is powerful for cross-disciplinary discovery — the same concept studied under different names in management vs psychology vs economics will be surfaced. However, it also means that papers using similar language for a different concept may be included, and highly technical or jargon-dense papers may be placed far from their semantic neighbours. Critical evaluation remains essential.",
    "doctoral_relevance": "Mixed search strategies — combining semantic tools with traditional Boolean keyword searches — currently offer the most robust coverage.",
    "instructor_emphasis": "Illustrate with the concept of 'trust' — different disciplines use 'trust', 'social capital', 'psychological safety', 'credibility' for overlapping phenomena."
},
"wrong_reasons": [
    "Option A is not guaranteed — semantic tools may retrieve fewer, more relevant papers, not more papers overall.",
    "Option C is incorrect — inclusion/exclusion criteria are needed regardless of search method.",
    "Option D overstates the case — both methods have distinct strengths; combination is best practice."
],
"teaching_insight": "Understanding *how* a search tool works shapes how a researcher interprets and validates its output.",
"follow_up": "Describe a scenario where semantic search would outperform keyword search, and one where the reverse would be true."
},

# ── Session 4: Systematic Review & PRISMA ──────────────────────────────────
{
"number": 16, "session": "S04", "difficulty": "Beginner", "clo": "CLO 3",
"concept": "PRISMA Purpose",
"question": "What is the PRIMARY purpose of the PRISMA flow diagram in a systematic review?",
"options": [
    "To display the statistical results of the reviewed studies",
    "To document and justify the process by which studies were identified, screened, and included or excluded",
    "To show the number of authors who contributed to the review",
    "To illustrate the conceptual relationship between reviewed papers"
],
"correct": 1,
"explanation": {
    "concise": "The PRISMA flow diagram makes the search and selection process transparent and reproducible.",
    "detailed": "PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) requires researchers to document how many records were identified through each database, how many were removed as duplicates, how many were screened by title/abstract, how many full texts were assessed, and how many were finally included — with reasons for each exclusion. This transparency allows readers to assess whether the review is comprehensive and unbiased.",
    "doctoral_relevance": "Journals that publish systematic reviews typically require a PRISMA flow diagram. Absence of one is a common desk-rejection trigger.",
    "instructor_emphasis": "Show a published PRISMA diagram and walk through each box with students."
},
"wrong_reasons": [
    "Option A describes meta-analytic forest plots, not the PRISMA flow diagram.",
    "Option C is unrelated — authorship is documented in the byline, not the PRISMA diagram.",
    "Option D describes concept maps or bibliometric visualisations, not PRISMA."
],
"teaching_insight": "Many students encounter PRISMA for the first time in this course. A visual walkthrough with a real example is essential.",
"follow_up": "Draw a simplified PRISMA flow diagram for a review that started with 500 records and included 28 studies, with plausible exclusion numbers at each stage."
},

{
"number": 17, "session": "S04", "difficulty": "Intermediate", "clo": "CLO 3",
"concept": "Inclusion/Exclusion Criteria",
"question": "A researcher reviews AI in healthcare and sets inclusion criteria as: peer-reviewed, English, 2015–2024, quantitative methods only. A colleague suggests adding 'qualitative studies.' What is the MOST valid justification for the original researcher's criteria?",
"options": [
    "Qualitative studies are not rigorous enough for systematic reviews",
    "The research question focuses on measurable outcomes (e.g., diagnostic accuracy), for which quantitative evidence is most appropriate",
    "Adding qualitative studies would make the review too long",
    "Qualitative studies cannot be systematically reviewed"
],
"correct": 1,
"explanation": {
    "concise": "Inclusion criteria should be driven by the research question, not by a hierarchy of methods. For measurable outcome questions, quantitative evidence is appropriate.",
    "detailed": "If the research question is 'How accurate is AI in diagnosing diabetic retinopathy compared to ophthalmologists?', then quantitative studies reporting sensitivity, specificity, and AUC values are what the question requires. Including qualitative studies (which cannot answer this question) would not improve the review. However, if the question also included 'How do clinicians perceive AI diagnostic tools?', then qualitative studies would be appropriate. Criteria must serve the question.",
    "doctoral_relevance": "Examiners will ask: 'Why did you exclude/include qualitative/quantitative studies?' The answer must be grounded in the research question, not in methodological prejudice.",
    "instructor_emphasis": "Introduce the concept of 'fit for purpose' — no method is universally superior; each serves specific question types."
},
"wrong_reasons": [
    "Option A is methodologically incorrect and reflects a positivist bias that is not epistemologically defensible.",
    "Option C is pragmatic rather than principled — length is not a valid inclusion criterion.",
    "Option D is false — qualitative systematic reviews (meta-synthesis) are an established methodology."
],
"teaching_insight": "Students often default to 'only quantitative' without thinking through the question. This example helps them see the question-driven logic.",
"follow_up": "Write inclusion and exclusion criteria for a review on 'patient experiences of AI in diagnosis' and justify each criterion."
},

# ── Session 5: Research Questions ───────────────────────────────────────────
{
"number": 18, "session": "S05", "difficulty": "Beginner", "clo": "CLO 2",
"concept": "Research Question vs Hypothesis",
"question": "Which of the following is a HYPOTHESIS rather than a research question?",
"options": [
    "How does AI-assisted recruitment affect candidate diversity?",
    "What factors explain variation in AI adoption rates across SMEs?",
    "AI-assisted recruitment reduces demographic diversity in shortlisted candidates compared to manual screening",
    "To what extent do employees trust AI performance management systems?"
],
"correct": 2,
"explanation": {
    "concise": "A hypothesis is a directional, testable prediction. A research question is open-ended and seeks to understand or explain.",
    "detailed": "Option C makes a specific, directional prediction: AI reduces diversity. This can be tested statistically. The other options ask open questions ('how', 'what', 'to what extent') without predicting the direction or nature of the answer. Research questions guide exploratory and explanatory studies; hypotheses are appropriate for confirmatory, theory-testing studies.",
    "doctoral_relevance": "Knowing whether to use a research question or a hypothesis signals methodological literacy. Mismatching the two (e.g., writing a hypothesis for a qualitative study) is a common proposal weakness.",
    "instructor_emphasis": "Show how Option C could be derived from Option A by adding directionality and a comparison group."
},
"wrong_reasons": [
    "Option A is an open question about a relationship — research question.",
    "Option B is an open explanatory question — research question.",
    "Option D uses 'to what extent' — a research question about degree, not a hypothesis."
],
"teaching_insight": "The conceptual distinction between questions and hypotheses is frequently confused in proposals.",
"follow_up": "Convert research question A into a hypothesis, and then into a null hypothesis."
},

# ── Sessions 6–16: Additional questions ─────────────────────────────────────
{
"number": 19, "session": "S06", "difficulty": "Intermediate", "clo": "CLO 4",
"concept": "Theoretical Framework Function",
"question": "What is the PRIMARY function of a theoretical framework in a research study?",
"options": [
    "To provide a literature review in paragraph form",
    "To offer a conceptual lens that explains why variables are expected to relate in a particular way",
    "To describe the research methodology in detail",
    "To justify the choice of statistical software"
],
"correct": 1,
"explanation": {
    "concise": "A theoretical framework provides the explanatory logic — it tells the reader WHY the hypothesised relationships should exist.",
    "detailed": "Without a theoretical framework, a study is descriptive at best. The framework draws on established theory (e.g., Social Exchange Theory, Institutional Theory, Resource-Based View) to explain the mechanism by which independent variables influence outcomes. It also constrains the scope of the study and guides interpretation of findings.",
    "doctoral_relevance": "Examiners and reviewers consistently ask: 'What theory drives this study?' A study without a clear theoretical anchor is almost impossible to publish in top journals.",
    "instructor_emphasis": "Use the analogy of a flashlight: the framework illuminates certain parts of the phenomenon and leaves others in the dark — that choice is deliberate and must be justified."
},
"wrong_reasons": [
    "Option A describes what some call the 'theoretical background' section — it provides context, not explanation.",
    "Option C describes the methods section, which is distinct from the framework.",
    "Option D is unrelated to theory — software choices are technical, not theoretical."
],
"teaching_insight": "Ask students to name the theory behind a paper they have read. If they cannot, discuss what that absence implies for the paper's contribution.",
"follow_up": "Identify one theory relevant to your research area and explain what mechanism it proposes."
},

{
"number": 20, "session": "S07", "difficulty": "Intermediate", "clo": "CLO 5",
"concept": "Quantitative Design Selection",
"question": "A researcher wants to test whether an AI-based leadership training intervention improves self-efficacy scores over 12 weeks. Which quantitative design is MOST appropriate?",
"options": [
    "Cross-sectional survey administered once",
    "Quasi-experimental pre-test/post-test design with a control group",
    "Retrospective content analysis of training materials",
    "Structural equation modelling without an intervention"
],
"correct": 1,
"explanation": {
    "concise": "Testing an intervention's effect over time requires a pre-test/post-test design with a control group to attribute change to the intervention.",
    "detailed": "A pre-test/post-test quasi-experimental design measures the outcome (self-efficacy) before and after the intervention, compares it to a group that did not receive the intervention, and attributes the difference to the training. Without a pre-test, you cannot know the baseline. Without a control group, you cannot rule out maturation, testing effects, or time as explanations for change.",
    "doctoral_relevance": "Causal claims require designs that rule out alternative explanations. Reviewers will ask whether the design justifies the causal language used in the findings.",
    "instructor_emphasis": "Draw the 2x2 Campbell & Stanley threats-to-validity table and ask students to identify which threats the design addresses."
},
"wrong_reasons": [
    "Option A captures only one point in time — cannot measure change.",
    "Option C analyses existing documents — cannot test the effect of a new intervention.",
    "Option D tests relationships, not causal intervention effects — and without an intervention, the question cannot be answered."
],
"teaching_insight": "Many students default to surveys for every quantitative question. This case shows when experimental/quasi-experimental designs are required.",
"follow_up": "What ethical considerations arise when randomly assigning some employees to a control group that does not receive beneficial training?"
},

{
"number": 21, "session": "S08", "difficulty": "Advanced", "clo": "CLO 5",
"concept": "Thematic Analysis",
"question": "In Braun and Clarke's reflexive thematic analysis, what distinguishes a THEME from a CODE?",
"options": [
    "Themes are longer than codes",
    "Codes are data-level labels; themes capture a pattern of shared meaning that answers something about the research question",
    "Codes are used in quantitative research and themes in qualitative research",
    "Themes must be supported by at least five participants"
],
"correct": 1,
"explanation": {
    "concise": "Codes label data features; themes represent patterns of shared meaning that speak to the research question.",
    "detailed": "In reflexive thematic analysis, codes are close to the data — they label what is happening in a segment. Themes are analytic abstractions: they capture a shared meaning pattern across codes that tells us something conceptually significant about the phenomenon. Themes are not summaries of codes; they are interpretive claims. Braun and Clarke (2006, 2019) explicitly argue against treating themes as frequency-based or as simple code clusters.",
    "doctoral_relevance": "Qualitative PhD defences frequently include the question: 'How did you move from codes to themes?' Candidates must articulate the analytic logic, not just the number of codes under each theme.",
    "instructor_emphasis": "Show a real example: a set of five interview codes, then demonstrate how they combine into an interpretive theme."
},
"wrong_reasons": [
    "Option A is wrong — themes are not defined by length.",
    "Option C is wrong — thematic analysis uses both codes and themes within qualitative research.",
    "Option D is wrong — Braun and Clarke explicitly reject frequency as the criterion for what constitutes a theme."
],
"teaching_insight": "The Braun and Clarke (2006) paper is one of the most cited in social science. Students should understand not just the steps but the philosophical underpinnings.",
"follow_up": "Given five interview codes on 'AI anxiety at work', develop one interpretive theme and explain the logic of your interpretation."
},

{
"number": 22, "session": "S09", "difficulty": "Intermediate", "clo": "CLO 5",
"concept": "Mixed Methods Integration",
"question": "In a convergent parallel mixed methods design, when does integration occur?",
"options": [
    "Before data collection, when the research questions are designed",
    "During data collection, by asking both open and closed questions in the same instrument",
    "At the interpretation stage, where quantitative and qualitative findings are compared and connected",
    "After publication, when other researchers cite both strands of the study"
],
"correct": 2,
"explanation": {
    "concise": "Convergent parallel design collects both strands simultaneously and integrates at interpretation to compare, confirm, or disconfirm findings.",
    "detailed": "In a convergent parallel design (Creswell & Plano Clark), quantitative and qualitative data are collected and analysed independently and simultaneously. Integration happens at the inference stage, where the researcher asks: Do the two strands converge? Do they diverge? If they diverge, why, and what does that tell us about the phenomenon? This meta-inference is the intellectual core of mixed methods research.",
    "doctoral_relevance": "Many students collect both types of data but never truly integrate them — they report them in separate chapters with a brief 'the findings complement each other' conclusion. Examiners recognise this as weak integration.",
    "instructor_emphasis": "Show a joint display table from a published mixed methods paper where quantitative and qualitative findings are placed side by side."
},
"wrong_reasons": [
    "Option A describes the design rationale, not integration.",
    "Option B describes a mixed-format survey instrument, not a mixed methods integration strategy.",
    "Option D describes secondary reception, not the study's own integration."
],
"teaching_insight": "True integration — not parallel reporting — is what distinguishes strong mixed methods research from two studies stapled together.",
"follow_up": "Design a joint display table that integrates survey data on AI adoption rates with interview data on employees' adoption experiences."
},

{
"number": 23, "session": "S10", "difficulty": "Advanced", "clo": "CLO 6",
"concept": "AI-Generated Survey Items",
"question": "A researcher uses ChatGPT to generate survey items for a scale measuring 'AI readiness.' What is the MOST important validation step before using these items?",
"options": [
    "Check whether the items are grammatically correct",
    "Count the number of items generated to ensure there are enough",
    "Subject the AI-generated items to content validation by domain experts and pilot testing for reliability",
    "Run the items through another AI tool for a second opinion"
],
"correct": 2,
"explanation": {
    "concise": "AI-generated items may be plausible-sounding but conceptually imprecise or construct-invalid. Expert review and pilot testing are essential.",
    "detailed": "Scale development requires that items have content validity (they cover the domain), face validity (they make sense to respondents), and adequate reliability (they cohere statistically). ChatGPT can generate item candidates rapidly, but it cannot assess whether the items fully represent the construct domain or whether they map onto how target respondents understand the concept. Expert review (typically a panel of 3–5 subject matter experts) and a pilot administration with reliability analysis (Cronbach's alpha, inter-item correlations) are minimum requirements.",
    "doctoral_relevance": "Instrument validity is a core quality criterion in quantitative research. Reviewers will ask for the validation evidence, not just the scale itself.",
    "instructor_emphasis": "Walk through a simple content validity index (CVI) calculation with a small example."
},
"wrong_reasons": [
    "Option A is necessary but not sufficient — grammatical correctness says nothing about construct validity.",
    "Option B — quantity of items is a practical consideration, not a validation step.",
    "Option D — using another AI for validation is circular and does not address the validity problem."
],
"teaching_insight": "This question surfaces the gap between generating items (easy) and validating a scale (rigorous).",
"follow_up": "Describe the steps you would take to validate a five-item scale generated by an AI, from expert review to pilot testing."
},

{
"number": 24, "session": "S11", "difficulty": "Advanced", "clo": "CLO 6",
"concept": "Interpreting AI Analysis Output",
"question": "An AI-assisted text analysis tool reports that 'sentiment toward AI in the workplace is 73% positive.' A researcher includes this finding in a paper. What critical question MUST the researcher address?",
"options": [
    "Whether the tool's interface is user-friendly",
    "How the tool operationalises 'positive sentiment' and whether its classification algorithm is valid for workplace discourse",
    "Whether 73% is a statistically significant number",
    "How many sentences were analysed"
],
"correct": 1,
"explanation": {
    "concise": "Sentiment classification is not neutral — the underlying model's training data and operationalisation determine what 'positive' means, and this must be critically evaluated.",
    "detailed": "AI sentiment tools are trained on labelled datasets — often product reviews, social media posts, or news articles — that may not represent workplace language. A word like 'efficient' might be positive in a product review but ambivalent in a workplace context ('the AI makes us more efficient, so they need fewer of us'). Before citing a sentiment percentage as a finding, researchers must understand what the model classifies as positive, on what training data, with what validation evidence.",
    "doctoral_relevance": "Using AI-generated numbers without understanding the underlying model is a form of methodological naivety that reviewers in top journals will challenge.",
    "instructor_emphasis": "Show the algorithm documentation or model card for one sentiment tool and ask students what they learn about its limitations."
},
"wrong_reasons": [
    "Option A is irrelevant to the research quality of the finding.",
    "Option C — '73%' is a descriptive percentage, not a test statistic; significance testing is the wrong frame here.",
    "Option D — sentence count is a useful descriptor but does not address validity."
],
"teaching_insight": "Students often treat AI output as objective data. This question teaches them to treat it as the product of an analytical choice.",
"follow_up": "Find the documentation for one AI text analysis tool and identify two assumptions it makes that a researcher should disclose."
},

{
"number": 25, "session": "S12", "difficulty": "Intermediate", "clo": "CLO 7",
"concept": "Academic Voice with AI",
"question": "A doctoral student uses AI to draft a methodology section. The output is well-structured and accurate. What does the student STILL need to do before submitting?",
"options": [
    "Nothing — if it is accurate, it is ready",
    "Add more references to make it longer",
    "Revise the draft to reflect their specific research design decisions, voice, and epistemic positioning, and disclose AI use",
    "Submit it and mention AI use only if asked"
],
"correct": 2,
"explanation": {
    "concise": "AI can draft structure, but the researcher must inject their specific design rationale, voice, and epistemic stance — and must disclose.",
    "detailed": "A methodology section is not merely a description of techniques — it is a justification of choices. Why this design? Why this sample? Why these instruments? These justifications are specific to the researcher's questions, context, and epistemological position, and AI cannot supply them. In addition, the final text must sound like a scholar writing in their field, not like a generically competent academic text. Disclosure of AI use is also now a requirement of most journals and institutions.",
    "doctoral_relevance": "The methodology chapter is where doctoral candidates demonstrate their understanding of research logic. An AI-drafted methodology that passes without revision does not demonstrate this understanding.",
    "instructor_emphasis": "Take an AI-generated methodology paragraph and annotate where the student must add their specific rationale."
},
"wrong_reasons": [
    "Option A is incorrect — accuracy is necessary but not sufficient for doctoral-level work.",
    "Option B — length is not a quality criterion.",
    "Option D — selective disclosure (only if asked) is a form of deception. Disclosure should be proactive."
],
"teaching_insight": "This question challenges students to see AI as a starting point, not an endpoint.",
"follow_up": "Identify three sentences in an AI-generated methodology paragraph where you would need to add your own specific rationale."
},

{
"number": 26, "session": "S13", "difficulty": "Advanced", "clo": "CLO 7, 8",
"concept": "Citation Ethics with AI",
"question": "An AI tool suggests five papers to support a claim in the researcher's manuscript. The researcher includes them without reading the original papers. This is BEST described as:",
"options": [
    "Acceptable if the AI tool is reliable",
    "Citation stuffing — adding references to appear thorough without engaging with the sources",
    "Appropriate — AI-suggested citations are pre-verified by the tool",
    "Secondary citation, which is standard academic practice"
],
"correct": 1,
"explanation": {
    "concise": "Including citations without reading the source is an academic integrity violation, regardless of how the citation was suggested.",
    "detailed": "Citing a paper without reading it misrepresents what the paper actually says. The cited paper may support a different claim, contradict the researcher's argument, or be retracted. This is true whether the citation came from an AI tool, a footnote in another paper, or a colleague's suggestion. The researcher is responsible for every citation they include.",
    "doctoral_relevance": "Many retraction cases involve citing papers that do not support the stated claims. AI-assisted citation does not reduce this responsibility — it may increase the risk.",
    "instructor_emphasis": "Share one example of a high-profile paper corrected because of citation errors. The RetractionWatch database is a useful resource."
},
"wrong_reasons": [
    "Option A — tool reliability is irrelevant to the researcher's obligation to read sources.",
    "Option C is false — AI tools do not verify citation accuracy; they generate plausible suggestions.",
    "Option D — secondary citation (citing a source via another paper) is acceptable only when the original is inaccessible, and must be indicated as such."
],
"teaching_insight": "AI-assisted citation creates a new temptation to cite without reading. This question makes the ethical stakes explicit.",
"follow_up": "Design a personal verification protocol for citations suggested by an AI tool."
},

{
"number": 27, "session": "S14", "difficulty": "Intermediate", "clo": "CLO 7",
"concept": "Responding to Peer Review",
"question": "A reviewer asks the researcher to 'add more discussion of the limitations.' What is the MOST appropriate response?",
"options": [
    "Add one sentence at the end of the conclusions saying 'this study has limitations'",
    "Add a paragraph listing every possible limitation, including those not relevant to the study",
    "Identify the specific limitations raised or implied by the reviewer, explain each clearly, and discuss their implications for the findings",
    "Write a rebuttal letter explaining that the study has no significant limitations"
],
"correct": 2,
"explanation": {
    "concise": "A rigorous limitations section is specific, honest, and links each limitation to its implications for interpreting the findings.",
    "detailed": "Reviewers ask for limitation discussion not as a formality but to assess whether researchers understand the boundaries of their own claims. Strong limitations sections identify what the study cannot claim (scope), what might have been measured differently (validity), and what alternative explanations remain possible (causal inference). They also distinguish between limitations that constrain the current findings and those that can be addressed in future research.",
    "doctoral_relevance": "The ability to identify and articulate limitations is a sign of methodological maturity. It builds, rather than undermines, the credibility of the findings.",
    "instructor_emphasis": "Show the difference between a token limitations paragraph and a substantive one from published papers."
},
"wrong_reasons": [
    "Option A — one sentence is insufficient for doctoral-level work and signals that the researcher has not engaged with the question.",
    "Option B — generic, undifferentiated lists of limitations show no analytical thinking about which limitations actually apply.",
    "Option D — claiming no significant limitations in a peer-reviewed study is rarely credible and signals defensiveness."
],
"teaching_insight": "Limitations are not weaknesses to hide — they are honest scholarly acknowledgements that strengthen the argument.",
"follow_up": "Write a three-limitation paragraph for a survey study on AI adoption in Indian manufacturing firms."
},

{
"number": 28, "session": "S15", "difficulty": "Advanced", "clo": "CLO 7, 8",
"concept": "Open Access and Dissemination",
"question": "A researcher wants to publish in a high-impact journal and also ensure maximum readership. What strategy BEST balances these goals?",
"options": [
    "Publish in a predatory open-access journal that charges no fee",
    "Target a subscription-based Q1 journal and post the accepted manuscript (post-print) on an institutional repository under the journal's self-archiving policy",
    "Publish only in open-access journals regardless of their impact factor",
    "Avoid open access because it is not accepted in top journals"
],
"correct": 1,
"explanation": {
    "concise": "Green open access — posting the accepted manuscript in an institutional repository — allows high-impact publishing alongside broad access without predatory APC fees.",
    "detailed": "Most subscription-based journals (including many Nature, Elsevier, and Sage titles) permit authors to self-archive the accepted manuscript (the peer-reviewed version before journal formatting) in an institutional repository after an embargo period. This is called green OA. It costs nothing and allows anyone — without a journal subscription — to read the research. This is distinct from gold OA (paying an APC to make the version of record freely available), which can cost $1,000–$5,000.",
    "doctoral_relevance": "Understanding open access models helps researchers make informed decisions about where and how to publish without sacrificing quality or paying unnecessary fees.",
    "instructor_emphasis": "Use SHERPA/RoMEO to look up a specific journal's self-archiving policy in class."
},
"wrong_reasons": [
    "Option A — predatory journals charge fees and do not provide genuine peer review. Publishing there damages research credibility.",
    "Option C — impact factor and quality matter. Open access alone is not a sufficient criterion.",
    "Option D — many top journals now offer open access options; the statement is factually wrong."
],
"teaching_insight": "Many early-career researchers do not understand the green/gold OA distinction. This question demystifies it.",
"follow_up": "Check the self-archiving policy for one journal in your field using SHERPA/RoMEO and report what you find."
},

{
"number": 29, "session": "S16", "difficulty": "Doctoral Challenge", "clo": "CLO 1, 8",
"concept": "Future of AI Research — Governance",
"question": "Which emerging concern is MOST likely to shape institutional policies on AI use in research over the next five years?",
"options": [
    "AI tools becoming too expensive for most universities to afford",
    "Questions of authorship attribution, research integrity, reproducibility of AI-assisted findings, and the governance of AI in peer review",
    "AI replacing all quantitative research methods",
    "Universities banning AI tools entirely due to student misuse"
],
"correct": 1,
"explanation": {
    "concise": "The core policy challenges are epistemic and ethical: authorship, integrity, reproducibility, and the role of AI in evaluating research.",
    "detailed": "As AI becomes embedded in literature review, analysis, writing, and now peer review itself, institutions and journals face hard questions: Who is accountable for AI-assisted errors? Can AI-assisted analyses be reproduced? When AI screens manuscripts for journals, what biases are introduced? These are not hypothetical — Nature, Science, and major publishers have already published editorial positions. Policy is evolving rapidly.",
    "doctoral_relevance": "Doctoral graduates who understand these governance debates will be better positioned to contribute to institutional policy and to publish in journals that are actively navigating these questions.",
    "instructor_emphasis": "Assign students to find and read one journal's current AI policy and report back."
},
"wrong_reasons": [
    "Option A — cost is a real access-equity concern but is not the primary driver of institutional policy on AI in research.",
    "Option C — this is a fear rather than an evidence-based projection. AI is unlikely to replace all quantitative methods.",
    "Option D — outright bans have been rare and are generally reversed; integration with governance is the direction most institutions are taking."
],
"teaching_insight": "Ending the course with governance questions helps students see research as a social institution, not just a set of techniques.",
"follow_up": "Draft a one-paragraph institutional AI use policy for a university research office, addressing authorship, disclosure, and verification."
},

# ── 30 additional questions for Quiz Bank breadth ───────────────────────────
{
"number": 30, "session": "S01", "difficulty": "Beginner", "clo": "CLO 1",
"concept": "Types of AI Research Tools",
"question": "Which tool would BEST help a researcher quickly understand the consensus across hundreds of papers on a specific question?",
"options": [
    "Microsoft Word",
    "Consensus.app",
    "Turnitin",
    "Mendeley reference manager"
],
"correct": 1,
"explanation": {
    "concise": "Consensus.app uses AI to extract and aggregate research findings across many papers in response to a question.",
    "detailed": "Consensus.app allows users to enter a research question in natural language and returns a synthesis of how studies across multiple papers answer that question. It surfaces consensus and disagreement. Turnitin is a plagiarism detector, Mendeley is a reference manager, and Word is a word processor — none designed for evidence synthesis.",
    "doctoral_relevance": "Knowing which tool serves which function prevents researchers from using powerful tools inappropriately.",
    "instructor_emphasis": "Demo Consensus.app with a question from the class's research area."
},
"wrong_reasons": [
    "Option A — Word is for writing, not searching.",
    "Option C — Turnitin checks originality, not literature synthesis.",
    "Option D — Mendeley organises references but does not synthesise findings."
],
"teaching_insight": "Matching the right tool to the right task is a foundational research competency.",
"follow_up": "Name three different tasks in research and identify the best AI tool for each."
},

{
"number": 31, "session": "S02", "difficulty": "Beginner", "clo": "CLO 2",
"concept": "Research Topic vs Research Problem",
"question": "What is the difference between a RESEARCH TOPIC and a RESEARCH PROBLEM?",
"options": [
    "There is no difference; they mean the same thing",
    "A research topic is a broad area of interest; a research problem is a specific, researchable issue within that area",
    "A research topic is more specific than a research problem",
    "A research problem is studied only in quantitative research"
],
"correct": 1,
"explanation": {
    "concise": "A topic is a subject area; a problem is a specific, answerable question or issue within that area.",
    "detailed": "'Artificial intelligence in healthcare' is a topic — vast and undirected. 'The effect of AI triage algorithms on emergency department waiting times in tier-2 Indian hospitals' is a research problem — bounded, specific, and researchable. The move from topic to problem requires identifying what is at stake, who is affected, and what remains unknown.",
    "doctoral_relevance": "Proposal committees routinely distinguish between 'interesting area' and 'researchable problem'. Candidates must show they have made this move.",
    "instructor_emphasis": "Give five broad topics and ask students to convert each into a focused research problem in two minutes."
},
"wrong_reasons": [
    "Option A — they are conceptually distinct.",
    "Option C — the reverse is true. Topics are broader.",
    "Option D — research problems exist in all paradigms."
],
"teaching_insight": "This is one of the most foundational distinctions in research methodology.",
"follow_up": "Convert 'sustainability in supply chains' from a topic into a specific research problem."
},

{
"number": 32, "session": "S05", "difficulty": "Advanced", "clo": "CLO 2",
"concept": "PICO Framework",
"question": "In health management research, the PICO framework structures research questions. What does the 'C' stand for, and why does it matter?",
"options": [
    "Context — to specify the setting of the study",
    "Comparison — to define what the intervention is being compared against",
    "Concept — to identify the theoretical framework",
    "Conclusion — to state the expected finding"
],
"correct": 1,
"explanation": {
    "concise": "'C' stands for Comparison — the control or alternative condition against which the intervention is evaluated.",
    "detailed": "In PICO (Population, Intervention, Comparison, Outcome), specifying the comparison clarifies the counterfactual: compared to what is the intervention being evaluated? Without a comparison, the research question cannot establish whether the intervention made a difference. For example: 'Does AI-assisted triage (I) reduce waiting times (O) in emergency departments (P) compared to nurse-led triage (C)?'",
    "doctoral_relevance": "PICO forces precision in question formulation and helps researchers design appropriate comparisons — a common weakness in proposals.",
    "instructor_emphasis": "Work through a full PICO formulation from scratch with the class."
},
"wrong_reasons": [
    "Option A — Context is used in PEO (Population, Exposure, Outcome), a variant for non-experimental questions.",
    "Option C — Concept appears in some qualitative frameworks but not PICO.",
    "Option D — PICO does not include the expected finding. Research questions should not embed the answer."
],
"teaching_insight": "PICO is widely used in health management and evidence-based practice courses — a core tool for this programme.",
"follow_up": "Formulate a PICO question for a study on telehealth AI in rural India."
},

{
"number": 33, "session": "S06", "difficulty": "Advanced", "clo": "CLO 4",
"concept": "Theory Borrowing",
"question": "A management researcher applies Social Exchange Theory to explain AI adoption in healthcare. What caveat is MOST important to address?",
"options": [
    "Social Exchange Theory was not developed for healthcare settings, so its applicability must be argued, not assumed",
    "Social Exchange Theory is outdated and should be replaced by a newer model",
    "The theory only applies to economic transactions, so it cannot be used in this context",
    "Using theory from sociology in a management study is methodologically inappropriate"
],
"correct": 0,
"explanation": {
    "concise": "Theory borrowed from another discipline or context must have its applicability to the new setting explicitly argued.",
    "detailed": "Social Exchange Theory (Blau, 1964; Homans, 1958) was developed to explain reciprocal exchanges in social relationships. Its application to technology adoption in healthcare organisations requires the researcher to argue why the social exchange logic applies — what is being exchanged, between whom, and how the theory's core mechanisms (reciprocity, trust, obligations) operate in the AI-healthcare context. This is not automatic; it must be theorised.",
    "doctoral_relevance": "Reviewers often ask: 'Why this theory?' The answer must go beyond 'it has been used before' to 'here is why its mechanisms apply to my phenomenon.'",
    "instructor_emphasis": "Ask students to map the key concepts of SET onto the AI adoption context explicitly."
},
"wrong_reasons": [
    "Option B — Social Exchange Theory remains widely used and theoretically productive.",
    "Option C — SET was always broader than economic exchange; it covers any social reciprocity.",
    "Option D — Interdisciplinary theory use is standard and valued in management research."
],
"teaching_insight": "The skill of arguing for a theory's applicability, rather than assuming it, marks doctoral-level theoretical literacy.",
"follow_up": "Argue in three sentences why Social Exchange Theory applies to AI adoption in a hospital setting."
},

{
"number": 34, "session": "S10", "difficulty": "Intermediate", "clo": "CLO 6",
"concept": "Informed Consent and AI",
"question": "A researcher uses an AI chatbot to conduct semi-structured interviews with healthcare workers about patient data. What is the PRIMARY ethical concern?",
"options": [
    "Chatbots ask questions too quickly",
    "Participants may not understand that they are talking to an AI, raising consent and transparency concerns",
    "AI chatbots cannot record audio interviews",
    "The findings from AI-conducted interviews are not publishable"
],
"correct": 1,
"explanation": {
    "concise": "Informed consent requires participants to know what they are participating in, including whether they are speaking to a human or an AI.",
    "detailed": "Research ethics frameworks (Belmont Report, APA, AoM) require that participants give informed consent — meaning they understand the nature of the research, who is involved, and how data will be used. Using an AI chatbot without disclosing this deceives participants about the nature of the interaction, which violates the transparency principle. There are also secondary concerns: AI chatbots cannot respond empathetically to distress, cannot detect and respond to coercive dynamics, and may fail to handle sensitive clinical topics appropriately.",
    "doctoral_relevance": "AI-mediated data collection is an emerging area in research ethics. Doctoral students should anticipate IRB/ethics committee questions about AI involvement in data collection.",
    "instructor_emphasis": "Role-play: how would you disclose AI chatbot involvement to a participant without making them withdraw?"
},
"wrong_reasons": [
    "Option A — speed is not the primary ethical concern.",
    "Option C — this is false; AI chatbots can be integrated with recording tools.",
    "Option D — publishability is a separate question; the ethical concern is independent of publication."
],
"teaching_insight": "AI in data collection raises new ethical questions that existing ethics frameworks are still catching up with.",
"follow_up": "Draft a consent form paragraph that discloses the use of an AI chatbot for data collection."
},

{
"number": 35, "session": "S11", "difficulty": "Doctoral Challenge", "clo": "CLO 6",
"concept": "Counterfactual Thinking in AI-Assisted Analysis",
"question": "An AI topic modelling tool identifies five themes in 500 employee survey responses. A doctoral researcher presents these themes as the definitive conceptual structure of employee experience. What critical step is MISSING?",
"options": [
    "The researcher should have used six themes instead of five",
    "The researcher should compare the AI-generated themes against an independent human coding of a subset of responses to assess convergence",
    "The researcher should use a different AI tool to confirm the themes",
    "The researcher should add more survey responses to improve the analysis"
],
"correct": 1,
"explanation": {
    "concise": "AI-generated topic models require validation against human interpretation to assess whether the themes are conceptually coherent and not artefacts of the algorithm.",
    "detailed": "Topic modelling algorithms (LDA, BERTopic, NMF) identify statistical co-occurrence patterns in text. These patterns may or may not correspond to conceptually meaningful categories. A theme that appears coherent statistically may combine ideas that a domain expert would separate, or may split a unified concept across two topics. Human validation — reviewing a sample of the original texts and assessing whether the AI labels capture what the texts are actually saying — is a necessary step.",
    "doctoral_relevance": "Reviewers in qualitative and mixed methods outlets expect evidence that AI-generated analytical categories have been subjected to human interpretive scrutiny.",
    "instructor_emphasis": "Show a topic model output and ask students to evaluate whether each topic makes conceptual sense."
},
"wrong_reasons": [
    "Option A — the number of themes is a methodological choice, not a quality criterion in itself.",
    "Option C — using a second AI tool does not add human interpretive validation.",
    "Option D — sample size improvements are useful but do not address the validation problem."
],
"teaching_insight": "AI analysis is a starting point for interpretation, not the endpoint. This distinction is central to responsible use of AI in qualitative research.",
"follow_up": "Design a validation protocol for AI-generated themes from a large dataset of customer feedback."
},

# Additional questions 36-100 to fill the bank
{
"number": 36, "session": "S04", "difficulty": "Intermediate", "clo": "CLO 3",
"concept": "Risk of Bias Assessment",
"question": "In a systematic review, the risk of bias assessment is conducted to:",
"options": [
    "Identify which studies support the researcher's hypothesis",
    "Evaluate the methodological quality of included studies and flag limitations that affect the confidence in pooled findings",
    "Reduce the number of studies included to make the review manageable",
    "Determine which authors are most trustworthy"
],
"correct": 1,
"explanation": {
    "concise": "Risk of bias tools (e.g., Cochrane RoB, Newcastle-Ottawa) evaluate study quality systematically, informing how much confidence to place in findings.",
    "detailed": "Risk of bias assessment asks: Did the study adequately randomise? Was allocation concealed? Were outcome assessors blinded? Was attrition addressed? These methodological features determine how much confidence we can place in a study's findings. A review that pools findings from high and low quality studies without distinguishing between them may produce a misleading meta-analytic estimate.",
    "doctoral_relevance": "PRISMA 2020 requires risk of bias assessment as a standard component. Reviewers will check for it.",
    "instructor_emphasis": "Walk through the Cochrane RoB-2 or Newcastle-Ottawa Scale for one study from your field."
},
"wrong_reasons": [
    "Option A — cherry-picking studies that support a hypothesis is a form of bias, not bias assessment.",
    "Option C — quality assessment can lead to exclusion of very low quality studies, but reducing number is a consequence, not the purpose.",
    "Option D — author trustworthiness is not a validity criterion."
],
"teaching_insight": "Students often confuse quality assessment with citation count. High citation does not mean high quality.",
"follow_up": "Apply a three-criterion quality checklist to one paper in your research area."
},

{
"number": 37, "session": "S07", "difficulty": "Advanced", "clo": "CLO 5",
"concept": "Measurement Validity",
"question": "A researcher measures 'innovation culture' using the number of patents filed. What type of validity concern does this raise?",
"options": [
    "External validity",
    "Construct validity — the measure may not capture the full conceptual domain of 'innovation culture'",
    "Statistical conclusion validity",
    "Internal validity"
],
"correct": 1,
"explanation": {
    "concise": "Patent count is a narrow proxy for innovation culture — it misses the cognitive, behavioural, and social dimensions of the construct.",
    "detailed": "Construct validity asks: does the measure actually capture what the construct means? Innovation culture is typically defined as shared values, norms, behaviours, and organisational structures that support creative activity. Patent count captures one observable output of innovation, but misses whether employees feel safe to experiment, whether failures are tolerated, and whether leadership models innovative behaviour. Measuring culture by outputs rather than the culture itself is a validity problem.",
    "doctoral_relevance": "Choosing valid indicators for latent constructs is one of the hardest challenges in quantitative management research.",
    "instructor_emphasis": "Ask students: 'What would a perfect measure of innovation culture look like?' The gap between their ideal and the patent measure illustrates the validity problem."
},
"wrong_reasons": [
    "Option A — external validity concerns generalisation to other populations; this is a measurement concern.",
    "Option C — statistical conclusion validity concerns statistical power and error; not the issue here.",
    "Option D — internal validity concerns causal inference design; not the measurement issue."
],
"teaching_insight": "Operationalisation decisions embed theoretical assumptions — a proxy measure is always a theoretical claim.",
"follow_up": "Propose three additional indicators for 'innovation culture' and explain what dimension each captures."
},

{
"number": 38, "session": "S08", "difficulty": "Beginner", "clo": "CLO 5",
"concept": "Purposive Sampling",
"question": "In qualitative research, purposive sampling means:",
"options": [
    "Selecting participants randomly from the population",
    "Selecting participants based on specific characteristics relevant to the research question",
    "Selecting the largest possible number of participants",
    "Selecting participants who volunteer"
],
"correct": 1,
"explanation": {
    "concise": "Purposive sampling deliberately selects information-rich participants based on their relevance to the research question.",
    "detailed": "Unlike probability sampling, which aims for statistical representativeness, purposive sampling aims for information richness. The researcher selects participants who have direct experience with the phenomenon, represent a range of perspectives, or hold particular expertise. In a qualitative study on AI adoption challenges in hospitals, purposive sampling might include: frontline nurses, IT implementation leads, hospital administrators, and patients — each adding a different perspective.",
    "doctoral_relevance": "Justifying sampling choices is essential in qualitative proposals. Reviewers expect clear reasoning for why particular participants are selected.",
    "instructor_emphasis": "Contrast purposive sampling with snowball, maximum variation, and theoretical sampling — all related but distinct."
},
"wrong_reasons": [
    "Option A — that describes probability sampling, which serves different goals.",
    "Option C — qualitative research does not aim for large samples; saturation is the criterion.",
    "Option D — that describes convenience or volunteer sampling, which is less rigorous than purposive."
],
"teaching_insight": "Students often confuse qualitative sampling with quantitative sampling logic. This distinction is fundamental.",
"follow_up": "Design a purposive sampling strategy for a qualitative study on how radiologists experience AI diagnostic tools."
},

{
"number": 39, "session": "S13", "difficulty": "Intermediate", "clo": "CLO 7, 8",
"concept": "Predatory Journals",
"question": "How can a researcher MOST reliably identify whether a journal is predatory?",
"options": [
    "Check whether the journal is listed in Beall's List and cross-verify using DOAJ, Scopus, or ESCI indexing",
    "Check whether the journal charges an article processing charge (APC)",
    "Check whether the journal publishes papers quickly",
    "Check whether the journal is published in English"
],
"correct": 0,
"explanation": {
    "concise": "Predatory journals often mimic legitimate journals. Cross-referencing Beall's List with established indexing databases provides the most reliable check.",
    "detailed": "Predatory journals typically: promise fast peer review, charge APCs without conducting genuine review, mimic the names of legitimate journals, and claim false indexing. Beall's List (archived and mirrored) catalogues known or suspected predatory publishers. DOAJ (Directory of Open Access Journals) lists vetted open access journals. Scopus, Web of Science, and ESCI indexing require journals to meet quality standards. A journal that appears on Beall's List and is absent from all indexing databases is a strong candidate for predatory status.",
    "doctoral_relevance": "Publishing in a predatory journal may permanently damage a researcher's reputation and is often disqualified from promotion and funding evaluations.",
    "instructor_emphasis": "Show Beall's List and walk through how to verify a journal's indexing status using Scopus's source list."
},
"wrong_reasons": [
    "Option B — APCs alone do not indicate predatory status. Many legitimate journals (PLOS, Nature Communications) charge APCs.",
    "Option C — publication speed is one indicator but not conclusive.",
    "Option D — language is irrelevant to journal quality."
],
"teaching_insight": "Predatory journal identification is a practical survival skill for doctoral students submitting their first manuscripts.",
"follow_up": "Check one open-access journal in your field using Beall's List and DOAJ and report your findings."
},

{
"number": 40, "session": "S16", "difficulty": "Intermediate", "clo": "CLO 8",
"concept": "Responsible AI Use in Research",
"question": "A researcher discloses: 'ChatGPT was used to improve the fluency of this manuscript.' This disclosure is:",
"options": [
    "Unnecessary, since AI tools are just like spellcheckers",
    "An appropriate example of transparent AI use disclosure, meeting the emerging standard set by major journals",
    "Damaging — journals will reject papers that used AI",
    "Sufficient only if the entire paper was written by AI"
],
"correct": 1,
"explanation": {
    "concise": "Transparent, specific disclosure of AI use is now required or recommended by most major journals and is the ethical standard.",
    "detailed": "Nature, Elsevier, Springer, and Wiley have all issued AI use policies requiring disclosure of how AI was used in research or writing. The disclosure in Option B is specific (ChatGPT for fluency improvement) and proportionate. It does not claim AI as an author, and it informs readers and editors of the extent of AI involvement. This meets the ethical standard of transparency.",
    "doctoral_relevance": "Understanding and complying with journal AI policies is a publication readiness requirement.",
    "instructor_emphasis": "Share the AI policy of one top journal in your field and discuss what it requires."
},
"wrong_reasons": [
    "Option A — spellcheckers do not generate, restructure, or synthesise text. AI writing tools do, which raises different integrity questions.",
    "Option C — this is false. Journals do not reject papers for disclosed AI use; they require disclosure.",
    "Option D — the disclosure requirement applies whenever AI was used in any meaningful way, not only when it wrote the whole paper."
],
"teaching_insight": "Disclosure norms are evolving. Students who graduate with this understanding will navigate the publishing landscape more effectively.",
"follow_up": "Write an AI use disclosure statement for a paper where AI was used for literature search, initial outlining, and grammar checking."
},

# ── Additional 60 questions (41-100) ────────────────────────────────────────
{
"number": 41, "session": "S01", "difficulty": "Beginner", "clo": "CLO 1",
"concept": "Generative AI vs Search AI",
"question": "What is the key difference between a generative AI tool (like ChatGPT) and an AI-powered search tool (like Semantic Scholar)?",
"options": [
    "Generative AI is free; search AI requires payment",
    "Generative AI creates new text based on training patterns; AI search tools retrieve and rank existing indexed documents",
    "Generative AI is more accurate for academic research",
    "There is no meaningful difference for research purposes"
],
"correct": 1,
"explanation": {
    "concise": "Generative AI produces text; AI search tools locate existing documents. Both are useful but serve very different functions.",
    "detailed": "ChatGPT-type tools generate responses by predicting likely text based on training data — they do not 'know' specific documents. Semantic Scholar, Elicit, and Consensus retrieve actual indexed papers and rank them by relevance. For academic research, this distinction is critical: generative AI can help structure writing, but only search tools can reliably surface real papers.",
    "doctoral_relevance": "Confusing these two types leads to using ChatGPT as a literature search tool — a category error that produces fabricated citations.",
    "instructor_emphasis": "Ask: 'Which tool would you use to find the five most-cited papers on organisational learning?' Then ask why."
},
"wrong_reasons": [
    "Option A — both have free and paid tiers; cost is not the distinction.",
    "Option C — search AI is more reliable for finding specific papers; generative AI may hallucinate.",
    "Option D — there is a fundamental architectural difference with major research implications."
],
"teaching_insight": "This is the single most important conceptual distinction in Session 1.",
"follow_up": "List two research tasks where generative AI is appropriate and two where it would be inappropriate."
},

{
"number": 42, "session": "S02", "difficulty": "Intermediate", "clo": "CLO 2",
"concept": "Gap from Contradiction",
"question": "Two groups of studies reach opposite conclusions on whether remote work increases or decreases productivity. How does a researcher use this contradiction?",
"options": [
    "Average the findings and report the middle ground",
    "Choose the majority finding and ignore the minority",
    "Treat the contradiction as a gap: investigate what moderating variables (context, measure, sample) explain the divergence",
    "Conclude that productivity cannot be studied scientifically"
],
"correct": 2,
"explanation": {
    "concise": "Contradictory findings often signal unexamined moderating variables — an ideal starting point for a new study.",
    "detailed": "When studies disagree, the question is not 'who is right?' but 'under what conditions is each finding correct?' The researcher's contribution may be to identify the boundary condition: perhaps remote work increases productivity for knowledge workers but decreases it for collaborative roles, or for employees with home office space but not for those in shared living situations.",
    "doctoral_relevance": "Meta-analytic moderation analysis and systematic review narratives both use contradiction as a productive research starting point.",
    "instructor_emphasis": "Introduce the term 'boundary conditions' and have students identify one for the remote work example."
},
"wrong_reasons": [
    "Option A — averaging findings without understanding why they differ is methodologically unjustified.",
    "Option B — ignoring minority findings is a form of publication bias.",
    "Option D — methodological nihilism is not a productive scholarly stance."
],
"teaching_insight": "Contradictions are gifts in the literature — they tell you where the interesting work is.",
"follow_up": "Find a contradiction in the literature on your research topic and propose a moderating variable that might explain it."
},

{
"number": 43, "session": "S03", "difficulty": "Beginner", "clo": "CLO 3",
"concept": "Boolean Logic in Search",
"question": "A researcher wants papers on 'machine learning' AND 'health outcomes' but NOT 'clinical trials.' Which Boolean string is correct?",
"options": [
    '"machine learning" OR "health outcomes" NOT "clinical trials"',
    '"machine learning" AND "health outcomes" NOT "clinical trials"',
    '"machine learning" AND "health outcomes" OR "clinical trials"',
    '"machine learning" OR "health outcomes" OR "clinical trials"'
],
"correct": 1,
"explanation": {
    "concise": "AND narrows results to papers containing both terms; NOT excludes papers containing the unwanted term.",
    "detailed": "Boolean operators structure database searches: AND requires both terms to be present (narrows), OR includes either term (broadens), NOT excludes papers with the specified term. The correct string retrieves papers about machine learning in health outcomes while excluding clinical trial papers, which are a different type of study.",
    "doctoral_relevance": "Boolean search is foundational for systematic reviews. Errors in the search string compromise the review's completeness.",
    "instructor_emphasis": "Run the four options in a database (Scopus or PubMed) and show students how different the result counts are."
},
"wrong_reasons": [
    "Option A — OR broadens instead of narrowing, combining machine learning OR health outcomes.",
    "Option C — the OR before 'clinical trials' would include those papers rather than excluding them.",
    "Option D — three ORs maximally broaden the search, retrieving papers on any of the three topics."
],
"teaching_insight": "Boolean logic mistakes are extremely common. A live database demonstration makes the errors concrete.",
"follow_up": "Write a Boolean search string for a review on 'AI in talent management, excluding performance appraisal.'"
},

{
"number": 44, "session": "S04", "difficulty": "Advanced", "clo": "CLO 3",
"concept": "Meta-Analysis vs Narrative Review",
"question": "When is a narrative synthesis MORE appropriate than a meta-analysis?",
"options": [
    "When the researcher wants to pool effect sizes statistically",
    "When studies are too heterogeneous in design, population, or outcome to justify statistical pooling",
    "When there are more than 50 studies available",
    "When the research question is quantitative"
],
"correct": 1,
"explanation": {
    "concise": "Narrative synthesis is appropriate when studies are too diverse to pool meaningfully — heterogeneity in design, sample, or measure makes meta-analysis invalid.",
    "detailed": "Meta-analysis statistically pools effect sizes from multiple studies. This is only valid when studies are sufficiently similar in design, population, intervention, and outcome measure (the clinical and methodological homogeneity criterion). When studies vary substantially — different types of AI, different organisational contexts, different outcome measures — pooling them produces a meaningless average. Narrative synthesis instead summarises and interprets the pattern of findings without statistical combination.",
    "doctoral_relevance": "Choosing between meta-analysis and narrative synthesis must be justified methodologically, not made by default.",
    "instructor_emphasis": "Show a heterogeneity test (I² statistic) from a published meta-analysis and explain what high heterogeneity implies."
},
"wrong_reasons": [
    "Option A — statistical pooling is the rationale for meta-analysis, not narrative synthesis.",
    "Option C — number of studies is not the criterion; heterogeneity is.",
    "Option D — quantitative questions do not automatically require meta-analysis."
],
"teaching_insight": "Many students assume more data always means meta-analysis. This question corrects that assumption.",
"follow_up": "Examine the I² statistic in a published meta-analysis in your field and interpret what it implies for the validity of the pooled estimate."
},

{
"number": 45, "session": "S05", "difficulty": "Intermediate", "clo": "CLO 2",
"concept": "Operationalisation",
"question": "Operationalisation in research means:",
"options": [
    "Explaining how the study will be funded",
    "Defining how abstract constructs will be measured in concrete, observable terms",
    "Writing the operational procedures of the research lab",
    "Identifying which statistical software will be used"
],
"correct": 1,
"explanation": {
    "concise": "Operationalisation translates theoretical constructs into measurable indicators.",
    "detailed": "'Employee engagement' is abstract. Operationalising it means deciding: will I use a validated scale (e.g., UWES)? Which items? How will responses be aggregated? The same applies to 'AI adoption' — does it mean awareness, intention to use, actual use, or proficient use? These decisions determine what the study actually measures, and measurement drives findings.",
    "doctoral_relevance": "Vague operationalisation is a common thesis weakness. Examiners ask: 'How did you measure X?'",
    "instructor_emphasis": "Take one construct from a student's research area and operationalise it together in class."
},
"wrong_reasons": [
    "Option A — funding is not operationalisation.",
    "Option C — lab procedures are a different kind of 'operational.'",
    "Option D — software choice follows from operationalisation; it is not the same thing."
],
"teaching_insight": "Every measurement decision in a study is an operationalisation decision — this concept applies throughout the research process.",
"follow_up": "Operationalise 'research productivity' for a study of faculty members in a business school."
},

{
"number": 46, "session": "S06", "difficulty": "Beginner", "clo": "CLO 4",
"concept": "Grand Theory vs Middle-Range Theory",
"question": "Why do most management researchers prefer middle-range theories over grand theories for empirical research?",
"options": [
    "Grand theories are too old to be relevant",
    "Middle-range theories make specific, testable predictions about bounded phenomena, making them more amenable to empirical investigation",
    "Grand theories are too abstract and are only used in philosophy",
    "Middle-range theories are only used in quantitative research"
],
"correct": 1,
"explanation": {
    "concise": "Middle-range theories specify mechanisms and relationships in bounded contexts, generating testable hypotheses.",
    "detailed": "Grand theories (e.g., systems theory, structuration theory) offer broad explanatory frameworks but are often too abstract to generate specific, testable predictions. Middle-range theories (Merton's term) — like Technology Acceptance Model, Social Exchange Theory, or Signalling Theory — specify which variables, which relationships, and which mechanisms operate in a defined domain. This specificity makes them far more useful for designing empirical studies.",
    "doctoral_relevance": "Choosing and justifying a theoretical framework requires understanding what kind of theory it is and what kind of questions it can answer.",
    "instructor_emphasis": "Give examples of grand theories and their middle-range derivatives in management."
},
"wrong_reasons": [
    "Option A — grand theories are still theoretically relevant; they are just harder to operationalise.",
    "Option C — grand theories are used across social science, not only philosophy.",
    "Option D — middle-range theories are used in qualitative and mixed methods research too."
],
"teaching_insight": "Most students have encountered grand theories without realising they are grand. Naming them helps.",
"follow_up": "Identify one grand theory and one middle-range theory in your research field and explain the difference in what each predicts."
},

{
"number": 47, "session": "S09", "difficulty": "Intermediate", "clo": "CLO 5",
"concept": "Triangulation",
"question": "What does triangulation mean in mixed methods research?",
"options": [
    "Using three researchers to code data independently",
    "Using three statistical tests to confirm a finding",
    "Using multiple methods, sources, or investigators to cross-check findings and build a more complete picture",
    "Mapping findings onto a triangular theoretical framework"
],
"correct": 2,
"explanation": {
    "concise": "Triangulation uses multiple methods or sources to cross-validate findings and provide a richer, more robust account.",
    "detailed": "Denzin (1978) identified four types of triangulation: data (multiple sources), investigator (multiple researchers), theory (multiple frameworks), and methodological (multiple methods). In mixed methods research, triangulation typically refers to using both quantitative and qualitative data on the same phenomenon to see whether they converge. Where they diverge, the divergence itself is informative — it suggests the two methods are capturing different aspects of the phenomenon.",
    "doctoral_relevance": "Triangulation is often cited in proposals as a quality-enhancement strategy, but it must be operationalised specifically, not used as a buzzword.",
    "instructor_emphasis": "Ask: 'If your qualitative and quantitative findings contradict each other, is that a problem or a finding?' The answer is: it is a finding."
},
"wrong_reasons": [
    "Option A — having three coders is inter-rater reliability, not triangulation.",
    "Option B — using three statistical tests is not triangulation; it may increase Type I error.",
    "Option D — there is no standard 'triangular framework' in research methodology."
],
"teaching_insight": "Triangulation is frequently misused in proposals. This question clarifies what it actually means.",
"follow_up": "Design a triangulation strategy for a study on patient satisfaction with AI-assisted diagnosis."
},

{
"number": 48, "session": "S10", "difficulty": "Advanced", "clo": "CLO 6",
"concept": "Algorithmic Bias in Data Collection",
"question": "A researcher uses an AI tool to recruit survey participants through social media algorithms. What is the MOST significant bias concern?",
"options": [
    "Social media platforms are too popular for research",
    "The algorithm may preferentially reach certain demographic groups, creating a non-representative sample without the researcher's awareness",
    "Online surveys are not valid data collection instruments",
    "AI tools cannot recruit research participants"
],
"correct": 1,
"explanation": {
    "concise": "Social media algorithms optimise for engagement, not representativeness — they systematically reach some groups more than others.",
    "detailed": "Recommender algorithms on Facebook, Instagram, or LinkedIn are designed to maximise engagement, not to sample populations representatively. They tend to show content to users who are most likely to interact with it — creating self-selection and algorithmic bias simultaneously. A study that recruits through social media AI may oversample younger, tech-savvy, urban, and English-speaking participants, making findings non-generalisable to the target population.",
    "doctoral_relevance": "Sampling bias is a threat to external validity. Researchers must describe and acknowledge recruitment limitations in their methodology.",
    "instructor_emphasis": "Ask: 'Who is not on social media in your target population?' The answer defines the sampling gap."
},
"wrong_reasons": [
    "Option A — popularity is irrelevant to bias.",
    "Option C — online surveys are a valid and widely published method.",
    "Option D — AI can be used for recruitment; the concern is about the bias it introduces."
],
"teaching_insight": "Digital research methods introduce new forms of bias that traditional sampling texts do not cover.",
"follow_up": "Propose two strategies to reduce algorithmic recruitment bias in a social media-based survey."
},

{
"number": 49, "session": "S12", "difficulty": "Intermediate", "clo": "CLO 7",
"concept": "Academic Paragraph Structure",
"question": "The PEEL structure for academic paragraphs stands for:",
"options": [
    "Purpose, Evidence, Evaluation, Link",
    "Point, Evidence, Explanation, Link",
    "Paragraph, Example, Evidence, Logic",
    "Position, Evidence, Evaluation, Literature"
],
"correct": 1,
"explanation": {
    "concise": "PEEL = Point (claim), Evidence (support), Explanation (why the evidence supports the claim), Link (to the next point or the overall argument).",
    "detailed": "PEEL is a paragraph structure tool widely used in academic writing development. The Point states the paragraph's main claim. Evidence provides specific data, quotations, or findings. Explanation interprets the evidence in relation to the claim — this is where the researcher's voice appears. Link connects the paragraph to the previous or next one, maintaining argument flow.",
    "doctoral_relevance": "Many doctoral students have technically correct paragraphs that lack analytical depth — usually because the Explanation step is missing or superficial.",
    "instructor_emphasis": "Take a student paragraph, label its PEEL components, and identify which are missing."
},
"wrong_reasons": [
    "Option A — 'Evaluation' is not a PEEL element; 'Explanation' is.",
    "Option C — 'Paragraph' and 'Logic' are not PEEL elements.",
    "Option D — 'Position' and 'Literature' are not the standard PEEL definitions."
],
"teaching_insight": "PEEL is simple but powerful — most writing weaknesses can be traced to a missing or underdeveloped PEEL element.",
"follow_up": "Write a PEEL paragraph arguing that AI literacy should be a mandatory research competency."
},

{
"number": 50, "session": "S15", "difficulty": "Intermediate", "clo": "CLO 7",
"concept": "H-index and Research Impact",
"question": "A researcher has an h-index of 12. What does this SPECIFICALLY mean?",
"options": [
    "The researcher has published 12 papers",
    "The researcher has at least 12 papers that have each been cited at least 12 times",
    "The researcher's best paper has been cited 12 times",
    "The researcher is ranked 12th in their field"
],
"correct": 1,
"explanation": {
    "concise": "The h-index of h means the researcher has h papers each with at least h citations.",
    "detailed": "Hirsch (2005) defined the h-index as follows: a scholar has an h-index of h if h of their publications have each been cited at least h times. A researcher with an h-index of 12 has at least 12 papers that have been cited at least 12 times each. Papers beyond h with fewer than h citations, and papers with more than h citations but fewer than the count of papers with ≥h citations, do not affect the index.",
    "doctoral_relevance": "The h-index is used in hiring, promotion, and grant decisions. Understanding it helps doctoral students track their own developing profiles.",
    "instructor_emphasis": "Show students how to find their h-index using Google Scholar, Scopus, or Web of Science."
},
"wrong_reasons": [
    "Option A — publication count is a different metric.",
    "Option C — that would be the maximum citation count, not h-index.",
    "Option D — h-index is not a ranking metric."
],
"teaching_insight": "Every doctoral student should know their h-index by graduation. Introduce this early.",
"follow_up": "Why might two researchers with the same number of publications have very different h-indexes?"
},

# Questions 51–100 (condensed for breadth across all sessions)
{
"number": 51, "session": "S01", "difficulty": "Beginner", "clo": "CLO 1",
"concept": "ResearchRabbit",
"question": "ResearchRabbit is best described as:",
"options": [
    "A plagiarism detection tool",
    "An AI-powered literature discovery tool that visualises citation networks and tracks new papers in a researcher's area",
    "A statistical analysis platform",
    "A reference formatting tool"
],
"correct": 1,
"explanation": {
    "concise": "ResearchRabbit discovers related literature through citation networks and sends alerts when new relevant papers are published.",
    "detailed": "ResearchRabbit allows users to add seed papers, then explores forward and backward citations to surface related work. It generates visual maps of how papers cluster and relate. Its alert feature notifies researchers of new publications matching their interests. This makes it particularly useful for staying current after the initial literature review.",
    "doctoral_relevance": "Staying current with new publications in a fast-moving field (like AI in management) is an ongoing obligation, not a one-time task.",
    "instructor_emphasis": "Demo: add one paper to ResearchRabbit and show the resulting citation graph."
},
"wrong_reasons": [
    "Option A — plagiarism detection is Turnitin, iThenticate.",
    "Option C — statistical platforms are SPSS, R, STATA.",
    "Option D — reference formatting is Zotero, Mendeley."
],
"teaching_insight": "Tool literacy reduces wasted search time and increases discovery coverage.",
"follow_up": "Set up a ResearchRabbit collection for your thesis topic and report on three papers it surfaced that you had not previously found."
},

{
"number": 52, "session": "S02", "difficulty": "Advanced", "clo": "CLO 2",
"concept": "Research Scope",
"question": "Why is narrowing the scope of a research study considered a scholarly strength rather than a limitation?",
"options": [
    "Narrow studies are easier to complete",
    "A narrower scope allows deeper investigation, greater analytical precision, and stronger claims within a defined boundary",
    "Narrow studies have lower word limits",
    "Scope narrowing is required by most journals"
],
"correct": 1,
"explanation": {
    "concise": "Narrow scope enables depth, precision, and defensible claims — broad studies often produce shallow findings that satisfy nobody.",
    "detailed": "Attempting to study AI adoption across all industries, all sizes of organisation, and all national contexts simultaneously produces unfocused findings that cannot be adequately explored in a single study. A narrowly scoped study — AI adoption in mid-sized Indian IT firms — can go deeper, use more focused methods, and produce insights that are genuinely applicable to a defined population.",
    "doctoral_relevance": "Examiners and reviewers value clarity of scope. 'I studied everything' is a research red flag.",
    "instructor_emphasis": "The phrase to teach: 'Say less, mean more.'"
},
"wrong_reasons": [
    "Option A — ease of completion is a practical benefit, not the scholarly justification.",
    "Option C — word limits do not determine scope.",
    "Option D — few journals specify scope narrowing as a formal requirement."
],
"teaching_insight": "Counterintuitive for many students: doing less better is more valuable than doing more poorly.",
"follow_up": "Narrow down 'AI and healthcare' to a scope suitable for a one-year doctoral study."
},

{
"number": 53, "session": "S07", "difficulty": "Beginner", "clo": "CLO 5",
"concept": "Likert Scale",
"question": "A 5-point Likert scale ranging from 'Strongly Disagree' to 'Strongly Agree' is:",
"options": [
    "A nominal scale that categorises respondents",
    "An ordinal scale that captures agreement intensity with ranked but unequal intervals",
    "A ratio scale with a true zero",
    "A continuous scale equivalent to interval measurement"
],
"correct": 1,
"explanation": {
    "concise": "Likert scales are ordinal — they rank responses but cannot guarantee equal psychological distances between scale points.",
    "detailed": "The distance between 'Disagree' and 'Neutral' is not necessarily the same psychological distance as between 'Neutral' and 'Agree.' This is the ordinal-vs-interval debate in scale measurement. In practice, many researchers treat Likert scales as interval (using means and standard deviations), but the theoretical basis for this is contested. The distinction matters when choosing statistical analyses.",
    "doctoral_relevance": "Whether to treat Likert data as ordinal or interval has methodological implications for choosing parametric vs non-parametric tests.",
    "instructor_emphasis": "Discuss the ongoing debate: Stevens (1946) strict ordinal view vs modern pragmatic interval treatment."
},
"wrong_reasons": [
    "Option A — nominal scales have no order (e.g., gender, nationality).",
    "Option C — ratio scales have a true zero (e.g., income, age).",
    "Option D — interval measurement requires equal intervals, which Likert scales cannot guarantee."
],
"teaching_insight": "This question opens a productive methodological discussion that connects to later choices in data analysis.",
"follow_up": "If you treat Likert data as ordinal, which statistical test would you use instead of a t-test?"
},

{
"number": 54, "session": "S08", "difficulty": "Intermediate", "clo": "CLO 5",
"concept": "Member Checking",
"question": "Member checking in qualitative research involves:",
"options": [
    "Checking that all team members have contributed equally",
    "Sharing interpretations or transcripts with participants to verify that the researcher's account reflects their experience",
    "Cross-checking data between two qualitative researchers",
    "Verifying that the correct number of members were sampled"
],
"correct": 1,
"explanation": {
    "concise": "Member checking returns interpretations to participants to confirm they accurately represent participants' meanings — a key credibility strategy.",
    "detailed": "Lincoln and Guba (1985) proposed member checking as a credibility technique in qualitative research. By sharing findings (summaries, themes, or interpretations) with participants, the researcher allows them to confirm, correct, or extend the account. This does not mean participants always agree — disagreement can itself be informative. Member checking is distinct from inter-rater reliability, which is a quantitative concept.",
    "doctoral_relevance": "Qualitative rigour criteria (credibility, transferability, dependability, confirmability) replace internal and external validity. Member checking addresses credibility.",
    "instructor_emphasis": "Role-play a member checking conversation: researcher presents a theme, participant pushes back. How does the researcher respond?"
},
"wrong_reasons": [
    "Option A — team equity is a different concern.",
    "Option C — checking between researchers is inter-rater reliability or peer debriefing.",
    "Option D — sample size verification is not member checking."
],
"teaching_insight": "Qualitative rigour criteria are often misunderstood as equivalents of quantitative validity. This question clarifies the distinction.",
"follow_up": "Describe how you would conduct member checking for a thematic analysis of senior leader interviews."
},

{
"number": 55, "session": "S11", "difficulty": "Intermediate", "clo": "CLO 6",
"concept": "Effect Size",
"question": "Why is reporting effect size MORE informative than reporting only p-values?",
"options": [
    "Effect sizes are easier to calculate than p-values",
    "P-values tell you whether a result is statistically significant; effect sizes tell you how large or meaningful the difference or relationship is",
    "Effect sizes replace the need for hypothesis testing",
    "Journal reviewers do not accept p-values anymore"
],
"correct": 1,
"explanation": {
    "concise": "P-values are affected by sample size; effect sizes measure the magnitude of the finding independent of sample size.",
    "detailed": "With a very large sample (n=10,000), even a trivial difference (d=0.01) can be statistically significant (p<0.05). Effect sizes (Cohen's d, Pearson's r, η²) quantify how large the difference or association is, independently of sample size. A statistically significant finding with a tiny effect size may have no practical significance. The APA manual now recommends reporting effect sizes for all primary findings.",
    "doctoral_relevance": "Top management journals routinely require effect size reporting. Studies that only report p-values are increasingly considered methodologically incomplete.",
    "instructor_emphasis": "Show a study with n=5000, p=0.001, d=0.05 and ask: does this finding matter practically?"
},
"wrong_reasons": [
    "Option A — effect sizes are not necessarily easier; some (partial η²) require additional calculation.",
    "Option C — effect sizes complement hypothesis testing; they do not replace it.",
    "Option D — p-values are still used and reported alongside effect sizes in most journals."
],
"teaching_insight": "The shift from p-value-only reporting to effect-size-inclusive reporting is one of the most important methodological developments in social science.",
"follow_up": "Interpret these three findings using Cohen's conventions: d=0.15, d=0.45, d=0.90."
},

{
"number": 56, "session": "S12", "difficulty": "Advanced", "clo": "CLO 7",
"concept": "Argument Structure in a Discussion Section",
"question": "In the discussion section of a research paper, the researcher's PRIMARY task is to:",
"options": [
    "Repeat the results in plain English",
    "Introduce new data collected after the study",
    "Interpret findings in relation to existing theory and literature, and explain what the results mean for knowledge and practice",
    "Describe the research methodology in more detail"
],
"correct": 2,
"explanation": {
    "concise": "The discussion moves from 'what we found' to 'what it means' — interpretation, not description, is the central task.",
    "detailed": "The results section presents findings. The discussion asks: Do these findings confirm, extend, or contradict existing theory? What mechanisms might explain unexpected findings? What do the results mean for practitioners? What are the theoretical implications? A discussion that only restates results adds no intellectual value. The best discussions connect empirical findings to theoretical debates and suggest directions for future research.",
    "doctoral_relevance": "Discussion sections reveal whether a researcher understands their own findings. Examiners pay close attention to the quality of interpretation.",
    "instructor_emphasis": "Annotate the discussion section of a published paper: highlight where the authors interpret, where they connect to theory, and where they suggest implications."
},
"wrong_reasons": [
    "Option A — repetition without interpretation adds nothing.",
    "Option B — introducing new data in the discussion violates standard research paper structure.",
    "Option D — methodology belongs in the methods section."
],
"teaching_insight": "Many students write discussions that describe rather than interpret — this question makes the distinction explicit.",
"follow_up": "Take one finding from a paper in your field and write a three-sentence interpretation that connects it to a specific theory."
},

{
"number": 57, "session": "S14", "difficulty": "Intermediate", "clo": "CLO 7",
"concept": "Reviewer Comments",
"question": "A reviewer writes: 'The theoretical framework is underdeveloped.' What does this MOST likely mean?",
"options": [
    "The paper uses too many theories",
    "The chosen theory is not explained thoroughly enough, or its connection to the research questions and hypotheses is not clearly argued",
    "The paper should use a different theory",
    "Theories are not needed in empirical research"
],
"correct": 1,
"explanation": {
    "concise": "Underdeveloped theory usually means the mechanism linking theory to study variables is not clearly articulated.",
    "detailed": "Reviewers mean different things by 'underdeveloped,' but the most common interpretation is: (a) the theory is mentioned but not explained, (b) the theory is explained but not connected to the specific hypotheses or questions, or (c) the theory is used but its application to the context is not justified. The fix is to add a paragraph that explicitly maps the theory's core constructs to the study variables and explains why the theory predicts the proposed relationships.",
    "doctoral_relevance": "Responding to 'underdeveloped framework' comments requires understanding what the reviewer is asking for — not just adding more text about the theory.",
    "instructor_emphasis": "Role-play: researcher receives this comment and must decide what to write in revision."
},
"wrong_reasons": [
    "Option A — too many theories is a different critique ('theoretical overload').",
    "Option C — the reviewer does not necessarily want a different theory; they want better use of the chosen one.",
    "Option D — empirical research requires theoretical grounding; this view is incorrect."
],
"teaching_insight": "Learning to decode reviewer language is a practical publication skill that students rarely encounter before their first submission.",
"follow_up": "Write a one-paragraph response to the reviewer comment 'the theoretical framework is underdeveloped' for a study using Technology Acceptance Model."
},

{
"number": 58, "session": "S16", "difficulty": "Doctoral Challenge", "clo": "CLO 1, 8",
"concept": "AI and Peer Review",
"question": "A journal uses AI to screen manuscripts for novelty and methodological quality before sending to human reviewers. What is the MOST significant concern?",
"options": [
    "AI reviews manuscripts too quickly",
    "The AI may systematically penalise research that uses methods or frameworks underrepresented in its training data, creating algorithmic gatekeeping",
    "Authors will try to write for the AI rather than for the field",
    "Human reviewers will become unnecessary"
],
"correct": 1,
"explanation": {
    "concise": "AI screeners trained on existing literature may penalise genuinely novel approaches, methods, or voices that diverge from the mainstream.",
    "detailed": "AI screening tools learn what 'quality' looks like from existing literature. But existing literature reflects historical publication biases: toward quantitative methods, Western samples, and established theoretical frameworks. Research using indigenous epistemologies, novel qualitative methods, or non-Western theoretical frameworks may be scored lower — not because they are low quality, but because they do not match the training distribution. This creates an algorithmic conservatism that could suppress innovation.",
    "doctoral_relevance": "This is an emerging institutional concern that doctoral graduates entering the academy will need to engage with and potentially advocate against.",
    "instructor_emphasis": "Discuss: should AI be used in peer review at all? What governance structures would you recommend?"
},
"wrong_reasons": [
    "Option A — speed is not the primary concern with AI peer review.",
    "Option C — strategic writing for AI is a secondary concern; the systemic bias concern is more significant.",
    "Option D — human reviewers will not become unnecessary in the foreseeable future; AI assists, not replaces."
],
"teaching_insight": "AI in peer review is happening now. Students who understand the implications can engage in scholarly conversations about governance.",
"follow_up": "Draft two recommendations for a journal editorial board considering AI screening tools, addressing both efficiency and equity concerns."
},

{
"number": 59, "session": "S09", "difficulty": "Beginner", "clo": "CLO 5",
"concept": "Explanatory Sequential Design",
"question": "In an explanatory sequential mixed methods design, which strand comes FIRST?",
"options": [
    "Qualitative",
    "Quantitative",
    "Both strands simultaneously",
    "Either, depending on the research question"
],
"correct": 1,
"explanation": {
    "concise": "In explanatory sequential design, quantitative data is collected first, then qualitative data is collected to explain the quantitative results.",
    "detailed": "The logic of explanatory sequential design: collect and analyse quantitative data, identify patterns or surprising findings that need explanation, then collect qualitative data specifically to understand why those quantitative findings occurred. This is useful when a quantitative study produces unexpected results, significant subgroup differences, or findings that require contextual understanding.",
    "doctoral_relevance": "Naming and justifying the mixed methods design type is expected in doctoral proposals.",
    "instructor_emphasis": "Contrast with exploratory sequential (qual→quant) and convergent parallel (both simultaneously)."
},
"wrong_reasons": [
    "Option A — qualitative first describes exploratory sequential design.",
    "Option C — simultaneous collection describes convergent parallel design.",
    "Option D — in this specific design type, the sequence is fixed by the design name."
],
"teaching_insight": "Mixed methods design names encode the logic and sequence of the study. Students should know the three major types.",
"follow_up": "Describe a research scenario that would justify an explanatory sequential design."
},

{
"number": 60, "session": "S13", "difficulty": "Advanced", "clo": "CLO 8",
"concept": "Research Integrity — Fabrication",
"question": "Data fabrication in research means:",
"options": [
    "Collecting data from participants who were not properly consented",
    "Creating or making up data that was never actually collected",
    "Reporting data in a different order than it was collected",
    "Using data from a previous study without citation"
],
"correct": 1,
"explanation": {
    "concise": "Fabrication means inventing data — recording data as collected when it was not.",
    "detailed": "Fabrication is among the most serious forms of research misconduct. It includes making up participant responses, creating fictional datasets, and reporting analyses of data that never existed. It is distinct from falsification (manipulating real data to change results) and from other forms of misconduct. The consequences include retraction, institutional investigation, funding loss, and career termination.",
    "doctoral_relevance": "Understanding the definitions of FFP (Fabrication, Falsification, Plagiarism) is a basic research integrity requirement.",
    "instructor_emphasis": "Discuss the Diederik Stapel case (social psychology) or the Hwang Woo-suk case (stem cell research) as famous fabrication cases."
},
"wrong_reasons": [
    "Option A — consent issues are a different ethical violation (informed consent breach).",
    "Option C — ordering data differently is not fabrication (though selective reporting is a related concern).",
    "Option D — using uncited data from a prior study may be self-plagiarism, not fabrication."
],
"teaching_insight": "Students often conflate different forms of research misconduct. Clear definitions matter.",
"follow_up": "Distinguish between fabrication, falsification, and plagiarism in your own words, with one example of each."
},

# Questions 61-100 — compressed with full structure
{
"number": 61, "session": "S01", "difficulty": "Advanced", "clo": "CLO 1",
"concept": "AI Limitations in Scientific Reasoning",
"question": "Which task is a large language model LEAST equipped to perform reliably in a research context?",
"options": [
    "Summarising the structure of a paper",
    "Generating plausible-sounding but unverified citations",
    "Identifying logical inconsistencies across a complex theoretical argument spanning multiple disciplines",
    "Suggesting related search terms for a literature review"
],
"correct": 2,
"explanation": {
    "concise": "Deep logical reasoning across complex, multi-disciplinary theoretical arguments is currently a significant weakness of LLMs.",
    "detailed": "LLMs excel at pattern completion, stylistic imitation, and retrieval of likely information. They struggle with deep logical consistency checking — especially when an argument spans multiple disciplines with different conceptual vocabularies and when detecting subtle non sequiturs requires genuine domain expertise. This is precisely the task required in doctoral theoretical framework evaluation.",
    "doctoral_relevance": "Doctoral scholars should not outsource their theoretical reasoning to AI tools. Critical evaluation of argument coherence remains a human responsibility.",
    "instructor_emphasis": "Test this live: ask an AI to evaluate the logical consistency of a complex theoretical argument and note its limitations."
},
"wrong_reasons": [
    "Option A — structure summarisation is well within current LLM capability.",
    "Option B — this is actually something LLMs do too readily, not a limitation.",
    "Option D — term suggestion is a strength, not a weakness."
],
"teaching_insight": "Knowing what AI cannot do is as important as knowing what it can do.",
"follow_up": "Name two other tasks where LLM limitations create significant risks for scholarly work."
},

{
"number": 62, "session": "S03", "difficulty": "Intermediate", "clo": "CLO 3",
"concept": "Reference Saturation",
"question": "In qualitative research, theoretical saturation means:",
"options": [
    "You have read all papers on the topic",
    "New data or literature is no longer producing new concepts or themes",
    "Your reference list contains 100 or more citations",
    "You have achieved a balance of old and new references"
],
"correct": 1,
"explanation": {
    "concise": "Saturation occurs when additional data or literature no longer yields new theoretical insights.",
    "detailed": "In grounded theory (Glaser & Strauss, 1967), theoretical saturation is reached when new interviews or data do not generate new categories or theoretical insights. In literature review contexts, saturation means additional searching does not surface new themes or arguments. This is a methodological criterion for stopping, not an arbitrary number.",
    "doctoral_relevance": "Examiners sometimes ask: 'How did you know when to stop collecting data?' Saturation is the principled answer.",
    "instructor_emphasis": "Distinguish between saturation as a stopping criterion and saturation as a quality criterion."
},
"wrong_reasons": [
    "Option A — you rarely read all papers; saturation is about conceptual coverage, not exhaustion.",
    "Option C — reference count is a quantity measure, not saturation.",
    "Option D — old/new balance is not the meaning of saturation."
],
"teaching_insight": "Saturation is frequently cited but poorly understood. This question clarifies the concept.",
"follow_up": "How would you practically determine whether you have reached saturation in a qualitative study with 18 participants?"
},

{
"number": 63, "session": "S04", "difficulty": "Beginner", "clo": "CLO 3",
"concept": "Grey Literature",
"question": "Grey literature in a systematic review refers to:",
"options": [
    "Papers published in journals with grey covers",
    "Unpublished, informally published, or non-peer-reviewed sources such as government reports, white papers, and conference proceedings",
    "Literature that is outdated and no longer relevant",
    "Papers in languages other than English"
],
"correct": 1,
"explanation": {
    "concise": "Grey literature is scholarly or policy-relevant output that falls outside traditional peer-reviewed journal publishing.",
    "detailed": "Grey literature includes: government and NGO reports, working papers, preprints, conference proceedings, theses, policy briefs, and industry reports. It matters in systematic reviews because peer-reviewed literature tends to overrepresent statistically significant positive findings (publication bias). Grey literature, which includes null findings and negative results, can provide a more balanced picture.",
    "doctoral_relevance": "PRISMA guidelines include grey literature search as a component of comprehensive systematic reviews.",
    "instructor_emphasis": "Show students where to find grey literature: SSRN, arXiv, OECD iLibrary, government websites."
},
"wrong_reasons": [
    "Option A — cover colour is irrelevant.",
    "Option C — grey literature is not defined by age.",
    "Option D — non-English literature is also grey if unpublished, but that is not the definition."
],
"teaching_insight": "Grey literature search is skipped by most students — but it is a systematic review quality indicator.",
"follow_up": "Name three types of grey literature relevant to a review on AI governance in healthcare."
},

{
"number": 64, "session": "S05", "difficulty": "Advanced", "clo": "CLO 2",
"concept": "Research Question Scope",
"question": "Which research question is BEST scoped for a single doctoral study?",
"options": [
    "How does technology affect society?",
    "What is the relationship between AI-assisted performance feedback and subsequent goal-setting behaviour among mid-level managers in Indian IT firms?",
    "Does AI improve everything in organisations?",
    "Why do organisations use AI?"
],
"correct": 1,
"explanation": {
    "concise": "A well-scoped question specifies the phenomenon, the population, the context, and the relationship under investigation.",
    "detailed": "Option B does four things: specifies the AI application (AI-assisted performance feedback), the outcome (goal-setting behaviour), the population (mid-level managers), and the context (Indian IT firms). This question is bounded enough to be answered in a single study with appropriate methods, yet specific enough to generate a meaningful contribution.",
    "doctoral_relevance": "Scope is a common weakness in proposals. A well-scoped question signals methodological maturity.",
    "instructor_emphasis": "Annotate Option B: circle the phenomenon, underline the outcome, box the population, highlight the context."
},
"wrong_reasons": [
    "Option A — 'technology' and 'society' are too broad for any single study.",
    "Option C — 'everything' is not a research question.",
    "Option D — 'why do organisations use AI?' without population or context is too broad."
],
"teaching_insight": "Teaching students to add specificity at each dimension (phenomenon, outcome, population, context) is a practical scoping technique.",
"follow_up": "Diagnose what is missing from this question and add the missing element: 'Does AI training improve performance?'"
},

{
"number": 65, "session": "S06", "difficulty": "Doctoral Challenge", "clo": "CLO 4",
"concept": "Theory Building vs Theory Testing",
"question": "What is the FUNDAMENTAL difference between inductive theory building and deductive theory testing in research?",
"options": [
    "Inductive research uses questionnaires; deductive research uses interviews",
    "Inductive reasoning moves from specific observations to general theory; deductive reasoning tests theory-derived predictions against data",
    "Inductive research is qualitative; deductive research is quantitative",
    "Inductive research is exploratory; deductive research is confirmatory only"
],
"correct": 1,
"explanation": {
    "concise": "Induction builds theory from data; deduction tests theoretical predictions against data — the direction of reasoning differs fundamentally.",
    "detailed": "Induction: researcher observes patterns in data → generates theoretical propositions. Deduction: researcher derives hypotheses from existing theory → tests hypotheses against data. These represent fundamentally different epistemological logics and relate to but do not determine the choice of qualitative vs quantitative methods. Induction is more common in qualitative research but can be used with quantitative data (e.g., data mining). Deduction is more common with quantitative data but can appear in qualitative research (e.g., deductive thematic analysis using a pre-existing framework).",
    "doctoral_relevance": "The induction/deduction distinction underpins the philosophical positioning chapter in a doctoral thesis.",
    "instructor_emphasis": "Use a diagram: theory at the top, data at the bottom, arrows going up (induction) and down (deduction)."
},
"wrong_reasons": [
    "Option A — method type does not determine inductive vs deductive logic.",
    "Option C — partly true but not the definition. Deductive qualitative research is a recognised approach.",
    "Option D — deductive research can be confirmatory but can also be explanatory."
],
"teaching_insight": "This distinction is foundational but frequently simplified. Doctoral-level understanding goes beyond 'qual=inductive, quant=deductive.'",
"follow_up": "Give an example of deductive reasoning in qualitative research."
},

{
"number": 66, "session": "S07", "difficulty": "Intermediate", "clo": "CLO 5",
"concept": "Common Method Bias",
"question": "Common method bias (CMB) is MOST likely to be a concern when:",
"options": [
    "Both the predictor and outcome variables are collected from the same source in the same survey at the same time",
    "The survey uses validated scales from previous research",
    "The sample size is very large",
    "The researcher collects data in multiple waves"
],
"correct": 0,
"explanation": {
    "concise": "CMB inflates correlations when both IV and DV are measured from the same respondent in the same instrument — a key threat in survey research.",
    "detailed": "When respondents answer questions about both the predictor (e.g., perceived AI fairness) and the outcome (e.g., trust in management) in the same survey session, their responses may be influenced by social desirability, consistency motives, or mood — inflating the apparent correlation between variables. This is Podsakoff et al.'s (2003) critique. Remedies include: temporal separation, multiple data sources, procedural remedies (scale separation), and statistical remedies (Harman's single-factor test, though this is widely criticised).",
    "doctoral_relevance": "CMB is a standard reviewer concern in survey-based management research. Proposals must address it.",
    "instructor_emphasis": "Explain Harman's single-factor test and why it is considered insufficient on its own."
},
"wrong_reasons": [
    "Option B — validated scales reduce measurement error but do not eliminate CMB.",
    "Option C — large samples increase power but do not reduce CMB.",
    "Option D — multiple waves (time-lagged design) is actually a remedy for CMB."
],
"teaching_insight": "Most students have never heard of CMB before doctoral study. It is one of the most frequently raised issues in management research review.",
"follow_up": "Design a study on AI fairness and employee trust that minimises CMB through a time-lagged data collection strategy."
},

{
"number": 67, "session": "S08", "difficulty": "Advanced", "clo": "CLO 5",
"concept": "Reflexivity in Qualitative Research",
"question": "Reflexivity in qualitative research requires researchers to:",
"options": [
    "Remain completely neutral and objective throughout the study",
    "Actively acknowledge and account for how their background, assumptions, and positionality shape the research process and interpretations",
    "Reflect on whether the study was completed on time",
    "Review literature to check that no similar studies exist"
],
"correct": 1,
"explanation": {
    "concise": "Reflexivity requires ongoing critical examination of how the researcher's identity and assumptions shape the research — it is not neutrality, but transparent engagement.",
    "detailed": "All researchers bring assumptions, experiences, and identity positions to their work. A qualitative researcher who has experienced AI bias may interpret interview data differently from one who has not. Reflexivity does not ask researchers to eliminate these influences — that is impossible — but to name, examine, and account for them in the methodological narrative. Positionality statements, research journals, and member checking all support reflexive practice.",
    "doctoral_relevance": "Reflexivity statements are now expected in qualitative doctoral theses and many qualitative journals.",
    "instructor_emphasis": "Ask students to write a positionality statement for their own research topic — a personal, specific account of how their background shapes their approach."
},
"wrong_reasons": [
    "Option A — complete neutrality is a positivist ideal that qualitative research explicitly rejects.",
    "Option C — reflection on time management is not research reflexivity.",
    "Option D — that describes gap analysis in literature review."
],
"teaching_insight": "Writing a positionality statement is a practical skill that many students find personally challenging — make space for this.",
"follow_up": "Write a three-sentence positionality statement for a qualitative study on AI in healthcare from your own perspective."
},

{
"number": 68, "session": "S10", "difficulty": "Beginner", "clo": "CLO 6",
"concept": "Research Ethics Approval",
"question": "When MUST a researcher seek ethics committee (IRB/IEC) approval?",
"options": [
    "Only when the study involves medical procedures",
    "When the research involves human participants, their data, or any activity that could affect their welfare",
    "Only when the study involves children",
    "Only when the research is funded by a government body"
],
"correct": 1,
"explanation": {
    "concise": "Any research involving human participants or their data requires ethics review — not just medical or child-related research.",
    "detailed": "Ethics committee review is required for any research involving human participants: surveys, interviews, observations, secondary data analysis of personal data, and AI-mediated data collection. The three Belmont principles (respect for persons, beneficence, justice) apply to all research with human subjects. Management, education, and AI research all require ethics review.",
    "doctoral_relevance": "Submitting a dissertation or paper without evidence of ethics approval is a serious procedural problem. Many journals require ethics statement disclosure.",
    "instructor_emphasis": "Walk students through your institution's ethics approval process for a hypothetical survey study."
},
"wrong_reasons": [
    "Option A — medical procedures are one context; ethics review is broader.",
    "Option C — children require additional protections but are not the only population requiring ethics review.",
    "Option D — funding source does not determine ethics review requirements."
],
"teaching_insight": "Many management researchers incorrectly assume ethics review is only for medical research.",
"follow_up": "Identify the ethics review categories at your institution and determine which category a survey study on AI and wellbeing would fall under."
},

{
"number": 69, "session": "S11", "difficulty": "Intermediate", "clo": "CLO 6",
"concept": "Grounded Theory Analysis",
"question": "In grounded theory, the constant comparative method means:",
"options": [
    "Comparing your study to previous studies at each stage",
    "Continuously comparing new data to existing codes and categories to refine and develop theory",
    "Comparing results between two different grounded theory studies",
    "Using a constant (fixed) analytical framework throughout the study"
],
"correct": 1,
"explanation": {
    "concise": "Constant comparison is the analytic engine of grounded theory — new data is always compared to existing categories, driving theoretical development.",
    "detailed": "Glaser and Strauss (1967) described constant comparison as the process of: comparing incident to incident → forming categories → comparing incidents to categories → comparing category to category. This iterative comparison generates increasingly abstract theoretical concepts. It is why grounded theory and data collection happen simultaneously — new data refines the emerging theory.",
    "doctoral_relevance": "Students claiming to use grounded theory must demonstrate constant comparison, theoretical sampling, and memo writing — not just labelling themes.",
    "instructor_emphasis": "Walk through a three-stage constant comparison with a small sample of interview quotes."
},
"wrong_reasons": [
    "Option A — that describes literature positioning, not the analytic method.",
    "Option C — comparing between separate grounded theory studies is a different activity.",
    "Option D — grounded theory is fundamentally anti-fixed-framework in its original form."
],
"teaching_insight": "Grounded theory is one of the most frequently misapplied methods. Many students use the label without the method.",
"follow_up": "Describe in three steps how you would apply constant comparison to interview data on AI adoption in hospitals."
},

{
"number": 70, "session": "S15", "difficulty": "Advanced", "clo": "CLO 7",
"concept": "Predatory Conferences",
"question": "How can a researcher identify a predatory conference?",
"options": [
    "Conferences with high registration fees are always predatory",
    "Predatory conferences often have vague scope, guarantee acceptance, charge high fees without offering genuine peer review, and mimic legitimate conference names",
    "Online conferences are typically predatory",
    "Conferences not held in major cities are predatory"
],
"correct": 1,
"explanation": {
    "concise": "Predatory conferences mimic legitimacy while providing no genuine peer review — they collect fees without scholarly gatekeeping.",
    "detailed": "Warning signs include: spam email invitations, vague multidisciplinary scope, guaranteed or rapid acceptance without substantive review, implausible keynote speaker lists, proceedings published in non-indexed volumes, and misleadingly similar names to legitimate conferences (e.g., 'International Conference on Business and Management' vs AAOM). Check the conference against established indexes (AOM, EURAM, AIS) and look for previous proceedings in Scopus.",
    "doctoral_relevance": "A predatory conference publication carries no scholarly weight and may raise questions about a candidate's judgement.",
    "instructor_emphasis": "Show an example of a predatory conference email invitation and walk through the warning signs."
},
"wrong_reasons": [
    "Option A — registration fees alone are not a determinant. Major conferences (Academy of Management) are expensive.",
    "Option C — online conferences are now mainstream and many are legitimate.",
    "Option D — geography is not a quality criterion."
],
"teaching_insight": "Doctoral students receive many predatory conference invitations. Teaching them to identify these protects their scholarly development.",
"follow_up": "Evaluate one conference invitation you have received (or a hypothetical one) using three of the criteria above."
},

# Questions 71-100: rapid-fire with full structure
{
"number": 71, "session": "S02", "difficulty": "Beginner", "clo": "CLO 2",
"concept": "CRAAP Test",
"question": "The CRAAP test for evaluating sources stands for:",
"options": [
    "Currency, Relevance, Authority, Accuracy, Purpose",
    "Content, Research, Analysis, Application, Publication",
    "Clarity, Reliability, Authority, Accessibility, Purpose",
    "Citation, Reference, Authority, Accuracy, Peer review"
],
"correct": 0,
"explanation": {
    "concise": "CRAAP = Currency (how recent), Relevance (to the research question), Authority (expertise of the author), Accuracy (evidence and citations), Purpose (intent of the source).",
    "detailed": "The CRAAP test is a practical framework for source evaluation: Currency asks when the source was published. Relevance asks how closely it relates to the topic. Authority asks about the author's credentials. Accuracy asks whether the information is supported by evidence. Purpose asks why the source was created — to inform, persuade, sell, or entertain.",
    "doctoral_relevance": "Critical source evaluation is a required skill in doctoral study, especially when AI tools surface diverse and mixed-quality sources.",
    "instructor_emphasis": "Apply the CRAAP test to three sources in class: one excellent, one borderline, one weak."
},
"wrong_reasons": [
    "Option B — none of these are CRAAP criteria.",
    "Option C — 'Clarity' and 'Accessibility' are not CRAAP criteria.",
    "Option D — 'Citation' and 'Peer review' are not CRAAP criteria (though related)."
],
"teaching_insight": "A simple, memorable framework sticks. CRAAP is practical for students evaluating AI-surfaced sources quickly.",
"follow_up": "Apply the CRAAP test to one AI-suggested source from your research area."
},

{
"number": 72, "session": "S07", "difficulty": "Advanced", "clo": "CLO 5",
"concept": "Multicollinearity",
"question": "In regression analysis, multicollinearity occurs when:",
"options": [
    "The sample size is too small for the number of variables",
    "Two or more predictor variables are highly correlated with each other, making it difficult to isolate their individual effects on the outcome",
    "The outcome variable is normally distributed",
    "The researcher uses too many control variables"
],
"correct": 1,
"explanation": {
    "concise": "Multicollinearity: high correlation between predictors inflates standard errors, making individual coefficient estimates unstable.",
    "detailed": "When predictors share substantial variance, the regression model cannot reliably separate their individual contributions. Variance Inflation Factor (VIF) is the standard diagnostic: VIF > 10 (or > 5 in conservative guidelines) indicates problematic multicollinearity. Remedies include combining correlated predictors, using PCA, removing a predictor, or increasing sample size.",
    "doctoral_relevance": "VIF reporting is expected in quantitative management papers. Reviewers will ask whether multicollinearity was checked.",
    "instructor_emphasis": "Show a VIF output from a regression analysis and interpret the values."
},
"wrong_reasons": [
    "Option A — small sample is a power issue, not multicollinearity.",
    "Option C — normality of outcome is an assumption, not multicollinearity.",
    "Option D — too many controls can exacerbate multicollinearity but is not the definition."
],
"teaching_insight": "Many students run regressions without checking VIF. This question motivates the diagnostic habit.",
"follow_up": "If two predictors have a correlation of r=0.85, what VIF would you expect, and how would you respond?"
},

{
"number": 73, "session": "S08", "difficulty": "Beginner", "clo": "CLO 5",
"concept": "Open vs Closed Coding",
"question": "In the first stage of grounded theory coding, open coding involves:",
"options": [
    "Applying a pre-existing coding framework to data",
    "Examining data closely and labelling all ideas, events, and phenomena without prior assumptions",
    "Counting the frequency of words in the data",
    "Identifying only negative cases in the data"
],
"correct": 1,
"explanation": {
    "concise": "Open coding is exploratory and inductive — the researcher approaches data without a predetermined framework, labelling what is there.",
    "detailed": "In Strauss and Corbin's grounded theory, open coding is the first analytic pass: the researcher reads data line by line (sometimes word by word), asks 'What is happening here?' and assigns codes to all potentially relevant content. There is no prior framework; codes emerge from the data. This is distinct from axial coding (finding relationships between codes) and selective coding (building the core category).",
    "doctoral_relevance": "Open coding requires genuine engagement with data — not template-filling. It is cognitively demanding and takes longer than students expect.",
    "instructor_emphasis": "Demonstrate open coding live with a short paragraph of interview data."
},
"wrong_reasons": [
    "Option A — applying a pre-existing framework is deductive coding, not open coding.",
    "Option C — word frequency counts are quantitative content analysis, not open coding.",
    "Option D — negative case analysis is a validation strategy, not open coding."
],
"teaching_insight": "The difference between open and deductive coding is practically important — starting with a framework versus letting the framework emerge are fundamentally different processes.",
"follow_up": "Open-code this sentence: 'I trust the AI system but I'm nervous about what it does with my data.'"
},

{
"number": 74, "session": "S12", "difficulty": "Intermediate", "clo": "CLO 7",
"concept": "Transition Sentences",
"question": "What is the purpose of a transition sentence between paragraphs?",
"options": [
    "To introduce a new citation",
    "To signal the argument's movement while maintaining logical coherence between ideas",
    "To begin a new section with a heading",
    "To summarise the entire paper so far"
],
"correct": 1,
"explanation": {
    "concise": "Transitions show readers how ideas connect — they make the argument's structure visible without interrupting the flow.",
    "detailed": "A good transition sentence does two things: it looks backward (echoes the idea just made) and forward (signals what comes next). 'While AI improves efficiency, its implementation raises equity concerns that require closer examination.' This closes the efficiency discussion and opens the equity discussion without a jarring break. Poor transitions leave readers to deduce the connection themselves.",
    "doctoral_relevance": "Argument flow is a core writing quality criterion. Papers with poor transitions feel disjointed even when the individual paragraphs are strong.",
    "instructor_emphasis": "Take a student's paragraph and write three different transition sentences that lead to three different subsequent ideas."
},
"wrong_reasons": [
    "Option A — citations support claims; they are not transition functions.",
    "Option C — headings signal section breaks, not inter-paragraph transitions.",
    "Option D — summaries belong at section endings, not between paragraphs."
],
"teaching_insight": "Teach the backward-forward structure: every transition looks back and looks ahead simultaneously.",
"follow_up": "Write a transition sentence connecting a paragraph on AI accuracy to the next paragraph on AI fairness."
},

{
"number": 75, "session": "S13", "difficulty": "Advanced", "clo": "CLO 8",
"concept": "Research Ethics — Anonymisation",
"question": "A researcher promises participants full anonymity, then uses detailed quotes that allow readers to identify the participant. This is:",
"options": [
    "Acceptable if the participant consented to direct quotes",
    "A breach of the confidentiality agreement and a violation of research ethics",
    "Acceptable in published research where institutional review has occurred",
    "Only a problem if the participant complains"
],
"correct": 1,
"explanation": {
    "concise": "Promising anonymity and then enabling identification through contextual details is a clear breach of informed consent.",
    "detailed": "Anonymity in research means that no one, including the researcher, can identify the participant from the published data. If detailed organisational role descriptions, unique experiences, or combined demographic details make a participant identifiable — even without naming them — the anonymity promise is broken. This is an ethics violation regardless of whether the participant explicitly consents to 'direct quotes' (consent to quoting does not equal consent to being identified).",
    "doctoral_relevance": "Qualitative researchers must think carefully about what details enable identification — especially in small populations (e.g., 'the only female senior consultant in the Bangalore office').",
    "instructor_emphasis": "Present a fictional quote that is clearly identifiable and discuss what changes would genuinely anonymise it."
},
"wrong_reasons": [
    "Option A — consent to quotes is not consent to identifiability.",
    "Option C — IRB approval does not authorise ethics violations in execution.",
    "Option D — ethics obligations exist independent of whether the victim is aware of or reports the breach."
],
"teaching_insight": "Anonymisation is more complex than using pseudonyms — it requires thinking about all contextual identifiers.",
"follow_up": "Review a published qualitative study and identify two ways the researcher protected participant anonymity beyond using pseudonyms."
},

{
"number": 76, "session": "S14", "difficulty": "Beginner", "clo": "CLO 7",
"concept": "Revision Letter",
"question": "A resubmission letter to a journal editor (revision letter) should:",
"options": [
    "Be as brief as possible, since editors are busy",
    "Argue that the reviewers were wrong",
    "Systematically address every reviewer comment, explain changes made, and quote the revised text where relevant",
    "Only address the major comments, not the minor ones"
],
"correct": 2,
"explanation": {
    "concise": "Revision letters must address every comment — major and minor — systematically, showing the reviewer their concerns were taken seriously.",
    "detailed": "A well-structured revision letter: (1) thanks the editor and reviewers, (2) summarises the major revisions made, (3) addresses each reviewer comment in sequence with sub-headers (Reviewer 1, Comment 1, etc.), (4) explains the change made or provides a reasoned response if disagreeing, and (5) quotes the revised text with line numbers. Ignoring minor comments signals carelessness. Disagreeing with reviewers is acceptable — but must be argued respectfully with evidence.",
    "doctoral_relevance": "The revision letter is often the difference between acceptance and rejection at the R&R stage. Students publishing for the first time frequently underestimate its importance.",
    "instructor_emphasis": "Show a real (anonymised) revision letter and walk through its structure."
},
"wrong_reasons": [
    "Option A — a brief revision letter looks dismissive. Length should match the volume of comments.",
    "Option B — arguing that reviewers are wrong is possible but must be done respectfully and with evidence, not as a general strategy.",
    "Option D — minor comments must also be addressed; ignoring them risks rejection."
],
"teaching_insight": "Many first-time R&R authors are surprised by how much work the revision letter requires. Set expectations early.",
"follow_up": "Write a response to this reviewer comment: 'The sample size of 45 is too small for the claimed generalisability.'"
},

{
"number": 77, "session": "S16", "difficulty": "Intermediate", "clo": "CLO 8",
"concept": "AI and Reproducibility",
"question": "A study uses a generative AI to assist with qualitative coding. A reviewer asks how the coding can be reproduced. The BEST response is:",
"options": [
    "The AI ensured perfect objectivity, so reproduction is not needed",
    "Providing the prompts, AI model version, and coding protocol used, plus demonstrating human-AI process documentation",
    "Saying that qualitative research is not meant to be reproduced",
    "Switching to quantitative methods"
],
"correct": 1,
"explanation": {
    "concise": "Reproducibility with AI assistance requires documenting the tool, version, prompts, and human oversight steps in enough detail that another researcher could understand and evaluate the process.",
    "detailed": "AI-assisted analysis introduces new reproducibility challenges: the same prompt may generate different outputs across model versions, and AI outputs depend on stochastic parameters. Researchers using AI in analysis must: document the specific model and version, record the prompts used, describe the human review and validation process, and archive where possible. This is analogous to documenting software versions in quantitative research.",
    "doctoral_relevance": "Research transparency is increasingly required by journals. AI-assisted analysis without documentation is vulnerable to reproducibility critiques.",
    "instructor_emphasis": "Connect to the Open Science movement and preregistration — how would these practices apply to AI-assisted qualitative research?"
},
"wrong_reasons": [
    "Option A — AI assistance does not guarantee objectivity; this is a misconception.",
    "Option C — while qualitative research has different reproducibility criteria, transparency is still required.",
    "Option D — switching methods does not address the transparency question and avoids the issue."
],
"teaching_insight": "AI-assisted research methods require new transparency norms that the field is actively developing.",
"follow_up": "Design a documentation protocol for AI-assisted qualitative coding that a reviewer would find credible."
},

{
"number": 78, "session": "S05", "difficulty": "Advanced", "clo": "CLO 2",
"concept": "Null Hypothesis",
"question": "Why do researchers state a null hypothesis in addition to the research hypothesis?",
"options": [
    "Because journals require two hypotheses per study",
    "The null hypothesis provides a specific statistical baseline that can be tested; research hypotheses are directional claims that cannot be directly falsified by data",
    "The null hypothesis describes what the researcher expects to find",
    "The null is used only in medical research"
],
"correct": 1,
"explanation": {
    "concise": "Statistical tests test the null hypothesis — they evaluate whether observed data is inconsistent with assuming no effect.",
    "detailed": "Statistical hypothesis testing operates by assuming the null (no effect, no relationship) is true, then asking: what is the probability of obtaining results as extreme as these if the null were true? If this probability (p-value) is below a threshold (α), we reject the null. We do not 'prove' the research hypothesis — we reject or fail to reject the null. This is the Popperian logic of falsification applied statistically.",
    "doctoral_relevance": "Understanding what hypothesis testing actually tests prevents misinterpretation of p-values and prevents claiming results 'prove' a hypothesis.",
    "instructor_emphasis": "Explain: rejecting H0 ≠ proving H1. It merely means the data is inconsistent with H0 at the chosen significance level."
},
"wrong_reasons": [
    "Option A — journal requirements vary; null hypotheses are a statistical logic requirement, not a formatting one.",
    "Option C — the null describes the 'no effect' baseline, not what the researcher expects.",
    "Option D — null hypothesis testing applies to all quantitative research."
],
"teaching_insight": "The logic of null hypothesis significance testing is poorly understood by many students who use it routinely.",
"follow_up": "State the null and alternative hypotheses for a study on whether AI training improves employee productivity."
},

{
"number": 79, "session": "S09", "difficulty": "Advanced", "clo": "CLO 5",
"concept": "Joint Display",
"question": "A joint display in mixed methods research is used to:",
"options": [
    "Show the research team's photo",
    "Visually integrate quantitative and qualitative findings to compare, contrast, and generate meta-inferences",
    "Display both participant quotes and statistical tables in separate appendices",
    "Combine the two research questions into one"
],
"correct": 1,
"explanation": {
    "concise": "A joint display is a visual integration tool — it places quantitative and qualitative data side by side to enable comparison and inference.",
    "detailed": "Creswell and Plano Clark recommend joint displays as a primary integration mechanism in mixed methods research. A joint display might show: quantitative subgroup means alongside representative qualitative quotes from those groups, or survey items alongside interview codes on the same theme. The joint display makes integration visible — allowing the researcher to draw meta-inferences about convergence, divergence, or elaboration.",
    "doctoral_relevance": "Mixed methods theses and papers that lack integration often receive reviewer criticism. A joint display is the most practical way to demonstrate genuine integration.",
    "instructor_emphasis": "Show a published joint display and walk students through how to read it."
},
"wrong_reasons": [
    "Option A — no research method involves displaying team photos.",
    "Option C — separate appendices is the opposite of integration.",
    "Option D — research questions are not combined; findings are integrated."
],
"teaching_insight": "Creating a joint display is a concrete, learnable integration skill. Assign one as practice.",
"follow_up": "Create a simple joint display for a study where survey data shows 60% of employees distrust AI, and interview data reveals distrust stems from lack of transparency."
},

{
"number": 80, "session": "S11", "difficulty": "Intermediate", "clo": "CLO 6",
"concept": "Mediation Analysis",
"question": "In mediation analysis, the mediator variable:",
"options": [
    "Strengthens or weakens the relationship between X and Y depending on group membership",
    "Explains HOW or WHY the independent variable affects the dependent variable",
    "Removes the need to measure the independent variable directly",
    "Replaces the dependent variable in the regression model"
],
"correct": 1,
"explanation": {
    "concise": "A mediator explains the mechanism through which X leads to Y — it answers 'how does this work?'",
    "detailed": "In mediation (Baron & Kenny, 1986; Hayes, 2013 PROCESS macro): X → M → Y. The mediator M transmits the effect of X to Y. For example: AI-assisted feedback (X) → increased goal clarity (M) → improved performance (Y). Mediation analysis tests whether removing the direct X→Y path reduces to near zero when M is included (full mediation) or whether X still has a direct effect (partial mediation).",
    "doctoral_relevance": "Mediation analysis is one of the most common analytical strategies in management research. PROCESS macro by Hayes is the standard tool.",
    "instructor_emphasis": "Draw the full mediation model on the board and label the a, b, c, and c' paths."
},
"wrong_reasons": [
    "Option A — that describes a moderator variable, not a mediator.",
    "Option C — mediation does not remove the need to measure X.",
    "Option D — mediators do not replace the dependent variable."
],
"teaching_insight": "Mediation and moderation are among the most frequently confused concepts in management research.",
"follow_up": "Diagram a mediation model for the relationship between AI transparency and employee trust, proposing one mediator."
},

{
"number": 81, "session": "S06", "difficulty": "Intermediate", "clo": "CLO 4",
"concept": "Conceptual Framework vs Theoretical Framework",
"question": "What distinguishes a CONCEPTUAL FRAMEWORK from a THEORETICAL FRAMEWORK?",
"options": [
    "There is no difference; the terms are interchangeable",
    "A theoretical framework draws on established theory; a conceptual framework may combine theories, prior findings, and researcher-generated propositions to show the study's logic",
    "A conceptual framework is used only in qualitative research",
    "A theoretical framework is required only in quantitative research"
],
"correct": 1,
"explanation": {
    "concise": "A theoretical framework borrows from existing theory; a conceptual framework synthesises multiple theoretical and empirical elements to map the study's own logic.",
    "detailed": "A theoretical framework uses one or two established theories to explain predicted relationships. A conceptual framework is broader: it maps all variables in the study and their proposed relationships, drawing on theory, prior empirical findings, and the researcher's own conceptual propositions. The conceptual framework is the researcher's roadmap — it shows what is being studied, why, and how.",
    "doctoral_relevance": "Both terms are used in PhD contexts; examiners expect candidates to distinguish between them and use them appropriately.",
    "instructor_emphasis": "Draw an example conceptual framework on the board: boxes for variables, arrows for relationships, labels for the theoretical basis of each relationship."
},
"wrong_reasons": [
    "Option A — they are related but not identical.",
    "Option C — conceptual frameworks are used across all paradigms.",
    "Option D — theoretical frameworks are used across all paradigms."
],
"teaching_insight": "Students often submit 'conceptual frameworks' that are actually just lists of variables. A true framework shows relationships and their theoretical basis.",
"follow_up": "Draw a conceptual framework for a study on AI and employee innovation behaviour, labelling the theoretical basis for each proposed relationship."
},

{
"number": 82, "session": "S03", "difficulty": "Doctoral Challenge", "clo": "CLO 3",
"concept": "Citation Analysis",
"question": "Bibliometric analysis using co-citation analysis is used to:",
"options": [
    "Count how many papers cite a specific author",
    "Identify intellectual structures in a field by mapping which papers are frequently cited together",
    "Find the most recent papers in a field",
    "Detect plagiarism between papers"
],
"correct": 1,
"explanation": {
    "concise": "Co-citation analysis reveals intellectual clusters — groups of papers that tend to be cited together, indicating shared conceptual territory.",
    "detailed": "When two papers are frequently cited together across many other papers, it suggests they represent related ideas in the mind of the research community. Co-citation analysis uses this pattern to map the intellectual structure of a field — identifying research fronts, foundational schools, and emerging clusters. VOSviewer and Bibliometrix R package are standard tools. This is a legitimate methodology for literature review in its own right, not just a search strategy.",
    "doctoral_relevance": "Bibliometric analysis is increasingly accepted as a methodology for systematic literature reviews, particularly in large, fast-moving fields.",
    "instructor_emphasis": "Demo VOSviewer with an exported Scopus dataset from the class's research area."
},
"wrong_reasons": [
    "Option A — that describes simple citation counting.",
    "Option C — recency is identified by publication date, not co-citation.",
    "Option D — plagiarism detection uses text similarity tools, not citation analysis."
],
"teaching_insight": "Bibliometric methods are underused by management doctoral students. Introducing them broadens methodological awareness.",
"follow_up": "Describe how you would use co-citation analysis to map the intellectual structure of AI in HR research."
},

{
"number": 83, "session": "S01", "difficulty": "Intermediate", "clo": "CLO 1",
"concept": "AI Tool Evaluation Criteria",
"question": "When evaluating an AI research tool for use in a systematic review, which criterion is MOST important?",
"options": [
    "The tool's visual interface and ease of navigation",
    "The transparency of the tool's search algorithm, index coverage, and validation evidence",
    "The number of users the tool has attracted",
    "Whether the tool was developed by a well-known technology company"
],
"correct": 1,
"explanation": {
    "concise": "For systematic review use, a tool must provide transparency about what it searches and how, so the review can be justified methodologically.",
    "detailed": "A systematic review must be reproducible. This requires knowing: which journals and databases the tool indexes, how its relevance ranking works, what time periods it covers, and whether the tool's performance has been validated in published studies. User numbers and brand recognition say nothing about methodological adequacy.",
    "doctoral_relevance": "PRISMA guidelines require documentation of search sources. Using a 'black box' AI tool that does not disclose its index makes this documentation impossible.",
    "instructor_emphasis": "Evaluate Consensus.app and Elicit together: what do they disclose about their methods?"
},
"wrong_reasons": [
    "Option A — visual design affects user experience, not research quality.",
    "Option C — user popularity is not a validity criterion.",
    "Option D — developer brand is not a methodological criterion."
],
"teaching_insight": "Teaching students to ask 'what does this tool actually search?' is one of the most practical skills in this session.",
"follow_up": "Evaluate one AI research tool using the transparency criterion and report what you can and cannot determine about how it works."
},

{
"number": 84, "session": "S10", "difficulty": "Advanced", "clo": "CLO 6",
"concept": "Secondary Data Ethics",
"question": "A researcher uses a social media company's public dataset for research on mental health. What is the MOST important ethical consideration?",
"options": [
    "Whether the dataset contains enough data points for analysis",
    "Whether individuals whose data is included gave meaningful consent for research use, and whether the research could cause harm to identifiable individuals",
    "Whether the dataset was downloaded legally",
    "Whether the social media company permits the analysis tool being used"
],
"correct": 1,
"explanation": {
    "concise": "Public availability does not equal research consent, especially for sensitive topics like mental health.",
    "detailed": "When users post publicly on social media, they consent to public viewing — not to inclusion in research datasets that could reveal sensitive patterns, lead to re-identification, or result in findings that stigmatise communities. The British Psychological Society and Association of Internet Researchers (AoIR) have guidelines specifically addressing this. Mental health data is particularly sensitive — terms used by users may be appropriated, quotes may be identifiable, and findings could affect how insurance or employers perceive mental health posts.",
    "doctoral_relevance": "Secondary data research requires ethics review, not just IRB-exempt status because data is 'public.'",
    "instructor_emphasis": "Read the AoIR ethical guidelines for internet research (freely available online) with students."
},
"wrong_reasons": [
    "Option A — sample size is a methodological, not ethical, concern.",
    "Option C — legal download is necessary but not sufficient for ethical research use.",
    "Option D — tool permissions are a terms-of-service issue, not the primary ethical concern."
],
"teaching_insight": "The 'public = shareable' assumption is one of the most common ethical misconceptions in digital research.",
"follow_up": "Draft an ethics consideration section for a study using Twitter/X data on employee burnout."
},

{
"number": 85, "session": "S12", "difficulty": "Beginner", "clo": "CLO 7",
"concept": "Abstract Structure",
"question": "In a structured abstract for an empirical paper, which element is TYPICALLY present?",
"options": [
    "A full literature review summary",
    "Purpose, design/methodology, findings, and implications",
    "The author's biographical details",
    "A list of all references used"
],
"correct": 1,
"explanation": {
    "concise": "Structured abstracts use labelled sections: Purpose, Design/Methodology/Approach, Findings, and Practical/Research/Social Implications — the PDFI structure common in Emerald and Elsevier journals.",
    "detailed": "Journals like Emerald (e.g., International Journal of Human Resource Management) require structured abstracts with explicit headings. Each section is typically 1–3 sentences. The Purpose states what the study set out to do. Design/Methodology describes how. Findings presents key results. Implications discusses what these mean for theory and practice. Originality/Value (in some formats) states the contribution.",
    "doctoral_relevance": "Abstracts are the most-read part of any paper. A well-structured abstract is the primary tool for communicating research value to busy reviewers.",
    "instructor_emphasis": "Write an abstract for a hypothetical study on AI and engagement using the structured format, sentence by sentence."
},
"wrong_reasons": [
    "Option A — abstracts summarise the paper, not the literature.",
    "Option C — author biographies appear in author notes, not abstracts.",
    "Option D — references do not appear in abstracts."
],
"teaching_insight": "Most students write descriptive rather than structured abstracts. Teaching the PDFI format is immediately practical.",
"follow_up": "Write a structured abstract (150–250 words) for a study on AI adoption in Indian hospitals using the PDFI format."
},

{
"number": 86, "session": "S13", "difficulty": "Intermediate", "clo": "CLO 7, 8",
"concept": "Self-Plagiarism",
"question": "Self-plagiarism in academic research occurs when a researcher:",
"options": [
    "Submits a paper with their own data without acknowledging previous papers that used similar data",
    "Resubmits previously published work as new without disclosure, or reuses substantial text from their own prior publications without attribution",
    "Cites their own papers too frequently",
    "Uses their own ideas without developing them further"
],
"correct": 1,
"explanation": {
    "concise": "Self-plagiarism is presenting previously published work — text or data — as new without disclosure.",
    "detailed": "Self-plagiarism (or 'duplicate publication') includes: (a) submitting the same paper to two journals simultaneously, (b) reusing substantial text from a previous paper without attribution, (c) publishing the same dataset in multiple papers without cross-referencing. It is a problem because it misrepresents the body of new work, potentially inflating publication counts and misleading readers about the newness of the evidence.",
    "doctoral_relevance": "Thesis chapters that draw on earlier published work must acknowledge this explicitly, with journal permissions where required.",
    "instructor_emphasis": "Distinguish self-plagiarism from legitimate practice: citing your own previous work, extending your own dataset in a new paper (with disclosure), and building on your own theory."
},
"wrong_reasons": [
    "Option A — the scenario in A does not constitute self-plagiarism; disclosure of data overlap is good practice but the scenario as stated is too vague.",
    "Option C — self-citation is not the same as self-plagiarism.",
    "Option D — developing your own ideas is encouraged; it is not self-plagiarism."
],
"teaching_insight": "Students approaching publication for the first time often do not know that reusing their own text requires attribution.",
"follow_up": "A researcher wants to reuse a methodology paragraph from a conference paper in a journal submission. What should they do?"
},

{
"number": 87, "session": "S07", "difficulty": "Beginner", "clo": "CLO 5",
"concept": "Internal vs External Validity",
"question": "External validity refers to:",
"options": [
    "Whether the study measures what it claims to measure",
    "The extent to which study findings can be generalised to other populations, settings, or times",
    "Whether the causal inference within the study is sound",
    "Whether the study's instruments were validated externally"
],
"correct": 1,
"explanation": {
    "concise": "External validity is about generalisability — can the findings travel beyond the specific study context?",
    "detailed": "A study conducted with 200 MBA students in one private university in a single city may have high internal validity (the experiment was done correctly) but questionable external validity (do these findings apply to full-time employees, public sector workers, or workers in different national contexts?). Experimental control tends to improve internal validity at the expense of external validity — a classic trade-off in research design.",
    "doctoral_relevance": "Discussing external validity limitations is a mandatory part of the limitations section. Examiners will ask about it.",
    "instructor_emphasis": "Illustrate the internal-external validity trade-off with a laboratory experiment vs a field study example."
},
"wrong_reasons": [
    "Option A — that describes construct validity.",
    "Option C — that describes internal validity.",
    "Option D — external validation of instruments is a construct validity concern."
],
"teaching_insight": "The four types of validity (internal, external, construct, statistical conclusion) are foundational but commonly confused.",
"follow_up": "A study of AI in five major hospitals in Mumbai has high internal validity. List three external validity concerns."
},

{
"number": 88, "session": "S11", "difficulty": "Advanced", "clo": "CLO 6",
"concept": "Moderation Analysis",
"question": "In moderation analysis, the moderator variable:",
"options": [
    "Explains the mechanism through which X affects Y",
    "Changes the strength or direction of the relationship between X and Y depending on its value",
    "Replaces the independent variable in the analysis",
    "Reduces the correlation between X and Y to zero"
],
"correct": 1,
"explanation": {
    "concise": "A moderator changes the X→Y relationship — the effect of X on Y is different at different levels of the moderator.",
    "detailed": "Moderation analysis (interaction analysis) tests whether the X→Y relationship is conditional on a third variable (M). Example: AI-assisted feedback (X) may increase performance (Y) more strongly for employees with high growth mindset (M=high) than low growth mindset (M=low). The moderation effect is the interaction term X*M in the regression equation. Significant interaction = significant moderation.",
    "doctoral_relevance": "Moderation analysis is extremely common in management research, particularly for testing boundary conditions of relationships.",
    "instructor_emphasis": "Draw a moderation diagram and compare it with a mediation diagram to ensure students distinguish them."
},
"wrong_reasons": [
    "Option A — that describes a mediator, not a moderator.",
    "Option C — moderators do not replace IVs.",
    "Option D — moderation changes the relationship; it does not necessarily reduce it to zero."
],
"teaching_insight": "Mediation vs moderation is one of the most persistent confusions in quantitative management research.",
"follow_up": "Propose a moderator for the relationship between AI adoption and employee innovation, and explain why it might moderate the relationship."
},

{
"number": 89, "session": "S14", "difficulty": "Advanced", "clo": "CLO 7",
"concept": "Desk Rejection",
"question": "A paper is desk-rejected by the editor before peer review. What does this typically mean?",
"options": [
    "The paper was rejected because it was submitted to the wrong address",
    "The editor determined that the paper does not meet the journal's scope, quality threshold, or formatting requirements — without sending it to reviewers",
    "The reviewers rejected the paper unanimously",
    "The paper was plagiarised"
],
"correct": 1,
"explanation": {
    "concise": "Desk rejection means the editor decided not to send the paper to reviewers — it failed scope, quality, or format checks at the editorial level.",
    "detailed": "Desk rejections (typically within 1–3 weeks) happen when: the paper is outside the journal's scope, the problem statement or gap is not compelling, the methodology is fundamentally flawed, the writing quality is too low, the contribution is not clearly articulated, or formatting requirements are not met. Desk rejection is not a comment on the research's merit per se — it may mean the paper needs significant development or targeting to a different journal.",
    "doctoral_relevance": "Desk rejection is common. First-time submitters should read the journal's aims and scope very carefully before submitting. The abstract and introduction are typically what the editor reads for desk review.",
    "instructor_emphasis": "Identify three common desk rejection triggers and ask students to self-review a paper against these criteria."
},
"wrong_reasons": [
    "Option A — submission format is procedural; desk rejection is editorial.",
    "Option C — desk rejection bypasses reviewers entirely.",
    "Option D — plagiarism detection would lead to a different type of rejection/notice."
],
"teaching_insight": "Understanding desk rejection helps students target journals better and write more compelling introductions.",
"follow_up": "Read the aims and scope of one target journal in your field and identify three reasons a poorly prepared paper might be desk-rejected."
},

{
"number": 90, "session": "S15", "difficulty": "Beginner", "clo": "CLO 7",
"concept": "Impact Factor",
"question": "A journal's impact factor (IF) is calculated as:",
"options": [
    "Total number of papers published in the journal",
    "Average number of citations to articles published in the journal in the two preceding years, divided by total articles published in those years",
    "Number of countries from which papers are received",
    "Percentage of submitted papers that are accepted for publication"
],
"correct": 1,
"explanation": {
    "concise": "IF = citations in year X to articles published in years X-1 and X-2 / total articles published in X-1 and X-2.",
    "detailed": "The impact factor (Clarivate) is the most widely used journal quality metric, despite its limitations. A journal with IF=5 means that articles published in the preceding two years are cited, on average, five times each in the current year. IF is field-dependent — top psychology journals may have IF=8, while top management journals may have IF=5. Citation-heavy fields have higher IFs by default.",
    "doctoral_relevance": "Promotion, hiring, and grant panels often use IF as a shorthand for journal quality. Understanding what it actually measures — and its limitations — is a scholarly competency.",
    "instructor_emphasis": "Look up the IF of three journals in your field using InCites/Clarivate and compare them."
},
"wrong_reasons": [
    "Option A — total publications is a volume measure, not IF.",
    "Option C — geographic reach is not part of IF.",
    "Option D — acceptance rate is a rejection rate measure, not IF."
],
"teaching_insight": "Many students know IF as a number without knowing what it measures. This question makes it concrete.",
"follow_up": "What are two limitations of impact factor as a journal quality measure?"
},

{
"number": 91, "session": "S16", "difficulty": "Advanced", "clo": "CLO 1, 8",
"concept": "AI and Academic Integrity Governance",
"question": "Which approach to institutional AI governance in universities is MOST likely to be sustainable?",
"options": [
    "A blanket ban on all AI tool use in academic work",
    "No policy — leave it to individual faculty discretion",
    "A nuanced, task-specific framework that distinguishes between appropriate and inappropriate AI use, with clear disclosure requirements and regular policy review",
    "Accepting all AI use without documentation, to prepare students for industry"
],
"correct": 2,
"explanation": {
    "concise": "Nuanced, task-specific policies with disclosure requirements and review cycles are the most practicable and pedagogically defensible approach.",
    "detailed": "Blanket bans are unenforceable and educationally counterproductive — AI literacy is itself a learning outcome. No policy creates inequity and confusion. Full acceptance without governance undermines assessment validity. The middle path — clearly specifying where AI can and cannot be used, what disclosure is required, and how this will be reviewed as technology evolves — balances academic integrity with pedagogical relevance.",
    "doctoral_relevance": "Doctoral graduates entering academia will be expected to contribute to institutional AI governance. Understanding the policy landscape is part of professional preparation.",
    "instructor_emphasis": "Share your institution's current AI policy and discuss: what would you change?"
},
"wrong_reasons": [
    "Option A — unenforceable and educationally counterproductive.",
    "Option B — no policy creates confusion and inequity.",
    "Option D — acceptance without governance undermines assessment integrity."
],
"teaching_insight": "Governance discussions help students see themselves as future academic citizens, not just current students.",
"follow_up": "Draft a three-point AI use policy for a doctoral research methods course."
},

{
"number": 92, "session": "S02", "difficulty": "Doctoral Challenge", "clo": "CLO 2",
"concept": "Ontological Assumptions",
"question": "A researcher believes that organisational performance is a social construct that exists differently for different stakeholders. This reflects which ontological position?",
"options": [
    "Realism — there is one objective reality about performance that exists independently of observers",
    "Constructivism — reality is constructed intersubjectively through social processes and meanings",
    "Pragmatism — whatever works to answer the research question is the right position",
    "Positivism — performance can be measured objectively with the right instruments"
],
"correct": 1,
"explanation": {
    "concise": "Constructivism holds that social phenomena like performance are not fixed objects but are constituted through social interaction and meaning-making.",
    "detailed": "Ontology asks: what is the nature of the reality being studied? Constructivism (social constructivism, interpretivist ontology) holds that social phenomena are not pre-given but are constituted through interaction, language, and context. 'Performance' means something different to a shareholder than to an employee — both constructions are real in their consequences. This position calls for qualitative methods that capture these multiple, constructed meanings.",
    "doctoral_relevance": "The philosophy of science chapter in a doctoral thesis requires the candidate to articulate and justify their ontological, epistemological, and methodological positions.",
    "instructor_emphasis": "Use the Burrell and Morgan (1979) paradigm grid to position different ontologies on the objectivist-subjectivist spectrum."
},
"wrong_reasons": [
    "Option A — realism holds that performance has an objective existence independent of observer constructions.",
    "Option C — pragmatism is a legitimate position but does not capture the specific constructivist claim in the question.",
    "Option D — positivism assumes an objective social reality measurable with appropriate instruments — the opposite of this position."
],
"teaching_insight": "Philosophy of science discussions often feel abstract to students. Grounding them in a concrete example (what is 'performance'?) makes them accessible.",
"follow_up": "Describe how the same research phenomenon (employee trust in AI) might be studied differently under realist vs constructivist ontologies."
},

{
"number": 93, "session": "S03", "difficulty": "Intermediate", "clo": "CLO 3",
"concept": "Backward and Forward Citation Search",
"question": "In citation chaining, 'forward citation search' means:",
"options": [
    "Searching the references listed at the end of a key paper",
    "Finding papers that have cited a key paper after its publication",
    "Searching only papers published before a specific year",
    "Using Boolean operators to extend a search"
],
"correct": 1,
"explanation": {
    "concise": "Forward citation search finds papers that have cited your seed paper — tracing how ideas were built upon over time.",
    "detailed": "Backward citation search (checking references in a paper) goes into the past — finding what influenced a paper. Forward citation search (using Google Scholar's 'Cited by' or Scopus's 'Cited by' function) goes into the future — finding who cited the paper after it was published. Both directions are important: backward reveals foundations, forward reveals how the field responded, extended, or critiqued the work.",
    "doctoral_relevance": "Combining backward and forward citation search is a robust supplementary strategy for systematic literature reviews.",
    "instructor_emphasis": "Demo Google Scholar's 'Cited by' feature on a foundational paper in the class's area."
},
"wrong_reasons": [
    "Option A — that describes backward citation search (reference lists).",
    "Option C — time restriction is a search filter, not citation chaining.",
    "Option D — Boolean operators are keyword search tools, not citation chaining."
],
"teaching_insight": "Citation chaining discovers papers that keyword search cannot find — it follows the intellectual chain of influence.",
"follow_up": "Perform a forward citation search on one foundational paper in your research area and identify the most-cited subsequent paper."
},

{
"number": 94, "session": "S04", "difficulty": "Intermediate", "clo": "CLO 3",
"concept": "Publication Bias",
"question": "Publication bias in research means:",
"options": [
    "Journals only publish papers by famous researchers",
    "Journals are more likely to publish studies with significant positive findings, leading to underrepresentation of null or negative results in the literature",
    "Researchers cite papers from their own country more often",
    "Reviewers are biased toward quantitative methods"
],
"correct": 1,
"explanation": {
    "concise": "Publication bias inflates the apparent evidence base for an effect because null results rarely get published.",
    "detailed": "Studies that find no significant effect (null results) are much less likely to be submitted or accepted for publication. This creates a distorted literature in which the apparent consensus in favour of a finding may be partly an artefact of selective publication. Funnel plots and Egger's test are used in meta-analyses to detect publication bias. Pre-registration is a remedy — locking in hypotheses before data collection.",
    "doctoral_relevance": "Systematic reviewers must account for publication bias. Failing to acknowledge it is a common weakness in reviews.",
    "instructor_emphasis": "Show a funnel plot from a published meta-analysis and explain the asymmetry test."
},
"wrong_reasons": [
    "Option A — journal author selection is peer review; not publication bias.",
    "Option C — that describes citation nationalism, a different bias.",
    "Option D — methodological bias in review is real but a different issue."
],
"teaching_insight": "Publication bias is why systematic reviews must search grey literature and why pre-registration matters.",
"follow_up": "How would you address potential publication bias in a systematic review on AI and employee creativity?"
},

{
"number": 95, "session": "S05", "difficulty": "Beginner", "clo": "CLO 2",
"concept": "Research Objective",
"question": "Research objectives are BEST described as:",
"options": [
    "The final conclusions of the study",
    "Specific, achievable statements describing what the study will do, derived from the research questions",
    "The journal where the research will be published",
    "The funding sources for the research"
],
"correct": 1,
"explanation": {
    "concise": "Objectives translate broad research questions into specific, actionable statements of what the study will accomplish.",
    "detailed": "Where a research question asks 'what is the relationship between X and Y?', an objective states: 'To examine the relationship between X and Y in population Z using method M.' Objectives are measurable and verifiable — you can confirm at the end of a study whether each was achieved. They structure the study and are referred back to in the conclusion.",
    "doctoral_relevance": "Thesis proposals require clear alignment between research questions, objectives, and methodology. Misalignment is a common examination concern.",
    "instructor_emphasis": "Convert a research question into two specific objectives as a class exercise."
},
"wrong_reasons": [
    "Option A — conclusions are outputs; objectives are inputs that guide the study.",
    "Option C — publication venue has no place in the research objectives.",
    "Option D — funding is contextual, not a research objective."
],
"teaching_insight": "Students often confuse objectives with broad goals. The key is specificity and achievability.",
"follow_up": "Write three research objectives for a study on AI adoption among nursing staff in rural hospitals."
},

{
"number": 96, "session": "S10", "difficulty": "Intermediate", "clo": "CLO 6",
"concept": "Survey Response Bias",
"question": "Social desirability bias in surveys means respondents tend to:",
"options": [
    "Answer questions too quickly without reading them carefully",
    "Report the answer they believe is socially acceptable or expected rather than their true view",
    "Skip questions that are difficult to understand",
    "Agree with all statements regardless of their actual views"
],
"correct": 1,
"explanation": {
    "concise": "Social desirability bias: respondents present themselves favourably, giving answers they think are expected or socially approved.",
    "detailed": "For sensitive topics — AI ethics views, discriminatory attitudes, actual behaviour vs stated intention — social desirability bias can substantially distort findings. Remedies include: anonymous surveys, indirect questioning, bogus pipeline procedures, and validated social desirability scales (e.g., Marlowe-Crowne) that allow statistical control.",
    "doctoral_relevance": "Surveys on sensitive topics without social desirability controls will face reviewer questions about response validity.",
    "instructor_emphasis": "Ask students: if asked about AI trust with patient data in a hospital survey, what bias would students expect?"
},
"wrong_reasons": [
    "Option A — that describes inattentive responding or satisficing.",
    "Option C — that describes item non-response.",
    "Option D — that describes acquiescence bias, a related but distinct response bias."
],
"teaching_insight": "Different types of response bias require different remedies — distinguishing them builds methodological sophistication.",
"follow_up": "Design a question on AI fairness perceptions that minimises social desirability bias."
},

{
"number": 97, "session": "S11", "difficulty": "Intermediate", "clo": "CLO 6",
"concept": "Confirmatory Factor Analysis",
"question": "Confirmatory Factor Analysis (CFA) is used to:",
"options": [
    "Explore what factors might underlie a dataset without prior theory",
    "Test whether a proposed factor structure (based on theory or prior research) fits the observed data",
    "Confirm that the sample size is adequate for analysis",
    "Generate topics from unstructured text data"
],
"correct": 1,
"explanation": {
    "concise": "CFA tests a theoretically specified factor structure against data — unlike EFA, which discovers structure inductively.",
    "detailed": "CFA (Structural Equation Modelling framework) tests whether a hypothesised measurement model — 'these four items should load on Factor 1, those three items on Factor 2' — fits the observed data. Fit indices (CFI, RMSEA, SRMR) indicate how well the model fits. CFA is used to establish construct validity before conducting structural equation modelling.",
    "doctoral_relevance": "Scale validation in management research typically requires CFA. Reviewers in quantitative journals expect to see fit indices.",
    "instructor_emphasis": "Show fit index interpretation guidelines (e.g., CFI>0.95, RMSEA<0.06) and apply them to a simple example."
},
"wrong_reasons": [
    "Option A — that describes Exploratory Factor Analysis (EFA).",
    "Option C — sample size adequacy is assessed with power analysis, not CFA.",
    "Option D — topic generation from text uses topic modelling (NLP), not CFA."
],
"teaching_insight": "The EFA-CFA distinction is critical in scale validation. Many students conflate them.",
"follow_up": "Explain when you would use EFA and when you would use CFA in developing a new scale for AI trust."
},

{
"number": 98, "session": "S15", "difficulty": "Intermediate", "clo": "CLO 7",
"concept": "Author Contribution Statement",
"question": "Author contribution statements (e.g., using CRediT taxonomy) are now required by many journals primarily to:",
"options": [
    "Allow journals to charge based on number of authors",
    "Transparently specify what each author contributed to the research, addressing honorary authorship and ghost authorship problems",
    "Determine the order of authorship on the paper",
    "Calculate the h-index contribution of each author"
],
"correct": 1,
"explanation": {
    "concise": "CRediT taxonomy specifications prevent ghost authorship (unacknowledged contributors) and honorary authorship (named without contribution).",
    "detailed": "The CRediT (Contributor Roles Taxonomy) system specifies 14 contribution types: Conceptualization, Data Curation, Formal Analysis, Funding Acquisition, Investigation, Methodology, Project Administration, Resources, Software, Supervision, Validation, Visualization, Writing – Original Draft, Writing – Review & Editing. Each author's contributions are listed. This addresses two ethics problems: guest/honorary authorship (senior researchers named without contribution) and ghost authorship (people who did the work but are excluded from the byline).",
    "doctoral_relevance": "Doctoral researchers who do not understand authorship norms may be exploited — listed as co-author on work not their own, or excluded from work they did.",
    "instructor_emphasis": "Review the ICMJE authorship criteria and the CRediT taxonomy. Ask: who would qualify as an author on a paper where a supervisor designed the study and a student collected and analysed the data?"
},
"wrong_reasons": [
    "Option A — authorship fees are not tied to author count in legitimate journals.",
    "Option C — authorship order is determined by convention and negotiation; CRediT does not determine it.",
    "Option D — h-index is a researcher-level metric not computed from CRediT statements."
],
"teaching_insight": "Authorship disputes are common in academia. Clarifying norms early protects doctoral students.",
"follow_up": "Using the CRediT taxonomy, describe the contribution statement for a study where a doctoral student did all the work under a supervisor's guidance."
},

{
"number": 99, "session": "S16", "difficulty": "Doctoral Challenge", "clo": "CLO 1, 8",
"concept": "Future of Research — Researcher Role",
"question": "As AI takes over more research tasks (literature search, data analysis, writing assistance), what becomes the MOST distinctive value of human researchers?",
"options": [
    "Speed of paper production",
    "Ability to process large datasets",
    "Judgement, ethical reasoning, original conceptual thinking, and accountability for research decisions",
    "Access to institutional subscriptions"
],
"correct": 2,
"explanation": {
    "concise": "What AI cannot replicate is what becomes most valuable: the human capacity to make accountable judgements, think originally, and reason ethically.",
    "detailed": "AI can search literature faster, analyse data more thoroughly, and draft text more fluently than most individual researchers. What remains distinctively human is: the ethical framing of research questions (who should be studied? what harms might the research cause?), the original conceptual leap (seeing a phenomenon as the instance of a new theoretical category), and the accountable decision-making (standing behind findings with one's reputation and career). These cannot be automated without losing the meaning of research as a social practice.",
    "doctoral_relevance": "This is the capstone insight of the course: the goal is not to outperform AI at routine tasks but to develop the distinctively human competencies that AI cannot replace.",
    "instructor_emphasis": "End the course by asking each student: what is the most important thing about your research that you, not AI, must provide?"
},
"wrong_reasons": [
    "Option A — speed is where AI has the greatest advantage.",
    "Option B — large-scale data processing is precisely AI's domain.",
    "Option D — institutional access is a resource, not a distinctive human competency."
],
"teaching_insight": "This question is designed to end the course on a philosophical note: what it means to be a researcher in an AI-enabled world.",
"follow_up": "In three sentences, describe your unique intellectual contribution to your research area — something an AI could not have conceived."
},

{
"number": 100, "session": "All", "difficulty": "Doctoral Challenge", "clo": "CLO 1-8",
"concept": "Integration — AI, Research, and Integrity",
"question": "A researcher uses AI throughout their study: gap identification, literature synthesis, survey item generation, data analysis, and manuscript drafting. After disclosure, a reviewer challenges whether any original scholarly contribution remains. What is the MOST powerful counter-argument?",
"options": [
    "AI use is now standard practice and should not require justification",
    "The researcher followed all institutional guidelines, so the contribution is valid",
    "The researcher's original contribution lies in the research design logic, theoretical framing, contextual judgement, interpretation of findings, and accountability for conclusions — none of which AI supplies",
    "The AI tools used are peer-reviewed and therefore their outputs are valid research contributions"
],
"correct": 2,
"explanation": {
    "concise": "The human researcher's distinctive contribution lies in the decisions, frameworks, and accountability that AI cannot provide — not in the execution of tasks AI performs faster.",
    "detailed": "This is the most important intellectual question the course raises. Even if AI performs the tasks of literature search, item generation, analysis, and writing, the researcher contributes: (a) identifying what problem matters and why (research problem formulation), (b) choosing and justifying the theoretical lens (interpretive framework), (c) making context-sensitive judgements throughout the process, (d) interpreting findings in light of theory and practice, and (e) standing behind the work as accountable knowledge-maker. These contributions are real and significant — but they must be made explicitly and cannot be hidden behind AI-assisted tasks.",
    "doctoral_relevance": "This argument is what a doctoral candidate must be able to make in their viva: 'This is what I, not the AI, contributed.'",
    "instructor_emphasis": "Use this as the final discussion question for the course: ask each student to name their unique contribution to their research."
},
"wrong_reasons": [
    "Option A — standard practice arguments do not establish intellectual contribution.",
    "Option B — institutional guideline compliance is a process criterion, not a contribution criterion.",
    "Option D — AI tools are not peer-reviewed as research agents; their outputs require human validation and interpretation."
],
"teaching_insight": "This question is the intellectual capstone of the course. It should generate genuine discussion and reflection.",
"follow_up": "Write a 200-word statement: 'My contribution to this research, independent of AI assistance, is...'"
},
]
