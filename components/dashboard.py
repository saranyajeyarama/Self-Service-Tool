import streamlit as st

def render_welcome_section():
    st.markdown("""
    <h1 style="font-size: 24px; margin-bottom: 1rem;">Welcome to Self Service SCM Scorecard</h1>
    <p style="max-width: 700px; margin-bottom: 2rem;">
        An analytical tool that enables users to generate and share SCM scorecards by categorising 
        customers/Channels into SCM quadrants based on user input KPI weightages and Quartile combinations.
    </p>
    """, unsafe_allow_html=True)

def render_manage_data_card():
    st.markdown("""
    <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; gap: 2rem; align-items: center;">
                <div class="icon-circle">📊</div>
                <div>
                    <h3 style="margin-bottom: 0.5rem;">Manage Data</h3>
                    <p>Start maximizing tool performance by uploading and managing your data</p>
                </div>
            </div>
            <button class="button">+ Manage Data</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_action_cards():
    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin: 2rem 0;">
        <div class="card" style="text-align: center;">
            <div class="icon-circle">📈</div>
            <h4 style="color: #0000A0;">Data Overview →</h4>
        </div>
        <div class="card" style="text-align: center;">
            <div class="icon-circle">🎯</div>
            <h4 style="color: #0000A0;">Create SCM Placements →</h4>
        </div>
        <div class="card" style="text-align: center;">
            <div class="icon-circle">📋</div>
            <h4 style="color: #0000A0;">SCM Scorecard →</h4>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_footer_nav():
    st.markdown("""
    <div class="footer-nav">
        <span class="footer-link">View Saved SCM Placements</span>
        <span class="footer-link">Compare SCM Placements</span>
        <span class="footer-link">Access management</span>
    </div>
    """, unsafe_allow_html=True)

def render_dashboard():
    st.markdown('<div class="content">', unsafe_allow_html=True)
    render_welcome_section()
    render_manage_data_card()
    render_action_cards()
    render_footer_nav()
    st.markdown('</div>', unsafe_allow_html=True)
    