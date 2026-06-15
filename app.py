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


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap');
:root{--navy:#172554;--blue:#1d4ed8;--indigo:#4338ca;--saffron:#f97316;--gold:#fbbf24;--rose:#be123c;--maroon:#7f1d1d;--slate:#f5f7fb;--border:#dbe4ff;--text:#172033;--muted:#5f6f89;--gold-pale:#fff7ed;--success-bg:#ecfdf5;--success-bd:#10b981;--warn-bg:#fff7ed;--warn-bd:#f97316;--shadow:0 6px 20px rgba(23,37,84,.08);--shadow-lg:0 14px 38px rgba(23,37,84,.16);--r:14px;--rl:22px}
#MainMenu,footer{visibility:hidden} header{background:transparent!important}.stDeployButton{display:none!important}
html,body,[class*="css"]{font-family:"DM Sans",sans-serif!important;color:var(--text);font-size:17px}
body{background:radial-gradient(circle at 0 0,rgba(249,115,22,.12),transparent 30%),radial-gradient(circle at 100% 0,rgba(67,56,202,.10),transparent 30%),linear-gradient(180deg,#fffaf5,#f8fbff)!important}
.main .block-container{padding:1.6rem 2.1rem 3.2rem!important;max-width:1280px!important}
p,li,label,div,span{overflow-wrap:anywhere} p,li{font-size:1.03rem;line-height:1.72} h1,h2,h3,h4{color:var(--navy)} h3{font-size:1.35rem!important}

/* Force sidebar to exist and keep Streamlit's own expand/collapse control available. */
[data-testid="stSidebar"]{display:block!important;visibility:visible!important;opacity:1!important;min-width:330px!important;max-width:330px!important;width:330px!important;background:linear-gradient(180deg,#111827,#172554 52%,#7f1d1d)!important;border-right:1px solid rgba(251,191,36,.28);box-shadow:12px 0 34px rgba(17,24,39,.16);z-index:999!important}
[data-testid="stSidebar"]>div,[data-testid="stSidebarContent"]{background:transparent!important;display:block!important;visibility:visible!important;opacity:1!important;overflow-y:auto!important}
[data-testid="stSidebar"] .block-container,[data-testid="stSidebar"] [data-testid="stVerticalBlock"]{padding:0!important;gap:.25rem!important}
[data-testid="collapsedControl"]{display:flex!important;visibility:visible!important;opacity:1!important}

.sb-brand{padding:1.35rem 1.05rem 1.05rem;border-bottom:1px solid rgba(251,191,36,.20);background:radial-gradient(circle at 88% 0,rgba(251,191,36,.28),transparent 28%),linear-gradient(135deg,#111827,#1e3a8a 55%,#9a3412);overflow:hidden}.sb-logo{width:54px;height:54px;border-radius:16px;background:linear-gradient(135deg,var(--gold),var(--saffron));display:flex;align-items:center;justify-content:center;font-size:1.75rem;margin-bottom:.72rem;box-shadow:0 7px 22px rgba(249,115,22,.34)}.sb-name{font-family:"Playfair Display",serif;font-size:1.12rem;font-weight:700;color:white;line-height:1.25}.sb-sub{font-size:.76rem;color:rgba(255,237,213,.9);text-transform:uppercase;letter-spacing:.08em;margin-top:.32rem;line-height:1.4}.sb-inst{display:inline-flex;margin-top:.55rem;padding:.2rem .55rem;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.16);border-radius:999px;color:rgba(255,255,255,.78);font-size:.68rem;font-weight:700}
.sb-panel{margin:.85rem;padding:.75rem .8rem;border-radius:16px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14)}.sb-panel-title,.sb-sec{font-size:.72rem;color:rgba(251,191,36,.92);text-transform:uppercase;letter-spacing:.10em;font-weight:800;margin-bottom:.45rem}.sb-sec{padding:.75rem 1rem .28rem;margin:0}.sb-chip-row{display:flex;flex-wrap:wrap;gap:.38rem}.sb-chip{padding:.18rem .48rem;border-radius:999px;font-size:.69rem;font-weight:700;color:#fff7ed;border:1px solid rgba(255,255,255,.17);background:rgba(255,255,255,.09)}
[data-testid="stSidebar"] label[data-baseweb="radio"]{background:rgba(255,255,255,.06)!important;border:1px solid rgba(255,255,255,.10)!important;border-radius:13px!important;padding:.58rem .68rem!important;margin:.08rem .85rem!important;min-height:43px!important;color:rgba(255,255,255,.82)!important}
[data-testid="stSidebar"] label[data-baseweb="radio"]:hover{background:rgba(251,191,36,.16)!important;border-color:rgba(251,191,36,.38)!important;transform:translateX(2px)}
[data-testid="stSidebar"] label[data-baseweb="radio"] p{color:rgba(255,255,255,.9)!important;font-size:.92rem!important;line-height:1.25!important;margin:0!important;white-space:normal!important}
.sb-progress{display:flex;gap:4px;flex-wrap:wrap;padding:.38rem 0 .58rem}.sb-dot{width:9px;height:9px;border-radius:50%;background:rgba(255,255,255,.18)}.sb-dot.done{background:rgba(251,191,36,.62)}.sb-dot.active{background:var(--gold);box-shadow:0 0 8px rgba(251,191,36,.7);transform:scale(1.22)}.sb-footer{margin:.8rem .85rem 1.1rem;padding:.85rem;border-radius:16px;background:rgba(0,0,0,.16);border:1px solid rgba(255,255,255,.10);font-size:.76rem;color:rgba(255,255,255,.68);line-height:1.65}.sb-footer-label{font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.12em;color:rgba(251,191,36,.86);margin-bottom:.28rem}.sb-footer-copy{margin-top:.4rem;padding-top:.4rem;border-top:1px solid rgba(255,255,255,.08);color:rgba(255,255,255,.5);font-size:.7rem}

.main .stButton>button,.main .stDownloadButton>button{background:linear-gradient(135deg,var(--blue),var(--indigo))!important;color:white!important;border:0!important;border-radius:12px!important;font-weight:800!important;font-size:.98rem!important;padding:.72rem .95rem!important;min-height:46px!important;box-shadow:0 8px 18px rgba(29,78,216,.18)!important;white-space:normal!important}
.main .stButton>button:hover,.main .stDownloadButton>button:hover{background:linear-gradient(135deg,var(--saffron),var(--rose))!important;transform:translateY(-2px)!important;box-shadow:0 12px 28px rgba(249,115,22,.25)!important}
.page-banner{background:radial-gradient(circle at 90% 15%,rgba(251,191,36,.22),transparent 25%),radial-gradient(circle at 10% 90%,rgba(249,115,22,.18),transparent 28%),linear-gradient(135deg,#172554,#1d4ed8 48%,#9a3412);border-radius:var(--rl);padding:2.15rem 2.35rem;margin-bottom:1.55rem;overflow:hidden;box-shadow:var(--shadow-lg);border:1px solid rgba(255,255,255,.22)}.banner-tag{display:inline-flex;background:rgba(251,191,36,.22);color:#fffbeb;padding:.28rem .75rem;border-radius:999px;font-size:.78rem;font-weight:900;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.8rem;border:1px solid rgba(251,191,36,.38)}.banner-h{font-family:"Playfair Display",serif;font-size:clamp(2.05rem,4vw,3.05rem);font-weight:700;color:white;line-height:1.12;margin:0 0 .7rem;max-width:850px}.banner-p{font-size:1.08rem;color:rgba(255,255,255,.86);max-width:860px;line-height:1.72}.banner-pills,.badge-row{display:flex;gap:.55rem;flex-wrap:wrap;margin-top:1rem}.pill,.badge{display:inline-flex;align-items:center;gap:.25rem;padding:.32rem .72rem;border-radius:999px;font-size:.82rem;font-weight:900;line-height:1.25}.pill-clo{background:rgba(255,255,255,.12);color:rgba(255,255,255,.92);border:1px solid rgba(255,255,255,.20)}.pill-gold{background:rgba(251,191,36,.24);color:#fffbeb;border:1px solid rgba(251,191,36,.42)}
.stat-row,.guide-grid,.step-grid,.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:1rem;margin:1rem 0 1.55rem}.stat-card,.guide-card,.feature-card,.download-card,.sess-card{background:rgba(255,255,255,.95);border:1px solid var(--border);border-radius:var(--r);padding:1.05rem 1.15rem;box-shadow:var(--shadow);transition:.2s}.stat-card:hover,.sess-card:hover{box-shadow:var(--shadow-lg);transform:translateY(-3px);border-color:var(--saffron)}.stat-card:before{content:"";display:block;height:4px;margin:-1.05rem -1.15rem .9rem;background:linear-gradient(90deg,var(--saffron),var(--gold),var(--blue))}.stat-n{font-family:"Playfair Display",serif;font-size:2.35rem;font-weight:700;color:var(--navy);line-height:1}.stat-l,.sess-c,.guide-card p,.feature-card p,.download-card p{font-size:.94rem;color:var(--muted);line-height:1.6;font-weight:600}.guide-card h4,.feature-card h4,.download-card h4{margin:0 0 .5rem;color:var(--navy);font-size:1.05rem}.sess-card{margin-bottom:.6rem;min-height:130px}.sess-n{font-family:"DM Mono",monospace;font-size:.72rem;font-weight:900;color:var(--saffron);text-transform:uppercase;letter-spacing:.08em}.sess-t{font-size:1rem;font-weight:900;color:var(--navy);margin-top:.38rem;line-height:1.35}
.concept-card,.gold-card,.reveal-box,.warn-box{border-radius:0 var(--r) var(--r) 0;padding:1rem 1.15rem;margin:.7rem 0;line-height:1.65}.concept-card{background:#eef5ff;border-left:5px solid var(--blue)}.concept-card strong{color:var(--navy);display:block;margin-bottom:.3rem;font-size:1.03rem}.gold-card{background:var(--gold-pale);border-left:5px solid var(--saffron)}.reveal-box{background:var(--success-bg);border:1px solid var(--success-bd);border-left:5px solid var(--success-bd)}.warn-box{background:var(--warn-bg);border:1px solid var(--warn-bd);border-left:5px solid var(--warn-bd);font-size:.98rem}
.quiz-wrap{background:rgba(255,255,255,.96);border:1px solid var(--border);border-radius:var(--rl);padding:1.35rem 1.45rem;margin:1.15rem 0;box-shadow:var(--shadow)}.quiz-meta{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:.8rem}.qbadge{padding:.24rem .62rem;border-radius:999px;font-size:.72rem;font-weight:900;text-transform:uppercase;letter-spacing:.04em}.qb-beg{background:#e8f8ef;color:#0d6e3f}.qb-int{background:#fff7ed;color:#9a3412}.qb-adv{background:#fff1f2;color:#9f1239}.qb-doc{background:#eef2ff;color:#3730a3}.qb-clo{background:#eff6ff;color:#1d4ed8}.qb-con{background:#f8fafc;color:#475569}.quiz-q{font-size:1.04rem;font-weight:700;color:var(--text);line-height:1.65;padding:.85rem 1rem;background:#f8fbff;border-radius:var(--r);border-left:4px solid var(--saffron);margin-bottom:1rem}
.flow-table{width:100%;border-collapse:separate;border-spacing:0;border-radius:var(--r);overflow:hidden;box-shadow:var(--shadow);margin:1rem 0 1.5rem;table-layout:fixed}.flow-table thead{background:linear-gradient(135deg,var(--navy),var(--blue))}.flow-table th{color:white;font-size:.86rem;padding:.72rem .9rem;text-align:left}.flow-table td{padding:.68rem .9rem;font-size:.92rem;border-bottom:1px solid var(--border);word-break:break-word;vertical-align:top}.flow-table tbody tr:nth-child(even){background:#f8fbff}.flow-n{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;background:linear-gradient(135deg,var(--saffron),var(--rose));color:white;border-radius:50%;font-size:.72rem;font-weight:900;font-family:"DM Mono",monospace}
.story-card{background:radial-gradient(circle at 85% 10%,rgba(251,191,36,.24),transparent 25%),linear-gradient(135deg,var(--navy),#1d4ed8 55%,#7f1d1d);border-radius:var(--rl);padding:1.9rem 2.05rem;color:white;overflow:hidden;box-shadow:var(--shadow-lg)}.story-card:before{content:"“";position:absolute;font-size:8rem;color:rgba(251,191,36,.15)}.story-t{font-family:"Playfair Display",serif;font-size:1.38rem;font-weight:700;color:#fef3c7;margin-bottom:.95rem}.story-b{font-size:1.02rem;line-height:1.78;color:rgba(255,255,255,.9)}.story-prompt{margin-top:1.1rem;padding:.75rem .95rem;background:rgba(251,191,36,.16);border:1px solid rgba(251,191,36,.34);border-radius:12px;font-size:.94rem;color:#fef3c7;font-style:italic}.divider{border:0;border-top:1px solid var(--border);margin:1.7rem 0}
.stExpander{border:1px solid var(--border)!important;border-radius:var(--r)!important;background:rgba(255,255,255,.84)!important}.stExpander summary{font-weight:800!important;font-size:1rem!important}.stTabs [data-baseweb="tab-list"]{background:#eef2ff;border-radius:var(--r);padding:.35rem;gap:.25rem;flex-wrap:wrap}.stTabs [data-baseweb="tab"]{border-radius:10px!important;font-weight:800!important;color:var(--muted)!important;font-size:.98rem!important;white-space:normal!important}.stTabs [aria-selected="true"]{background:white!important;color:var(--navy)!important;box-shadow:var(--shadow)!important}
@media(max-width:900px){[data-testid="stSidebar"]{min-width:300px!important;max-width:300px!important;width:300px!important}.main .block-container{padding:1rem!important}.page-banner{padding:1.55rem 1.25rem}.flow-table{table-layout:auto}.sess-card{min-height:auto}}
</style>
""", unsafe_allow_html=True)

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
    choice = st.radio("Navigate the Studio", nav_labels, index=nav_labels.index(current_label) if current_label in nav_labels else 0, key="__sidebar_nav_radio__", label_visibility="collapsed")
    selected_page = label_to_page.get(choice)
    if selected_page and selected_page != cur:
        nav_to(selected_page)
        st.rerun()

    active_idx = next((i for i, (sid, *_rest) in enumerate(SESSION_NAV) if sid == cur), -1)
    dots = "".join(f'<div class="sb-dot {"active" if i == active_idx else "done" if 0 <= i < active_idx else ""}"></div>' for i in range(len(SESSION_NAV)))
    st.markdown(f'<div class="sb-panel"><div class="sb-panel-title">Session Progress</div><div class="sb-progress">{dots}</div><div style="color:rgba(255,255,255,.68);font-size:.75rem;line-height:1.5">Choose any session. The highlighted dot shows the active module.</div></div>', unsafe_allow_html=True)
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
