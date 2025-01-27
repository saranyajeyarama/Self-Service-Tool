import streamlit as st

def initialize_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    # if 'show_modal' not in st.session_state:
    #     st.session_state.show_modal = True
    # if 'show_create_market' not in st.session_state:
    #     st.session_state.show_create_market = False
    