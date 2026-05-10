"""
Session 02 — Research Problem Identification & Gap Analysis
"""
import streamlit as st
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils import (concept_card, gold_card, reveal_box, warn_box,
                   section_divider, session_header, teaching_flow,
                   render_quiz_block, render_activity, render_case)

S02_QUIZ = [
    {
        "number": 1, "session": "S02", "difficulty": "Beginner", "clo": "CLO 2",
        "concept": "Research Gap Types",
        "question": "Which of the following is the BEST example of a 'contextual gap' in research?",
        "options": [
            "No studies exist on any aspect of AI in HR",
            "AI-assisted performance management has been studied extensively in US firms but rarely in South Asian family businesses",
            "Two studies reach opposite conclusions on AI fairness",
            "No quantitative method has been applied to AI adoption research"
        ],
        "correct": 1,
        "explanation": {
            "concise": "A contextual gap exists when a phenomenon is studied in some settings but not others — in this case, US vs South Asian family business context.",
            "detailed": "The four main gap types are: empirical (phenomenon unstudied), theoretical (no theory explains it), methodological (methods not yet applied), and contextual (studied in one context, not another). The example in option B is a clear contextual gap — existing research is geographically and organisationally bounded, leaving South Asian family businesses underrepresented.",
            "doctoral_relevance": "Most doctoral research fills a contextual gap rather than an entirely new topical gap. Reviewers are looking for a specific, defensible gap claim.",
            "instructor_emphasis": "Draw the 2x2 gap matrix on the board: empirical/theoretical on one axis, methodological/contextual on the other."
        },
        "wrong_reasons": [
            "Option A is an empirical gap, and one that is almost certainly false — AI in HR is well-studied.",
            "Option C describes a contradiction gap, which is real but a different type.",
            "Option D describes a methodological gap."
        ],
        "teaching_insight": "Teaching students to name the gap type forces precision in their literature review writing.",
        "follow_up": "Identify the gap type in your own research area and write one sentence describing it."
    },
    {
        "number": 2, "session": "S02", "difficulty": "Intermediate", "clo": "CLO 2",
        "concept": "Problem Statement Structure",
        "question": "A strong research problem statement should include which of the following elements?",
        "options": [
            "The researcher's personal interest in the topic",
            "The phenomenon, the existing knowledge state, the gap, and the significance",
            "The complete literature review and methodology",
            "A list of all variables to be measured"
        ],
        "correct": 1,
        "explanation": {
            "concise": "A strong problem statement identifies what the phenomenon is, what we know, what we don't know, and why it matters to know it.",
            "detailed": "The four-element structure: (1) Name the phenomenon precisely. (2) Acknowledge existing knowledge — what research exists. (3) Specify the gap — what remains unknown or contested. (4) State significance — who benefits from closing this gap and how. This structure appears in most top journal articles' introduction sections, and is the structure thesis examiners and proposal reviewers expect.",
            "doctoral_relevance": "Thesis proposal committees evaluate whether the problem statement is researchable, bounded, and significant. All four elements must be present.",
            "instructor_emphasis": "Annotate a published paper's introduction: identify all four elements and show how they appear in sequence."
        },
        "wrong_reasons": [
            "Option A — personal interest is motivation, not the scholarly problem.",
            "Option C — the problem statement is one paragraph in the introduction, not the full review.",
            "Option D — variable lists belong in the methods section."
        ],
        "teaching_insight": "Students who learn this four-element structure write dramatically better introductions in every subsequent assignment.",
        "follow_up": "Write a four-sentence problem statement for a study on AI bias in hospital triage systems."
    },
    {
        "number": 3, "session": "S02", "difficulty": "Advanced", "clo": "CLO 2",
        "concept": "Significance vs Novelty",
        "question": "A colleague says your proposed study is 'interesting but not important.' What is the most likely meaning of this critique?",
        "options": [
            "The study topic is too obscure for mainstream journals",
            "The study asks a question no one has asked but whose answer does not advance theory, policy, or practice",
            "The study methodology is not sophisticated enough",
            "The study has too small a sample"
        ],
        "correct": 1,
        "explanation": {
            "concise": "Interesting = novel; important = significant. A study can be new without its answer mattering to anyone beyond the researcher.",
            "detailed": "Significance requires that closing the gap advances something: theory (new conceptual contribution), practice (actionable for managers, clinicians, policymakers), or methodology (new analytical tools). A study of typeface preferences among accountants in Fiji may be completely unstudied (interesting) but offers no clear path to advancing accounting theory or practice (not important).",
            "doctoral_relevance": "Every research proposal must answer 'so what?' in relation to theory and practice. Examiners ask this question directly.",
            "instructor_emphasis": "Run a 30-second drill: each student states their research topic and must answer 'so what?' immediately."
        },
        "wrong_reasons": [
            "Option A conflates obscurity with lack of significance — niche topics can be highly significant.",
            "Option C — methodology is a separate dimension of quality.",
            "Option D — sample size is an adequacy concern, not a significance concern."
        ],
        "teaching_insight": "Students often confuse their own enthusiasm for a topic with the topic's scholarly significance. This is a gentle correction.",
        "follow_up": "For your research area, write one sentence on novelty and one on significance without using the same argument for both."
    },
    {
        "number": 4, "session": "S02", "difficulty": "Doctoral Challenge", "clo": "CLO 2, 8",
        "concept": "Ethics of Problem Framing",
        "question": "A researcher frames a study as 'Why do women fail to advance in corporate leadership?' A reviewer suggests reframing as 'What organisational conditions constrain women's leadership advancement?' The reframe is MOST valuable because:",
        "options": [
            "It is more politically correct",
            "It shifts analytical focus from individual deficit to structural constraint, which is theoretically more defensible and generates different, potentially more actionable findings",
            "It uses more academic language",
            "It broadens the sample to include more participants"
        ],
        "correct": 1,
        "explanation": {
            "concise": "The reframe is not cosmetic — it changes the unit of analysis, the theoretical assumptions, and the kinds of solutions it can generate.",
            "detailed": "The original framing naturalises women's failure as an individual characteristic. The reframe asks what organisations do, not what women fail to do. This is theoretically grounded in feminist organisational theory (Acker, 1990 — 'gendered organisations') and generates findings actionable by organisations rather than prescriptions for individual women to change themselves.",
            "doctoral_relevance": "Research framing is not politically neutral — it determines whose problems get studied and what kinds of solutions become thinkable.",
            "instructor_emphasis": "Connect to Merton's concept of opportunity structures. The reframe is better sociology, not just better politics."
        },
        "wrong_reasons": [
            "Option A — 'political correctness' trivialises a genuine theoretical improvement.",
            "Option C — language choice is a symptom of the reframe, not its value.",
            "Option D — sample breadth is unrelated to the framing shift."
        ],
        "teaching_insight": "This question opens important conversations about whose perspective research encodes and what assumptions it naturalises.",
        "follow_up": "Identify a research question in your field that might benefit from a similar structural reframe."
    },
    {
        "number": 5, "session": "S02", "difficulty": "Intermediate", "clo": "CLO 2",
        "concept": "AI in Gap Analysis",
        "question": "A researcher uses Elicit.org to map the literature on AI in employee wellbeing. The results show strong consensus that AI reduces workload. What should the researcher do NEXT?",
        "options": [
            "Accept the consensus and design a replication study",
            "Conclude there is no gap in this area",
            "Probe boundary conditions: in what contexts, for which employees, using which AI types is this finding supported or challenged?",
            "Search for a completely different topic"
        ],
        "correct": 2,
        "explanation": {
            "concise": "Consensus in the literature is not the end of inquiry — it is an invitation to examine boundary conditions and contextual variation.",
            "detailed": "Strong consensus on a main effect often masks important moderating conditions. Does AI reduce workload for all employees equally? For knowledge workers vs manual workers? In high-autonomy vs low-autonomy roles? In Western vs non-Western organisations? These boundary condition questions are where contextual and moderating gaps live — and they are highly publishable.",
            "doctoral_relevance": "Examiners expect candidates to show that they have looked beyond simple agreement to find where the knowledge is genuinely incomplete.",
            "instructor_emphasis": "Introduce 'boundary conditions' as the doctoral researcher's primary gap-finding tool in a consensus literature."
        },
        "wrong_reasons": [
            "Option A — simple replication adds limited value unless the context is demonstrably different.",
            "Option B — consensus on a main effect does not exhaust all research questions.",
            "Option D — abandoning a productive area when consensus exists is strategically unwise."
        ],
        "teaching_insight": "Students who find consensus feel defeated. Reframe it: consensus = where the interesting moderating questions live.",
        "follow_up": "Identify three boundary conditions that might limit the generalisability of the workload-reduction finding."
    },
]

