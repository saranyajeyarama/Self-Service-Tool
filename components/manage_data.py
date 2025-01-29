import streamlit as st

def render_manage_data():
    st.markdown("""
        <style>
            .upload-container {
                text-align: center;
                margin-top: 30px;
            }
            .upload-box {
                border: 2px dashed #ccc;
                padding: 30px;
                border-radius: 10px;
                text-align: center;
                background-color: #f9f9f9;
                margin-top: 20px;
                transition: all 0.3s ease;
            }
            .upload-box:hover {
                border-color: #0033A0;
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
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
                transition: background-color 0.3s;
            }
            .upload-actions button:hover {
                background-color: #002280;
            }
        </style>
        
        <div class="upload-container">
            <h3 style="font-weight: bold;">Upload Mapping File</h3>
            <div class="upload-box">
                <p>Drag and drop file to upload</p>
                <button>Select File</button>
                <p style="font-size: 12px; color: #666;">XLS, file size no more than 20MB</p>
            </div>
            <div class="upload-actions">
                <button>Download Template</button>
                <button>Upload File</button>
            </div>
        </div>
    """, unsafe_allow_html=True)
