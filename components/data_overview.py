import streamlit as st
import pandas as pd

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
        
        # Sample DataFrame for Table Representation
        data = {
            "Global Channel": ["Click & Mortar", "Discounters", "Drugstore / Pharmacy", "LAR", "Supermarket"],
            "Local Channel": ["LAR", "Other OOH", "Traditional Convenience", "LAR", "Supermarket"],
            "Retailer": ["Retailer A", "Retailer B", "Retailer C", "Retailer A", "Retailer B"],
            "GSV MAT (Mn AUD)": [29.9, 29.9, 29.9, 29.9, 29.9],
            "GSV TY vs LY %": [15.3, 15.3, 15.3, 15.3, 15.3],
            "NSV MAT (Mn AUD)": [19.6, 19.6, 19.6, 19.6, 19.6],
            "NSV TY vs LY %": [17.6, 17.6, 17.6, 17.6, 17.6],
            "MAC % MAT": [42.4, 42.4, 42.4, 42.4, 42.4],
            "MAC % TY vs LY %": [-0.0, -0.0, 0.0, 0.01, -0.1],
            "Contribution % MAT": [22.6, 36.2, 22.6, 22.6, 22.6],
            "Contribution % TY vs LY %": [-3.7, 0.0, 0.0, 0.0, 0.0],
            "Status": ["low", "medium", "medium", "high", "low"]
        }
        
        df = pd.DataFrame(data)
        
        # Apply Filters
        if global_channel != "All":
            df = df[df["Global Channel"] == global_channel]
        if local_channel != "All":
            df = df[df["Local Channel"] == local_channel]
        if retailer != "All":
            df = df[df["Retailer"] == retailer]
        
        def get_status_color(status):
            if status == "low":
                return '<span class="status-indicator low"></span>'
            elif status == "medium":
                return '<span class="status-indicator medium"></span>'
            elif status == "high":
                return '<span class="status-indicator high"></span>'
            return ''
        
        df["Status"] = df["Status"].apply(get_status_color)
        
        st.markdown(df.to_html(escape=False, index=False, classes='styled-table'), unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### Retailer Data")
