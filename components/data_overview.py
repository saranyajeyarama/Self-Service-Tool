import streamlit as st
import pandas as pd
import os

def render_data_overview():
    st.markdown("""
    <style>
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .overview-header {
            font-size: 24px;
            font-weight: bold;
        }
        .info-legend-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }
        .currency-info {
            font-size: 14px;
            font-weight: bold;
        }
        .legend {
            display: flex;
            gap: 10px;
            font-size: 14px;
        }
        .legend span {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
        }
        .low { background-color: red; }
        .medium { background-color: orange; }
        .high { background-color: green; }
        .dropdown-container {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }
        .styled-table {
            border-collapse: collapse;
            width: 100%;
            border: 1px solid #ddd;
        }
        .styled-table th, .styled-table td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .styled-table th {
            background-color: #0033A0;
            color: white;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header Section
    st.markdown("""
    <div class='header-container'>
        <div class='overview-header'>Data Overview</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Currency and Legend Section
    st.markdown("""
    <div class='info-legend-container'>
        <div class='currency-info'>
            Currency: <strong>AUD</strong> | Data considered for calculation: <strong>2024 P06</strong>
        </div>
        <div class='legend'>
            <span><span class='status-indicator low'></span> LOW</span>
            <span><span class='status-indicator medium'></span> MEDIUM</span>
            <span><span class='status-indicator high'></span> HIGH</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for different views
    tab1, tab2, tab3 = st.tabs(["Global channel", "Local channel", "Retailer"])
    
    with tab1:
        st.markdown("### Global Channel Data")
    
    with tab2:
        st.markdown("### Local Channel Data")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            global_channel = st.selectbox("Global channel", ["All", "Click & Mortar", "Discounters", "Supermarket"])
        with col2:
            local_channel = st.selectbox("Local channel", ["All", "LAR", "Other OOH", "Traditional Convenience"])
        with col3:
            retailer = st.selectbox("Retailer", ["All", "Retailer A", "Retailer B", "Retailer C"])
        
        # Load data safely
        file_path = r"C:\Users\aditya.kumar\mars_proj\Self-Service-Tool\SCM Self Service Scorecard data.xlsx"
        
        if os.path.exists(file_path):
            df = pd.read_excel(file_path, sheet_name="Local Channel")
            
            # Ensure column names are properly formatted
            df.columns = df.columns.str.strip()

            # Apply Filters only if the column exists
            if "Global Channel" in df.columns and global_channel != "All":
                df = df[df["Global Channel"].str.strip() == global_channel]
            if "Local Channel" in df.columns and local_channel != "All":
                df = df[df["Local Channel"].str.strip() == local_channel]
            if "Retailer" in df.columns and retailer != "All":
                df = df[df["Retailer"].str.strip() == retailer]
            
            # Function to apply status colors
            def get_status_color(status):
                if status == "low":
                    return '<span class="status-indicator low"></span>'
                elif status == "medium":
                    return '<span class="status-indicator medium"></span>'
                elif status == "high":
                    return '<span class="status-indicator high"></span>'
                return ''
            
            if "Status" in df.columns:
                df["Status"] = df["Status"].apply(get_status_color)
            
            st.markdown(df.to_html(escape=False, index=False, classes='styled-table'), unsafe_allow_html=True)
        else:
            st.error(f"⚠ Data file not found: {file_path}")
    
    with tab3:
        st.markdown("### Retailer Data")
