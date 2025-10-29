import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RICE/ICE Scoring Calculator",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    /* Clean background */
    .main {
        background-color: #f8f9fa;
    }
    
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }
    
    .main-header h1 {
        color: #1a1a1a;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #6c757d;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    div[data-testid="stVerticalBlock"] > div:has(div.element-container) {
        background-color: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #5865f2;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    
    .stButton>button:hover {
        background-color: #4752c4;
    }
    
    /* Form styling */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        border: 1px solid #dee2e6;
        border-radius: 6px;
        padding: 0.5rem;
    }
    
    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: #5865f2;
        box-shadow: 0 0 0 0.2rem rgba(88, 101, 242, 0.25);
    }
    
    /* Slider styling */
    .stSlider>div>div>div>div {
        background-color: #5865f2;
    }
    
    /* Radio button styling */
    .stRadio>label {
        font-weight: 600;
        color: #1a1a1a;
        font-size: 1rem;
    }
    
    /* Section headers */
    h2, h3 {
        color: #1a1a1a;
        font-weight: 600;
    }
    
    /* DataFrame styling */
    .dataframe {
        font-size: 0.9rem;
    }
    
    /* Success message */
    .stSuccess {
        background-color: #d4edda;
        border-color: #c3e6cb;
        color: #155724;
    }
    
    /* Info message */
    .stInfo {
        background-color: #e7f3ff;
        border-color: #b3d9ff;
        color: #004085;
    }
</style>
""", unsafe_allow_html=True)

if 'ideas' not in st.session_state:
    st.session_state.ideas = []

st.markdown('<div class="main-header"><h1>📊 RICE/ICE Scoring Calculator</h1></div>', unsafe_allow_html=True)
st.markdown('<p class="subtitle" style="text-align: center;">Prioritize your product ideas with data-driven decision making</p>', unsafe_allow_html=True)

col_toggle, col_spacer = st.columns([1, 3])
with col_toggle:
    framework = st.radio(
        "Framework:",
        ["RICE", "ICE"],
        horizontal=True,
        help="RICE = (Reach × Impact × Confidence) ÷ Effort | ICE = (Impact × Confidence) ÷ Effort"
    )

st.markdown("---")

st.markdown("### ➕ Add New Idea")

with st.form("idea_form", clear_on_submit=True):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        idea_name = st.text_input("Idea/Feature Name *", placeholder="e.g., User Dashboard Redesign")
    
    with col2:
        st.write("")
    
    idea_description = st.text_area("Description (optional)", placeholder="Brief description of the idea...", height=80)
    
    st.markdown("**Scoring Criteria**")
    
    if framework == "RICE":
        col_a, col_b, col_c, col_d = st.columns(4)
        
        with col_a:
            reach = st.slider(
                "Reach",
                min_value=1,
                max_value=10,
                value=5,
                help="How many people will this impact?"
            )
        
        with col_b:
            impact = st.slider(
                "Impact",
                min_value=1,
                max_value=10,
                value=5,
                help="How much will it impact each person?"
            )
        
        with col_c:
            confidence = st.slider(
                "Confidence",
                min_value=1,
                max_value=10,
                value=5,
                help="How confident are you in your estimates?"
            )
        
        with col_d:
            effort = st.slider(
                "Effort",
                min_value=1,
                max_value=10,
                value=5,
                help="How much time/resources will it take?"
            )
    else:
        reach = None
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            impact = st.slider(
                "Impact",
                min_value=1,
                max_value=10,
                value=5,
                help="How much will it impact?"
            )
        
        with col_b:
            confidence = st.slider(
                "Confidence",
                min_value=1,
                max_value=10,
                value=5,
                help="How confident are you?"
            )
        
        with col_c:
            effort = st.slider(
                "Effort",
                min_value=1,
                max_value=10,
                value=5,
                help="How much effort/time needed?"
            )
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
    with col_btn1:
        submitted = st.form_submit_button("Calculate Score", use_container_width=True)
    
    if submitted:
        if not idea_name.strip():
            st.error("⚠️ Please enter an idea name")
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
            st.success(f"✅ Added '{idea_name}' with score: {round(score, 2)}")
            st.rerun()

st.markdown("---")

if st.session_state.ideas:
    st.markdown("### 📈 Prioritization Results")
    
    df = pd.DataFrame(st.session_state.ideas)
    df_sorted = df.sort_values('Score', ascending=False).reset_index(drop=True)
    
    def get_priority(score, framework_type):
        if framework_type == "RICE":
            if score >= 50:
                return "🟢 High"
            elif score >= 20:
                return "🟡 Medium"
            else:
                return "🔴 Low"
        else:
            if score >= 20:
                return "🟢 High"
            elif score >= 10:
                return "🟡 Medium"
            else:
                return "🔴 Low"
    
    df_sorted['Priority'] = df_sorted.apply(lambda row: get_priority(row['Score'], row['Framework']), axis=1)
    
    base_cols = ['Idea', 'Description', 'Impact', 'Confidence', 'Effort', 'Score', 'Framework', 'Priority']
    available_cols = [col for col in base_cols if col in df_sorted.columns]
    
    if 'Reach' in df_sorted.columns:
        available_cols.insert(3, 'Reach')
    
    df_display = df_sorted[available_cols]
    
    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True,
        height=min(400, len(df_display) * 35 + 38)
    )
    
    col_info, col_clear = st.columns([3, 1])
    
    with col_info:
        st.caption(f"💡 {len(st.session_state.ideas)} idea(s) evaluated")
    
    with col_clear:
        if st.button("Clear All", type="secondary", use_container_width=True):
            st.session_state.ideas = []
            st.rerun()
else:
    st.info("👆 Add your first idea above to start prioritizing!")
