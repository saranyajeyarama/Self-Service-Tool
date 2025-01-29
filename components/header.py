import streamlit as st

def render_header():
    st.markdown("""
        <style>
            .top-bar {
                background-color: #0033A0; /* Exact blue color */
                height: 50px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 20px;
                color: white;
                font-family: Arial, sans-serif;
            }
            .top-bar .left-section {
                display: flex;
                align-items: center;
                gap: 15px;
            }
            .top-bar .right-section {
                display: flex;
                align-items: center;
                gap: 15px;
            }
            .top-bar a {
                text-decoration: none;
                color: white;
                font-size: 14px;
                font-weight: 500;
            }
            .top-bar .icon {
                font-size: 18px;
            }
        </style>
        <div class="top-bar">
            <div class="left-section">
                <strong>MARS</strong>
                <strong>SCM</strong>
                <a href="#">Landing Page</a>
            </div>
            <div class="right-section">
                <a href="#">User Guide</a>
                <a href="#">Glossary</a>
                <span class="icon">🔍</span>
                <span class="icon">👤</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