S02_ACTIVITY = {
    "title": "Research Gap Identification Workshop",
    "task": "Select a paper you have read in your research area. Read only the 'Future Research' section and the conclusion. List the gaps the authors themselves identify. Then search for one of those gaps in Elicit or Consensus to check whether it has been studied since publication. Report: (a) the gap as stated by the original authors, (b) whether it has been addressed, and (c) if not, why it might still be open.",
    "student_role": "Gap analyst",
    "expected_output": "A structured gap note: gap statement, evidence of whether it has been addressed, and if still open, one reason it persists.",
    "time_minutes": 25,
    "sample_answer": "In Tambe et al. (2019) on AI in HR, the authors note that 'the long-term effects of algorithmic management on employee psychological wellbeing remain understudied.' A search in Consensus.app (2024) reveals some papers on algorithmic management and stress, but almost none in non-Western contexts or longitudinal designs. The gap persists partly because longitudinal studies are expensive and access to firm-level algorithmic HR data is restricted.",
    "weak_answer": "The paper had a future research section. I found some other papers on the same topic. The gap might be closed.",
    "improved_answer": "Tambe et al. (2019) call for research on 'AI adoption challenges in resource-constrained firms.' A search on Elicit returns papers primarily from large US and European firms. Indian SMEs and family businesses are almost absent. The gap persists likely due to access challenges and the assumption that AI adoption patterns from large firms generalise to smaller ones — an assumption that is theoretically contestable.",
    "debrief": "Ask: 'How many future research directions from your paper have actually been studied since it was published?' Most will find some, but not all. Discuss what makes a gap persist.",
    "grading_hints": "Strong answers name a specific gap, provide evidence of search, and offer a scholarly explanation for why the gap persists.",
    "common_mistakes": "Students list generic topics rather than specific, bounded gaps. Push them toward precision.",
    "scholarly_link": "Gap identification is the foundation of the Research Proposal (Sections 1–3). This activity directly prepares for the proposal assignment."
}

