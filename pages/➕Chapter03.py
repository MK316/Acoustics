import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os
from PIL import Image
import pandas as pd

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Lecture slides", "🌀 Web Resources", "🌀 Videolinks", "🌀 Apps", "💾 Download"])



# CSS to adjust the alignment of the dropdown to match the buttons
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;  /* Adjust this value to align with the buttons */
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the path to the slides folder
slides_path = "pages/AAP03/"  # Ensure this is correct relative to your app's location
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
    st.caption("Chapter 2: Slides 1~64")

#######################################################

##########
with tab2:
    st.write("1. Digital Signal Processing")
    web_url = "https://www.techtarget.com/whatis/definition/digital-signal-processing-DSP"
    st.markdown(f"📎 [Click here to visit DSP intro]({web_url})", unsafe_allow_html=True)
    
##########
with tab3:
    st.caption("Video contents")

    video_url2 = "https://www.youtube.com/embed/hiflzRL7sUY?si=yI6gbYVtT99gEowg"
    video_url1 = "https://www.youtube.com/embed/-7PYX0ohST4?si=x_D5KnAd83NwSe1q"

    st.markdown("#### 1. How Does LP record music?")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url1}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )
    
    
    st.markdown("#### 2. Spectrogram generation demo (3D)")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url2}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )


##########
# Sentence Split & Audio tab


def generate_waveform(frequencies, duration_ms, sample_rate, num_samples):
    t = np.linspace(0, duration_ms / 1000, int(sample_rate * (duration_ms / 1000)), endpoint=False)
    waveform = np.sum([np.sin(2 * np.pi * f * t) for f in frequencies], axis=0)
    sample_indices = np.linspace(0, len(t) - 1, num_samples, dtype=int)
    sampled_t = t[sample_indices]
    sampled_waveform = waveform[sample_indices]
    return t, waveform, sampled_t, sampled_waveform

def plot_waveform(t, waveform, sampled_t, sampled_waveform):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, waveform, label='Waveform')
    ax.scatter(sampled_t, sampled_waveform, color='red')  # sample points
    
    # 각 샘플 점에서 x축과 y축에 도달할 때까지 선을 그림
    for x, y in zip(sampled_t, sampled_waveform):
        ax.vlines(x, 0, y, color='gray', linestyle=':', linewidth=0.5)  # 세로선은 x축에서 샘플 y값까지만
        ax.hlines(y, 0, x, color='gray', linestyle=':', linewidth=0.5)  # 가로선은 y축에서 샘플 x값까지만
    
    ax.set_title('Complex Waveform with Samples')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.grid(True, which='both', linestyle='-', linewidth=0.5, color='lightgray')  # 전체 그리드 강조
    ax.legend()
    return fig



def calculate_rms(sampled_waveform):
    squares = sampled_waveform ** 2
    mean_squares = np.mean(squares)
    rms = np.sqrt(mean_squares)
    return squares, mean_squares, rms

# Streamlit interface
with tab4:
    st.markdown('### RMS Amplitude Calculator')
    
    # User input
    num_samples = st.selectbox('Select number of samples:', (5, 10, 20))
    
    # Constants
    frequencies = [100, 150, 300]  # Hz
    duration_ms = 50  # milliseconds
    sample_rate = 10000  # samples per second
    
    # Generate and plot waveform
    t, waveform, sampled_t, sampled_waveform = generate_waveform(frequencies, duration_ms, sample_rate, num_samples)
    fig = plot_waveform(t, waveform, sampled_t, sampled_waveform)
    st.pyplot(fig)  # Use st.pyplot to display the matplotlib figure
    
    # Calculations
    squares, mean_squares, rms = calculate_rms(sampled_waveform)
    data = pd.DataFrame({
        'Sample Time (s)': sampled_t,
        'Sample Amplitude': sampled_waveform,
        'Squares': squares
    })
    
    # Display results
    st.write('Sampled Data and Squares:', data)
    st.write(f'Mean of Squares: {mean_squares:.2f}')
    st.write(f'RMS Amplitude: {rms:.2f}')

##########    
with tab5:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)

