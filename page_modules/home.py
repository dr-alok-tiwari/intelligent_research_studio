import textwrap

import streamlit as st

SESSION_DATA = [
    ("s01", "AI & Research Landscape", "CLO 1", "Situating AI in scholarly practice", "🧭"),
    ("s02", "Research Problem & Gap", "CLO 2", "From curiosity to researchable problem", "🎯"),
    ("s03", "AI Literature Search", "CLO 3", "Beyond Google Scholar", "🔎"),
    ("s04", "Systematic Review & PRISMA", "CLO 3", "Rigour in evidence synthesis", "📊"),
    ("s05", "Research Questions", "CLO 2,5", "Precision in inquiry framing", "❓"),
    ("s06", "Theoretical Frameworks", "CLO 4", "Grounding research in theory", "🧩"),
    ("s07", "Quantitative Methods", "CLO 5", "Survey, scale, statistical design", "📈"),
    ("s08", "Qualitative Methods", "CLO 5", "Interview, coding, thematic analysis", "🎙️"),
    ("s09", "Mixed Methods & AI", "CLO 5", "Integration logics and design", "🔀"),
    ("s10", "AI for Data Collection", "CLO 6", "Instruments, ethics, and bias", "📝"),
    ("s11", "Analysis & Interpretation", "CLO 6", "From output to argument", "🧠"),
    ("s12", "Academic Writing with AI", "CLO 7", "Voice, structure, and integrity", "✍️"),
    ("s13", "Citation, Ethics & Integrity", "CLO 7,8", "Integrity in the AI era", "⚖️"),
    ("s14", "Peer Review & Revision", "CLO 7", "Scholarly dialogue and revision", "🛠️"),
    ("s15", "Scholarly Dissemination", "CLO 7,8", "Getting research read", "📣"),
    ("s16", "Capstone & Future of AI", "CLO 1-8", "Synthesis and outlook", "🚀"),
]


def _pdf_escape(text: str) -> str:
    replacements = {"—": "-", "–": "-", "•": "-", "→": "->", "©": "(c)", "’": "'", "“": '"', "”": '"'}
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = text.encode("latin-1", "replace").decode("latin-1")
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _handbook_rows():
    sections = [
        ("Intelligent Research Studio - User Handbook", [
            "Course: Intelligent Research: AI Applications & Techniques",
            "Creator: Dr. Alok Tiwari, Assistant Professor - Big Data Analytics",
            "Purpose: A classroom-ready teaching studio for FPM/doctoral research training.",
        ]),
        ("1. Start Here", [
            "Open the Home page first. Read the orientation block, then use the left sidebar to move through the course.",
            "Use Projector Mode before class when the app is shown on a classroom screen.",
            "The app is self-contained: sessions, cases, activities, quizzes, reflections, and course overview are built in.",
        ]),
        ("2. Recommended Classroom Flow", [
            "Begin with the page banner and learning objective.",
            "Teach Concepts, then use Story/Demo/Activity sections to create discussion.",
            "Use Reveal buttons only after students attempt answers.",
            "End each session with reflection, quiz, or a short research-positioning exercise.",
        ]),
        ("3. Sidebar Navigation", [
            "The left sidebar is the control centre. It includes Home, Course Overview, Quiz Bank, and all 16 sessions.",
            "Session progress dots show where the current session sits in the course journey.",
            "The sidebar is intentionally kept visible and readable for live classroom teaching.",
        ]),
        ("4. Academic Integrity Reminder", [
            "Do not paste confidential data into public AI tools.",
            "Always verify references, methods, claims, and generated summaries.",
            "Disclose AI assistance where institutional or journal policy requires it.",
        ]),
        ("5. Troubleshooting", [
            "If the sidebar looks collapsed, widen the browser window or use the top-left sidebar control.",
            "If content appears small in class, enable Projector Mode.",
            "If a page shows an error, refresh the app and reopen the session from the sidebar.",
        ]),
        ("6. Copyright", ["(c) Dr. Alok Tiwari. All rights reserved."]),
    ]
    rows = []
    for heading, bullets in sections:
        rows.append(("heading", heading))
        for bullet in bullets:
            for line in textwrap.wrap(bullet, width=92):
                rows.append(("body", line))
        rows.append(("space", ""))
    return rows


