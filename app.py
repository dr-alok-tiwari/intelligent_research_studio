"""
Intelligent Research: AI Applications & Techniques
Complete Classroom Teaching System — GIM Panaji
Single-page app with session_state routing. No pages/ folder used.
"""
import streamlit as st
import importlib, sys, os

sys.path.insert(0, os.path.dirname(__file__))

st.set_page_config(
    page_title="Intelligent Research · GIM",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Session state defaults ──────────────────────────────────────────────
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "projector_mode" not in st.session_state:
    st.session_state.projector_mode = False

def nav_to(page):
    st.session_state.current_page = page

# ── GLOBAL STYLES ──────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

/* ── Variables ── */
:root {
  --navy:       #0f2147;
  --navy-mid:   #1a3a6e;
  --navy-light: #2a5298;
  --gold:       #c8a951;
  --gold-light: #e8cc7a;
  --gold-pale:  #fdf8ec;
  --slate:      #f0f4fb;
  --border:     #d4dff5;
  --text:       #1a1f2e;
  --muted:      #6b7a99;
  --success-bg: #edfaf3;
  --success-bd: #2d9960;
  --warn-bg:    #fff8e6;
  --warn-bd:    #e8a020;
  --shadow:     0 2px 12px rgba(15,33,71,.08);
  --shadow-lg:  0 8px 32px rgba(15,33,71,.15);
  --r:  10px;
  --rl: 16px;
}

/* ── Reset Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton, [data-testid="stSidebarNav"] { display: none !important; }
html, body, [class*="css"] { font-family: "DM Sans", sans-serif !important; color: var(--text); }
.main .block-container { padding: 1.4rem 2rem 3rem !important; max-width: 1180px; }

/* ═══════════════════════════════════════════
   SIDEBAR — definitive styles
═══════════════════════════════════════════ */
[data-testid="stSidebar"] { background: var(--navy) !important; }

/* Strip every default Streamlit padding/gap inside sidebar */
[data-testid="stSidebar"] > div:first-child,
[data-testid="stSidebar"] section,
[data-testid="stSidebar"] [data-testid="stSidebarContent"],
[data-testid="stSidebar"] .block-container { padding: 0 !important; gap: 0 !important; }
[data-testid="stSidebar"] .element-container { margin: 0 !important; padding: 0 !important; }
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0 !important; }
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div { margin: 0 !important; padding: 0 !important; }

