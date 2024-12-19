import streamlit as st
from nbconvert import HTMLExporter
import nbformat
import pickle
import pandas as pd

# Custom CSS for pink, red, and yellow theme
st.markdown("""
    <style>
        /* Background color for the app */
        body {
            background-color: #FFFDE7; /* Light yellow */
        }
        /* Sidebar background color */
        .sidebar .sidebar-content {
            background-color: #FCE4EC; /* Light pink */
        }
        /* Headers and Titles */
        h1, h2, h3, h4, h5, h6 {
            color: #D50000; /* Bright red */
        }
        /* Buttons */
        .stButton button {
            background-color: #F8BBD0; /* Soft pink */
            color: #D50000; /* Bright red */
        }
        /* Input fields */
        .stTextInput, .stNumberInput, .stSelectbox {
            background-color: #FFEBEE; /* Very light red */
            border: 1px solid #D50000; /* Bright red border */
        }
        /* Markdown text color */
        .stMarkdown p {
            color: #C51162; /* Pinkish red */
        }
        /* DataFrame table borders */
        .stDataFrame {
            border: 2px solid #FFEB3B; /* Yellow border */
        }
        /* Subheader text */
        .stSubheader {
            color: #FF6F00; /* Orange */
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Data Overview", "EDA", "Model"])

# EDA Page
if page == "EDA":
    st.title("Exploratory Data Analysis")

    st.markdown("1. PM2.5")
    st.image('pm2.5.png')
    
    st.markdown("2. PM10")
    st.image('PM10.png')

    st.markdown("3. DEWP")
    st.image('dewp.png')

    st.markdown("4. station")
    st.image('station.png')

    st.markdown("5. TEMP")
    st.image('temp.png')

