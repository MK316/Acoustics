import streamlit as st

# Create tabs for different sections of the course
tabs = st.tabs(["🍐 Course Overview", "🍏 Evaluation"])
                
# Content for the Schedule tab
with tabs[1]:
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
