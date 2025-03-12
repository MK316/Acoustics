import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os
from PIL import Image

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["📖 Lecture slides", "🌀 Quantal theory", "🌀 Harmonics", "🌀 Resonant frequencies", "🌀 Spectral tilt", "🌀 Videolinks", "💾 Download"])

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



def generate_sine_wave(freq, duration, sample_rate, amplitude=1.0):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = amplitude * np.sin(2 * np.pi * freq * t)
    return waveform

def apply_spectral_tilt(waveform, sample_rate, tilt_amount):
    # Apply a simple spectral tilt by multiplying the waveform by a linearly decreasing amplitude envelope
    t = np.linspace(0, 1, int(sample_rate * len(waveform) / sample_rate))
    envelope = np.linspace(1, tilt_amount, len(t))
    return waveform * envelope

# def main():
#     st.title("Audio Spectral Tilt Comparison")

#     with st.sidebar:
#         freq = st.slider("Frequency", 100, 1000, 440)
#         duration = st.slider("Duration", 1, 5, 3)
#         sample_rate = 44100
#         tilt_amount = st.slider("Tilt Amount", 0.1, 1.0, 0.5)

#     # Generate original sine wave
#     waveform = generate_sine_wave(freq, duration, sample_rate)
#     tilted_waveform = apply_spectral_tilt(waveform, sample_rate, tilt_amount)

#     # Save waveforms as temporary files to play in Streamlit
#     sf.write('normal.wav', waveform, sample_rate)
#     sf.write('tilted.wav', tilted_waveform, sample_rate)

#     st.header("Normal Sine Wave")
#     st.audio('normal.wav')

#     st.header("Sine Wave with Spectral Tilt")
#     st.audio('tilted.wav')

#     # Optional: Display waveform plots
#     fig, ax = plt.subplots(2, 1, figsize=(10, 6))
#     ax[0].plot(waveform)
#     ax[0].set_title("Normal Waveform")
#     ax[1].plot(tilted_waveform)
#     ax[1].set_title("Tilted Waveform")
#     st.pyplot(fig)

# if __name__ == "__main__":
#     main()

# CSS to adjust the alignment of the dropdown to match the buttons
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;  /* Adjust this value to align with the buttons */
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the path to the slides folder
slides_path = "pages/AAP02/"  # Ensure this is correct relative to your app's location
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)


# Initialize session state for slide index if not set or out of bounds
if "slide_index" not in st.session_state or st.session_state.slide_index >= num_slides:
    st.session_state.slide_index = 0

# Check if there are slides in the folder
if num_slides == 0:
    st.error("No slides found in the specified folder.")
    st.stop()  # Stop the app if there are no slides


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


with tab1:
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
                st.warning("Final slide")

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
    st.caption("Chapter 2: Slides 1~51")

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
    st.title("Resonance Frequency Calculator")
    st.markdown('#### 1. Closed tube at both ends')

    # Input for the length of the tube - closed at both ends
    L = st.number_input('Enter the length of the tube (L) in cm for closed tube:', min_value=0.01, value=1.00, step=0.01)

    # Calculate resonant frequencies for a tube closed at both ends
    RF1_closed = 35000 / (2 * L)
    RF2_closed = 2 * RF1_closed
    RF3_closed = 3 * RF1_closed

    # Display the results for a tube closed at both ends
    st.write(f"First resonant frequency (F1): {RF1_closed:.2f} Hz")
    st.write(f"Second resonant frequency (F2): {RF2_closed:.2f} Hz")
    st.write(f"Third resonant frequency (F3): {RF3_closed:.2f} Hz")


    st.markdown('#### 2. Tube with one open end')

    # Input for the length of the tube - one open end
    L2 = st.number_input('Enter the length of the tube (L) in cm for open tube:', min_value=0.01, value=1.00, step=1.00)

    # Calculate resonant frequencies for a tube with one open end
    RF1_open = 35000 / (4*L2)  # for n=1
    RF2_open = 3*35000 / (4*L2)  # for n=2
    RF3_open = 5*35000 / (4*L2) # for n=3

    # Display the results for a tube with one open end
    st.write(f"First resonant frequency (F1): {RF1_open:.2f} Hz")
    st.write(f"Second resonant frequency (F2): {RF2_open:.2f} Hz")
    st.write(f"Third resonant frequency (F3): {RF3_open:.2f} Hz")

    st.markdown("#### 3. Ruben's tube demonstration")

    st.caption("Video: Resonant frequencies and standing waves")
    video_url_4 = "https://www.youtube.com/embed/zSQP0D4p8Xo?si=XrBzZ0Qy03pjf-Lf"
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url_4}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )
 ##############
with tab5:
    st.markdown("💦 Article to read: Sluijter & Van Heuven (1996) Spectral tilt as an acoustic correlate of linguistic stress [download](https://www.researchgate.net/publication/14340446_Spectral_tilt_as_an_acoustic_correlate_of_linguistic_stress)")
    st.markdown("---")
    st.markdown("#### 🌀 Spectral Tilt and Sound Quality Analysis (simple demo)")

    freq = st.sidebar.slider("Frequency", 100, 5000, 440, 100, key='freq')
    duration = st.sidebar.slider("Duration", 1, 5, 1, key='duration')
    sample_rate = 44100
    tilt_amount_high = 0.1
    tilt_amount_low = 0.5

    waveform = generate_sine_wave(freq, duration, sample_rate)
    waveform_high_tilt = apply_spectral_tilt(waveform, sample_rate, tilt_amount_high)
    waveform_low_tilt = apply_spectral_tilt(waveform, sample_rate, tilt_amount_low)

    # Save waveforms to temporary files
    sf.write('waveform_original.wav', waveform, sample_rate)
    sf.write('waveform_high_tilt.wav', waveform_high_tilt, sample_rate)
    sf.write('waveform_low_tilt.wav', waveform_low_tilt, sample_rate)


    # Audio playback
    st.markdown("#### Original Wave")
    st.audio('waveform_original.wav')

    st.markdown("#### High Spectral Tilt")
    st.audio('waveform_high_tilt.wav')

    st.markdown("#### Low Spectral Tilt")
    st.audio('waveform_low_tilt.wav')
    st.markdown("---")
    # Optional: Display waveform plots for visual comparison
    fig, ax = plt.subplots(3, 1, figsize=(10, 8))
    ax[0].plot(waveform)
    ax[0].set_title("Original Waveform")
    ax[1].plot(waveform_high_tilt)
    ax[1].set_title("High Tilt Waveform")
    ax[2].plot(waveform_low_tilt)
    ax[2].set_title("Low Tilt Waveform")
    st.pyplot(fig)

######################################################
with tab6:


    video_url0 = "https://www.youtube.com/embed/7cDAYFTXq3E?si=xjLndaN5Nopm3yvF"

    st.markdown("#### 1. Types of sounds: Longitudinal vs. Transverse waves")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url0}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )




    video_url1 = "https://www.youtube.com/embed/N7NQMhIbz3A?si=G_so9F4daJQPRiY2"

    st.markdown("#### 2. Spectrogram generation demo (3D)")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url1}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )



    video_url2 = "https://www.youtube.com/embed/dihQuwrf9yQ?si=33-SxIxrhNXp59AG"

    st.markdown("#### 3. What is resonance?")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url2}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )

with tab7:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
