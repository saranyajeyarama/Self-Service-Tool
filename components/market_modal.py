import streamlit as st

def render_create_market_dialog():
    st.markdown("""
    <div style="
        position: fixed;
        top: 0;
        left: 0;
        width: 1366px;
        height: 713px;
        background: rgba(148.75, 148.75, 148.75, 0.10);
        backdrop-filter: blur(12px);
        z-index: 1002;
        display: flex;
        align-items: center;
        justify-content: center;
    ">
        <div class="modal" style="background: white; width: 600px;">
            <h2 style="font-size: 20px; margin-bottom: 1.5rem;">Create New Market</h2>
            <div style="margin-bottom: 1rem;">
                <label style="display: block; margin-bottom: 0.5rem; color: #666;">Market Name</label>
                <input type="text" placeholder="Enter market name" style="
                    width: 100%;
                    padding: 0.75rem;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    font-size: 14px;
                ">
            </div>
            <div style="margin-bottom: 1.5rem;">
                <label style="display: block; margin-bottom: 0.5rem; color: #666;">Market Code</label>
                <input type="text" placeholder="Enter market code" style="
                    width: 100%;
                    padding: 0.75rem;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    font-size: 14px;
                ">
            </div>
            <div style="display: flex; justify-content: flex-end; gap: 1rem;">
                <button class="button" style="background: #fff; color: #0000A0; border: 1px solid #0000A0;" onclick="document.querySelector('#cancel_create_market').click()">
                    Cancel
                </button>
                <button class="button" onclick="document.querySelector('#create_market').click()">
                    Create Market
                </button>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Cancel", key="cancel_create_market", type="primary"):
            st.session_state.show_create_market = False
            st.rerun()
    with col2:
        if st.button("Create", key="create_market", type="primary"):
            st.session_state.show_create_market = False
            st.rerun()

def render_market_modal():
    if st.session_state.show_modal:
        st.markdown("""
        <div class="modal-backdrop">
            <div class="modal">
                <h2 style="font-size: 20px; margin-bottom: 1rem;">Select a market</h2>
                <div class="market-grid">
                    <button class="market-button">🇨🇳 China</button>
                    <button class="market-button">🇺🇸 U.S.</button>
                    <button class="market-button">🇦🇪 U.A.E</button>
                    <button class="market-button">🇫🇷 France</button>
                    <button class="market-button">🇦🇪 U.A.E</button>
                    <button class="market-button" style="border: 1px dashed #AAAAAA;" onclick="document.querySelector('#show_create_market').click()">
                        <span style="color: #0000A0;">+ Create new market</span>
                    </button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Show Create Market", key="show_create_market"):
            st.session_state.show_create_market = True
            st.rerun()

        if st.button('Close Market Selection', key='close_modal'):
            st.session_state.show_modal = False
            st.rerun()

    if st.session_state.get('show_create_market', False):
        render_create_market_dialog()