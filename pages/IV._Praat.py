import streamlit as st

tab0, tab1, tab2, tab3, tab4 = st.tabs(["Praat Introduction", "Getting started", "Basic functions", "Speech manipulation","Automation with scripting"])

with tab0:
    st.image("https://github.com/MK316/Acoustics/raw/main/images/praat-icon.jpg", caption="Doing Phonetics by Computer")
    st.markdown("---")
    st.markdown("""
    - Praat is a free software for speech analysis and phonetic research, widely used in linguistics and language education. It offers spectrograms, pitch tracking, formant analysis, and speech synthesis, with scripting support for automation.
    - [Software to download](https://www.fon.hum.uva.nl/praat/)
    - How to install: Just double click the icon appearing after downloading file.
    """)

with tab1:
    st.caption("TBA")

with tab2:
    st.caption("TBA")
    
with tab3:
    st.caption("TBA")


with tab4:
    st.caption("TBA")





