import streamlit as st

tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["💍Praat Introduction", "praat picture", "💍Getting started", "💍Basic functions", "💍Speech manipulation","💍Automation with scripting"])

with tab0:
    st.image("https://github.com/MK316/Acoustics/raw/main/images/praat01.jpg", 
             caption="Doing Phonetics by Computer; icon, Praat objects window, Praat picture window")
    
    st.markdown("---")
    
    st.markdown("""
    - Praat is a free software for speech analysis and phonetic research, widely used in linguistics and language education. It offers spectrograms, pitch tracking, formant analysis, and speech synthesis, with scripting support for automation.
    - [Software to download](https://www.fon.hum.uva.nl/praat/)
    - **How to install:** Just double-click the icon appearing after downloading the file.
    
    ### 📒 Praat Windows Overview
    - **Double click the icon to start**
    - **Praat Objects Window:** This is the main control panel where you load, create, and manipulate audio files. It lists all active objects (e.g., sounds, TextGrids) and allows access to analysis and modification functions.
    - **Praat Picture Window:** This window is used for generating high-quality visualizations of spectrograms, pitch contours, and other speech data. It provides tools for customizing and exporting figures for presentations or research papers.
    """)


with tab1:
    st.markdown('''
    ### Vowel duration and post-vocalic stop voicing
    - Test sentence: "I said, **made** and **mate**." "I said, **mate** and **made**."
    ''')     
    st.markdown("#### Screen capture")
    st.image("https://github.com/MK316/Acoustics/raw/main/praat/Isaidmateandmade-capture.png", caption="I said made and mate. I said mate and made.")
    st.markdown("#### Praat picture")
    st.image("https://github.com/MK316/Acoustics/raw/main/praat/Isaidmateandmade.png", caption="I said made and mate. I said mate and made.")
with tab2:
    st.caption("TBA")
    
with tab3:
    st.caption("TBA")


with tab4:
    st.caption("TBA")

with tab5:
    st.caption("TBA")



