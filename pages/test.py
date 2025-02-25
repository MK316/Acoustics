import streamlit as st
import requests

st.title("View Python Script from GitHub")

# Define GitHub file URL
github_url = "https://github.com/MK316/Acoustics/raw/main/praat/daga.py"

try:
    response = requests.get(github_url)
    response.raise_for_status()
    script_content = response.text

    st.subheader("Python Script Content")
    st.code(script_content, language="python")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching script: {e}")
