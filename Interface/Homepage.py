import streamlit as st

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Personalized Medicine for Lung Cancer",
    page_icon="assets/favicon.png",
    layout="wide"
)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------

try:
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.image(
        "assets/logo.png",
        width=180
    )

    st.markdown(
        """
        ## Personalized Medicine
        ### for Lung Cancer
        """
    )

    st.divider()

    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(0,180,216,0.20), rgba(30,86,160,0.30));
        border: 1px solid rgba(174,214,241,0.35);
        border-radius: 12px;
        padding: 14px 16px;
        margin: 4px 0;
    ">
        <div style="font-size:0.75rem; color:rgba(255,255,255,0.65); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:6px;">Platform</div>
        <div style="font-size:0.95rem; color:#AED6F1; font-weight:600;">AI-Powered Precision Oncology</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <div style="padding: 4px 0;">
        <div style="font-size:0.72rem; color:rgba(255,255,255,0.50); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:12px;">Navigation</div>
    """, unsafe_allow_html=True)

    nav_items = [
        ("💊", "Drug Recommendation", "Generate personalized drug rankings"),
        ("🧪", "Drug Explorer", "Visualize molecular structures"),
        ("🧬", "Biomarker Explorer", "Explore gene expression profiles"),
        ("🧠", "Model Information", "Architecture & performance metrics"),
    ]

    for icon, label, desc in nav_items:
        st.markdown(f"""
        <div style="
            display:flex; align-items:center; gap:10px;
            padding:10px 12px; margin-bottom:4px;
            border-radius:10px;
            background:rgba(255,255,255,0.05);
            border:1px solid rgba(174,214,241,0.12);
        ">
            <span style="font-size:1.1rem;">{icon}</span>
            <div>
                <div style="font-size:0.85rem; font-weight:600; color:rgba(255,255,255,0.90);">{label}</div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.45);">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <div style="font-size:0.72rem; color:rgba(255,255,255,0.35); text-align:center; line-height:1.6;">
        Iqra University · Precision Oncology<br>
        CCLE · GDSC · DepMap
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Hero Banner
# --------------------------------------------------

try:
    st.image("assets/banner.png", use_container_width=True)
except:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #0A1628 0%, #1B3A6B 50%, #1E56A0 100%);
        border-radius: 16px;
        padding: 48px 40px;
        text-align: center;
        margin-bottom: 8px;
    ">
        <div style="font-size: 3rem; margin-bottom: 8px;">🫁</div>
        <h1 style="color:#AED6F1; font-size:2.4rem; margin:0; font-family:'Space Grotesk',sans-serif;">
            Personalized Medicine for Lung Cancer
        </h1>
        <p style="color:rgba(255,255,255,0.65); margin-top:12px; font-size:1.05rem;">
            AI-Powered Precision Oncology · Graph Neural Networks · Multi-Omics
        </p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Hero Text
# --------------------------------------------------

st.markdown("""
<div style="padding: 8px 0 4px;">
    <h1 style="margin-bottom: 4px;">🫁 Personalized Medicine for Lung Cancer</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background: linear-gradient(135deg, #EBF5FB, #D6EAF8);
    border-left: 4px solid #1E56A0;
    border-radius: 0 12px 12px 0;
    padding: 18px 22px;
    margin: 8px 0 16px;
">
    <p style="margin:0; font-size:1.05rem; color:#0A1628; line-height:1.7;">
        <strong>AI-Powered Precision Oncology</strong> using Multi-Omics Data and Graph Neural Networks.
        This platform integrates biological, genomic and molecular information to predict drug response
        and recommend personalized treatments for Non-Small Cell Lung Cancer (NSCLC).
    </p>
</div>
""", unsafe_allow_html=True)

