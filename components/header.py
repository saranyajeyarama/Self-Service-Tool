import streamlit as st

def render_header():
    st.markdown("""
    <div class="header">
        <div style="display: flex; align-items: center; gap: 2rem;">
            <span style="font-weight: bold;">MARS</span>
            <span style="font-weight: bold;">SCM</span>
            <span>Landing Page</span>
        </div>
        <div style="display: flex; align-items: center; gap: 1.5rem;">
            <span>User Guide</span>
            <span>Glossary</span>
            <span>🔍</span>
            <span>👤</span>
        </div>
    </div>
    """, unsafe_allow_html=True)