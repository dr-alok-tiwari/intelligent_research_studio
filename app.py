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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@650;750&family=JetBrains+Mono:wght@500;700&display=swap');

:root{
  --bg:#fffaf3;
  --surface:#ffffff;
  --surface-soft:#fff7ed;
  --surface-warm:#ffedd5;
  --line:#fed7aa;
  --line-strong:#fb923c;
  --ink:#1f2937;
  --ink-soft:#475569;
  --muted:#64748b;
  --navy:#172554;
  --navy-mid:#1d4ed8;
  --blue:#2563eb;
  --saffron:#f97316;
  --saffron-deep:#c2410c;
  --saffron-dark:#7c2d12;
  --gold:#f59e0b;
  --green:#059669;
  --rose:#be123c;
  --slate:#fff7ed;
  --gold-pale:#fffbeb;
  --success-bg:#ecfdf5;
  --success-bd:#10b981;
  --warn-bg:#fff7ed;
  --warn-bd:#f97316;

  --font-sans:"Inter", "DM Sans", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-display:"Playfair Display", Georgia, serif;
  --font-mono:"JetBrains Mono", "DM Mono", monospace;

  --fs-xs:.75rem;
  --fs-sm:.875rem;
  --fs-base:1rem;
  --fs-md:1.0625rem;
  --fs-lg:1.18rem;
  --fs-xl:1.44rem;
  --fs-2xl:1.9rem;
  --fs-hero:clamp(2.25rem,4vw,3.3rem);

  --lh-tight:1.18;
  --lh-title:1.28;
  --lh-body:1.66;

  --sp-1:.25rem;
  --sp-2:.5rem;
  --sp-3:.75rem;
  --sp-4:1rem;
  --sp-5:1.25rem;
  --sp-6:1.5rem;
  --sp-8:2rem;

  --r-sm:10px;
  --r:16px;
  --r-lg:24px;
  --r-xl:32px;
  --shadow:0 8px 24px rgba(154,52,18,.09);
  --shadow-lg:0 18px 44px rgba(154,52,18,.15);
  --ring:0 0 0 3px rgba(249,115,22,.16);
}

