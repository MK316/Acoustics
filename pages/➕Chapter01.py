import streamlit as st
import requests  # To fetch file from GitHub

tab1, tab2 = st.tabs(["Lecture slides", "Others"])

with tab1:
    st.write("### Download Lecture Slides")

    # GitHub raw URL of the file (Replace with your actual raw file URL)
    file_url = "https://raw.githubusercontent.com/your_username/your_repo/main/lecture_slides.pdf"

    # Fetch the file from GitHub
    response = requests.get(file_url)
    
    if response.status_code == 200:
        st.download_button(
            label="Download Slides 📂",
            data=response.content,
            file_name="lecture_slides.pdf",
            mime="application/pdf"
        )
    else:
        st.error("Error: Unable to fetch the file from GitHub.")

with tab2:
    st.write("This section can contain other links or information.")
