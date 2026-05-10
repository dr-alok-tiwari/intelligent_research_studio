"""
Session 01 — AI & the Research Landscape
Complete classroom teaching module.
"""
import streamlit as st
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils import (concept_card, gold_card, reveal_box, warn_box,
                   section_divider, session_header, teaching_flow,
                   render_quiz_block, render_activity, render_case)

# ── Quiz questions specific to S01 ──────────────────────────────────────────
S01_QUIZ = [
    {
        "number": 1, "session": "S01", "difficulty": "Beginner", "clo": "CLO 1",
        "concept": "Role of AI in Research",
        "question": "Which statement BEST describes the current role of AI tools in academic research?",
        "options": [
            "AI replaces human judgment in designing research studies",
            "AI assists researchers by automating repetitive tasks while scholars retain interpretive authority",
            "AI produces research findings that can be published without scholarly review",
            "AI is primarily useful for formatting and typesetting manuscripts"
        ],
        "correct": 1,
        "explanation": {
            "concise": "AI augments scholarly work; it does not replace the researcher's epistemic responsibility.",
            "detailed": "Current AI tools accelerate literature discovery, suggest methodological patterns, and help structure writing. Interpretation of findings, ethical framing of questions, and validity judgements remain firmly with the human researcher. This distinction matters both practically and institutionally.",
            "doctoral_relevance": "Doctoral scholars must articulate where AI ends and their original intellectual contribution begins — a distinction increasingly required by journals and ethics committees.",
            "instructor_emphasis": "Ask: 'If AI found your research gap, does that gap belong to you?' This opens discussion on intellectual ownership."
        },
        "wrong_reasons": [
            "Option A overstates AI capability. Current AI cannot design rigorous studies — it can suggest designs, but not assess their suitability for a specific context.",
            "Option C is factually incorrect. AI outputs require human validation; no journal accepts AI as an author or sole analytical engine.",
            "Option D severely understates AI's role. AI applications span literature synthesis, hypothesis generation, and data analysis."
        ],
        "teaching_insight": "Students often hold either extreme: AI is magic or AI is useless. This question surfaces the nuanced middle ground.",
        "follow_up": "Name one research task where AI involvement raises an ethical question and explain why."
    },
    {
        "number": 2, "session": "S01", "difficulty": "Intermediate", "clo": "CLO 1",
        "concept": "AI Hallucination",
        "question": "A doctoral student uses an AI tool to generate a literature review summary. Which concern is MOST legitimate from a scholarly standpoint?",
        "options": [
            "The summary may be too well-written for the student's level",
            "The AI may fabricate citations or misrepresent source arguments, compromising the review's accuracy",
            "Using AI makes the literature review too long",
            "AI summaries are always accurate because they draw on large training datasets"
        ],
        "correct": 1,
        "explanation": {
            "concise": "AI language models hallucinate — they generate plausible-sounding but sometimes incorrect citations and summaries.",
            "detailed": "LLMs produce outputs by predicting statistically likely text, not by retrieving verified facts. They can invent journal names, volume numbers, and entire papers. For literature reviews, a fabricated citation that makes it into a published paper constitutes academic misconduct, even if unintentional.",
            "doctoral_relevance": "Every AI-assisted literature output must be cross-checked against the original source. This is not optional — it is a basic scholarly standard.",
            "instructor_emphasis": "Demonstrate live: ask ChatGPT for five citations on a topic, then verify each in Google Scholar. Expect at least one to be wrong."
        },
        "wrong_reasons": [
            "Option A is not a scholarly concern — writing quality is not an integrity issue in this context.",
            "Option C is irrelevant; length is not the problem here.",
            "Option D is false. Citation accuracy is particularly poor in generative AI."
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
            "detailed": "Most LLMs and semantic search tools are trained predominantly on English-language, Western academic outputs. For topics like trust, leadership, or ethics — where cultural context is central — this bias is not merely technical. It shapes the researcher's understanding of the phenomenon.",
            "doctoral_relevance": "Doctoral scholars must evaluate AI tools not only for accuracy but for representational coverage. A systematic review using AI must account for the tool's training data limitations.",
            "instructor_emphasis": "Ask: 'Who is missing from your AI-generated literature map?' This connects to debates about epistemic justice."
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
        "concept": "AI and Epistemology",
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
            "detailed": "Every training corpus reflects choices: which journals to include, which languages to index, which forms of knowledge count as 'evidence'. When AI tools are used unreflectively, they can reinforce positivist, Western, and quantitative epistemological frameworks at the expense of interpretivist, indigenous, or decolonial ways of knowing.",
            "doctoral_relevance": "Doctoral scholars working in critical management studies or non-mainstream traditions must be alert to how AI tools position their epistemological standpoint.",
            "instructor_emphasis": "Connect this to Haraway's 'situated knowledge' — no tool is god-trick objective. AI is a situated technology."
        },
        "wrong_reasons": [
            "Option A is a resource issue, not an epistemological critique.",
            "Option B is empirically contestable — AI does process qualitative data — and misses the philosophical point.",
            "Option D is a practical inconvenience, not an epistemic critique."
        ],
        "teaching_insight": "This question differentiates students who understand research philosophy from those who see methods as neutral techniques.",
        "follow_up": "How might a researcher using an interpretivist epistemology adapt AI tool use to remain epistemologically consistent?"
    },
    {
        "number": 5, "session": "S01", "difficulty": "Intermediate", "clo": "CLO 1, 8",
        "concept": "AI Authorship and Integrity",
        "question": "A student submits a literature review entirely generated by AI and lists themselves as the sole author. Which statement BEST characterises this situation?",
        "options": [
            "This is acceptable if the AI output is grammatically correct",
            "This is a form of academic misconduct equivalent to ghost-writing, and potentially constitutes plagiarism depending on institutional policy",
            "This is fine because AI tools do not hold copyright",
            "This is acceptable as long as the student reads the output before submitting"
        ],
        "correct": 1,
        "explanation": {
            "concise": "Submitting AI-generated work without disclosure is academic misconduct at most institutions.",
            "detailed": "Most universities now require disclosure of substantive AI use. Submitting a section the student did not write — regardless of whether the 'author' is human or machine — misrepresents the student's intellectual contribution. The question of copyright is separate from academic integrity.",
            "doctoral_relevance": "Journals now routinely require AI use statements. Doctoral students must understand appropriate use versus misrepresentation.",
            "instructor_emphasis": "Share your institution's current AI policy and any relevant journal policies (Nature, Elsevier) before this question."
        },
        "wrong_reasons": [
            "Option A confuses technical quality with integrity — grammatical correctness has no bearing on academic honesty.",
            "Option C conflates copyright (legal) with academic integrity (ethical). They are different.",
            "Option D is insufficient — reading AI output before submission does not constitute intellectual authorship."
        ],
        "teaching_insight": "Students often confuse 'using AI' with 'submitting AI work'. This question clarifies the boundary.",
        "follow_up": "Draft a two-sentence AI use disclosure statement for a research paper that used AI for literature search and initial drafting."
    },
]

