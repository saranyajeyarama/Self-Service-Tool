import streamlit as st
from components.login import render_login
from components.header import render_header
from components.dashboard import render_dashboard
# from components.market_modal import render_market_modal
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
query_params = st.experimental_get_query_params()
if 'code' in query_params and 'state' in query_params:
    # Verify state parameter
    if query_params['state'][0] == st.session_state.get('state', ''):
        # Process authentication code
        result = st.session_state.auth.process_auth_code(query_params['code'][0])
        if result and 'access_token' in result:
            st.session_state.user = result.get('id_token_claims')
            st.session_state.logged_in = True
            # Clear query parameters
            st.experimental_set_query_params()
            st.rerun()
    else:
        st.error('Invalid state parameter. Please try logging in again.')

# Load CSS
load_css()

# Main app logic
if not st.session_state.get('logged_in', False):
    render_login()
else:
    render_header()
    render_dashboard()
    # render_market_modal()