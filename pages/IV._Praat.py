import streamlit as st

tab1, tab2 = st.tabs(["Praat software", "manual"])

with tab1:
  st.image("https://github.com/MK316/Acoustics/raw/main/images/praat-icon.jpg", caption="Doing Phonetics by Computer")
  st.markdown("---")
  st.markdown("""
  - [Software to download]()
  - How to install: Just double click the icon appearing after downloading file.
  """)

with tab2:
