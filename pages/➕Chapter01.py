import streamlit as st

tab1, tab2 = st.tabs(["Lecture slides", "Others"])

with tab1:
    st.write("### Lecture Slides Viewer")

    # GitHub raw URL of the file
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Embed PDF in an iframe
    st.components.v1.iframe(pdf_url, width=700, height=600)

with tab2:
    st.write("This section can contain other links or information.")
