import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RICE/ICE Scoring Calculator",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* Main background with smooth gradient */
    .main {
        background: linear-gradient(120deg, #667eea 0%, #9198e5 35%, #e8eaf6 70%, #ffffff 100%);
        background-attachment: fixed;
        padding: 0;
    }
    
    .stApp {
        background: transparent;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sticky header with framework toggle */
    .sticky-header {
        position: sticky;
        top: 0;
        z-index: 1000;
        background: white;
        padding: 1.5rem 3rem;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
        border-radius: 0 0 16px 16px;
        margin: 0 0 3rem 0;
    }
    
    .header-content {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .app-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a1a2e;
        margin: 0;
        line-height: 1.2;
    }
    
    .app-subtitle {
        font-size: 0.875rem;
        color: #6b7280;
        margin: 0.25rem 0 0 0;
        font-weight: 400;
    }
    
    /* Container */
    .content-wrapper {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 3rem 3rem 3rem;
    }
    
    /* Module cards with color highlights */
    .module-card {
        background: white;
        border-radius: 16px;
        padding: 2.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        margin-bottom: 2rem;
        border-left: 4px solid #667eea;
    }
    
    .module-card.results {
        border-left-color: #10b981;
    }
    
    .card-header {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #f3f4f6;
    }
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif;
        color: #1a1a2e;
    }
    
    .section-label {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #6b7280;
        margin-bottom: 0.75rem;
        display: block;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.625rem 1.5rem;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.2s ease;
        box-shadow: 0 2px 4px rgba(102, 126, 234, 0.2);
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    .stButton>button[kind="secondary"] {
        background: white;
        color: #667eea;
        border: 2px solid #e5e7eb;
        box-shadow: none;
    }
    
    .stButton>button[kind="secondary"]:hover {
        border-color: #667eea;
        background: #f9fafb;
    }
    
    /* Input fields */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        padding: 0.75rem;
        font-size: 0.9rem;
        transition: border-color 0.2s;
    }
    
    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Labels */
    .stTextInput>label,
    .stTextArea>label,
    .stSlider>label {
        font-weight: 500;
        color: #374151;
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
    }
    
    /* Sliders */
    .stSlider>div>div>div>div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stSlider>div>div>div {
        padding: 0.5rem 0;
    }
    
    /* Radio buttons in header */
    .stRadio>div {
        background: #f9fafb;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: 2px solid #e5e7eb;
        display: flex;
        gap: 1rem;
    }
    
    .stRadio>label {
        font-weight: 600;
        color: #374151;
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
    }
    
    /* DataFrame */
    .dataframe {
        font-size: 0.875rem;
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Messages */
    .stSuccess {
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        border-radius: 8px;
        color: #065f46;
        padding: 1rem;
    }
    
    .stInfo {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        border-radius: 8px;
        color: #1e40af;
        padding: 1.25rem;
        font-size: 0.9rem;
    }
    
    .stError {
        background: #fef2f2;
        border: 1px solid #fecaca;
        border-radius: 8px;
        color: #991b1b;
        padding: 1rem;
    }
    
    /* Priority badges - modern text-based */
    .priority-high {
        background: #ecfdf5;
        color: #065f46;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid #a7f3d0;
    }
    
    .priority-medium {
        background: #fef3c7;
        color: #92400e;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid #fcd34d;
    }
    
    .priority-low {
        background: #fef2f2;
        color: #991b1b;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid #fecaca;
    }
    
    /* Spacing utilities */
    .spacer {
        height: 2rem;
    }
    
    .spacer-small {
        height: 1rem;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    
    /* Framework selector in header */
    .framework-selector {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .framework-label {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #6b7280;
    }
</style>
""", unsafe_allow_html=True)

if 'ideas' not in st.session_state:
    st.session_state.ideas = []

st.markdown('<div class="sticky-header">', unsafe_allow_html=True)
st.markdown('<div class="header-content">', unsafe_allow_html=True)

col_title, col_framework = st.columns([2, 1])

with col_title:
    st.markdown('<div class="app-title">RICE/ICE Scoring Calculator</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Prioritize product ideas with data-driven scoring</div>', unsafe_allow_html=True)

with col_framework:
    st.markdown('<span class="section-label">Framework</span>', unsafe_allow_html=True)
    framework = st.radio(
        "Select Framework",
        ["RICE", "ICE"],
        horizontal=True,
        help="RICE = (Reach × Impact × Confidence) ÷ Effort  |  ICE = (Impact × Confidence) ÷ Effort",
        label_visibility="collapsed"
    )

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

st.markdown('<div class="module-card">', unsafe_allow_html=True)
st.markdown('<div class="card-header">Add New Idea</div>', unsafe_allow_html=True)

with st.form("idea_form", clear_on_submit=True):
    idea_name = st.text_input("Idea Name", placeholder="e.g., Dashboard Redesign")
    
    st.markdown('<div class="spacer-small"></div>', unsafe_allow_html=True)
    
    idea_description = st.text_area(
        "Description (Optional)", 
        placeholder="Brief description of the idea...", 
        height=100
    )
    
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown('<span class="section-label">Scoring Criteria</span>', unsafe_allow_html=True)
    
    if framework == "RICE":
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            reach = st.slider("Reach", 1, 10, 5, help="Number of people impacted")
        
        with col2:
            impact = st.slider("Impact", 1, 10, 5, help="Impact per person")
        
        with col3:
            confidence = st.slider("Confidence", 1, 10, 5, help="Confidence in estimates")
        
        with col4:
            effort = st.slider("Effort", 1, 10, 5, help="Time and resources needed")
    else:
        reach = None
        col1, col2, col3 = st.columns(3)
        
        with col1:
            impact = st.slider("Impact", 1, 10, 5, help="Overall impact")
        
        with col2:
            confidence = st.slider("Confidence", 1, 10, 5, help="Confidence level")
        
        with col3:
            effort = st.slider("Effort", 1, 10, 5, help="Effort required")
    
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    
    col_btn, col_empty = st.columns([1, 3])
    with col_btn:
        submitted = st.form_submit_button("Calculate Score", use_container_width=True)
    
    if submitted:
        if not idea_name.strip():
            st.error("Please enter an idea name")
        else:
            if framework == "RICE":
                score = (reach * impact * confidence) / effort
                new_idea = {
                    "Idea": idea_name,
                    "Description": idea_description if idea_description else "-",
                    "Reach": reach,
                    "Impact": impact,
                    "Confidence": confidence,
                    "Effort": effort,
                    "Score": round(score, 2),
                    "Framework": "RICE"
                }
            else:
                score = (impact * confidence) / effort
                new_idea = {
                    "Idea": idea_name,
                    "Description": idea_description if idea_description else "-",
                    "Impact": impact,
                    "Confidence": confidence,
                    "Effort": effort,
                    "Score": round(score, 2),
                    "Framework": "ICE"
                }
            
            st.session_state.ideas.append(new_idea)
            st.success(f"Added '{idea_name}' with score: {round(score, 2)}")
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

if st.session_state.ideas:
    st.markdown('<div class="module-card results">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">Prioritization Results</div>', unsafe_allow_html=True)
    
    df = pd.DataFrame(st.session_state.ideas)
    df_sorted = df.sort_values('Score', ascending=False).reset_index(drop=True)
    
    def get_priority(score, framework_type):
        if framework_type == "RICE":
            if score >= 50:
                return "● High"
            elif score >= 20:
                return "● Medium"
            else:
                return "● Low"
        else:
            if score >= 20:
                return "● High"
            elif score >= 10:
                return "● Medium"
            else:
                return "● Low"
    
    df_sorted['Priority'] = df_sorted.apply(
        lambda row: get_priority(row['Score'], row['Framework']), 
        axis=1
    )
    
    base_cols = ['Idea', 'Description', 'Impact', 'Confidence', 'Effort', 'Score', 'Framework', 'Priority']
    available_cols = []
    
    for col in base_cols:
        if col in df_sorted.columns:
            available_cols.append(col)
    
    if 'Reach' in df_sorted.columns and framework == "RICE":
        idx = available_cols.index('Impact')
        available_cols.insert(idx, 'Reach')
    
    df_display = df_sorted[available_cols]
    
    column_config = {
        "Priority": st.column_config.TextColumn(
            "Priority",
            help="Priority level based on score",
            width="small"
        ),
        "Score": st.column_config.NumberColumn(
            "Score",
            help="Calculated priority score",
            format="%.2f"
        )
    }
    
    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True,
        height=min(500, len(df_display) * 35 + 38),
        column_config=column_config
    )
    
    st.markdown('<div class="spacer-small"></div>', unsafe_allow_html=True)
    
    col_info, col_clear = st.columns([4, 1])
    
    with col_info:
        st.caption(f"{len(st.session_state.ideas)} idea(s) evaluated")
    
    with col_clear:
        if st.button("Clear All", type="secondary", use_container_width=True):
            st.session_state.ideas = []
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="module-card results">', unsafe_allow_html=True)
    st.info("Add your first idea above to start prioritizing your product backlog")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
