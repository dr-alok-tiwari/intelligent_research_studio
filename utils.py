"""Shared utilities — uses CSS classes defined in app.py global styles."""
import streamlit as st


def concept_card(title: str, body: str):
    st.markdown(f'<div class="concept-card"><strong>{title}</strong>{body}</div>', unsafe_allow_html=True)


def gold_card(title: str, body: str):
    st.markdown(f'<div class="gold-card"><strong>{title}</strong> {body}</div>', unsafe_allow_html=True)


def reveal_box(body: str):
    st.markdown(f'<div class="reveal-box">{body}</div>', unsafe_allow_html=True)


def warn_box(body: str):
    st.markdown(f'<div class="warn-box">⚠️ {body}</div>', unsafe_allow_html=True)


def section_divider():
    st.markdown('<hr class="divider">', unsafe_allow_html=True)


def session_header(code: str, title: str, clos: list, why: str):
    pills = "".join(f'<span class="pill pill-clo">{c}</span>' for c in clos)
    st.markdown(f"""
<div class="page-banner">
  <div class="banner-tag">Session {code}</div>
  <div class="banner-h">{title}</div>
  <div class="banner-p">{why}</div>
  <div class="banner-pills">{pills}</div>
</div>""", unsafe_allow_html=True)


def teaching_flow(steps: list):
    st.markdown("### 🕐 75-Minute Teaching Flow")
    durations = [5, 10, 15, 15, 15, 10, 5]
    rows = ""
    for i, step in enumerate(steps):
        dur = durations[i] if i < len(durations) else 10
        rows += f"<tr><td><span class='flow-n'>{i+1}</span></td><td>{step}</td><td>{dur} min</td></tr>"
    st.markdown(f"""
<table class="flow-table">
  <thead><tr><th>#</th><th>Activity</th><th>Time</th></tr></thead>
  <tbody>{rows}</tbody>
</table>""", unsafe_allow_html=True)


def render_quiz_question(q: dict, key_prefix: str):
    DIFF_MAP = {
        "Beginner": ("qbadge qb-beg", "🟢"),
        "Intermediate": ("qbadge qb-int", "🟡"),
        "Advanced": ("qbadge qb-adv", "🟠"),
        "Doctoral Challenge": ("qbadge qb-doc", "🔴"),
    }
    diff_cls, diff_icon = DIFF_MAP.get(q.get("difficulty", ""), ("qbadge", "⚪"))
    concept_safe = q.get("concept", "")
    clo_safe = q.get("clo", "")

    st.markdown(f"""
<div class="quiz-wrap">
  <div class="quiz-meta">
    <span class="{diff_cls}">{diff_icon} {q.get('difficulty','')}</span>
    <span class="qbadge qb-clo">{clo_safe}</span>
    <span class="qbadge qb-con">💡 {concept_safe}</span>
  </div>
  <div class="quiz-q">Q{q.get('number','')}. {q.get('question','')}</div>
</div>""", unsafe_allow_html=True)

    rkey = f"{key_prefix}_r_{q['number']}"
    skey = f"{key_prefix}_s_{q['number']}"
    revkey = f"{key_prefix}_rv_{q['number']}"
    shown = f"{key_prefix}_shown_{q['number']}"

    if shown not in st.session_state:
        st.session_state[shown] = False

    labels = [f"{chr(65+i)}. {opt}" for i, opt in enumerate(q["options"])]
    choice = st.radio("Choose your answer:", labels, index=None, key=rkey)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Submit Answer", key=skey):
            if choice is None:
                st.warning("Select an option first.")
            else:
                chosen = labels.index(choice)
                if chosen == q["correct"]:
                    st.success(f"✅ Correct! — {labels[q['correct']]}")
                else:
                    st.error(f"❌ Incorrect. You chose **{chr(65+chosen)}**. Correct: **{chr(65+q['correct'])}**.")
    with c2:
        if st.button("Reveal Answer", key=revkey):
            st.session_state[shown] = True

    if st.session_state[shown]:
        exp = q.get("explanation", {})
        correct_lbl = labels[q["correct"]]
        st.markdown(f"""
<div class="reveal-box">
  <strong>✅ Correct Answer: {correct_lbl}</strong><br><br>
  <strong>In brief:</strong> {exp.get('concise','')}<br><br>
  <strong>Full explanation:</strong> {exp.get('detailed','')}<br><br>
  <strong>Doctoral relevance:</strong> {exp.get('doctoral_relevance','')}<br><br>
  <strong>Instructor emphasis:</strong> {exp.get('instructor_emphasis','')}
</div>""", unsafe_allow_html=True)
        wrong_opts = [j for j in range(4) if j != q["correct"]]
        st.markdown("**Why the other options are wrong:**")
        for idx, reason in zip(wrong_opts, q.get("wrong_reasons", [])):
            st.markdown(f"- **{chr(65+idx)}.** {reason}")
        with st.expander("📌 Teaching Insight & Follow-up"):
            st.markdown(f"**Teaching Insight:** {q.get('teaching_insight','')}")
            st.markdown(f"**Follow-up Discussion:** {q.get('follow_up','')}")


