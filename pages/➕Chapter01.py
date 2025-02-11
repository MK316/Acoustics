import streamlit as st

tab1, tab2, tab3 = st.tabs(["📖 Lecture slides", "🌀 Apps", "💾 Download"])


with tab1:
    st.write("Other content here.")

with tab2:
    st.caption("Apps to help the content")
    
with tab3:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)