*{box-sizing:border-box}
#MainMenu,footer{visibility:hidden}
header{background:rgba(255,250,243,.86)!important;backdrop-filter:blur(10px);border-bottom:1px solid rgba(253,186,116,.35)}
.stDeployButton{display:none!important}
html,body,[class*="css"]{font-family:var(--font-sans)!important;color:var(--ink);font-size:16.5px}
body{background:linear-gradient(180deg,#fff7ed 0%,#fffaf3 34%,#ffffff 100%)!important}
.main .block-container{padding:1.45rem 2.05rem 3.25rem!important;max-width:1240px!important}

/* Unified typography scale */
p,li,div,span,label{overflow-wrap:anywhere}
p,li{font-size:var(--fs-base);line-height:var(--lh-body);color:var(--ink-soft)}
h1,h2,h3,h4{font-family:var(--font-sans)!important;color:var(--navy);letter-spacing:-.025em;line-height:var(--lh-title)}
h1{font-size:var(--fs-2xl)!important;font-weight:900!important}
h2{font-size:var(--fs-xl)!important;font-weight:850!important}
h3{font-size:1.28rem!important;font-weight:850!important;margin-top:1.15rem!important;margin-bottom:.65rem!important}
h4{font-size:var(--fs-md)!important;font-weight:850!important}
strong{font-weight:850;color:var(--navy)}

/* Always visible light saffron sidebar */
[data-testid="stSidebar"]{display:block!important;visibility:visible!important;opacity:1!important;min-width:330px!important;max-width:330px!important;width:330px!important;background:linear-gradient(180deg,#fff7ed 0%,#ffedd5 54%,#fffaf3 100%)!important;border-right:1px solid #fdba74!important;box-shadow:12px 0 30px rgba(154,52,18,.10);z-index:999!important}
[data-testid="stSidebar"]>div,[data-testid="stSidebarContent"]{background:transparent!important;display:block!important;visibility:visible!important;opacity:1!important;overflow-y:auto!important}
[data-testid="stSidebar"] .block-container,[data-testid="stSidebar"] [data-testid="stVerticalBlock"]{padding:0!important;gap:.28rem!important}
[data-testid="collapsedControl"]{display:flex!important;visibility:visible!important;opacity:1!important}

.sb-brand{padding:1.35rem 1.05rem 1.05rem;border-bottom:1px solid #fdba74;background:radial-gradient(circle at 90% 0,rgba(255,255,255,.42),transparent 28%),linear-gradient(135deg,#fb923c 0%,#f59e0b 50%,#fff7ed 100%)}
.sb-logo{width:52px;height:52px;border-radius:17px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:1.65rem;margin-bottom:.72rem;box-shadow:0 8px 22px rgba(154,52,18,.18);border:1px solid rgba(255,255,255,.78)}
.sb-name{font-family:var(--font-display);font-size:1.12rem;font-weight:750;color:var(--saffron-dark);line-height:1.23;letter-spacing:-.01em}
.sb-sub{font-size:var(--fs-xs);color:#9a3412;text-transform:uppercase;letter-spacing:.08em;margin-top:.34rem;line-height:1.38;font-weight:850}
.sb-inst{display:inline-flex;margin-top:.55rem;padding:.24rem .6rem;background:#fff7ed;border:1px solid #fdba74;border-radius:999px;color:#9a3412;font-size:.7rem;font-weight:850}
.sb-panel{margin:.82rem;padding:.8rem .84rem;border-radius:17px;background:rgba(255,255,255,.76);border:1px solid #fdba74;box-shadow:0 6px 18px rgba(154,52,18,.07)}
.sb-panel-title,.sb-sec{font-size:.7rem;color:var(--saffron-deep);text-transform:uppercase;letter-spacing:.11em;font-weight:900;margin-bottom:.45rem}
.sb-sec{padding:.72rem 1rem .28rem;margin:0}
.sb-chip-row{display:flex;flex-wrap:wrap;gap:.38rem}.sb-chip{padding:.22rem .52rem;border-radius:999px;font-size:.69rem;font-weight:850;color:#9a3412;border:1px solid #fdba74;background:#fff7ed}
[data-testid="stSidebar"] label[data-baseweb="radio"]{background:rgba(255,255,255,.76)!important;border:1px solid #fed7aa!important;border-radius:14px!important;padding:.58rem .68rem!important;margin:.08rem .85rem!important;min-height:44px!important;color:var(--ink)!important;transition:all .16s ease!important;box-shadow:0 2px 8px rgba(154,52,18,.04)}
[data-testid="stSidebar"] label[data-baseweb="radio"]:hover{background:#fff!important;border-color:#fb923c!important;transform:translateX(2px);box-shadow:0 8px 18px rgba(249,115,22,.12)}
[data-testid="stSidebar"] label[data-baseweb="radio"]:has(input:checked){background:#fff!important;border-color:#f97316!important;box-shadow:var(--ring),0 9px 20px rgba(249,115,22,.12)}
[data-testid="stSidebar"] label[data-baseweb="radio"] p{color:var(--ink)!important;font-size:.9rem!important;font-weight:750!important;line-height:1.28!important;margin:0!important;white-space:normal!important}
.sb-progress{display:flex;gap:4px;flex-wrap:wrap;padding:.38rem 0 .58rem}.sb-dot{width:9px;height:9px;border-radius:50%;background:#fed7aa}.sb-dot.done{background:#fb923c}.sb-dot.active{background:#c2410c;box-shadow:0 0 8px rgba(194,65,12,.46);transform:scale(1.25)}
.sb-footer{margin:.8rem .85rem 1.1rem;padding:.85rem;border-radius:16px;background:rgba(255,255,255,.76);border:1px solid #fdba74;font-size:.76rem;color:#7c2d12;line-height:1.6}.sb-footer-label{font-size:.68rem;font-weight:900;text-transform:uppercase;letter-spacing:.12em;color:#c2410c;margin-bottom:.28rem}.sb-footer-copy{margin-top:.4rem;padding-top:.4rem;border-top:1px solid #fed7aa;color:#9a3412;font-size:.7rem}

/* Buttons and form widgets */
.main .stButton>button,.main .stDownloadButton>button{background:linear-gradient(135deg,#f97316,#f59e0b)!important;color:white!important;border:0!important;border-radius:14px!important;font-weight:850!important;font-size:.95rem!important;line-height:1.2!important;padding:.72rem 1rem!important;min-height:46px!important;box-shadow:0 9px 20px rgba(249,115,22,.20)!important;white-space:normal!important;transition:all .18s ease!important}
.main .stButton>button:hover,.main .stDownloadButton>button:hover{background:linear-gradient(135deg,#ea580c,#be123c)!important;transform:translateY(-2px)!important;box-shadow:0 14px 30px rgba(249,115,22,.28)!important;color:white!important}
.main .stButton>button:focus,.main .stDownloadButton>button:focus{box-shadow:var(--ring),0 9px 20px rgba(249,115,22,.20)!important}
.stSelectbox label,.stRadio label,.stTextInput label,.stTextArea label{font-size:.92rem!important;font-weight:800!important;color:var(--saffron-dark)!important}
[data-baseweb="select"]>div,input,textarea{border-radius:12px!important;border-color:#fed7aa!important;background:#fff!important;font-size:.95rem!important}

/* Page banner */
.page-banner{position:relative;background:radial-gradient(circle at 88% 10%,rgba(255,255,255,.42),transparent 26%),linear-gradient(135deg,#fff7ed 0%,#fed7aa 42%,#fb923c 100%);border-radius:var(--r-lg);padding:2.05rem 2.25rem;margin-bottom:1.4rem;box-shadow:var(--shadow-lg);border:1px solid #fdba74;overflow:hidden}
.page-banner::after{content:"";position:absolute;right:-80px;bottom:-90px;width:220px;height:220px;border-radius:50%;background:rgba(255,255,255,.22);pointer-events:none}
.banner-tag{display:inline-flex;align-items:center;background:#fff;color:#c2410c;padding:.32rem .78rem;border-radius:999px;font-size:.76rem;font-weight:900;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.82rem;border:1px solid #fdba74;box-shadow:0 3px 10px rgba(154,52,18,.06)}
.banner-h{font-family:var(--font-display)!important;font-size:var(--fs-hero);font-weight:750;color:var(--saffron-dark);line-height:1.08;margin:0 0 .72rem;max-width:900px;letter-spacing:-.035em}
.banner-p{font-size:var(--fs-md);color:#7c2d12;max-width:900px;line-height:1.62;font-weight:600;margin:0}.banner-pills,.badge-row{display:flex;gap:.55rem;flex-wrap:wrap;margin-top:1rem}.pill,.badge{display:inline-flex;align-items:center;gap:.25rem;padding:.34rem .76rem;border-radius:999px;font-size:.82rem;font-weight:850;line-height:1.25}.pill-clo{background:#fff;color:#7c2d12;border:1px solid #fdba74}.pill-gold{background:#7c2d12;color:#fff7ed;border:1px solid #7c2d12}

/* Cards and grids */
.stat-row,.guide-grid,.step-grid,.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(218px,1fr));gap:1rem;margin:1rem 0 1.45rem}
.stat-card,.guide-card,.feature-card,.download-card,.sess-card,.tool-card,.activity-card,.case-card{background:#fff;border:1px solid #fed7aa;border-radius:var(--r);padding:1rem 1.1rem;box-shadow:var(--shadow);transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.stat-card:hover,.guide-card:hover,.sess-card:hover,.tool-card:hover,.activity-card:hover,.case-card:hover{box-shadow:var(--shadow-lg);transform:translateY(-3px);border-color:#fb923c}.stat-card:before{content:"";display:block;height:4px;margin:-1rem -1.1rem .9rem;background:linear-gradient(90deg,#f97316,#f59e0b,#fed7aa)}
.stat-n{font-family:var(--font-display);font-size:2.24rem;font-weight:750;color:#7c2d12;line-height:1}.stat-l{font-size:.9rem;color:var(--muted);line-height:1.45;font-weight:750;margin-top:.35rem}.guide-card h4,.feature-card h4,.download-card h4{margin:0 0 .45rem;color:#7c2d12;font-size:var(--fs-base);font-weight:850}.guide-card p,.feature-card p,.download-card p{font-size:.94rem;color:var(--muted);line-height:1.6;font-weight:500;margin:0}
.sess-card{margin-bottom:.58rem;min-height:132px;background:linear-gradient(180deg,#fff,#fffaf3)}.sess-n{font-family:var(--font-mono);font-size:.72rem;font-weight:900;color:#ea580c;text-transform:uppercase;letter-spacing:.07em}.sess-t{font-size:1rem;font-weight:850;color:var(--navy);margin-top:.38rem;line-height:1.35}.sess-c{font-size:.9rem;color:#64748b;line-height:1.55;font-weight:600;margin-top:.38rem}

/* Activity, case and tool cards */
.activity-head{display:flex;align-items:center;gap:.78rem;margin-bottom:.85rem}.activity-icon{width:40px;height:40px;border-radius:13px;background:linear-gradient(135deg,#f97316,#c2410c);display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.12rem;box-shadow:0 8px 18px rgba(249,115,22,.20)}.activity-title,.case-title,.tool-title{font-size:1rem;font-weight:850;color:var(--navy);line-height:1.35}.activity-sub,.tool-body{font-size:.9rem;color:var(--muted);line-height:1.55;font-weight:500}.time-pill{margin-left:auto;background:#fff7ed;border:1px solid #fdba74;color:#9a3412;padding:.26rem .62rem;border-radius:999px;font-size:.76rem;font-weight:850;white-space:nowrap}.activity-body,.case-question{font-size:.96rem;line-height:1.6;color:var(--ink-soft);font-weight:500}.case-scenario{background:#fff7ed;border:1px solid #fed7aa;border-radius:12px;padding:.85rem .95rem;font-size:.95rem;line-height:1.62;color:var(--ink-soft);margin:.75rem 0}.tool-card{background:linear-gradient(180deg,#fff,#fffaf3);margin-bottom:.75rem}.tool-title{color:#7c2d12;margin-bottom:.35rem}
.metric-strip{display:flex;gap:.65rem;align-items:center;margin:.85rem 0 1.2rem;flex-wrap:wrap}.metric-pill{background:#fff;border:1px solid #fed7aa;border-radius:999px;padding:.44rem .82rem;font-size:.86rem;color:#7c2d12;font-weight:800;box-shadow:0 4px 12px rgba(154,52,18,.05)}.metric-pill.soft{background:#fff7ed;color:#9a3412}

/* Teaching and quiz content */
.concept-card,.gold-card,.reveal-box,.warn-box{border-radius:0 var(--r) var(--r) 0;padding:1rem 1.12rem;margin:.72rem 0;line-height:1.62;font-size:.98rem;color:var(--ink-soft)}.concept-card{background:#fff7ed;border-left:5px solid #f97316}.concept-card strong{display:block;margin-bottom:.32rem;font-size:1rem;color:#7c2d12}.gold-card{background:#fffbeb;border-left:5px solid #f59e0b}.reveal-box{background:#ecfdf5;border:1px solid #10b981;border-left:5px solid #10b981}.warn-box{background:#fff7ed;border:1px solid #f97316;border-left:5px solid #f97316}
.quiz-wrap{background:#fff;border:1px solid #fed7aa;border-radius:var(--r-lg);padding:1.2rem 1.25rem;margin:1.05rem 0;box-shadow:var(--shadow)}.quiz-meta{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:.82rem}.qbadge{padding:.25rem .62rem;border-radius:999px;font-size:.72rem;font-weight:900;text-transform:uppercase;letter-spacing:.035em}.qb-beg{background:#ecfdf5;color:#047857}.qb-int{background:#fff7ed;color:#9a3412}.qb-adv{background:#fff1f2;color:#9f1239}.qb-doc{background:#eef2ff;color:#3730a3}.qb-clo{background:#eff6ff;color:#1d4ed8}.qb-con{background:#f8fafc;color:#475569}.quiz-q{font-size:1rem;font-weight:750;color:var(--ink);line-height:1.62;padding:.85rem .95rem;background:#fffaf3;border-radius:var(--r-sm);border-left:4px solid #f97316;margin-bottom:.15rem}
.flow-table{width:100%;border-collapse:separate;border-spacing:0;border-radius:var(--r);overflow:hidden;box-shadow:var(--shadow);margin:1rem 0 1.5rem;table-layout:fixed}.flow-table thead{background:linear-gradient(135deg,#f97316,#c2410c)}.flow-table th{color:white;font-size:.86rem;padding:.72rem .9rem;text-align:left;font-weight:850}.flow-table td{padding:.7rem .9rem;font-size:.92rem;line-height:1.55;border-bottom:1px solid #fed7aa;word-break:break-word;vertical-align:top}.flow-table tbody tr:nth-child(even){background:#fff7ed}.flow-n{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;background:linear-gradient(135deg,#f97316,#be123c);color:white;border-radius:50%;font-size:.72rem;font-weight:900;font-family:var(--font-mono)}
.story-card{background:linear-gradient(135deg,#fff7ed,#fed7aa 38%,#fb923c);border-radius:var(--r-lg);padding:1.75rem 1.9rem;color:#7c2d12;box-shadow:var(--shadow-lg);border:1px solid #fdba74}.story-t{font-family:var(--font-display);font-size:1.32rem;font-weight:750;color:#7c2d12;margin-bottom:.9rem;line-height:1.3}.story-b{font-size:1rem;line-height:1.7;color:#7c2d12;font-weight:600}.story-prompt{margin-top:1rem;padding:.78rem .92rem;background:#fff;border:1px solid #fdba74;border-radius:12px;font-size:.94rem;color:#9a3412;font-style:italic}.divider{border:0;border-top:1px solid #fed7aa;margin:1.55rem 0}

/* Streamlit components */
.stExpander{border:1px solid #fed7aa!important;border-radius:var(--r)!important;background:#fff!important;box-shadow:0 4px 14px rgba(154,52,18,.04)!important}.stExpander summary{font-weight:800!important;font-size:.98rem!important;color:var(--navy)!important}.stTabs [data-baseweb="tab-list"]{background:#fff7ed;border-radius:var(--r);padding:.35rem;gap:.25rem;flex-wrap:wrap;border:1px solid #fed7aa}.stTabs [data-baseweb="tab"]{border-radius:10px!important;font-weight:800!important;color:#9a3412!important;font-size:.94rem!important;white-space:normal!important}.stTabs [aria-selected="true"]{background:white!important;color:#7c2d12!important;box-shadow:var(--shadow)!important}.stAlert{border-radius:var(--r)!important}

@media(max-width:900px){html,body,[class*="css"]{font-size:15.5px}[data-testid="stSidebar"]{min-width:300px!important;max-width:300px!important;width:300px!important}.main .block-container{padding:1rem!important}.page-banner{padding:1.45rem 1.25rem}.flow-table{table-layout:auto}.sess-card{min-height:auto}}
</style>
""",
    unsafe_allow_html=True,
)

if st.session_state.projector_mode:
    st.markdown("<style>html,body,[class*='css']{font-size:18px!important}.main .block-container{max-width:1360px!important}</style>", unsafe_allow_html=True)

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
    st.markdown(f'<div class="sb-panel"><div class="sb-panel-title">Session Progress</div><div class="sb-progress">{dots}</div><div style="color:#9a3412;font-size:.75rem;line-height:1.5;font-weight:750">Choose any session. The highlighted dot shows the active module.</div></div>', unsafe_allow_html=True)
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
