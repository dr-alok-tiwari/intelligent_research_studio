import streamlit as st

SESSION_DATA = [
    ("s01","AI & Research Landscape",     "CLO 1",  "Situating AI in scholarly practice"),
    ("s02","Research Problem & Gap",       "CLO 2",  "From curiosity to researchable problem"),
    ("s03","AI Literature Search",         "CLO 3",  "Beyond Google Scholar"),
    ("s04","Systematic Review & PRISMA",   "CLO 3",  "Rigour in evidence synthesis"),
    ("s05","Research Questions",           "CLO 2,5","Precision in inquiry framing"),
    ("s06","Theoretical Frameworks",       "CLO 4",  "Grounding research in theory"),
    ("s07","Quantitative Methods",         "CLO 5",  "Survey, scale, statistical design"),
    ("s08","Qualitative Methods",          "CLO 5",  "Interview, coding, thematic analysis"),
    ("s09","Mixed Methods & AI",           "CLO 5",  "Integration logics and design"),
    ("s10","AI for Data Collection",       "CLO 6",  "Instruments, ethics, and bias"),
    ("s11","Analysis & Interpretation",    "CLO 6",  "From output to argument"),
    ("s12","Academic Writing with AI",     "CLO 7",  "Voice, structure, and integrity"),
    ("s13","Citation, Ethics & Integrity", "CLO 7,8","Integrity in the AI era"),
    ("s14","Peer Review & Revision",       "CLO 7",  "Scholarly dialogue and revision"),
    ("s15","Scholarly Dissemination",      "CLO 7,8","Getting research read"),
    ("s16","Capstone & Future of AI",      "CLO 1-8","Synthesis and outlook"),
]

def render():
    st.markdown("""
<div class="page-banner">
  <div class="banner-tag">GIM · FPM · 2025–26</div>
  <div class="banner-h">Intelligent Research:<br>AI Applications &amp; Techniques</div>
  <div class="banner-p">A complete classroom teaching system — 16 sessions, 100+ quizzes, interactive activities,
  full case analyses, and visual diagrams. No external notes required.</div>
  <div class="banner-pills">
    <span class="pill pill-gold">📽️ Projector-Ready</span>
    <span class="pill pill-clo">16 Sessions</span>
    <span class="pill pill-clo">100+ Quiz Questions</span>
    <span class="pill pill-clo">Reveal-Based Interaction</span>
    <span class="pill pill-clo">No API Key Required</span>
  </div>
</div>""", unsafe_allow_html=True)

    # Stat row
    st.markdown("""
<div class="stat-row">
  <div class="stat-card"><div class="stat-n">16</div><div class="stat-l">Complete Teaching Sessions</div></div>
  <div class="stat-card"><div class="stat-n">100+</div><div class="stat-l">Quiz Questions with Explanations</div></div>
  <div class="stat-card"><div class="stat-n">8</div><div class="stat-l">Course Learning Outcomes</div></div>
  <div class="stat-card"><div class="stat-n">75'</div><div class="stat-l">Structured Teaching Flow / Session</div></div>
</div>""", unsafe_allow_html=True)

    col_l, col_r = st.columns([3, 2])
    with col_l:
        st.markdown("### How to Use This App")
        st.markdown("""
1. **Select a session** from the sidebar to access full teaching material.
2. **Toggle Projector Mode** from the sidebar before class for large-font display.
3. Work through each section: Concepts → Story → Visual → Demo → Activity → Case → Quiz → Reflection.
4. All answers hidden behind **Reveal** buttons — use during class discussion.
5. Visit the **Quiz Bank** for formative assessment or exam revision.
        """)
    with col_r:
        st.markdown("### Quick Access")
        if st.button("📚  Open Quiz Bank", use_container_width=True):
            st.session_state.current_page = "quiz_bank"; st.rerun()
        if st.button("📋  Course Overview", use_container_width=True):
            st.session_state.current_page = "course_overview"; st.rerun()
        if st.button("▶  Start with Session 01", use_container_width=True):
            st.session_state.current_page = "s01"; st.rerun()
        st.markdown("""
<div style="background:var(--gold-pale);border:1px solid rgba(200,169,81,.35);
border-radius:10px;padding:.75rem 1rem;margin-top:.5rem;font-size:.79rem;color:#8a5a00;line-height:1.6">
💡 <strong>Fully self-contained.</strong> No API key, no paid service, no placeholder content.
</div>""", unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("### All 16 Sessions")

    cols = st.columns(4)
    for i, (sid, title, clo, theme) in enumerate(SESSION_DATA):
        with cols[i % 4]:
            st.markdown(f"""
<div class="sess-card">
  <div class="sess-n">S{i+1:02d} · {clo}</div>
  <div class="sess-t">{title}</div>
  <div class="sess-c">{theme}</div>
</div>""", unsafe_allow_html=True)
            if st.button("Open →", key=f"hm_s_{sid}", use_container_width=True):
                st.session_state.current_page = sid; st.rerun()

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("### Course Learning Outcomes")
    clos = [
        ("CLO 1","Critically evaluate AI tools used in academic research workflows"),
        ("CLO 2","Formulate rigorous research problems and questions using AI-assisted gap analysis"),
        ("CLO 3","Conduct and report systematic literature reviews with AI search tools"),
        ("CLO 4","Apply appropriate theoretical frameworks informed by AI-assisted mapping"),
        ("CLO 5","Select and justify quantitative, qualitative, or mixed methods"),
        ("CLO 6","Interpret AI-generated outputs with scholarly integrity and epistemic caution"),
        ("CLO 7","Produce publication-ready academic writing, citations, and ethical declarations"),
        ("CLO 8","Reflect critically on the limitations, biases, and governance issues of AI in research"),
    ]
    cols2 = st.columns(2)
    for i, (code, desc) in enumerate(clos):
        with cols2[i % 2]:
            st.markdown(f"""
<div style="display:flex;gap:.55rem;align-items:flex-start;background:var(--slate);
border:1px solid var(--border);border-radius:10px;padding:.6rem .8rem;margin-bottom:.5rem">
  <div style="background:var(--navy);color:white;padding:.15rem .42rem;border-radius:5px;
  font-size:.62rem;font-weight:700;font-family:'DM Mono',monospace;white-space:nowrap;margin-top:.05rem">{code}</div>
  <div style="font-size:.79rem;color:var(--text);line-height:1.45">{desc}</div>
</div>""", unsafe_allow_html=True)
