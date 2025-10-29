import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RICE/ICE Scoring Calculator",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    /* Card styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Custom card container */
    .card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }
    
    /* Header styling */
    h1 {
        color: white !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    
    h2 {
        color: #333 !important;
        font-weight: 600 !important;
        font-size: 1.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    h3 {
        color: #555 !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
    }
    
    /* Subtitle */
    .subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Priority badges */
    .priority-high {
        background: #10b981;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-weight: 600;
        display: inline-block;
    }
    
    .priority-medium {
        background: #f59e0b;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-weight: 600;
        display: inline-block;
    }
    
    .priority-low {
        background: #ef4444;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-weight: 600;
        display: inline-block;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Input field styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 2px solid #e5e7eb;
    }
    
    /* Slider styling */
    .stSlider>div>div>div>div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* DataFrame styling */
    .dataframe {
        border: none !important;
    }
    
    /* Toggle styling */
    .stRadio>div {
        background: white;
        padding: 0.5rem;
        border-radius: 8px;
    }
    
    /* Info box */
    .info-box {
        background: #ede9fe;
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

if 'ideas' not in st.session_state:
    st.session_state.ideas = []

st.title("📊 RICE/ICE Scoring Calculator")
st.markdown('<p class="subtitle">Prioritize your product ideas with data-driven decision making</p>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Scoring Framework")
    framework = st.radio(
        "Choose your framework:",
        ["RICE", "ICE"],
        help="RICE includes Reach, while ICE focuses on Impact, Confidence, and Effort"
    )
    
    st.markdown("---")
    st.markdown("#### Formula")
    if framework == "RICE":
        st.markdown("""
        <div class="info-box">
        <strong>RICE Score =</strong><br>
        (Reach × Impact × Confidence) ÷ Effort
        </div>
        """, unsafe_allow_html=True)
        st.caption("**Reach:** How many people will this impact?")
        st.caption("**Impact:** How much will it impact each person?")
        st.caption("**Confidence:** How confident are you in your estimates?")
        st.caption("**Effort:** How much time/resources will it take?")
    else:
        st.markdown("""
        <div class="info-box">
        <strong>ICE Score =</strong><br>
        (Impact × Confidence) ÷ Effort
        </div>
        """, unsafe_allow_html=True)
        st.caption("**Impact:** How much will it impact each person?")
        st.caption("**Confidence:** How confident are you in your estimates?")
        st.caption("**Effort:** How much time/resources will it take?")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Add New Idea")
    
    with st.form("idea_form", clear_on_submit=True):
        idea_name = st.text_input("Idea/Feature Name", placeholder="e.g., User Dashboard Redesign")
        idea_description = st.text_area("Description (optional)", placeholder="Brief description of the idea...", height=100)
        
        st.markdown("#### Scoring")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if framework == "RICE":
                reach = st.slider(
                    "Reach",
                    min_value=1,
                    max_value=10,
                    value=5,
                    help="How many people will this reach? (1=Very Few, 10=Everyone)"
                )
            
            impact = st.slider(
                "Impact",
                min_value=1,
                max_value=10,
                value=5,
                help="How much impact per person? (1=Minimal, 10=Massive)"
            )
        
        with col_b:
            confidence = st.slider(
                "Confidence",
                min_value=1,
                max_value=10,
                value=5,
                help="How confident are you? (1=Low, 10=High)"
            )
            
            effort = st.slider(
                "Effort",
                min_value=1,
                max_value=10,
                value=5,
                help="How much effort/time needed? (1=Minimal, 10=Extensive)"
            )
        
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
                st.success(f"✅ Added '{idea_name}' with score: {round(score, 2)}")
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.ideas:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📈 Prioritization Results")
    
    df = pd.DataFrame(st.session_state.ideas)
    df_sorted = df.sort_values('Score', ascending=False).reset_index(drop=True)
    
    def get_priority(score, framework):
        if framework == "RICE":
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
        height=400
    )
    
    col_clear, col_info = st.columns([1, 3])
    with col_clear:
        if st.button("Clear All Ideas", type="secondary"):
            st.session_state.ideas = []
            st.rerun()
    
    with col_info:
        st.caption(f"💡 Total ideas evaluated: {len(st.session_state.ideas)} | Framework: {framework}")
    
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.info("👆 Add your first idea above to start prioritizing your product backlog!")
    st.markdown('</div>', unsafe_allow_html=True)