@st.cache_data(show_spinner=False)
def build_handbook_pdf() -> bytes:
    rows = _handbook_rows()
    pages, current, line_count = [], [], 0
    for kind, text in rows:
        needed = 2 if kind == "heading" else 1
        if line_count + needed > 42:
            pages.append(current)
            current, line_count = [], 0
        current.append((kind, text))
        line_count += needed
    if current:
        pages.append(current)

    objects = ["<< /Type /Catalog /Pages 2 0 R >>", "", "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>", "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>"]
    page_ids = []
    for page in pages:
        page_id = len(objects) + 1
        content_id = len(objects) + 2
        page_ids.append(page_id)
        objects.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents {content_id} 0 R >>")
        y = 748
        commands = []
        if page_id == page_ids[0]:
            commands.append(f"BT /F2 18 Tf 1 0 0 1 54 770 Tm ({_pdf_escape('Intelligent Research Studio')}) Tj ET")
            y = 735
        for kind, text in page:
            if kind == "space":
                y -= 8
            elif kind == "heading":
                y -= 8
                commands.append(f"BT /F2 13 Tf 1 0 0 1 54 {y} Tm ({_pdf_escape(text)}) Tj ET")
                y -= 18
            else:
                commands.append(f"BT /F1 10.5 Tf 1 0 0 1 68 {y} Tm ({_pdf_escape(text)}) Tj ET")
                y -= 14
        footer = f"Page {len(page_ids)} of {len(pages)}  |  (c) Dr. Alok Tiwari"
        commands.append(f"BT /F1 8.5 Tf 1 0 0 1 54 32 Tm ({_pdf_escape(footer)}) Tj ET")
        stream = "\n".join(commands)
        objects.append(f"<< /Length {len(stream.encode('latin-1'))} >>\nstream\n{stream}\nendstream")
    objects[1] = f"<< /Type /Pages /Kids [{' '.join(f'{pid} 0 R' for pid in page_ids)}] /Count {len(page_ids)} >>"

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for obj_id, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{obj_id} 0 obj\n".encode("latin-1"))
        pdf.extend(obj.encode("latin-1"))
        pdf.extend(b"\nendobj\n")
    xref_start = len(pdf)
    pdf.extend(f"xref\n0 {len(objects)+1}\n".encode("latin-1"))
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode("latin-1"))
    pdf.extend(f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n".encode("latin-1"))
    return bytes(pdf)


def render():
    st.markdown("""
<div class="page-banner">
  <div class="banner-tag">GIM · FPM · 2025–26</div>
  <div class="banner-h">Intelligent Research:<br>AI Applications &amp; Techniques</div>
  <div class="banner-p">A vibrant classroom teaching system for research scholars — with structured sessions,
  reveal-based activities, cases, prompts, quizzes, and a downloadable handbook for first-time users.</div>
  <div class="banner-pills">
    <span class="pill pill-gold">📽️ Projector-Ready</span>
    <span class="pill pill-clo">🧭 Visible Sidebar</span>
    <span class="pill pill-clo">📘 PDF Handbook</span>
    <span class="pill pill-clo">🎯 16 Sessions</span>
    <span class="pill pill-clo">🧠 No API Key Required</span>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown("### 📘 Begin Here: Handbook and Studio Guide")
    st.markdown("""
<div class="guide-grid">
  <div class="guide-card"><h4>1️⃣ Use the left sidebar</h4><p>Navigate Home, Course Overview, Quiz Bank, and all 16 sessions from the teaching sidebar.</p></div>
  <div class="guide-card"><h4>2️⃣ Teach session-by-session</h4><p>Each session follows a classroom pathway: concept, story, visual, demo, activity, case, quiz, and reflection.</p></div>
  <div class="guide-card"><h4>3️⃣ Reveal answers live</h4><p>Use reveal-based interaction after students attempt the question. This keeps the class active rather than passive.</p></div>
  <div class="guide-card"><h4>4️⃣ Switch Projector Mode</h4><p>Turn on Projector Mode from the sidebar before class for larger text and better classroom visibility.</p></div>
</div>""", unsafe_allow_html=True)

    dl_col, info_col = st.columns([1, 2])
    with dl_col:
        st.download_button(
            "📘 Download PDF Handbook",
            data=build_handbook_pdf(),
            file_name="Intelligent_Research_Studio_Handbook_Dr_Alok_Tiwari.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    with info_col:
        st.markdown("""
<div class="download-card"><h4>What the handbook includes</h4>
<p>Studio orientation, sidebar navigation, recommended classroom flow, student usage instructions,
academic integrity reminders, troubleshooting, and copyright details.</p></div>""", unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.markdown("""
<div class="stat-row">
  <div class="stat-card"><div class="stat-n">16</div><div class="stat-l">Complete Teaching Sessions</div></div>
  <div class="stat-card"><div class="stat-n">100+</div><div class="stat-l">Quiz Questions with Explanations</div></div>
  <div class="stat-card"><div class="stat-n">8</div><div class="stat-l">Course Learning Outcomes</div></div>
  <div class="stat-card"><div class="stat-n">75′</div><div class="stat-l">Structured Teaching Flow / Session</div></div>
</div>""", unsafe_allow_html=True)

    st.markdown("### ⚡ Quick Access")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📚 Open Quiz Bank", use_container_width=True):
            st.session_state.current_page = "quiz_bank"; st.rerun()
    with c2:
        if st.button("📋 Course Overview", use_container_width=True):
            st.session_state.current_page = "course_overview"; st.rerun()
    with c3:
        if st.button("▶ Start with Session 01", use_container_width=True):
            st.session_state.current_page = "s01"; st.rerun()

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("### 🗂️ All 16 Sessions")
    cols = st.columns(4)
    for i, (sid, title, clo, theme, icon) in enumerate(SESSION_DATA):
        with cols[i % 4]:
            st.markdown(f"""
<div class="sess-card">
  <div class="sess-n">{icon} S{i+1:02d} · {clo}</div>
  <div class="sess-t">{title}</div>
  <div class="sess-c">{theme}</div>
</div>""", unsafe_allow_html=True)
            if st.button(f"Open {icon}", key=f"hm_s_{sid}", use_container_width=True):
                st.session_state.current_page = sid; st.rerun()

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("### 🎯 Course Learning Outcomes")
    clos = [
        ("CLO 1", "Critically evaluate AI tools used in academic research workflows", "🧭"),
        ("CLO 2", "Formulate rigorous research problems and questions using AI-assisted gap analysis", "🎯"),
        ("CLO 3", "Conduct and report systematic literature reviews with AI search tools", "🔎"),
        ("CLO 4", "Apply appropriate theoretical frameworks informed by AI-assisted mapping", "🧩"),
        ("CLO 5", "Select and justify quantitative, qualitative, or mixed methods", "📊"),
        ("CLO 6", "Interpret AI-generated outputs with scholarly integrity and epistemic caution", "🧠"),
        ("CLO 7", "Produce publication-ready academic writing, citations, and ethical declarations", "✍️"),
        ("CLO 8", "Reflect critically on the limitations, biases, and governance issues of AI in research", "⚖️"),
    ]
    cols2 = st.columns(2)
    for i, (code, desc, icon) in enumerate(clos):
        with cols2[i % 2]:
            st.markdown(f"""
<div style="display:flex;gap:.7rem;align-items:flex-start;background:#ffffff;
border:1px solid var(--border);border-radius:14px;padding:.8rem .95rem;margin-bottom:.65rem;box-shadow:var(--shadow)">
  <div style="background:linear-gradient(135deg,var(--saffron),var(--rose));color:white;padding:.24rem .55rem;border-radius:9px;
  font-size:.78rem;font-weight:900;font-family:'DM Mono',monospace;white-space:nowrap;margin-top:.05rem">{icon} {code}</div>
  <div style="font-size:.96rem;color:var(--text);line-height:1.58;font-weight:600">{desc}</div>
</div>""", unsafe_allow_html=True)
