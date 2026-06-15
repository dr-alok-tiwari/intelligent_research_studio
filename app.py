"""
Intelligent Research: AI Applications & Techniques
Complete Classroom Teaching System — GIM Panaji
Single-page app with session_state routing. No pages/ folder used.
"""
import importlib
import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(__file__))

st.set_page_config(
    page_title="Intelligent Research · GIM",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "projector_mode" not in st.session_state:
    st.session_state.projector_mode = False

SESSION_NAV = [
    ("s01", "AI & Research Landscape", ["CLO 1"], "🧭"),
    ("s02", "Research Problem & Gap", ["CLO 2"], "🎯"),
    ("s03", "AI Literature Search", ["CLO 3"], "🔎"),
    ("s04", "Systematic Review & PRISMA", ["CLO 3"], "📊"),
    ("s05", "Research Questions", ["CLO 2", "CLO 5"], "❓"),
    ("s06", "Theoretical Frameworks", ["CLO 4"], "🧩"),
    ("s07", "Quantitative Methods", ["CLO 5"], "📈"),
    ("s08", "Qualitative Methods", ["CLO 5"], "🎙️"),
    ("s09", "Mixed Methods & AI", ["CLO 5"], "🔀"),
    ("s10", "AI for Data Collection", ["CLO 6"], "📝"),
    ("s11", "Analysis & Interpretation", ["CLO 6"], "🧠"),
    ("s12", "Academic Writing with AI", ["CLO 7"], "✍️"),
    ("s13", "Citation, Ethics & Integrity", ["CLO 7", "CLO 8"], "⚖️"),
    ("s14", "Peer Review & Revision", ["CLO 7"], "🛠️"),
    ("s15", "Scholarly Dissemination", ["CLO 7", "CLO 8"], "📣"),
    ("s16", "Capstone & Future of AI", ["CLO 1", "CLO 8"], "🚀"),
]
MAIN_NAV = [
    ("home", "🏠", "Home"),
    ("course_overview", "📋", "Course Overview"),
    ("quiz_bank", "📚", "Quiz Bank · 100+ Qs"),
]


def nav_to(page: str) -> None:
    st.session_state.current_page = page


st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap');

:root{
  --ink:#1f2937;
  --navy:#172554;
  --blue:#2563eb;
  --saffron:#f97316;
  --saffron-deep:#ea580c;
  --saffron-soft:#fff7ed;
  --saffron-mid:#fed7aa;
  --gold:#f59e0b;
  --rose:#be123c;
  --cream:#fffbf3;
  --card:#ffffff;
  --border:#fed7aa;
  --muted:#64748b;
  --green:#059669;
  --shadow:0 8px 24px rgba(154,52,18,.10);
  --shadow-lg:0 18px 42px rgba(154,52,18,.16);
  --r:16px;
  --rl:24px;
}

#MainMenu,footer{visibility:hidden}
header{background:rgba(255,251,243,.82)!important;backdrop-filter:blur(8px)}
.stDeployButton{display:none!important}
html,body,[class*="css"]{font-family:"DM Sans",sans-serif!important;color:var(--ink);font-size:17px}
body{background:linear-gradient(180deg,#fff7ed 0%,#fffaf3 34%,#ffffff 100%)!important}
.main .block-container{padding:1.55rem 2.1rem 3.2rem!important;max-width:1280px!important}
p,li,label,div,span{overflow-wrap:anywhere}p,li{font-size:1.03rem;line-height:1.72}h1,h2,h3,h4{color:var(--navy)}h3{font-size:1.38rem!important;font-weight:800!important}

/* Light saffron sidebar */
[data-testid="stSidebar"]{display:block!important;visibility:visible!important;opacity:1!important;min-width:330px!important;max-width:330px!important;width:330px!important;background:linear-gradient(180deg,#fff7ed 0%,#ffedd5 52%,#fffaf3 100%)!important;border-right:1px solid #fdba74!important;box-shadow:12px 0 30px rgba(154,52,18,.10);z-index:999!important}
[data-testid="stSidebar"]>div,[data-testid="stSidebarContent"]{background:transparent!important;display:block!important;visibility:visible!important;opacity:1!important;overflow-y:auto!important}
[data-testid="stSidebar"] .block-container,[data-testid="stSidebar"] [data-testid="stVerticalBlock"]{padding:0!important;gap:.28rem!important}
[data-testid="collapsedControl"]{display:flex!important;visibility:visible!important;opacity:1!important}

.sb-brand{padding:1.35rem 1.05rem 1.05rem;border-bottom:1px solid #fdba74;background:radial-gradient(circle at 90% 0,rgba(255,255,255,.36),transparent 26%),linear-gradient(135deg,#f97316 0%,#f59e0b 48%,#fff7ed 100%)}
.sb-logo{width:54px;height:54px;border-radius:16px;background:white;display:flex;align-items:center;justify-content:center;font-size:1.75rem;margin-bottom:.72rem;box-shadow:0 8px 22px rgba(154,52,18,.18);border:1px solid rgba(255,255,255,.75)}
.sb-name{font-family:"Playfair Display",serif;font-size:1.13rem;font-weight:700;color:#7c2d12;line-height:1.25}.sb-sub{font-size:.76rem;color:#9a3412;text-transform:uppercase;letter-spacing:.08em;margin-top:.32rem;line-height:1.4}.sb-inst{display:inline-flex;margin-top:.55rem;padding:.22rem .58rem;background:#fff7ed;border:1px solid #fdba74;border-radius:999px;color:#9a3412;font-size:.69rem;font-weight:800}
.sb-panel{margin:.85rem;padding:.78rem .82rem;border-radius:17px;background:rgba(255,255,255,.72);border:1px solid #fdba74;box-shadow:0 6px 18px rgba(154,52,18,.07)}.sb-panel-title,.sb-sec{font-size:.72rem;color:#c2410c;text-transform:uppercase;letter-spacing:.10em;font-weight:900;margin-bottom:.45rem}.sb-sec{padding:.75rem 1rem .28rem;margin:0}.sb-chip-row{display:flex;flex-wrap:wrap;gap:.38rem}.sb-chip{padding:.2rem .5rem;border-radius:999px;font-size:.7rem;font-weight:800;color:#9a3412;border:1px solid #fdba74;background:#fff7ed}
[data-testid="stSidebar"] label[data-baseweb="radio"]{background:rgba(255,255,255,.72)!important;border:1px solid #fed7aa!important;border-radius:14px!important;padding:.6rem .7rem!important;margin:.08rem .85rem!important;min-height:44px!important;color:#1f2937!important;transition:all .16s ease!important}
[data-testid="stSidebar"] label[data-baseweb="radio"]:hover{background:#ffffff!important;border-color:#fb923c!important;transform:translateX(2px);box-shadow:0 8px 18px rgba(249,115,22,.12)}
[data-testid="stSidebar"] label[data-baseweb="radio"] p{color:#1f2937!important;font-size:.93rem!important;font-weight:700!important;line-height:1.28!important;margin:0!important;white-space:normal!important}
.sb-progress{display:flex;gap:4px;flex-wrap:wrap;padding:.38rem 0 .58rem}.sb-dot{width:9px;height:9px;border-radius:50%;background:#fed7aa}.sb-dot.done{background:#fb923c}.sb-dot.active{background:#c2410c;box-shadow:0 0 8px rgba(194,65,12,.46);transform:scale(1.25)}.sb-footer{margin:.8rem .85rem 1.1rem;padding:.85rem;border-radius:16px;background:rgba(255,255,255,.72);border:1px solid #fdba74;font-size:.78rem;color:#7c2d12;line-height:1.65}.sb-footer-label{font-size:.68rem;font-weight:900;text-transform:uppercase;letter-spacing:.12em;color:#c2410c;margin-bottom:.28rem}.sb-footer-copy{margin-top:.4rem;padding-top:.4rem;border-top:1px solid #fed7aa;color:#9a3412;font-size:.72rem}

/* Buttons and interactive elements */
.main .stButton>button,.main .stDownloadButton>button{background:linear-gradient(135deg,#f97316,#f59e0b)!important;color:white!important;border:0!important;border-radius:14px!important;font-weight:900!important;font-size:.99rem!important;padding:.72rem 1rem!important;min-height:48px!important;box-shadow:0 9px 20px rgba(249,115,22,.22)!important;white-space:normal!important;transition:all .18s ease!important}
.main .stButton>button:hover,.main .stDownloadButton>button:hover{background:linear-gradient(135deg,#ea580c,#be123c)!important;transform:translateY(-2px)!important;box-shadow:0 14px 30px rgba(249,115,22,.28)!important;color:white!important}

.page-banner{background:radial-gradient(circle at 90% 12%,rgba(255,255,255,.34),transparent 27%),linear-gradient(135deg,#fff7ed 0%,#fed7aa 42%,#f97316 100%);border-radius:var(--rl);padding:2.15rem 2.35rem;margin-bottom:1.55rem;box-shadow:var(--shadow-lg);border:1px solid #fdba74}.banner-tag{display:inline-flex;background:#ffffff;color:#c2410c;padding:.3rem .78rem;border-radius:999px;font-size:.79rem;font-weight:900;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.82rem;border:1px solid #fdba74}.banner-h{font-family:"Playfair Display",serif;font-size:clamp(2.05rem,4vw,3.08rem);font-weight:700;color:#7c2d12;line-height:1.12;margin:0 0 .72rem;max-width:900px}.banner-p{font-size:1.08rem;color:#7c2d12;max-width:900px;line-height:1.72;font-weight:600}.banner-pills,.badge-row{display:flex;gap:.55rem;flex-wrap:wrap;margin-top:1rem}.pill,.badge{display:inline-flex;align-items:center;gap:.25rem;padding:.34rem .76rem;border-radius:999px;font-size:.83rem;font-weight:900;line-height:1.25}.pill-clo{background:#fff;color:#7c2d12;border:1px solid #fdba74}.pill-gold{background:#7c2d12;color:#fff7ed;border:1px solid #7c2d12}

.stat-row,.guide-grid,.step-grid,.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:1rem;margin:1rem 0 1.55rem}.stat-card,.guide-card,.feature-card,.download-card,.sess-card{background:#fff;border:1px solid #fed7aa;border-radius:var(--r);padding:1.08rem 1.18rem;box-shadow:var(--shadow);transition:.2s}.stat-card:hover,.sess-card:hover,.guide-card:hover{box-shadow:var(--shadow-lg);transform:translateY(-3px);border-color:#fb923c}.stat-card:before{content:"";display:block;height:4px;margin:-1.08rem -1.18rem .9rem;background:linear-gradient(90deg,#f97316,#f59e0b,#fed7aa)}.stat-n{font-family:"Playfair Display",serif;font-size:2.35rem;font-weight:700;color:#7c2d12;line-height:1}.stat-l,.sess-c,.guide-card p,.feature-card p,.download-card p{font-size:.95rem;color:#64748b;line-height:1.62;font-weight:650}.guide-card h4,.feature-card h4,.download-card h4{margin:0 0 .5rem;color:#7c2d12;font-size:1.07rem}.sess-card{margin-bottom:.58rem;min-height:132px;background:linear-gradient(180deg,#fff,#fffaf3)}.sess-n{font-family:"DM Mono",monospace;font-size:.73rem;font-weight:900;color:#ea580c;text-transform:uppercase;letter-spacing:.08em}.sess-t{font-size:1.02rem;font-weight:900;color:var(--navy);margin-top:.38rem;line-height:1.35}

.concept-card,.gold-card,.reveal-box,.warn-box{border-radius:0 var(--r) var(--r) 0;padding:1rem 1.15rem;margin:.7rem 0;line-height:1.65}.concept-card{background:#fff7ed;border-left:5px solid #f97316}.concept-card strong{color:#7c2d12;display:block;margin-bottom:.3rem;font-size:1.04rem}.gold-card{background:#fffbeb;border-left:5px solid #f59e0b}.reveal-box{background:#ecfdf5;border:1px solid #10b981;border-left:5px solid #10b981}.warn-box{background:#fff7ed;border:1px solid #f97316;border-left:5px solid #f97316;font-size:.98rem}
.quiz-wrap{background:#fff;border:1px solid #fed7aa;border-radius:var(--rl);padding:1.35rem 1.45rem;margin:1.15rem 0;box-shadow:var(--shadow)}.quiz-meta{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:.8rem}.qbadge{padding:.24rem .62rem;border-radius:999px;font-size:.72rem;font-weight:900;text-transform:uppercase;letter-spacing:.04em}.qb-beg{background:#ecfdf5;color:#047857}.qb-int{background:#fff7ed;color:#9a3412}.qb-adv{background:#fff1f2;color:#9f1239}.qb-doc{background:#eef2ff;color:#3730a3}.qb-clo{background:#eff6ff;color:#1d4ed8}.qb-con{background:#f8fafc;color:#475569}.quiz-q{font-size:1.04rem;font-weight:750;color:var(--ink);line-height:1.65;padding:.85rem 1rem;background:#fffaf3;border-radius:var(--r);border-left:4px solid #f97316;margin-bottom:1rem}
.flow-table{width:100%;border-collapse:separate;border-spacing:0;border-radius:var(--r);overflow:hidden;box-shadow:var(--shadow);margin:1rem 0 1.5rem;table-layout:fixed}.flow-table thead{background:linear-gradient(135deg,#f97316,#c2410c)}.flow-table th{color:white;font-size:.86rem;padding:.72rem .9rem;text-align:left}.flow-table td{padding:.68rem .9rem;font-size:.92rem;border-bottom:1px solid #fed7aa;word-break:break-word;vertical-align:top}.flow-table tbody tr:nth-child(even){background:#fff7ed}.flow-n{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;background:linear-gradient(135deg,#f97316,#be123c);color:white;border-radius:50%;font-size:.72rem;font-weight:900;font-family:"DM Mono",monospace}
.story-card{background:linear-gradient(135deg,#fff7ed,#fed7aa 38%,#f97316);border-radius:var(--rl);padding:1.9rem 2.05rem;color:#7c2d12;box-shadow:var(--shadow-lg);border:1px solid #fdba74}.story-t{font-family:"Playfair Display",serif;font-size:1.38rem;font-weight:700;color:#7c2d12;margin-bottom:.95rem}.story-b{font-size:1.02rem;line-height:1.78;color:#7c2d12;font-weight:600}.story-prompt{margin-top:1.1rem;padding:.75rem .95rem;background:#fff;border:1px solid #fdba74;border-radius:12px;font-size:.94rem;color:#9a3412;font-style:italic}.divider{border:0;border-top:1px solid #fed7aa;margin:1.7rem 0}
.stExpander{border:1px solid #fed7aa!important;border-radius:var(--r)!important;background:#fff!important}.stExpander summary{font-weight:850!important;font-size:1rem!important}.stTabs [data-baseweb="tab-list"]{background:#fff7ed;border-radius:var(--r);padding:.35rem;gap:.25rem;flex-wrap:wrap}.stTabs [data-baseweb="tab"]{border-radius:10px!important;font-weight:850!important;color:#9a3412!important;font-size:.98rem!important;white-space:normal!important}.stTabs [aria-selected="true"]{background:white!important;color:#7c2d12!important;box-shadow:var(--shadow)!important}
@media(max-width:900px){[data-testid="stSidebar"]{min-width:300px!important;max-width:300px!important;width:300px!important}.main .block-container{padding:1rem!important}.page-banner{padding:1.55rem 1.25rem}.flow-table{table-layout:auto}.sess-card{min-height:auto}}
</style>
""",
    unsafe_allow_html=True,
)

if st.session_state.projector_mode:
    st.markdown("<style>html,body,[class*='css']{font-size:18.5px!important}.main .block-container{max-width:1360px!important}</style>", unsafe_allow_html=True)

with st.sidebar:
    cur = st.session_state.current_page
    st.markdown("""
<div class="sb-brand">
  <div class="sb-logo">🎓</div>
  <div class="sb-name">Intelligent Research Studio</div>
  <div class="sb-sub">AI Applications &amp; Techniques</div>
  <div class="sb-inst">GIM · FPM · Classroom Ready</div>
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="sb-panel"><div class="sb-panel-title">Studio Status</div>
<div class="sb-chip-row"><span class="sb-chip">✅ Sidebar On</span><span class="sb-chip">📘 Handbook</span><span class="sb-chip">🧠 No API Key</span></div></div>
""", unsafe_allow_html=True)

    projector_now = st.toggle("📽️ Projector Mode", value=st.session_state.projector_mode, key="__projector_toggle__")
    if projector_now != st.session_state.projector_mode:
        st.session_state.projector_mode = projector_now
        st.rerun()

    st.markdown('<div class="sb-sec">Main Navigation</div>', unsafe_allow_html=True)
    nav_labels, label_to_page = [], {}
    for pid, icon, label in MAIN_NAV:
        nav_label = f"{icon}  {label}"
        nav_labels.append(nav_label)
        label_to_page[nav_label] = pid
    for i, (sid, title, clos, icon) in enumerate(SESSION_NAV, start=1):
        nav_label = f"{icon}  S{i:02d} · {title} · {' · '.join(clos)}"
        nav_labels.append(nav_label)
        label_to_page[nav_label] = sid

    current_label = next((label for label, page in label_to_page.items() if page == cur), "🏠  Home")
    choice = st.radio(
        "Navigate the Studio",
        nav_labels,
        index=nav_labels.index(current_label) if current_label in nav_labels else 0,
        key=f"__sidebar_nav_radio__{cur}",
        label_visibility="collapsed",
    )
    selected_page = label_to_page.get(choice)
    if selected_page and selected_page != cur:
        nav_to(selected_page)
        st.rerun()

    active_idx = next((i for i, (sid, *_rest) in enumerate(SESSION_NAV) if sid == cur), -1)
    dots = "".join(f'<div class="sb-dot {"active" if i == active_idx else "done" if 0 <= i < active_idx else ""}"></div>' for i in range(len(SESSION_NAV)))
    st.markdown(f'<div class="sb-panel"><div class="sb-panel-title">Session Progress</div><div class="sb-progress">{dots}</div><div style="color:#9a3412;font-size:.75rem;line-height:1.5;font-weight:700">Choose any session. The highlighted dot shows the active module.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-footer"><div class="sb-footer-label">Created for classroom teaching</div><div>Dr. Alok Tiwari</div><div>Assistant Professor — Big Data Analytics</div><div class="sb-footer-copy">© Dr. Alok Tiwari · All rights reserved</div></div>', unsafe_allow_html=True)


def load(module_path: str) -> None:
    try:
        mod = importlib.import_module(module_path)
        importlib.reload(mod)
        mod.render()
    except Exception:
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
