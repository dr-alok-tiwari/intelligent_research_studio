import streamlit as st
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.quiz_bank_data import QUIZ_BANK

DIFF_MAP = {
    "Beginner":         ("qbadge qb-beg", "🟢"),
    "Intermediate":     ("qbadge qb-int", "🟡"),
    "Advanced":         ("qbadge qb-adv", "🟠"),
    "Doctoral Challenge":("qbadge qb-doc","🔴"),
}

def render_q(q, key_prefix):
    diff_cls, diff_icon = DIFF_MAP.get(q["difficulty"], ("qbadge", "⚪"))
    concept_safe = q.get("concept", "")
    clo_safe = q.get("clo", "")

    st.markdown(f"""
<div class="quiz-wrap">
  <div class="quiz-meta">
    <span class="{diff_cls}">{diff_icon} {q['difficulty']}</span>
    <span class="qbadge qb-clo">{clo_safe}</span>
    <span class="qbadge qb-con">💡 {concept_safe}</span>
  </div>
  <div class="quiz-q">Q{q['number']}. {q['question']}</div>
</div>""", unsafe_allow_html=True)

    rkey = f"{key_prefix}_r_{q['number']}"
    skey = f"{key_prefix}_s_{q['number']}"
    revkey = f"{key_prefix}_rv_{q['number']}"
    ans_key = f"{key_prefix}_ans_{q['number']}"
    rev_shown = f"{key_prefix}_shown_{q['number']}"

    if rev_shown not in st.session_state:
        st.session_state[rev_shown] = False

    labels = [f"{chr(65+i)}. {opt}" for i, opt in enumerate(q["options"])]
    choice = st.radio("Choose your answer:", labels, index=None, key=rkey)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Submit Answer", key=skey):
            if choice is None:
                st.warning("Please select an option first.")
            else:
                chosen = labels.index(choice)
                if chosen == q["correct"]:
                    st.success(f"✅ Correct! — {labels[q['correct']]}")
                else:
                    st.error(f"❌ Incorrect. You chose **{chr(65+chosen)}**. The correct answer is **{chr(65+q['correct'])}**.")
    with c2:
        if st.button("Reveal Answer", key=revkey):
            st.session_state[rev_shown] = True

    if st.session_state[rev_shown]:
        exp = q["explanation"]
        correct_lbl = labels[q["correct"]]
        st.markdown(f"""
<div class="reveal-box">
  <strong>✅ Correct Answer: {correct_lbl}</strong><br><br>
  <strong>In brief:</strong> {exp['concise']}<br><br>
  <strong>Full explanation:</strong> {exp['detailed']}<br><br>
  <strong>Why this matters for doctoral research:</strong> {exp['doctoral_relevance']}<br><br>
  <strong>What to emphasise in class:</strong> {exp['instructor_emphasis']}
</div>""", unsafe_allow_html=True)
        wrong_opts = [j for j in range(4) if j != q["correct"]]
        st.markdown("**Why the other options are wrong:**")
        for idx, reason in zip(wrong_opts, q.get("wrong_reasons", [])):
            st.markdown(f"- **{chr(65+idx)}.** {reason}")
        with st.expander("📌 Teaching Insight & Follow-up Question"):
            st.markdown(f"**Teaching Insight:** {q.get('teaching_insight','')}")
            st.markdown(f"**Follow-up Discussion:** {q.get('follow_up','')}")

def render():
    st.markdown("""
<div class="page-banner">
  <div class="banner-tag">Assessment Resource</div>
  <div class="banner-h">Quiz Bank</div>
  <div class="banner-p">100 questions across all 16 sessions — filter by session, difficulty level, or CLO.
  No answers are pre-selected. Use Reveal Answer buttons after class discussion.</div>
  <div class="banner-pills">
    <span class="pill pill-gold">🟢 Beginner</span>
    <span class="pill pill-clo">🟡 Intermediate</span>
    <span class="pill pill-clo">🟠 Advanced</span>
    <span class="pill pill-clo">🔴 Doctoral Challenge</span>
  </div>
</div>""", unsafe_allow_html=True)

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        sessions = ["All"] + sorted(set(q["session"] for q in QUIZ_BANK))
        sel_s = st.selectbox("Filter by Session", sessions, key="qb_sess")
    with col2:
        diffs = ["All", "Beginner", "Intermediate", "Advanced", "Doctoral Challenge"]
        sel_d = st.selectbox("Filter by Difficulty", diffs, key="qb_diff")
    with col3:
        clos = ["All"] + sorted(set(q["clo"] for q in QUIZ_BANK))
        sel_c = st.selectbox("Filter by CLO", clos, key="qb_clo")

    filtered = QUIZ_BANK
    if sel_s != "All": filtered = [q for q in filtered if q["session"] == sel_s]
    if sel_d != "All": filtered = [q for q in filtered if q["difficulty"] == sel_d]
    if sel_c != "All": filtered = [q for q in filtered if q["clo"] == sel_c]

    # Summary metrics
    st.markdown(f"""
<div style="display:flex;gap:.6rem;align-items:center;margin:.8rem 0 1.2rem;flex-wrap:wrap">
  <div style="background:var(--slate);border:1px solid var(--border);border-radius:8px;
  padding:.4rem .9rem;font-size:.8rem;color:var(--navy);font-weight:600">
    Showing {len(filtered)} question{'s' if len(filtered)!=1 else ''}
  </div>
  {''.join(f"""<div style="background:var(--gold-pale);border:1px solid rgba(200,169,81,.3);
  border-radius:8px;padding:.4rem .9rem;font-size:.75rem;color:#8a5a00">
  {d}: {sum(1 for q in filtered if q['difficulty']==d)}
  </div>""" for d in ["Beginner","Intermediate","Advanced","Doctoral Challenge"] if any(q['difficulty']==d for q in filtered))}
</div>""", unsafe_allow_html=True)

    if not filtered:
        st.info("No questions match the selected filters.")
        return

    for q in filtered:
        render_q(q, "qbank")