S02_CASE = {
    "title": "The Too-Broad Proposal",
    "scenario": "Vikram submits a research proposal titled 'The Impact of Technology on Organisations.' His supervisor returns it immediately with one comment: 'This is not a research problem — it is a library.' Vikram is confused. He thought broad scope showed ambition.",
    "question": "Why was Vikram's proposal rejected, and how should he revise it?",
    "weak_response": "Vikram should narrow his topic to just AI or just organisations.",
    "strong_response": "Vikram's proposal fails the specificity test: 'technology' is thousands of topics, and 'organisations' is every possible setting. A doctoral study must be bounded enough to be answerable with a specific method in a specific time. Vikram needs to: (a) specify the technology (e.g., AI-assisted scheduling), (b) identify the outcome (e.g., employee autonomy), (c) define the population (e.g., nursing staff), and (d) situate in a context (e.g., Indian public hospitals). The revised title might be: 'AI-Assisted Scheduling and Perceived Autonomy Among Nurses in Indian Public Hospitals.'",
    "issue_diagnosis": "Scope is too broad to be researchable with any specific method. No gap can be identified without specificity.",
    "theory": "Research scope must match the study's capacity to generate valid, bounded knowledge claims.",
    "research_gap": "Cannot be identified from such a broad frame.",
    "research_question": "How does AI-assisted work scheduling affect perceived autonomy among nursing staff in Indian public hospitals?",
    "scholarly_framing": "A narrowly scoped study produces deeper, more defensible findings than a broadly scoped one. Saying less, meaning more.",
    "instructor_note": "Use this case to establish the scope-depth trade-off early. Students often confuse ambition with breadth."
}