# ── Activity ─────────────────────────────────────────────────────────────────
S01_ACTIVITY = {
    "title": "AI Tool Audit",
    "task": "Select any ONE AI research tool (Consensus.app, Elicit.org, Connected Papers, ResearchRabbit, or Semantic Scholar). Enter a research question relevant to your thesis area. Record: (a) how many results it returns, (b) whether citations are verifiable, (c) what the tool does NOT tell you about how it works.",
    "student_role": "Critical evaluator of AI research tools",
    "expected_output": "A one-page audit note covering the three recorded points above, plus one sentence on whether you would use this tool in a systematic review and why.",
    "time_minutes": 20,
    "sample_answer": "Using Consensus.app with the question 'Does AI adoption increase employee burnout?' — the tool returned 12 papers, 8 of which were verifiable in Google Scholar. Four citations could not be located. The tool does not disclose which databases it indexes or how its relevance algorithm works, making it unsuitable as a sole search tool for a systematic review. It is useful for rapid scoping but requires supplementation with Scopus or Web of Science.",
    "weak_answer": "I used Consensus.app and it gave me some papers about AI. The results look good. I would use it for my research.",
    "improved_answer": "I used Consensus.app to search 'AI adoption and employee trust in healthcare.' It returned 9 papers, but I could only verify 7 through Scopus — two references did not exist as stated. The tool gave no information about its indexing coverage or ranking algorithm. I would use it for initial scoping but not as the primary search tool in a systematic review, because PRISMA requires transparent, reproducible search documentation.",
    "debrief": "Ask: 'What would happen if you used only this tool for your literature review?' Lead students to see that tool limitations require multi-source strategies.",
    "grading_hints": "Award marks for: specificity of critique (not just 'it was good/bad'), evidence of verification, and clear reasoning on suitability.",
    "common_mistakes": "Students describe only what the tool does, not what it does not do or cannot tell them. Push them to the critical evaluation.",
    "scholarly_link": "This activity directly supports CLO 1 (critically evaluate AI tools) and prepares for systematic review methodology in S03–S04."
}

