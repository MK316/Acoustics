import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Lecture slides", "🌀 Quantal theory", "🌀 Harmonics", "Resonant freq", "💾 Download"])

# Define the function to plot all harmonics
def plot_harmonics(num_modes=3, num_points=500):
    # Create a figure object with specified size
    plt.figure(figsize=(10, 6))
    x = np.linspace(0, 1, num_points)
    
    # Loop through each mode and plot it
    for mode in range(num_modes):
        y = np.sin(np.pi * (mode + 1) * x)  # Calculate the y-values using the sine function
        plt.subplot(num_modes, 1, mode + 1)  # Create a subplot for each mode
        plt.plot(x, y)  # Plot the current mode
        plt.title(f'Mode {mode + 1}')  # Set the title for each mode
        plt.ylim(-1.5, 1.5)  # Set the y-axis limits
        plt.grid(True)  # Enable the grid

    # Adjust layout to prevent overlapping
    plt.tight_layout()
    # Use Streamlit's function to display the matplotlib plot
    st.pyplot(plt)

with tab1:
    st.write("Other content here.")

#######################################################

with tab2:
    st.markdown("#### 🎓 Quantal Theory of Speech Acoustics")
    st.caption("Understanding Stability and Efficiency in Speech Production")
    
    st.markdown("""
    #### 1. What is Quantal Theory?
    Quantal Theory, proposed by **Kenneth N. Stevens (1972, 1989)**, explains how **speech sounds are produced efficiently and remain stable** despite variability in articulation.
    ##### Articles related
    """)

    st.markdown("- [Clements & Ridouane (2006) Quantal phonetics and distinctive features](https://www.isca-archive.org/exling_2006/clements06_exling.pdf)")
    st.markdown("- [Stevens, K.N. (1972) The quantal nature of speech](https://www.kul.pl/files/30/fonetyka/Stevens_72_Quantal.pdf)")

    # Embed YouTube video using <iframe> 
    st.markdown("""
    ---
    #### 🎥 Pitch Hearing Demonstration
    Watch this video to understand **how small changes in articulation can lead to major acoustic effects**.
    """)

    # Embed YouTube video using a clickable link
    st.markdown("- [YouTube link](https://www.youtube.com/watch?v=QFq9ywKuCYo)")

    video_url = "https://www.youtube.com/embed/PM4WSBZanQQ?si=WCErVnSrSjeLkme2"
    
    st.markdown(
        f"""
        <iframe width="400" height="300" src="{video_url}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    ---
    ##### 🎵 Interactive: Simulating Quantal vs. Non-Quantal Effects
    Try adjusting the **articulatory position** (simulated as tongue height) and observe:
    - **Stable Regions**: Small articulation changes **do not** significantly affect the waveform.
    - **Unstable Regions**: Small articulation changes **cause a major waveform shift**.

    Move the slider and see how quantal effects work!
    """)

    articulation_position = st.slider("Select an Articulatory Position (Simulated Tongue Height)", 
                                      min_value=1, max_value=100, value=50, step=1)

    
    # Default frequency in case articulation_position is out of defined ranges
    frequency = 300  # Safe default value
    
    if 10 <= articulation_position <= 40:
        frequency = 300  # Stable zone (like vowel /i/)
    elif 41 <= articulation_position <= 59:
        frequency = 300 + (articulation_position - 40) * 8  # Non-quantal zone (unstable transition)
    elif 60 <= articulation_position <= 90:
        frequency = 450  # Stable zone (like vowel /a/)

    
    # Generate waveform
    duration = 0.05  # Short duration for display
    sampling_rate = 44100
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * t)
    
    # Plot waveform
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(t[:500], waveform[:500], color="blue", linewidth=2)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Waveform at Articulatory Position {articulation_position} (Frequency: {frequency} Hz)")
    ax.grid(True)
    
    # Display plot
    st.pyplot(fig)
    
    # Explanation of the effect
    if 10 <= articulation_position <= 40 or 60 <= articulation_position <= 90:
        st.success("✅ **You are in a Quantal Zone!** Small changes in articulation do NOT drastically change acoustics.")
    else:
        st.warning("⚠ **You are in a Non-Quantal Zone!** Small articulation changes cause a BIG acoustic shift.")
    
    st.markdown("""
    ---
    ##### 🎯 Key Takeaways
    - **Quantal Zones (Stable Regions)**: Articulatory adjustments do not drastically affect the sound.
    - **Non-Quantal Zones (Unstable Regions)**: Small articulation changes lead to **big** acoustic differences.
    - **This is why languages prefer quantal sounds**, ensuring **clear and stable communication**.

    ---
    **Try adjusting the slider above** and observe the effects in action!
    """)


######################################################
with tab3:
    st.title('Guitar String Harmonics Simulator')
    # mode = st.sidebar.slider('Select Mode', 0, 2, 0, key='harmonic_mode')  # Ensuring slider is associated with this tab
    plot_harmonics()

    st.markdown("---")
    st.markdown("#### Video: String vibration with different notes")
    st.markdown("- [YouTube link](https://www.youtube.com/watch?v=QFq9ywKuCYo)")

    video_url_1 = "https://www.youtube.com/embed/BSIw5SgUirg?si=Lu0byguLK4o8-0ye"
    video_url_2 = "https://www.youtube.com/embed/to_dtcZP1EE?si=jIxg-W6b6Ewl-gvv"
    video_url_3 = "https://www.youtube.com/embed/rkI0Nf6dHjQ?si=7trzlldwi3pSvZOF"
    
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url_1}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("#### Video: Visible Sound vibration")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url_2}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )

    

    st.markdown("#### Video: Sound travel and medium")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url_3}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )

######################################################

with tab4:
    st.title('Resonant Frequency Calculator for a Closed Tube')

    # Input for the length of the tube
    L = st.number_input('Enter the length of the tube (L) in cm:', min_value=0.01, value=1.00, step=0.01)

    # Calculate resonant frequencies
    RF1 = 35000 / (2 * L)
    RF2 = 2 * RF1
    RF3 = 3 * RF1

    # Display the results
    st.write(f"First resonant frequency: {RF1:.2f} Hz")
    st.write(f"Second resonant frequency: {RF2:.2f} Hz")
    st.write(f"Third resonant frequency: {RF3:.2f} Hz")

######################################################
with tab5:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
