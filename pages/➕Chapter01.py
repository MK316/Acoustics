import streamlit as st
import base64
import requests

tab1, tab2 = st.tabs(["Lecture slides", "Others"])

with tab1:
    st.write("### Lecture Slides Viewer")

    # GitHub raw URL of the PDF file
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Fetch the PDF content
    response = requests.get(pdf_url)
    
    if response.status_code == 200:
        base64_pdf = base64.b64encode(response.content).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error("Error: Unable to load the PDF.")

with tab2:
    st.write("Other content here.")






