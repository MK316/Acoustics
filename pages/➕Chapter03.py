import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["📖 Lecture slides", "Videolinks", "🌀 Apps", "💾 Download"])

##########
with tab1:
    st.write("Other content here.")

##########
with tab2:
    st.caption("Video contents")

    video_url1 = "https://www.youtube.com/embed/hiflzRL7sUY?si=yI6gbYVtT99gEowg"

    st.markdown("#### 1. Spectrogram generation demo (3D)")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url1}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )
##########
with tab3:
    st.caption("Apps to help the content")
##########    
with tab4:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