def render_quiz_block(questions: list, key_prefix: str, title: str = "Quiz"):
    st.markdown(f"### 📝 {title}")
    for q in questions:
        render_quiz_question(q, key_prefix)


def render_activity(a: dict, key: str):
    st.markdown(f"""
<div class="activity-card">
  <div class="activity-head">
    <div class="activity-icon">🏋️</div>
    <div>
      <div class="activity-title">{a['title']}</div>
      <div class="activity-sub">Student role: {a.get('student_role','')}</div>
    </div>
    <div class="time-pill">⏱ {a.get('time_minutes',20)} min</div>
  </div>
  <div class="activity-body"><strong>Task:</strong> {a['task']}</div>
  <div class="activity-sub"><strong>Expected output:</strong> {a.get('expected_output','')}</div>
</div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Show Suggested Solution", key=f"act_sol_{key}"):
            st.markdown(f"""
<div class="reveal-box">
  <strong>Sample High-Quality Answer:</strong><br>{a.get('sample_answer','')}<br><br>
  <strong>Weak Answer (avoid):</strong><br>{a.get('weak_answer','')}<br><br>
  <strong>Improved Version:</strong><br>{a.get('improved_answer','')}
</div>""", unsafe_allow_html=True)
    with c2:
        if st.button("Show Debrief Points", key=f"act_deb_{key}"):
            st.markdown(f"**Debrief:** {a.get('debrief','')}")
            st.markdown(f"**Grading Hints:** {a.get('grading_hints','')}")
            st.markdown(f"**Common Mistakes:** {a.get('common_mistakes','')}")


def render_case(c: dict, key: str):
    st.markdown(f"""
<div class="case-card">
  <div class="case-title">📋 {c['title']}</div>
  <div class="case-scenario"><strong>Scenario:</strong> {c['scenario']}</div>
  <div class="case-question">❓ {c['question']}</div>
</div>""", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Show Weak Response", key=f"case_weak_{key}"):
            warn_box(c.get("weak_response", ""))
    with c2:
        if st.button("Show Strong Response", key=f"case_strong_{key}"):
            reveal_box(c.get("strong_response", ""))
    with c3:
        if st.button("Reveal Full Analysis", key=f"case_full_{key}"):
            st.markdown(f"""
<div class="reveal-box">
  <strong>Issue Diagnosis:</strong> {c.get('issue_diagnosis','')}<br><br>
  <strong>Theoretical Interpretation:</strong> {c.get('theory','')}<br><br>
  <strong>Research Gap Identified:</strong> {c.get('research_gap','')}<br><br>
  <strong>Possible Research Question:</strong> {c.get('research_question','')}<br><br>
  <strong>Stronger Scholarly Framing:</strong> {c.get('scholarly_framing','')}<br><br>
  <strong>Instructor Note:</strong> {c.get('instructor_note','')}
</div>""", unsafe_allow_html=True)
