import streamlit as st
from components.login import render_login
from components.header import render_header
from components.dashboard import render_dashboard
from components.sidebar import render_sidebar
from utils.session import initialize_session_state
from utils.styles import load_css
from utils.auth import init_auth

# Set page config
st.set_page_config(layout="wide", page_title="SCM Scorecard")

# Initialize session state
initialize_session_state()

# Initialize authentication
init_auth()

# Handle SSO callback
query_params = st.query_params
if 'code' in query_params and 'state' in query_params:
    # Verify state parameter
    if query_params.get('state') == st.session_state.get('state', ''):
        # Process authentication code
        result = st.session_state.auth.process_auth_code(query_params.get('code'))
        if result and 'access_token' in result:
            st.session_state.user = result.get('id_token_claims')
            st.session_state.logged_in = True
            # Clear query parameters
            st.query_params.clear()
            st.rerun()
    else:
        st.error('Invalid state parameter. Please try logging in again.')

# Load CSS
load_css()

# # Main app logic
# if not st.session_state.get('logged_in', False):
#     render_login()
# else:
render_header()
render_sidebar()

# Render content based on current page
current_page = st.session_state.get('current_page', 'home')

if current_page == 'home':
    render_dashboard()
elif current_page == 'manage-data':
    st.title("Manage Data")
    st.write("Data management interface will be implemented here")
elif current_page == 'data-overview':
    st.title("Data Overview")
    st.write("Data overview and analytics will be implemented here")
elif current_page == 'create-placement':
    st.title("Create Placement")
    st.write("Placement creation interface will be implemented here")
elif current_page == 'saved-placements':
    st.title("Saved Placements")
    st.write("Saved placements list will be implemented here")
elif current_page == 'compare-placement':
    st.title("Compare Placement")
    st.write("Placement comparison interface will be implemented here")
elif current_page == 'scm-scorecard':
    st.title("SCM Scorecard")
    st.write("SCM scorecard interface will be implemented here")