import streamlit as st
import streamlit.components.v1 as components
import os

# Page config
st.set_page_config(page_title="Nanda Santosh Portfolio", layout="wide")

# Read HTML from the index.html file in current directory
html_path = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=1000, scrolling=True)
else:
    st.error("⚠️ index.html not found. Please ensure it's in the same folder as app.py.")