# ── Case ─────────────────────────────────────────────────────────────────────
S01_CASE = {
    "title": "The Confident Literature Review",
    "scenario": "Priya, a first-year doctoral student, spends 25 minutes on Consensus.app and ChatGPT, collects 15 AI-suggested citations, and submits a literature review section to her supervisor. She is confident the review is comprehensive because 'the AI found everything.' Her supervisor returns it with major revisions. Three of the citations do not exist. Two papers are misrepresented.",
    "question": "What went wrong, and what should Priya have done differently?",
    "weak_response": "Priya should have used a different AI tool.",
    "strong_response": "Priya made three errors: she relied on a single source type (generative AI) rather than a multi-source search strategy; she did not verify any citations against actual databases; and she conflated the appearance of comprehensiveness (15 papers) with actual comprehensiveness. She should have: (a) used Scopus or Web of Science for systematic search, (b) verified each citation before including it, and (c) understood the difference between generative AI (which produces plausible text) and search AI (which retrieves real indexed papers).",
    "issue_diagnosis": "Over-reliance on generative AI for literature search, combined with failure to verify citations.",
    "theory": "Generative AI hallucination is well-documented (Bender et al., 2021 — 'stochastic parrots'). AI produces probabilistically likely text, not verified facts.",
    "research_gap": "No gap per se — this is a methodological error, not a research gap.",
    "research_question": "Not applicable — the case is about method, not research design.",
    "scholarly_framing": "The scholarly standard is that every citation in a literature review must be verified against the original source. This applies regardless of how the citation was suggested.",
    "instructor_note": "Use this case to establish a non-negotiable class standard: every citation must be verified. Do this before students submit any literature review work."
}

# ── Diagram data ─────────────────────────────────────────────────────────────
def render_ai_research_landscape_diagram():
    import plotly.graph_objects as go

    fig = go.Figure()

    # Concentric zones
    fig.add_shape(type="circle", x0=-3, y0=-3, x1=3, y1=3,
                  line=dict(color="#1a3a6e", width=2), fillcolor="rgba(26,58,110,0.07)")
    fig.add_shape(type="circle", x0=-2, y0=-2, x1=2, y1=2,
                  line=dict(color="#c8a951", width=2), fillcolor="rgba(200,169,81,0.08)")
    fig.add_shape(type="circle", x0=-1, y0=-1, x1=1, y1=1,
                  line=dict(color="#1a7a4a", width=2), fillcolor="rgba(26,122,74,0.12)")

    # Labels
    annotations = [
        dict(x=0, y=0, text="<b>Human<br>Researcher</b>", showarrow=False,
             font=dict(size=13, color="#1a3a6e")),
        dict(x=0, y=1.5, text="AI Tools<br>(Assistance Layer)", showarrow=False,
             font=dict(size=11, color="#8a5a00")),
        dict(x=0, y=2.5, text="Scholarly Ecosystem<br>(Journals, Peers, Ethics Boards)", showarrow=False,
             font=dict(size=10, color="#1a3a6e")),
        dict(x=1.5, y=-0.4, text="Search AI<br>(Elicit, Consensus)", showarrow=True,
             ax=40, ay=-30, font=dict(size=10)),
        dict(x=-1.5, y=-0.4, text="Generative AI<br>(ChatGPT, Claude)", showarrow=True,
             ax=-40, ay=-30, font=dict(size=10)),
        dict(x=0, y=-1.5, text="Analysis AI<br>(NLP, Topic Models)", showarrow=True,
             ax=0, ay=30, font=dict(size=10)),
    ]
    fig.update_layout(
        annotations=annotations,
        xaxis=dict(visible=False, range=[-3.5, 3.5]),
        yaxis=dict(visible=False, range=[-3.5, 3.5]),
        height=420,
        margin=dict(l=10, r=10, t=30, b=10),
        title="AI Tools in the Research Ecosystem",
        title_font=dict(size=15, color="#1a3a6e"),
        plot_bgcolor="white",
        paper_bgcolor="white",
    )
    return fig


