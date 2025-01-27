import streamlit as st

def render_sidebar():
    with st.sidebar:
        # Market Selection
        st.markdown("""
        <div style='margin-bottom: 2rem;'>
            <h3 style='color: #666; font-size: 14px; margin-bottom: 0.5rem;'>SELECTED MARKET</h3>
        </div>
        """, unsafe_allow_html=True)
        
        selected_market = st.selectbox(
            "",
            ["🇨🇳 China", "🇺🇸 U.S.", "🇦🇪 U.A.E", "🇫🇷 France"],
            label_visibility="collapsed"
        )
        
        st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
        
        # Navigation
        st.markdown("""
        <h3 style='color: #666; font-size: 14px; margin-bottom: 1rem;'>NAVIGATION</h3>
        """, unsafe_allow_html=True)
        
        # Custom CSS for navigation
        st.markdown("""
        <style>
            .nav-link {
                display: flex;
                align-items: center;
                padding: 0.75rem 1rem;
                margin: 0.25rem 0;
                border-radius: 4px;
                color: #333;
                text-decoration: none;
                transition: background-color 0.2s;
            }
            
            .nav-link:hover {
                background-color: rgba(0, 0, 160, 0.04);
            }
            
            .nav-link.active {
                background-color: rgba(0, 0, 160, 0.08);
                color: #0000A0;
            }
            
            .nav-link svg {
                margin-right: 0.75rem;
                width: 20px;
                height: 20px;
            }
        </style>
        """, unsafe_allow_html=True)
        
        # Navigation items
        nav_items = [
            ("🏠 Home", "home"),
            ("📊 Manage Data", "manage-data"),
            ("📈 Data Overview", "data-overview"),
            ("🎯 Create Placement", "create-placement"),
            ("💾 Saved Placements", "saved-placements"),
            ("🔄 Compare Placement", "compare-placement"),
            ("📑 SCM Scorecard", "scm-scorecard")
        ]
        
        for label, key in nav_items:
            active = st.session_state.get('current_page', 'home') == key
            if st.button(
                label,
                key=f"nav_{key}",
                use_container_width=True,
                type="secondary" if active else "secondary",
            ):
                st.session_state.current_page = key
                st.rerun()
            
        # Add some spacing at the bottom
        st.markdown("<div style='flex-grow: 1;'></div>", unsafe_allow_html=True)