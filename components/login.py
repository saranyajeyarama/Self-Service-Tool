import streamlit as st
from utils.auth import init_auth
import uuid

def render_login():
    # Initialize authentication
    init_auth()
    
    # Ensure session state is initialized properly
    if "auth" not in st.session_state:
        st.session_state.auth = None

    # Center the content using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    # Add custom styling for col2
    st.markdown("""
        <style>
            [data-testid="column"][data-testid="stVerticalBlock"] {
                background-color: white;
                border-radius: 6px;
                padding: 2rem;
                box-shadow: 0px 2px 10px rgba(0, 0, 160, 0.16);
            }
        </style>
    """, unsafe_allow_html=True)
    
    with col2:
        # Add some vertical spacing
        st.markdown("<br>" * 4, unsafe_allow_html=True)
        
        # Create a container for the login card
        with st.container():
            # MARS logo and line
            st.markdown("""
                <div style='text-align: center;'>
                    <div style='
                        display: inline-block;
                        background-color: #0000A0;
                        color: white;
                        padding: 0.5rem 1rem;
                        font-weight: bold;
                        font-size: 24px;
                        margin-bottom: 0.5rem;
                    '>
                        MARS
                    </div>
                </div>
                <div style='
                    width: 90px;
                    height: 4px;
                    background: #EC6D2D;
                    margin: 0 auto;
                '>
                </div>
            """, unsafe_allow_html=True)
            
            # Add some spacing
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Title and subtitle
            st.markdown("""
                <h1 style='
                    text-align: center;
                    color: #393939;
                    font-size: 24px;
                    margin: 2rem 0;
                '>
                    SCM Scorecard
                </h1>
                <h2 style='
                    text-align: center;
                    color: #393939;
                    font-size: 18px;
                    margin-bottom: 3rem;
                '>
                    Self Service Tool
                </h2>
            """, unsafe_allow_html=True)
            
            # Center the button using columns
            btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
            with btn_col2:
                if st.button("Single sign on", key="sso-login", type="primary", use_container_width=True):
                    try:
                        # Generate state parameter for security
                        st.session_state.state = str(uuid.uuid4())

                        # Get authorization URL and redirect
                        auth_url = st.session_state.auth.get_auth_url()
                        if auth_url:
                            st.query_params.update({
                                "response_type": "code",
                                "state": st.session_state.state
                            })
                            st.markdown(f'<meta http-equiv="refresh" content="0;url={auth_url}">', unsafe_allow_html=True)
                        else:
                            st.error("Failed to retrieve authentication URL. Please try again.")
                    except Exception as e:
                        st.error(f"Authentication Error: {e}")

    # Set background color for the entire page
    st.markdown("""
        <style>
            .stApp {
                background-color: #daecf3;
            }
            
            [data-testid="stButton"] button {
                background-color: #0000A0;
                color: white;
                font-weight: bold;
                padding: 0.75rem 1.5rem;
                border-radius: 4px;
            }
            
            [data-testid="stButton"] button:hover {
                background-color: #000080;
            }
        </style>
    """, unsafe_allow_html=True)