# Core technologies in a pill row
st.markdown("""
<div style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:8px;">
    <span style="background:#1E56A0; color:#fff; border-radius:20px; padding:5px 14px; font-size:0.82rem; font-weight:600;">🧬 Gene Expression Profiling</span>
    <span style="background:#2E86C1; color:#fff; border-radius:20px; padding:5px 14px; font-size:0.82rem; font-weight:600;">🧬 Mutation Analysis</span>
    <span style="background:#0077B6; color:#fff; border-radius:20px; padding:5px 14px; font-size:0.82rem; font-weight:600;">🧠 Task-Aware Representation Learning</span>
    <span style="background:#00B4D8; color:#fff; border-radius:20px; padding:5px 14px; font-size:0.82rem; font-weight:600;">💊 Drug Molecular Graphs</span>
    <span style="background:#1B3A6B; color:#fff; border-radius:20px; padding:5px 14px; font-size:0.82rem; font-weight:600;">🔗 Graph Neural Networks</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# Statistics
# --------------------------------------------------

st.markdown('<h2 style="margin-bottom:0.8rem;">📊 Dataset Overview</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("NSCLC Cell Lines", "92")

with col2:
    st.metric("Anticancer Drugs", "229")

with col3:
    st.metric("Drug Responses", "19,207")

with col4:
    st.metric("Task-Aware Features", "272")

st.divider()

# --------------------------------------------------
# Data Sources
# --------------------------------------------------

st.markdown('<h2 style="margin-bottom:0.8rem;">📂 Data Sources</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

source_style = """
    background: linear-gradient(160deg, {bg1}, {bg2});
    border: 1px solid {border};
    border-radius: 16px;
    padding: 24px 22px;
    height: 100%;
"""

with col1:
    st.markdown(f"""
    <div style="{source_style.format(bg1='#EBF5FB', bg2='#D6EAF8', border='#AED6F1')}">
        <div style="font-size:1.8rem; margin-bottom:10px;">🔬</div>
        <h3 style="color:#0A1628; margin:0 0 4px; font-size:1.2rem;">CCLE</h3>
        <div style="font-size:0.78rem; color:#5D7B9A; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;">Cancer Cell Line Encyclopedia</div>
        <ul style="color:#2C3E50; font-size:0.88rem; line-height:1.8; padding-left:16px; margin:0;">
            <li>Gene Expression</li>
            <li>NSCLC Cell Lines</li>
            <li>Molecular Profiles</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="{source_style.format(bg1='#1B3A6B', bg2='#1E56A0', border='#2E86C1')}">
        <div style="font-size:1.8rem; margin-bottom:10px;">💉</div>
        <h3 style="color:#AED6F1; margin:0 0 4px; font-size:1.2rem;">GDSC</h3>
        <div style="font-size:0.78rem; color:rgba(174,214,241,0.70); font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;">Genomics of Drug Sensitivity</div>
        <ul style="color:rgba(255,255,255,0.80); font-size:0.88rem; line-height:1.8; padding-left:16px; margin:0;">
            <li>Drug Response Data</li>
            <li>IC50 Measurements</li>
            <li>Therapeutic Screening</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="{source_style.format(bg1='#0077B6', bg2='#00B4D8', border='#90E0EF')}">
        <div style="font-size:1.8rem; margin-bottom:10px;">🗺️</div>
        <h3 style="color:#fff; margin:0 0 4px; font-size:1.2rem;">DepMap</h3>
        <div style="font-size:0.78rem; color:rgba(255,255,255,0.70); font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;">Cancer Dependency Map</div>
        <ul style="color:rgba(255,255,255,0.85); font-size:0.88rem; line-height:1.8; padding-left:16px; margin:0;">
            <li>Mutation Features</li>
            <li>Dependency Information</li>
            <li>Functional Genomics</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# Architecture
# --------------------------------------------------

st.markdown('<h2 style="margin-bottom:0.8rem;">🏗️ Proposed Framework</h2>', unsafe_allow_html=True)

try:
    st.image("assets/Architecture.png", use_container_width=True)
except:
    pass

st.markdown("""
<div style="
    background: linear-gradient(135deg, #EBF5FB, #D6EAF8);
    border-left: 4px solid #00B4D8;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin-top: 8px;
">
    <p style="margin:0; color:#0A1628; line-height:1.7; font-size:0.93rem;">
    The proposed framework integrates multi-omics cancer data,
    representation learning, molecular graph construction and
    Graph Neural Networks to predict drug sensitivity and
    recommend personalized treatments for lung cancer.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# Workflow
# --------------------------------------------------

st.markdown('<h2 style="margin-bottom:0.8rem;">⚙️ End-to-End Workflow</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

workflow_items = [
    {
        "step": "01",
        "title": "Data Collection",
        "emoji": "📥",
        "items": ["CCLE", "GDSC", "DepMap", "Gene Expression", "Mutation Features"],
        "bg1": "#EBF5FB", "bg2": "#D6EAF8",
        "border": "#AED6F1", "num_color": "#1E56A0",
        "text": "#0A1628", "item_color": "#2C3E50"
    },
    {
        "step": "02",
        "title": "AI Processing",
        "emoji": "⚙️",
        "items": ["Feature Engineering", "Autoencoder", "272 Task-Aware Features", "Drug Graph Construction", "Graph Neural Network"],
        "bg1": "#1B3A6B", "bg2": "#1E56A0",
        "border": "#2E86C1", "num_color": "#AED6F1",
        "text": "#AED6F1", "item_color": "rgba(255,255,255,0.80)"
    },
    {
        "step": "03",
        "title": "Model Output",
        "emoji": "🎯",
        "items": ["Drug Response Prediction", "Drug Ranking", "Top Candidate Drugs", "Personalized Medicine"],
        "bg1": "#0077B6", "bg2": "#00B4D8",
        "border": "#90E0EF", "num_color": "#fff",
        "text": "#fff", "item_color": "rgba(255,255,255,0.85)"
    }
]

for col, item in zip([col1, col2, col3], workflow_items):
    with col:
        items_html = "".join([
            f'<li style="color:{item["item_color"]}; padding:2px 0;">{i}</li>'
            for i in item["items"]
        ])
        st.markdown(f"""
        <div style="
            background: linear-gradient(160deg, {item['bg1']}, {item['bg2']});
            border: 1px solid {item['border']};
            border-radius: 16px;
            padding: 22px 20px;
            height: 380px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            box-sizing: border-box;
        ">
            <div style="
                position:absolute; top:-8px; right:-8px;
                font-size:3.5rem; opacity:0.08; font-weight:900;
                color:{item['num_color']};
                font-family:'Space Grotesk',sans-serif;
            ">{item['step']}</div>
            <div style="font-size:1.6rem; margin-bottom:8px;">{item['emoji']}</div>
            <h3 style="color:{item['text']}; margin:0 0 12px; font-size:1.05rem; font-weight:700;">
                {item['step']} · {item['title']}
            </h3>
            <ul style="font-size:0.88rem; line-height:1.9; padding-left:16px; margin:0;">
                {items_html}
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# Platform Features
# --------------------------------------------------

st.markdown('<h2 style="margin-bottom:0.8rem;">⭐ Platform Features</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

features_left = [
    "Personalized Drug Ranking",
    "Graph Neural Networks",
    "Drug Molecular Analysis",
    "NSCLC-Specific Framework",
    "Drug Sensitivity Prediction",
]

features_right = [
    "Multi-Modal Learning",
    "Representation Learning",
    "Molecular Graph Construction",
    "Precision Oncology Support",
    "Explainable AI Workflow",
]

def feature_card(items, col):
    with col:
        items_html = "".join([
            f"""<div style="
                display:flex; align-items:center; gap:10px;
                padding:9px 12px; margin-bottom:6px;
                background:var(--white,#fff);
                border:1px solid #D6EAF8;
                border-radius:10px;
                box-shadow:0 2px 6px rgba(10,22,40,0.06);
            ">
                <span style="color:#2E86C1; font-size:1rem;">✓</span>
                <span style="color:#0A1628; font-size:0.88rem; font-weight:500;">{f}</span>
            </div>"""
            for f in items
        ])
        st.markdown(items_html, unsafe_allow_html=True)

feature_card(features_left, col1)
feature_card(features_right, col2)

st.divider()

# --------------------------------------------------
# Navigation Cards
# --------------------------------------------------

st.markdown('<h2 style="margin-bottom:0.8rem;">🚀 Explore the Platform</h2>', unsafe_allow_html=True)

nav_cards = [
    ("💊", "Drug Recommendation", "Generate personalized drug recommendations for individual NSCLC samples using Graph Neural Networks.", "#1B3A6B", "#1E56A0", "#AED6F1", "#fff"),
    ("🧬", "Biomarker Explorer", "Explore gene expression profiles and lung cancer biomarkers across cell lines.", "#0077B6", "#00B4D8", "#fff", "#fff"),
    ("🧪", "Drug Explorer", "Visualize molecular structures and graph-based drug representations.", "#EBF5FB", "#D6EAF8", "#1B3A6B", "#2C3E50"),
    ("🧠", "Model Information", "Understand the architecture, methodology and model performance.", "#2E86C1", "#1E56A0", "#AED6F1", "#fff"),
]

for row in range(2):
    col_a, col_b = st.columns(2)
    for col, card in zip([col_a, col_b], nav_cards[row*2:(row+1)*2]):
        emoji, title, desc, bg1, bg2, title_color, desc_color = card
        with col:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {bg1}, {bg2});
                border-radius: 14px;
                padding: 22px 22px;
                margin-bottom: 12px;
                cursor: pointer;
                transition: transform 0.2s;
                height: 180px;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                box-sizing: border-box;
            ">
                <div style="font-size:1.6rem; margin-bottom:8px;">{emoji}</div>
                <h3 style="color:{title_color}; margin:0 0 6px; font-size:1.05rem;">{title}</h3>
                <p style="color:{desc_color}; opacity:0.80; font-size:0.87rem; margin:0; line-height:1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# Goal
# --------------------------------------------------

st.markdown('<h2 style="margin-bottom:0.8rem;">🎯 Project Goal</h2>', unsafe_allow_html=True)

st.markdown("""
<div style="
    background: linear-gradient(135deg, #0A1628 0%, #1B3A6B 100%);
    border-radius: 16px;
    padding: 32px 36px;
    color: white;
">
    <p style="font-size:1.02rem; line-height:1.8; color:rgba(255,255,255,0.85); margin:0 0 20px;">
        To enable precision oncology by predicting how individual lung cancer samples respond
        to different therapeutic agents and recommending the most effective personalized treatment options.
    </p>
    <div style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:24px;">
        <span style="background:rgba(174,214,241,0.20); border:1px solid rgba(174,214,241,0.35); border-radius:8px; padding:6px 14px; font-size:0.84rem; color:#AED6F1;">Cancer Genomics</span>
        <span style="background:rgba(174,214,241,0.20); border:1px solid rgba(174,214,241,0.35); border-radius:8px; padding:6px 14px; font-size:0.84rem; color:#AED6F1;">Representation Learning</span>
        <span style="background:rgba(174,214,241,0.20); border:1px solid rgba(174,214,241,0.35); border-radius:8px; padding:6px 14px; font-size:0.84rem; color:#AED6F1;">Drug Molecular Structures</span>
        <span style="background:rgba(174,214,241,0.20); border:1px solid rgba(174,214,241,0.35); border-radius:8px; padding:6px 14px; font-size:0.84rem; color:#AED6F1;">Graph Neural Networks</span>
    </div>
    <div style="
        background: rgba(0,180,216,0.20);
        border-left: 3px solid #00B4D8;
        border-radius: 0 10px 10px 0;
        padding: 12px 16px;
    ">
        <p style="margin:0; font-size:0.92rem; color:#AED6F1; font-style:italic;">
            "Harnessing AI and Graph Neural Networks to build the future of Personalized Medicine for Lung Cancer."
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
