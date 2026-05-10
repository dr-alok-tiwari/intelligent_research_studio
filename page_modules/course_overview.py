import streamlit as st

def render():
    st.markdown("""
<div class="page-banner">
  <div class="banner-tag">Course Overview</div>
  <div class="banner-h">Intelligent Research:<br>AI Applications &amp; Techniques</div>
  <div class="banner-p">Programme context, session sequence, assessment alignment, and integrated AI tools.</div>
</div>""", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📖 Programme Context", "📅 Session Sequence", "📊 Assessment", "🛠️ AI Tools Used"])

    with tab1:
        st.markdown("### Programme Context")
        st.markdown("""
This course sits within the PGDM-BDA and PGDM-HCM programmes at the Goa Institute of Management.
It addresses a gap that most research methodology courses leave open: not just *what* to do in a research
project, but *how AI tools change the way scholars read, think, write, and communicate*.

The 16 sessions move from conceptual foundations to practical application, ending with a capstone that
requires students to produce a complete research proposal section using the tools and frameworks discussed.

The course assumes students can read academic papers but does not assume prior programming or data
science experience. Tools introduced are no-code or low-code wherever possible.
        """)

        st.markdown("### Design Principles")
        for p in [
            ("Critical over Uncritical", "Every AI tool is introduced alongside its limitations, biases, and risks. The course trains users, not promoters."),
            ("Doctoral Level Rigour", "Content is pitched at doctoral standard — relevant for PhD and PGDM students producing original research."),
            ("Immediate Applicability", "Each session produces a deliverable that feeds directly into the Research Proposal assessment."),
            ("No Placeholders", "Every section of the app contains complete, usable content — no 'content to be added' anywhere."),
        ]:
            st.markdown(f"""
<div class="concept-card">
  <strong>{p[0]}</strong>{p[1]}
</div>""", unsafe_allow_html=True)

    with tab2:
        st.markdown("### Session Sequence")
        sessions = [
            ("S01","AI & the Research Landscape","CLO 1","Situating AI in scholarly practice"),
            ("S02","Research Problem Identification & Gap Analysis","CLO 2","From curiosity to researchable problem"),
            ("S03","AI-Assisted Literature Search","CLO 3","Beyond Google Scholar"),
            ("S04","Systematic Review & PRISMA","CLO 3","Rigour in evidence synthesis"),
            ("S05","Research Questions & Hypotheses","CLO 2, 5","Precision in inquiry framing"),
            ("S06","Theoretical Frameworks","CLO 4","Grounding research in theory"),
            ("S07","Quantitative Methods with AI","CLO 5","Survey, scale, and statistical design"),
            ("S08","Qualitative Methods with AI","CLO 5","Interview, coding, and thematic analysis"),
            ("S09","Mixed Methods & AI Integration","CLO 5","Integration logics and design"),
            ("S10","AI for Data Collection","CLO 6","Instruments, ethics, and bias"),
            ("S11","AI-Assisted Analysis & Interpretation","CLO 6","From output to argument"),
            ("S12","Academic Writing with AI","CLO 7","Voice, structure, and integrity"),
            ("S13","Citation, Plagiarism & Research Ethics","CLO 7, 8","Integrity in the AI era"),
            ("S14","Peer Review & Revision","CLO 7","Scholarly dialogue and revision"),
            ("S15","Dissemination & Publication Strategy","CLO 7, 8","Getting research read"),
            ("S16","Capstone & the Future of AI Research","CLO 1–8","Synthesis and outlook"),
        ]
        for code, title, clo, theme in sessions:
            with st.expander(f"**{code}**  ·  {title}"):
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown(f"**CLO:** {clo}")
                with col2:
                    st.markdown(f"**Theme:** {theme}")
                if st.button(f"Open {code} →", key=f"co_open_{code.lower()}"):
                    st.session_state.current_page = code.lower(); st.rerun()

    with tab3:
        st.markdown("### Assessment Alignment")
        st.markdown("""
| Component | Weight | Sessions Covered |
|---|---|---|
| Formative Quizzes (best 8 of 16) | 20% | All |
| Annotated Bibliography Assignment | 20% | S03, S04 |
| Research Proposal (Sections 1–3) | 30% | S02, S05, S06 |
| Reflective Portfolio | 15% | S12, S13, S15 |
| Final Presentation (Capstone) | 15% | S16 |
        """)
        st.markdown("### Session → Proposal Section Mapping")
        st.markdown("""
| Proposal Section | Primary Sessions | Supporting Sessions |
|---|---|---|
| 1. Background & Problem Statement | S02 | S01, S03 |
| 2. Literature Review | S03, S04 | S01 |
| 3. Theoretical Framework | S06 | S05 |
| 4. Research Questions & Hypotheses | S05 | S06 |
| 5. Methodology | S07/S08/S09 | S10 |
| 6. Data Analysis Plan | S11 | S07–S09 |
| 7. Ethics Statement | S13 | S10 |
        """)

    with tab4:
        st.markdown("### AI Tools Integrated in This Course")
        tools = [
            ("Consensus.app",       "Evidence-based literature discovery — asks research questions and returns synthesised answers"),
            ("Elicit.org",          "Research question decomposition and structured literature mapping"),
            ("Connected Papers",    "Citation network visualisation — shows intellectual lineage of a field"),
            ("ResearchRabbit",      "Literature mapping and new paper alerts in your research area"),
            ("Semantic Scholar",    "Open-access semantic search with 200M+ papers"),
            ("Scite.ai",            "Citation context — shows whether papers support, contrast, or mention a claim"),
            ("Zotero",              "Reference management — integrates with AI plugins for annotation"),
            ("ChatGPT / Claude",    "Drafting, paraphrasing, structuring — with strong critical caution required"),
            ("Atlas.ti (AI mode)",  "AI-assisted qualitative coding — human validation mandatory"),
            ("PROCESS macro (Hayes)","Mediation and moderation analysis — standard tool in management research"),
            ("VOSviewer",           "Bibliometric network visualisation for systematic reviews"),
            ("Tableau Public",      "Data visualisation for mixed methods presentations"),
        ]
        cols = st.columns(2)
        for i, (tool, use) in enumerate(tools):
            with cols[i % 2]:
                st.markdown(f"""
<div style="background:var(--slate);border:1px solid var(--border);border-radius:10px;
padding:.7rem .9rem;margin-bottom:.55rem">
  <div style="font-weight:700;font-size:.85rem;color:var(--navy);margin-bottom:.25rem">🔧 {tool}</div>
  <div style="font-size:.78rem;color:var(--muted);line-height:1.5">{use}</div>
</div>""", unsafe_allow_html=True)