/* Brand header */
.sb-brand {
  padding: 1.25rem 1rem .9rem;
  border-bottom: 1px solid rgba(200,169,81,.2);
  background: linear-gradient(150deg, #0c1730 0%, #1a3a6e 100%);
  position: relative; overflow: hidden;
}
.sb-brand::after {
  content:""; position:absolute; top:-35px; right:-35px;
  width:120px; height:120px; border-radius:50%;
  background: radial-gradient(circle, rgba(200,169,81,.13) 0%, transparent 70%);
}
.sb-logo {
  width:44px; height:44px; border-radius:11px;
  background: linear-gradient(135deg, #c8a951, #e8cc7a);
  display:flex; align-items:center; justify-content:center;
  font-size:1.4rem; margin-bottom:.65rem;
  box-shadow: 0 3px 12px rgba(200,169,81,.35);
}
.sb-name { font-family:"Playfair Display",serif; font-size:.96rem; font-weight:700; color:#fff; line-height:1.3; }
.sb-sub  { font-size:.63rem; color:rgba(200,169,81,.82); text-transform:uppercase; letter-spacing:.09em; margin-top:.2rem; }
.sb-inst { font-size:.61rem; color:rgba(255,255,255,.34); margin-top:.12rem; }

/* Section labels (MAIN / SESSIONS) */
.sb-sec {
  padding: .65rem 1rem .15rem;
  font-size: .57rem;
  text-transform: uppercase;
  letter-spacing: .14em;
  color: rgba(200,169,81,.48);
  font-weight: 700;
}

/* Progress dots */
.sb-progress { display:flex; gap:3px; flex-wrap:wrap; padding:.28rem 1rem .52rem; }
.sb-dot { width:7px; height:7px; border-radius:50%; background:rgba(255,255,255,.13); transition:all .2s; }
.sb-dot.done   { background:rgba(200,169,81,.52); }
.sb-dot.active { background:#c8a951; box-shadow:0 0 5px rgba(200,169,81,.55); }

/* Projector pill wrapper */
.sb-proj { padding: .42rem .8rem; }

/* Active stripe wrapper */
.sb-active-stripe > div { position: relative; }

/* Footer */
.sb-footer {
  padding: .8rem 1rem .95rem;
  border-top: 1px solid rgba(255,255,255,.06);
  font-size: .62rem; color: rgba(255,255,255,.38); line-height: 1.72;
}
.sb-footer-label {
  font-size: .58rem; font-weight:700; text-transform:uppercase;
  letter-spacing:.12em; color:rgba(200,169,81,.5); margin-bottom:.28rem;
}
.sb-footer-copy {
  margin-top:.28rem; padding-top:.28rem;
  border-top:1px solid rgba(255,255,255,.05);
  color:rgba(255,255,255,.25); font-size:.59rem;
}

/* ══════════════════════════════════
   THE BUTTON RULE — all: unset approach.
   Forces every element to be purely our styles.
   "all: unset" removes browser UA + Streamlit theme in one shot.
══════════════════════════════════ */
[data-testid="stSidebar"] .stButton,
[data-testid="stSidebar"] .stButton > div { width: 100% !important; display: block !important; }

[data-testid="stSidebar"] .stButton > button {
  all: unset;
  /* Box model */
  display: flex !important;
  align-items: center !important;
  justify-content: flex-start !important;
  width: 100% !important;
  box-sizing: border-box !important;
  /* Spacing */
  padding: .44rem 1rem !important;
  margin: 0 !important;
  /* Text */
  font-family: "DM Sans", sans-serif !important;
  font-size: .82rem !important;
  font-weight: 400 !important;
  line-height: 1.4 !important;
  color: rgba(255,255,255,.7) !important;
  text-align: left !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  /* Appearance */
  background: transparent !important;
  border-radius: 4px !important;
  cursor: pointer !important;
  transition: background .13s, color .13s !important;
}

/* Force ALL children left — Streamlit injects p, span, div */
[data-testid="stSidebar"] .stButton > button * {
  all: unset !important;
  font: inherit !important;
  color: inherit !important;
  text-align: left !important;
  display: inline !important;
  pointer-events: none !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
  background: rgba(255,255,255,.09) !important;
  color: #fff !important;
}

/* Active nav item — gold stripe */
.sb-active-stripe .stButton > button {
  background: rgba(200,169,81,.1) !important;
  color: #e8cc7a !important;
  font-weight: 600 !important;
  border-left: 3px solid #c8a951 !important;
  padding-left: calc(1rem - 3px) !important;
}
.sb-active-stripe .stButton > button * { color: #e8cc7a !important; }
.sb-active-stripe .stButton > button:hover { background: rgba(200,169,81,.15) !important; }

/* Projector button — overrides nav rule, centred */
.sb-proj .stButton > button {
  all: unset !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
  box-sizing: border-box !important;
  padding: .42rem .8rem !important;
  font-family: "DM Sans", sans-serif !important;
  font-size: .76rem !important;
  font-weight: 500 !important;
  color: rgba(255,255,255,.78) !important;
  text-align: center !important;
  background: rgba(255,255,255,.07) !important;
  border: 1px solid rgba(255,255,255,.15) !important;
  border-radius: 8px !important;
  cursor: pointer !important;
  transition: background .13s, color .13s, border-color .13s !important;
}
.sb-proj .stButton > button * {
  all: unset !important; font: inherit !important; color: inherit !important;
  text-align: center !important; display: inline !important;
}
.sb-proj .stButton > button:hover {
  background: rgba(200,169,81,.16) !important;
  border-color: rgba(200,169,81,.4) !important;
  color: #e8cc7a !important;
}

/* ═══════════════════════════════════════════
   PAGE BANNER
═══════════════════════════════════════════ */
.page-banner {
  background: linear-gradient(135deg, var(--navy) 0%, #1e4482 60%, #0f2147 100%);
  border-radius: var(--rl); padding: 1.8rem 2.2rem;
  margin-bottom: 1.8rem; position: relative; overflow: hidden;
  box-shadow: var(--shadow-lg);
}
.page-banner::before {
  content:""; position:absolute; bottom:-50px; right:-30px;
  width:220px; height:220px; border-radius:50%;
  background: radial-gradient(circle, rgba(200,169,81,.1) 0%, transparent 65%);
}
.banner-tag {
  display:inline-block; background:rgba(200,169,81,.18);
  color:var(--gold-light); padding:.18rem .65rem; border-radius:20px;
  font-size:.68rem; font-weight:700; text-transform:uppercase; letter-spacing:.1em;
  margin-bottom:.65rem; border:1px solid rgba(200,169,81,.3);
}
.banner-h { font-family:"Playfair Display",serif; font-size:1.85rem; font-weight:700;
  color:#fff; line-height:1.25; margin:0 0 .45rem; position:relative; z-index:1; }
.banner-p { font-size:.88rem; color:rgba(255,255,255,.6); max-width:580px;
  line-height:1.6; position:relative; z-index:1; }
.banner-pills { display:flex; gap:.4rem; flex-wrap:wrap; margin-top:.9rem; }
.pill { padding:.17rem .58rem; border-radius:20px; font-size:.67rem; font-weight:600; }
.pill-clo  { background:rgba(255,255,255,.1); color:rgba(255,255,255,.8); border:1px solid rgba(255,255,255,.15); }
.pill-gold { background:rgba(200,169,81,.2); color:var(--gold-light); border:1px solid rgba(200,169,81,.3); }

/* ─── STAT CARDS ─── */
.stat-row { display:grid; grid-template-columns:repeat(4,1fr); gap:.9rem; margin-bottom:1.8rem; }
.stat-card { background:#fff; border:1px solid var(--border); border-radius:var(--r);
  padding:1.1rem 1.3rem; box-shadow:var(--shadow); position:relative; overflow:hidden; transition:all .2s; }
.stat-card::after { content:""; position:absolute; top:0;left:0;right:0; height:3px; background:linear-gradient(90deg,var(--navy-mid),var(--gold)); }
.stat-card:hover { box-shadow:var(--shadow-lg); transform:translateY(-2px); }
.stat-n { font-family:"Playfair Display",serif; font-size:2.1rem; font-weight:700; color:var(--navy); line-height:1; }
.stat-l { font-size:.76rem; color:var(--muted); margin-top:.28rem; font-weight:500; }

/* ─── SESSION GRID ─── */
.sess-card { background:#fff; border:1px solid var(--border); border-radius:var(--r);
  padding:.9rem 1rem; cursor:pointer; transition:all .2s; box-shadow:var(--shadow); margin-bottom:.4rem; }
.sess-card:hover { border-color:var(--navy-mid); box-shadow:var(--shadow-lg); transform:translateY(-2px); }
.sess-n { font-family:"DM Mono",monospace; font-size:.62rem; font-weight:600; color:var(--gold); text-transform:uppercase; letter-spacing:.1em; }
.sess-t { font-size:.8rem; font-weight:600; color:var(--navy); margin-top:.28rem; line-height:1.3; }
.sess-c { font-size:.63rem; color:var(--muted); margin-top:.45rem; }

/* ─── CONTENT CARDS ─── */
.concept-card { background:var(--slate); border-left:4px solid var(--navy-mid);
  border-radius:0 var(--r) var(--r) 0; padding:.95rem 1.1rem; margin:.55rem 0; }
.concept-card strong { color:var(--navy); display:block; margin-bottom:.25rem; }
.gold-card { background:var(--gold-pale); border-left:4px solid var(--gold);
  border-radius:0 var(--r) var(--r) 0; padding:.95rem 1.1rem; margin:.55rem 0; }
.reveal-box { background:var(--success-bg); border:1px solid var(--success-bd);
  border-radius:var(--r); padding:1rem 1.2rem; margin:.65rem 0; }
.warn-box { background:var(--warn-bg); border:1px solid var(--warn-bd);
  border-radius:var(--r); padding:.75rem .95rem; margin:.55rem 0; font-size:.86rem; }

/* ─── QUIZ CARD ─── */
.quiz-wrap { background:#fff; border:1px solid var(--border); border-radius:var(--rl);
  padding:1.3rem 1.5rem; margin:1.1rem 0; box-shadow:var(--shadow); }
.quiz-meta { display:flex; gap:.45rem; flex-wrap:wrap; margin-bottom:.75rem; }
.qbadge { padding:.17rem .52rem; border-radius:20px; font-size:.63rem; font-weight:700; text-transform:uppercase; letter-spacing:.05em; }
.qb-beg { background:#e8f8ef; color:#0d6e3f; }
.qb-int { background:#fff8e6; color:#8a5a00; }
.qb-adv { background:#fef2f2; color:#9b2226; }
.qb-doc { background:#f0f0ff; color:#3730a3; }
.qb-clo { background:var(--slate); color:var(--navy-mid); }
.qb-con { background:#f5f5f5; color:#555; }
.quiz-q { font-size:.93rem; font-weight:500; color:var(--text); line-height:1.55;
  padding:.75rem .95rem; background:var(--slate); border-radius:var(--r);
  border-left:3px solid var(--gold); margin-bottom:.9rem; }

/* ─── TEACHING FLOW ─── */
.flow-table { width:100%; border-collapse:separate; border-spacing:0;
  border-radius:var(--r); overflow:hidden; box-shadow:var(--shadow); margin:1rem 0 1.5rem; }
.flow-table thead { background:var(--navy); }
.flow-table thead th { color:rgba(255,255,255,.82); font-size:.72rem; padding:.55rem .9rem; font-weight:600; text-align:left; }
.flow-table tbody tr:nth-child(even) { background:var(--slate); }
.flow-table tbody tr:nth-child(odd)  { background:#fff; }
.flow-table tbody td { padding:.5rem .9rem; font-size:.81rem; border-bottom:1px solid var(--border); }
.flow-table tbody tr:last-child td { border-bottom:none; }
.flow-n { display:inline-flex; align-items:center; justify-content:center;
  width:22px; height:22px; background:var(--navy); color:#fff;
  border-radius:50%; font-size:.63rem; font-weight:700; font-family:"DM Mono",monospace; }

/* ─── STORY ─── */
.story-card { background:linear-gradient(135deg,var(--navy) 0%,#1e4488 100%);
  border-radius:var(--rl); padding:1.8rem 2rem; color:#fff; position:relative; overflow:hidden;
  box-shadow:0 8px 32px rgba(15,33,71,.2); }
.story-card::before { content:"C"; position:absolute; top:-.5rem; left:1rem;
  font-family:"Playfair Display",serif; font-size:8rem; font-weight:700;
  color:rgba(200,169,81,.13); line-height:1; }
.story-t { font-family:"Playfair Display",serif; font-size:1.2rem; font-weight:700;
  color:var(--gold-light); margin-bottom:.9rem; position:relative; z-index:1; }
.story-b { font-size:.88rem; line-height:1.75; color:rgba(255,255,255,.84); position:relative; z-index:1; }
.story-prompt { margin-top:1.1rem; padding:.65rem .9rem;
  background:rgba(200,169,81,.14); border:1px solid rgba(200,169,81,.28);
  border-radius:8px; font-size:.8rem; color:var(--gold-light); font-style:italic; }

/* ─── DIVIDER ─── */
.divider { border:none; border-top:1px solid var(--border); margin:1.6rem 0; }

/* ═══════════════════════════════════════════
   STREAMLIT MAIN-AREA OVERRIDES
═══════════════════════════════════════════ */
.stExpander { border:1px solid var(--border) !important; border-radius:var(--r) !important; }
.stExpander summary { font-weight:600 !important; }

.main .stButton>button {
  background:var(--navy) !important; color:#fff !important;
  border:none !important; border-radius:8px !important;
  font-weight:600 !important; font-family:"DM Sans",sans-serif !important;
  transition:all .2s !important;
}
.main .stButton>button:hover {
  background:var(--navy-light) !important;
  transform:translateY(-1px) !important;
  box-shadow:0 4px 12px rgba(15,33,71,.22) !important;
}
div[data-testid="stRadio"] > label { font-weight:500; color:var(--navy); font-size:.9rem; }
.stTabs [data-baseweb="tab-list"] { background:var(--slate); border-radius:var(--r); padding:.3rem; gap:.2rem; }
.stTabs [data-baseweb="tab"] { border-radius:6px !important; font-weight:500 !important; color:var(--muted) !important; }
.stTabs [aria-selected="true"] { background:#fff !important; color:var(--navy) !important; box-shadow:var(--shadow) !important; }
</style>
""", unsafe_allow_html=True)

# ── NAV DATA ─────────────────────────────────────────────────────────────────
SESSION_NAV = [
    ("s01","AI & Research Landscape",     ["CLO 1"]),
    ("s02","Research Problem & Gap",       ["CLO 2"]),
    ("s03","AI Literature Search",         ["CLO 3"]),
    ("s04","Systematic Review & PRISMA",   ["CLO 3"]),
    ("s05","Research Questions",           ["CLO 2","CLO 5"]),
    ("s06","Theoretical Frameworks",       ["CLO 4"]),
    ("s07","Quantitative Methods",         ["CLO 5"]),
    ("s08","Qualitative Methods",          ["CLO 5"]),
    ("s09","Mixed Methods & AI",           ["CLO 5"]),
    ("s10","AI for Data Collection",       ["CLO 6"]),
    ("s11","Analysis & Interpretation",    ["CLO 6"]),
    ("s12","Academic Writing with AI",     ["CLO 7"]),
    ("s13","Citation, Ethics & Integrity", ["CLO 7","CLO 8"]),
    ("s14","Peer Review & Revision",       ["CLO 7"]),
    ("s15","Scholarly Dissemination",      ["CLO 7","CLO 8"]),
    ("s16","Capstone & Future of AI",      ["CLO 1","CLO 8"]),
]

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    cur = st.session_state.current_page

    # Brand block (pure HTML, no buttons inside)
    st.markdown("""
<div class="sb-brand">
  <div class="sb-logo">🎓</div>
  <div class="sb-name">Intelligent Research</div>
  <div class="sb-sub">AI Applications &amp; Techniques</div>
  <div class="sb-inst">GIM.FPM</div>
</div>""", unsafe_allow_html=True)

    # Projector toggle — rendered as its own block, styled by .sb-proj CSS
    st.markdown('<div class="sb-proj">', unsafe_allow_html=True)
    proj_label = "🖥️  Exit Projector Mode" if st.session_state.projector_mode else "📽️  Projector Mode"
    if st.button(proj_label, key="__proj__", use_container_width=True):
        st.session_state.projector_mode = not st.session_state.projector_mode
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # ── MAIN nav section label
    st.markdown('<div class="sb-sec">Main</div>', unsafe_allow_html=True)

    for pid, icon, label in [
        ("home",            "🏠", "Home"),
        ("course_overview", "📋", "Course Overview"),
        ("quiz_bank",       "📚", "Quiz Bank · 100+ Qs"),
    ]:
        is_active = cur == pid
        marker = "▶ " if is_active else ""
        # Active items get a gold left stripe via a sibling div trick
        if is_active:
            st.markdown('<div class="sb-active-stripe">', unsafe_allow_html=True)
        if st.button(f"{marker}{icon}  {label}", key=f"__nav_{pid}__", use_container_width=True):
            nav_to(pid); st.rerun()
        if is_active:
            st.markdown('</div>', unsafe_allow_html=True)

    # ── SESSIONS section
    # Progress dots
    active_idx = next((i for i,(sid,*_) in enumerate(SESSION_NAV) if sid==cur), -1)
    dots = "".join(
        f'<div class="sb-dot {"active" if i==active_idx else "done" if i<active_idx else ""}" title="S{i+1:02d}"></div>'
        for i in range(16)
    )
    st.markdown(f"""
<div class="sb-sec" style="margin-top:.8rem">Sessions</div>
<div class="sb-progress">{dots}</div>
""", unsafe_allow_html=True)

    for i, (sid, stitle, sclos) in enumerate(SESSION_NAV):
        short = stitle[:25] + ("…" if len(stitle) > 25 else "")
        is_active = cur == sid
        marker = "▶ " if is_active else ""
        lbl = f"{marker}{i+1:02d}  {short}"
        if is_active:
            st.markdown('<div class="sb-active-stripe">', unsafe_allow_html=True)
        if st.button(lbl, key=f"__snav_{sid}__", use_container_width=True):
            nav_to(sid); st.rerun()
        if is_active:
            st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
<div class="sb-footer">
  <div class="sb-footer-label">GIM.FPM</div>
  <div>Dr. Alok Tiwari</div>
  <div>Asst. Professor — Big Data Analytics</div>
  <div class="sb-footer-copy">© Dr. Alok Tiwari · All rights reserved</div>
</div>""", unsafe_allow_html=True)

# ── ROUTER ────────────────────────────────────────────────────────────────────
def load(module_path: str):
    try:
        mod = importlib.import_module(module_path)
        importlib.reload(mod)
        mod.render()
    except Exception as e:
        st.error(f"Could not load `{module_path}`")
        import traceback
        with st.expander("Details"):
            st.code(traceback.format_exc())

cur = st.session_state.current_page
if cur == "home":
    load("page_modules.home")
elif cur == "course_overview":
    load("page_modules.course_overview")
elif cur == "quiz_bank":
    load("page_modules.quiz_bank")
elif cur in [s[0] for s in SESSION_NAV]:
    load(f"sessions.{cur}")
else:
    st.warning(f"Unknown page: `{cur}`")
