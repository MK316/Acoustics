import streamlit as st
import requests

# Create tabs for different sections of the course
tabs = st.tabs(["🍐 Weekly", "🍏 Assignment details", "🐾 Padlet"])
                
# Content for the Schedule tab
with tabs[0]:
    st.caption("Spring 2025")
    # URL of the raw markdown file on GitHub
    markdown_url = "https://raw.githubusercontent.com/MK316/Acoustics/refs/heads/main/README.md"
    
    try:
        response = requests.get(markdown_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        markdown_content = response.text
        st.markdown(markdown_content, unsafe_allow_html=True)
    except requests.exceptions.HTTPError as err:
        st.error(f"Failed to retrieve Markdown content: {err}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

with tabs[1]:
  st.write("When necessary, assignments will be detailed in this section.")

with tabs[2]:
    st.header("🐾 Files to share: on Padlet")
    st.write("This Padlet serves as a dynamic hub for our Acoustics course. Here, you'll find additional course materials, additional reading resources, and online tools. It's also a space for sharing files and submitting assignments.")
    st.components.v1.iframe("https://padlet.com/mirankim316/acoustics", width=700, height=800)