def render():
    session_header(
        code="S02",
        title="Research Problem Identification & Gap Analysis",
        clos=["CLO 2"],
        why="No research skill is more foundational than identifying a genuine, significant gap. Students who cannot do this cannot design a study worth doing."
    )
    teaching_flow([
        "Opening: What makes a research problem 'real'?",
        "Theoretical Concepts — gap types, problem structure",
        "Research Story — narrative reveal",
        "Visual: Gap Analysis Flowchart",
        "Demonstration — live gap analysis with AI tools",
        "Activity — Gap Identification Workshop",
        "Case + Quiz + Reflection"
    ])
    section_divider()

    st.markdown("## 📖 A. Theoretical Concepts")

    with st.expander("1. The Four Gap Types", expanded=False):
        concept_card("Empirical Gap", "A phenomenon that has not been studied. Rare in mature fields — most topics have some coverage.")
        concept_card("Theoretical Gap", "No theory adequately explains an observed phenomenon, or an existing theory has not been applied to a new context.")
        concept_card("Methodological Gap", "A method that has not been applied to a topic — e.g., no longitudinal studies on AI adoption despite extensive cross-sectional evidence.")
        concept_card("Contextual Gap", "A well-studied phenomenon in one setting that has not been examined in a different geographic, industrial, or organisational context.")
        gold_card("Most Doctoral Gaps", "Are contextual or theoretical — combining a studied phenomenon with an understudied context or an untested theoretical explanation.")

    with st.expander("2. Problem Statement — Four-Element Structure", expanded=False):
        st.markdown("""
**Element 1 — Phenomenon:** Name the specific thing you are studying. Not 'AI' but 'AI-assisted performance feedback.'

**Element 2 — State of knowledge:** What do we know? 'AI performance management has been shown to improve output metrics in large technology firms (Smith, 2020; Jones, 2022).'

**Element 3 — The gap:** What is missing? 'However, its effects on employee trust and psychological safety in hybrid work environments remain largely unstudied.'

**Element 4 — Significance:** Why does closing this gap matter? 'As AI performance systems expand into remote and hybrid settings, understanding their trust implications is critical for organisations managing post-pandemic work arrangements.'

**Weak problem statement:** 'AI affects employees in many ways. More research is needed.'

**Strong problem statement:** 'While AI-assisted performance management has been adopted extensively in large technology firms, its effects on perceived fairness and employee trust in hybrid work settings — particularly in Indian IT services organisations — remain understudied. This gap matters because perceived fairness is a key driver of talent retention, and Indian IT firms are among the world's largest users of AI HR systems.'
        """)

    with st.expander("3. From Topic to Research Problem", expanded=False):
        st.markdown("""
**Step 1:** Start with a broad interest area (e.g., AI in healthcare)
**Step 2:** Identify a phenomenon within that area (e.g., AI triage algorithms)
**Step 3:** Conduct a rapid literature scan — what has been studied?
**Step 4:** Identify the boundary of existing knowledge
**Step 5:** State what lies beyond that boundary (the gap)
**Step 6:** Ask: is closing this gap significant to theory, practice, or policy?
**Step 7:** Write the problem statement using the four-element structure

**Common mistake:** Jumping from 'I'm interested in AI' directly to 'I will study AI.' Steps 2–6 cannot be skipped.

**Doctoral-level insight:** The gap is not just 'unexplored' — it is 'unexplored AND significant.' Both conditions must hold.
        """)

    with st.expander("4. AI Tools for Gap Analysis", expanded=False):
        concept_card("Elicit.org", "Decomposes a research question and finds papers addressing it. Useful for checking whether a gap has been addressed.")
        concept_card("Consensus.app", "Shows the degree of consensus or disagreement on a specific research question. Consensus = possible boundary condition gap. Disagreement = possible contradiction gap.")
        concept_card("Connected Papers", "Reveals what has NOT been studied by showing the existing network. White spaces in the network suggest unexplored territory.")
        warn_box("AI tools reveal what is in the indexed literature. They cannot tell you what the literature misses. Always supplement with manual search in Scopus and targeted journal searches.")

    section_divider()

    st.markdown("## 📖 B. Tell Me the Research Story")
    if st.button("🎭 Tell Me the Research Story", key="s02_story"):
        st.markdown("""<div class="gold-card">
<strong>The Map with the Blank Spot</strong><br><br>

Every good research project begins with a map — a map of what is known. The researcher reads, searches, synthesises, and gradually constructs this map in their mind. Most of the territory has been explored. There are roads, landmarks, well-trodden paths. But somewhere on the map, if you look closely, there is a blank spot.

Not a void — there are roads leading to it. There are papers that stop just short of it. There are authors who mention it in their future research sections, as if to say: 'We know this is here, but we did not go there.'

The doctoral researcher's job is not to redraw the entire map. It is to go to the blank spot, explore it carefully, and come back with a faithful account of what is there.

The blank spot is not always obvious. Sometimes it is hidden by a word — 'context.' Every map of research is drawn from somewhere. Most maps of AI in organisations were drawn from offices in California and London. If you are studying organisations in Bangalore, Nairobi, or São Paulo, you are already looking at the edge of the map.

The skill is learning to see the blank spots — not just to repeat what the explorers who went before you found, but to ask what they did not ask, go where they did not go, and notice what they walked past.

<em>Classroom prompt: Draw a map of your research area on paper. Where are the blank spots?</em>
</div>""", unsafe_allow_html=True)

    section_divider()

    st.markdown("## 📊 C. Visual: Gap Analysis Decision Path")
    st.markdown("*Follow this path to determine whether you have a genuine research gap.*")

    try:
        import plotly.graph_objects as go
        fig = go.Figure()
        steps = [
            (0.1, 0.9, "1. Identify broad topic area"),
            (0.1, 0.72, "2. Search existing literature"),
            (0.1, 0.54, "3. What is well-established?"),
            (0.1, 0.36, "4. What is missing / contested / context-limited?"),
            (0.1, 0.18, "5. Is closing the gap significant?"),
        ]
        outcomes = [
            (0.65, 0.36, "✅ You have a CONTEXTUAL gap", "#1a7a4a"),
            (0.65, 0.54, "✅ You have a THEORETICAL gap", "#1a3a6e"),
            (0.65, 0.18, "⚠️ Not yet — revisit significance", "#8a5a00"),
        ]
        for x, y, label in steps:
            fig.add_annotation(x=x, y=y, text=label, showarrow=False,
                               xanchor="left", font=dict(size=12))
            if y > 0.2:
                fig.add_annotation(x=x+0.03, y=y-0.09, text="↓", showarrow=False,
                                   font=dict(size=18, color="#1a3a6e"))
        for x, y, label, color in outcomes:
            fig.add_annotation(x=x, y=y, text=label, showarrow=False,
                               xanchor="left", font=dict(size=11, color=color),
                               bgcolor="rgba(240,245,255,0.9)", bordercolor=color,
                               borderwidth=1, borderpad=4)
        fig.update_layout(
            xaxis=dict(visible=False, range=[0, 1]),
            yaxis=dict(visible=False, range=[0.05, 1]),
            height=350, margin=dict(l=10, r=10, t=30, b=10),
            title="Gap Analysis Decision Path", title_font=dict(size=14, color="#1a3a6e"),
            plot_bgcolor="white", paper_bgcolor="white",
        )
        st.plotly_chart(fig, use_container_width=True)
    except ImportError:
        st.info("Steps: broad topic → literature search → map known territory → identify boundary → assess significance")

    with st.expander("🔍 How to Use This Diagram in Class"):
        st.markdown("""
Walk students through the five steps for their own research area. At each step, they should write one sentence. By step 5, they either have a gap worth pursuing or they need to revisit.

**Common failure point:** Step 5 — students can identify an unexplored topic but cannot explain why it matters. If step 5 fails, go back to step 4 and choose a different boundary.

**Instructor note:** Do this exercise as a class first, then ask students to repeat it individually for their thesis area. Review step 5 statements as homework.
        """)

    section_divider()

    st.markdown("## 🏋️ D. Classroom Activity")
    render_activity(S02_ACTIVITY, key="s02_act")

    section_divider()

    st.markdown("## 📋 E. Mini Case")
    render_case(S02_CASE, key="s02_case")

    section_divider()

    st.markdown("## 📝 F. Session Quiz")
    render_quiz_block(S02_QUIZ, key_prefix="s02", title="Session 02 — Five Questions")

    section_divider()

    st.markdown("## ✅ G. Reflection & Output")
    st.markdown("""
**After this session, you should be able to:**
- [ ] Name all four gap types and give an example of each
- [ ] Write a four-element research problem statement
- [ ] Distinguish between a topic and a research problem
- [ ] Use Elicit or Consensus to check whether a specific gap has been addressed
- [ ] Explain why novelty and significance are separate criteria

**What to produce:**
A one-paragraph research problem statement for your thesis area, using the four-element structure. Bring to the next session for peer feedback.

**Link to assessment:**
This directly feeds into Section 1 (Background and Problem Statement) of your Research Proposal assignment.
    """)