def render():
    # ── Header ───────────────────────────────────────────────────────────────
    session_header(
        code="S01",
        title="AI & the Research Landscape",
        clos=["CLO 1", "CLO 8"],
        why="Before using AI tools in research, scholars must understand what these tools are, how they work, and where their limits lie. This session builds the critical foundation for everything that follows."
    )

    teaching_flow([
        "Welcome & session framing (why this matters)",
        "Theoretical Concepts — types of AI, how they work",
        "Tell Me the Research Story (narrative reveal)",
        "Visual: AI Research Ecosystem Diagram",
        "Instructor-led demonstration (live AI tool use)",
        "Classroom Activity — AI Tool Audit",
        "Mini Case + Quiz",
    ])

    section_divider()

    # ── A. Theoretical Concepts ───────────────────────────────────────────────
    st.markdown("## 📖 A. Theoretical Concepts")
    st.markdown("*Read this section before class. It provides the conceptual foundation for all session activities.*")

    with st.expander("1. What is AI? (Simple Explanation)", expanded=False):
        concept_card(
            "Artificial Intelligence — Simple Definition",
            "AI refers to computer systems that perform tasks that normally require human intelligence: recognising patterns, understanding language, making decisions. In research, AI tools process large volumes of academic text and surface relevant information faster than any human could manually."
        )
        st.markdown("**Weak understanding:** 'AI is like a very fast Google.'")
        st.markdown("**Strong understanding:** 'AI uses statistical models trained on data to predict relevant outputs — it has no genuine understanding of content, which creates specific risks for scholarly use.'")
        warn_box("Common misconception: AI 'knows' things. In reality, AI predicts statistically likely text or rankings based on training patterns. It can be confidently wrong.")

    with st.expander("2. Types of AI Tools in Research", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            concept_card("Generative AI", "Produces new text (summaries, drafts, explanations). Examples: ChatGPT, Claude, Gemini. Risk: hallucination — fabricated citations, misrepresented findings.")
            concept_card("Semantic Search AI", "Retrieves existing indexed papers by meaning, not just keywords. Examples: Elicit, Consensus, Semantic Scholar. More reliable for citation discovery than generative AI.")
        with col2:
            concept_card("Citation Network AI", "Maps intellectual relationships between papers using co-citation patterns. Examples: Connected Papers, ResearchRabbit. Reveals conceptual clusters not visible through keyword search.")
            concept_card("Analysis AI", "Processes data — text, images, responses. Examples: NLP topic models, AI coding assistants, AI survey analysis. Requires methodological validation before publication.")
        st.markdown("**How it connects to CLO 1:** Critically evaluating AI tools means knowing which type to use for which task.")

    with st.expander("3. The Epistemic Authority Problem", expanded=False):
        gold_card(
            "Core Concept",
            "Epistemic authority = the right to assert knowledge claims. In research, this authority rests with the human researcher, not the AI tool. AI can assist the epistemic process but cannot bear epistemic responsibility."
        )
        st.markdown("""
**Why this matters for doctoral research:**
- If an AI tool makes an error, the researcher is responsible — not the tool.
- Journal retractions due to AI hallucination are the researcher's problem, not OpenAI's.
- Intellectual contribution (what makes the work yours) must be distinguishable from AI-assisted task execution.

**Weak version:** 'I used AI to help me, so the work is partially AI's.'

**Strong version:** 'AI assisted with specific tasks; the research questions, theoretical framing, interpretation of findings, and scholarly judgement are entirely mine.'
        """)
        st.markdown("**Common misconception:** Using AI means sharing intellectual credit. Incorrect — tools (whether a calculator, SPSS, or ChatGPT) are aids to human thinking, not co-thinkers.")
        st.markdown("**Instructor note:** Ask students: 'Would you credit Microsoft Word as a co-author because it corrected your spelling?' The logic is the same.")

    with st.expander("4. AI Hallucination — What It Is and Why It Matters", expanded=False):
        st.markdown("""
**What hallucination means:**
Large language models predict the next word/sentence based on statistical patterns in training data. They do not 'look up' facts. When a model encounters a gap in its training data, it fills that gap with statistically plausible but potentially fictitious content.

**Research implications:**
- Fabricated journal names, volume numbers, page ranges
- Papers that sound real but do not exist
- Real papers with misrepresented arguments
- Authors attributed to papers they did not write

**Verification protocol (mandatory):**
1. Copy every AI-suggested citation into Scopus, Google Scholar, or the journal website
2. Verify author, title, year, journal, DOI
3. Read at least the abstract before citing
4. Do not cite based on AI summary alone — read the original

**Why this matters at doctoral level:**
A single fabricated citation in a published paper constitutes academic misconduct. Ignorance of the AI's error is not an accepted defence.
        """)

    with st.expander("5. Weak vs Strong Understanding — Summary Table", expanded=False):
        st.markdown("""
| Concept | Weak Understanding | Strong Understanding |
|---|---|---|
| AI role in research | AI does research for me | AI assists specific tasks; I retain interpretive authority |
| AI accuracy | AI is accurate because it uses big data | AI is probabilistically plausible; accuracy must be verified |
| AI tools | All AI tools do the same thing | Different AI types (generative, search, network, analysis) serve different functions |
| AI authorship | AI-assisted work is partially AI's | Tools are not authors; intellectual contribution remains human |
| AI bias | AI is neutral and objective | AI encodes training data biases; corpus composition shapes outputs |
        """)

    section_divider()

    # ── B. Tell Me the Research Story ────────────────────────────────────────
    st.markdown("## 📖 B. Tell Me the Research Story")
    st.markdown("*Click below to reveal an engaging narrative for classroom storytelling.*")

    if st.button("🎭 Tell Me the Research Story", key="s01_story"):
        st.markdown("""
<div class="gold-card">
<strong>The Researcher and the Oracle</strong><br><br>

Imagine a scholar in 1990 who wants to understand everything ever written about employee trust. She sits in a library for three months, reading, taking notes, building a map of ideas by hand. The process is slow. She misses papers. Some journals are only available across the country. She makes do.

Now imagine her counterpart today. He sits down, types a question into Elicit, and in ninety seconds has a list of the most relevant papers across thirty years of research. He asks ChatGPT to summarise the consensus. He opens Connected Papers and sees a visual map of how ideas connect. He finishes what took his predecessor three months in an afternoon.

But here is the question that matters: has he understood anything?

The 1990 scholar read everything slowly. She noticed the contradiction between two papers no algorithm would have flagged. She saw that researchers in Japan and Brazil asked the same question but framed it entirely differently. She developed, over those three months, a genuine conceptual map in her own mind.

Her counterpart has a list. A fast, comprehensive, AI-generated list. What he does with it — the connections he draws, the questions he asks, the gaps he notices — that is the scholarship. The AI got him to the starting line faster. The race itself is still his to run.

This is the central tension of this course. AI is genuinely useful. It would be foolish to ignore it. But it is a tool, not a mind. And the most important things it cannot do — judge, interpret, question, and take responsibility — are precisely the things that make research worth doing.

<em>Use this in class: ask students to name one thing the AI-assisted researcher might miss that the slow reader would catch.</em>
</div>
""", unsafe_allow_html=True)

    section_divider()

    # ── C. Visual Explanation ─────────────────────────────────────────────────
    st.markdown("## 📊 C. Visual Explanation: AI in the Research Ecosystem")
    st.markdown("*The diagram below shows how AI tools relate to the human researcher and the broader scholarly ecosystem.*")

    try:
        import plotly.graph_objects as go
        fig = render_ai_research_landscape_diagram()
        st.plotly_chart(fig, use_container_width=True)
    except ImportError:
        st.info("Install plotly to see the interactive diagram: `pip install plotly`")

    with st.expander("🔍 How to Interpret This Diagram"):
        st.markdown("""
**Centre circle (green):** The human researcher — the locus of epistemic authority, interpretive judgement, and scholarly accountability.

**Middle ring (gold):** AI tools — they assist tasks in the assistance layer but do not replace the researcher at the centre. The three tool types (Search AI, Generative AI, Analysis AI) orbit the researcher, not the other way around.

**Outer ring (blue):** The scholarly ecosystem — journals, peer reviewers, ethics boards, and the academic community. This ecosystem validates research, and its standards apply regardless of how AI was used.

**Key insight:** AI tools are in the middle ring, not the centre. They serve the researcher; the researcher does not serve the algorithm.

**Classroom discussion prompt:** Draw this diagram on the board and ask: 'What happens if a researcher puts the AI in the centre and themselves in the middle ring?'

**CLO connection:** CLO 1 — critically evaluating AI tools means understanding their position in the research process, not simply learning to use them.
        """)

    section_divider()

    # ── D. Instructor-Led Demonstration ──────────────────────────────────────
    st.markdown("## 🎓 D. Instructor-Led Demonstration")

    with st.expander("Step-by-Step Classroom Demo: Spotting AI Hallucination"):
        st.markdown("""
**Setup (before class):** Open ChatGPT or any LLM in a browser tab, ready to project.

**Step 1 — Generate citations (3 minutes)**
Ask the AI: *"Give me five recent, highly cited papers on AI adoption in healthcare organisations."*
Show students the result. It looks authoritative — authors, journals, years.

**Step 2 — Verify in real time (5 minutes)**
Take the first three citations. Open Google Scholar (or Scopus) and search for each.
Ask students to watch and predict: will we find them?
Typically, 1–2 will either not exist, have wrong details, or be misattributed.

**Step 3 — Debrief (5 minutes)**
Ask: *"What does this tell you about using AI for citation generation?"*
Expected student responses: don't trust it blindly / always verify / use it for ideas not facts.

**Step 4 — Contrast with Elicit (5 minutes)**
Run the same query in Elicit.org. Show how it retrieves actual indexed papers (not generated text), with links to source documents.
Ask: *"What is the fundamental difference between what ChatGPT did and what Elicit did?"*

**Step 5 — Conclusion**
Summarise: Generative AI predicts; search AI retrieves. Both are useful. Neither replaces verification.

**What to ask students:**
- 'Before today, how many of you had verified AI-suggested citations?' (hands up)
- 'After today, will your workflow change?' (discuss)

**How to conclude:**
'The skill is not avoiding AI — it is using it with appropriate scepticism. That scepticism is what this course trains.'
        """)

    section_divider()

    # ── E. Classroom Activity ─────────────────────────────────────────────────
    st.markdown("## 🏋️ E. Classroom Activity")
    render_activity(S01_ACTIVITY, key="s01_act")

    section_divider()

    # ── F. Mini Case ──────────────────────────────────────────────────────────
    st.markdown("## 📋 F. Mini Case")
    render_case(S01_CASE, key="s01_case")

    section_divider()

    # ── G. Quiz ───────────────────────────────────────────────────────────────
    st.markdown("## 📝 G. Session Quiz")
    render_quiz_block(S01_QUIZ, key_prefix="s01", title="Session 01 — Five Questions")

    section_divider()

    # ── H. Reflection & Output ────────────────────────────────────────────────
    st.markdown("## ✅ H. Reflection & Output")
    st.markdown("""
**After this session, you should be able to:**
- [ ] Distinguish between generative AI and AI-powered search tools
- [ ] Describe at least two risks of using AI without verification in academic research
- [ ] Explain what 'epistemic authority' means and why it rests with the researcher, not the AI
- [ ] Verify a citation provided by an AI tool using Scopus or Google Scholar
- [ ] Draft a one-sentence AI use disclosure

**What to produce before the next session:**
Write a one-paragraph 'AI tool evaluation note' for one tool you have used or plan to use, addressing: (a) what it does, (b) what it does not disclose about how it works, and (c) one scholarly use case where you would and one where you would not trust its output.

**Link to assessment:**
This session's concepts underpin the AI tool transparency criteria in the Annotated Bibliography assignment (Sessions 3–4) and the philosophical positioning section of the Research Proposal.
    """)
