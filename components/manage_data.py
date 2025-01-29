import streamlit as st

# Ensure session state has the required keys
if "show_upload_modal" not in st.session_state:
    st.session_state.show_upload_modal = False

if "selected_tab" not in st.session_state:
    st.session_state.selected_tab = "Mapping File"

def toggle_modal():
    """Function to toggle the modal state."""
    st.session_state.show_upload_modal = not st.session_state.show_upload_modal

def set_tab(tab_name):
    """Function to switch tabs on button click."""
    st.session_state.selected_tab = tab_name

def render_manage_data():
    # ✅ Ensure session state is initialized inside the function too
    if "show_upload_modal" not in st.session_state:
        st.session_state.show_upload_modal = False

    if "selected_tab" not in st.session_state:
        st.session_state.selected_tab = "Mapping File"

    st.markdown("""
        <style>
            .tab-container {
                display: flex;
                gap: 10px;
                margin-bottom: 20px;
            }
            .tab-button {
                background-color: white;
                border: 2px solid #0033A0;
                color: #0033A0;
                padding: 10px 15px;
                border-radius: 5px;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease-in-out;
            }
            .tab-button.active {
                background-color: #0033A0;
                color: white;
            }
            .tab-button:hover {
                background-color: #002280;
                color: white;
            }
            .upload-container {
                text-align: center;
                margin-top: 30px;
            }
            .upload-box {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 20px;
                margin: 20px auto;
                border-radius: 8px;
                text-align: center;
                width: 60%;
            }
            .upload-box img {
                width: 60px;
                margin-bottom: 10px;
            }
            .upload-actions {
                display: flex;
                justify-content: center;
                gap: 15px;
                margin-top: 20px;
            }
            .upload-actions button {
                background-color: #0033A0;
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
                font-size: 16px;
                transition: background-color 0.3s;
            }
            .upload-actions button:hover {
                background-color: #002280;
            }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Render Button-Based Tabs
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        if st.button("Mapping File", key="map_file", use_container_width=True):
            set_tab("Mapping File")

    with col2:
        if st.button("Internal KPIs", key="int_kpis", use_container_width=True):
            set_tab("Internal KPIs")

    with col3:
        if st.button("External KPIs", key="ext_kpis", use_container_width=True):
            set_tab("External KPIs")

    with col4:
        if st.button("Will/Skill", key="will_skill", use_container_width=True):
            set_tab("Will/Skill")

    with col5:
        if st.button("Future CAGR", key="future_cagr", use_container_width=True):
            set_tab("Future CAGR")

    with col6:
        if st.button("KPI Weightage", key="kpi_weight", use_container_width=True):
            set_tab("KPI Weightage")

    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ Render Content Based on Selected Tab
    if st.session_state.selected_tab == "Mapping File":
        st.markdown("<h3 style='text-align: center;'>Upload Mapping File</h3>", unsafe_allow_html=True)

        # Upload Section
        st.markdown("""
            <div class="upload-box">
                <img src="https://img.icons8.com/ios/50/printer.png" alt="Upload Icon">
                <p>Upload Mapping File</p>
                <div class="upload-actions">
                    <button>Download Template</button>
                    <button onclick="toggle_modal()">Upload File</button>
                </div>
            </div>
        """, unsafe_allow_html=True)

    elif st.session_state.selected_tab == "Internal KPIs":
        st.markdown("### Internal KPIs Content Coming Soon...")

    elif st.session_state.selected_tab == "External KPIs":
        st.markdown("### External KPIs Content Coming Soon...")

    elif st.session_state.selected_tab == "Will/Skill":
        st.markdown("### Will/Skill Content Coming Soon...")

    elif st.session_state.selected_tab == "Future CAGR":
        st.markdown("### Future CAGR Content Coming Soon...")

    elif st.session_state.selected_tab == "KPI Weightage":
        st.markdown("### KPI Weightage Content Coming Soon...")

    # **Pop-up Modal for Uploading Files**
    if st.session_state.show_upload_modal:
        st.markdown('<div class="modal-overlay"></div>', unsafe_allow_html=True)
        with st.container():
            st.markdown(f"""
                <div class="modal-container">
                    <span class="close-button" onclick="toggle_modal()">❌</span>
                    <h4 style="text-align: left;">Upload Mapping File</h4>
                    
                    <div class="upload-box">
                        <img src="https://img.icons8.com/ios/50/upload-to-cloud.png" alt="Upload Icon" style="width: 50px; display: block; margin: 10px auto;">
                        <p>Drag and drop file to upload</p>
                        <button>Select File</button>
                        <p style="font-size: 12px; color: #666;">XLS, file size no more than 20MB</p>
                    </div>

                    <div style="background: #f9f9f9; padding: 10px; margin-top: 15px; border-radius: 5px; text-align: left;">
                        <img src="https://img.icons8.com/color/48/microsoft-excel.png" alt="Excel Icon" style="width: 24px; vertical-align: middle;">
                        <span style="margin-left: 10px;">File_Name_109934.xls</span>
                        <div class="upload-progress">
                            <progress value="32" max="100" style="width: 100%;"></progress> 
                            <p>32% Uploading... 4 seconds left</p>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: space-between; margin-top: 20px;">
                        <span class="cancel-button" onclick="toggle_modal()">Cancel</span>
                        <button class="validate-button">Validate Data</button>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        # Close Modal when "Cancel" or ❌ is clicked
        if st.button("Close", key="close-modal"):
            st.session_state.show_upload_modal = False
