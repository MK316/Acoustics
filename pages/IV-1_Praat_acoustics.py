import streamlit as st
from PIL import Image
import os
tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["💍Praat Introduction", "praat picture", "💍Getting started", "💍Basic functions", "💍Speech manipulation","💍Automation with scripting"])

# CSS to adjust the alignment of the dropdown to match the buttons
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;  /* Adjust this value to align with the buttons */
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the path to the slides folder
slides_path = "lectureslides"  # Ensure this is correct relative to your app's location
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)

# Initialize session state variables if they do not exist
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0  # Start with the first slide

# Function to load and display the image based on the current index with resizing
def display_image():
    slide_path = os.path.join(slides_path, slide_files[st.session_state.slide_index])
    image = Image.open(slide_path)
    
    # Set your desired width for resizing
    desired_width = 1200  # Adjust this value as needed
    aspect_ratio = image.height / image.width
    new_height = int(desired_width * aspect_ratio)
    resized_image = image.resize((desired_width, new_height))

    st.image(resized_image, caption=f"Slide {st.session_state.slide_index + 1} of {num_slides}")


with tab0:

    # Arrange 'Start', 'Previous', 'Next', and 'Slide Selector' in a single row
    col1, col2, col3, col4 = st.columns([1, 1, 1, 5])
    
    with col1:
        if st.button("⛳", key="start", help="Reset to the first slide"):
            st.session_state.slide_index = 0

    with col2:
        if st.button("◀️", key="previous", help="Go back to the previous slide"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1
            else:
                st.warning("This is the first slide.")

    with col3:
        if st.button("▶️", key="next", help="Go to the next slide"):
            if st.session_state.slide_index < num_slides - 1:
                st.session_state.slide_index += 1
            else:
                st.warning("This is the end of the slides.")

    with col4:
        # Display slide selector dropdown
        selected_slide = st.selectbox("",
                                      options=[f"Slide {i + 1}" for i in range(num_slides)],
                                      index=st.session_state.slide_index)

        # Update slide index if dropdown selection changes
        selected_slide_index = int(selected_slide.split()[-1]) - 1
        if selected_slide_index != st.session_state.slide_index:
            st.session_state.slide_index = selected_slide_index

    # Display the image
    display_image()
    st.markdown("---")
    st.markdown("#### ❄️ Praat software (installation)")
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
    ### 🌀 Research topic example: 
    #### 1. Vowel duration and post-vocalic stop voicing
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



