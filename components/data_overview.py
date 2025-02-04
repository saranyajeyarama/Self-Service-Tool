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
    
    file_path = r"C:\\Users\\aditya.kumar\\mars_proj\\Self-Service-Tool\\SCM Self Service Scorecard data.xlsx"
    
    with tab1:
        st.markdown("### Global Channel Data")
        
        col1 = st.columns(1)
        with col1[0]:
            global_channel = st.selectbox("Global channel", ["All", "Click & Mortar", "Discounters", "Supermarket", "Multiple Convenience", "Other OOH", "LAR", "Traditional Independent", "Drugstore / Pharmacy", "Other Specialist", "ODD", "Pure-Play", "Unattended Retail"])
        
        if os.path.exists(file_path):
            df_global = pd.read_excel(file_path, sheet_name="Global Channel")
            df_global.columns = df_global.columns.str.strip()
            
            if "Global Channel" in df_global.columns and global_channel != "All":
                df_global = df_global[df_global["Global Channel"].str.strip() == global_channel]
            
            st.dataframe(df_global)
        else:
            st.error(f"⚠ Data file not found: {file_path}")
    
    with tab2:
        st.markdown("### Local Channel Data")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            global_channel = st.selectbox("Global channel", ["All", "Click & Mortar", "Discounters", "Supermarket"])
        with col2:
            local_channel = st.selectbox("Local channel", ["All", "LAR", "Other OOH", "Traditional Convenience", "Wholesale", "Mass", "Vending", "Corporate P&C", "LARS", "Grocery", "Pureplay", "Pharmacy", "Cinema", "Unstructured P&C", "Click&Mortar", "Discounters", "ODD", "Food Service"])
        with col3:
            retailer = st.selectbox("Retailer", ["All", "Retailer A", "Retailer B", "Retailer C"])
        
        if os.path.exists(file_path):
            df = pd.read_excel(file_path, sheet_name="Local Channel")
            df.columns = df.columns.str.strip()

            if "Global Channel" in df.columns and global_channel != "All":
                df = df[df["Global Channel"].str.strip() == global_channel]
            if "Local Channel" in df.columns and local_channel != "All":
                df = df[df["Local Channel"].str.strip() == local_channel]
            if "Retailer" in df.columns and retailer != "All":
                df = df[df["Retailer"].str.strip() == retailer]
            
            st.dataframe(df)
        else:
            st.error(f"⚠ Data file not found: {file_path}")
    
    with tab3:
        st.markdown("### Retailer Data")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            retailer_filter = st.selectbox("Retailer", ["All", "BIG W", "MC DONALDS", "WOOLWORTHS ONLINE", "COSTCO", "WOOLWORTHS SUPERMARKET", "INDEPENDENT GROCERY", "CINEMA", "TOTAL CONVENIENCE EX 7-ELEVEN", "TOTAL ODD", "UNSTRUCTURED CONVENIENCE"])
        with col2:
            local_channel_filter = st.selectbox("Local Channel", ["All", "Mass", "Food Service", "Click&Mortar", "LARS", "Grocery", "Cinema", "Corporate P&C", "ODD", "Unstructured P&C"])
        with col3:
            global_channel_filter = st.selectbox("Global Channel", ["All", "Other Specialist", "Other OOH", "Click & Mortar", "LAR", "Supermarket", "Traditional Convenience"])
        
        if os.path.exists(file_path):
            df_retailer = pd.read_excel(file_path, sheet_name="Retailer")
            df_retailer.columns = df_retailer.columns.str.strip()
            
            if "Retailer" in df_retailer.columns and retailer_filter != "All":
                df_retailer = df_retailer[df_retailer["Retailer"].str.strip() == retailer_filter]
            if "Local Channel" in df_retailer.columns and local_channel_filter != "All":
                df_retailer = df_retailer[df_retailer["Local Channel"].str.strip() == local_channel_filter]
            if "Global Channel" in df_retailer.columns and global_channel_filter != "All":
                df_retailer = df_retailer[df_retailer["Global Channel"].str.strip() == global_channel_filter]
            
            st.dataframe(df_retailer)
        else:
            st.error(f"⚠ Data file not found: {file_path}")
