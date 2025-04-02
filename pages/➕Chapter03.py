import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os
from PIL import Image
import pandas as pd
from scipy.fft import fft

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["📖 Lecture slides", "🌀 Web Resources", "🌀 Videolinks", "🌀 Apps", "APP2", "APP3", "💾 Download"])



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
    ax.scatter(sampled_t, sampled_waveform, color='red')
    for x, y in zip(sampled_t, sampled_waveform):
        ax.vlines(x, 0, y, color='gray', linestyle=':', linewidth=0.5)
        ax.hlines(y, 0, x, color='gray', linestyle=':', linewidth=0.5)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_title('Complex Waveform with Samples')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.legend()
    ax.grid(False)
    return fig

def calculate_rms(sampled_waveform):
    squares = sampled_waveform ** 2
    mean_squares = np.mean(squares)
    rms = np.sqrt(mean_squares)
    return squares, mean_squares, rms

# Streamlit interface
with tab4:
    st.markdown('#### ❄️ RMS Amplitude Calculator (simulation)')
    
    # User input
    num_samples = st.text_input('Enter number of samples:', '10')  # Text input for number of samples
    num_samples = int(num_samples)  # Convert input to integer
    duration_ms = st.text_input('Enter duration in milliseconds:', '100')  # Text input for duration
    duration_ms = int(duration_ms)  # Convert input to integer

    # Constants
    frequencies = [100, 150, 300]  # Hz
    sample_rate = 10000  # samples per second
    
    # Generate and plot waveform
    t, waveform, sampled_t, sampled_waveform = generate_waveform(frequencies, duration_ms, sample_rate, num_samples)
    fig = plot_waveform(t, waveform, sampled_t, sampled_waveform)
    st.pyplot(fig)
    st.caption("📌 This complex wave has three component waves at 100Hz, 150Hz, 300Hz.")
    # Calculations
    squares, mean_squares, rms = calculate_rms(sampled_waveform)
    data = pd.DataFrame({
        'Sample Time (s)': sampled_t,
        'Sample Amplitude': sampled_waveform,
        'Squares': squares
    })
    
    # Adjust index to start from 1
    data.index = data.index + 1
    
    # Add a row for the sum of squares
    sum_data = pd.DataFrame({'Sample Time (s)': ["Sum"], 'Sample Amplitude': [""], 'Squares': [squares.sum()]})
    data = pd.concat([data, sum_data], ignore_index=False)
    
    # Display results
    st.write('✏️ **Sampled Data and Squares:**', data)
    st.text(f"🔵 Mean of Squares Calculation: Total of Squares / Number of Samples = {squares.sum():.2f} / {len(squares)}")
    st.write(f"🔵 Mean of Squares: {mean_squares:.2f}")
    st.text(f"🔵 RMS Calculation: Square Root of Mean of Squares = sqrt({mean_squares:.2f})")
    st.write(f"🔴 RMS Amplitude: {rms:.2f}")

##########  
with tab5:

    def calculate_interval(sampling_rate, window_size):
        # Calculate the chunk duration in milliseconds
        chunk_duration = (window_size / sampling_rate) * 1000
        
        # Calculate the frequency interval
        freq_interval = sampling_rate / window_size
        
        # Generate frequencies
        frequencies = [i * freq_interval for i in range(int(window_size/2))]  # Only half due to Nyquist
        return chunk_duration, freq_interval, frequencies[:10]  # Display only the first 10 frequencies
    
    def plot_frequencies(frequencies):
        plt.figure(figsize=(10, 4))
        indices = range(len(frequencies))  # Create an index array for the x-values
        plt.stem(indices, frequencies)  # Remove use_line_collection argument
        plt.xlabel('Index')
        plt.ylabel('Frequency (Hz)')
        plt.title('Frequency Components')
        plt.grid(True)
        plt.tight_layout()
        return plt
    
    # Streamlit interface
    st.title('Audio Sampling and Window Size Analysis')
    
    # User inputs
    sampling_rate = st.number_input('Enter the sampling rate (in Hz)', value=22000, min_value=1000)
    window_size = st.number_input('Enter the window size (in samples)', value=1024, min_value=128)
    
    if st.button('Calculate'):
        chunk_duration, freq_interval, frequencies = calculate_interval(sampling_rate, window_size)
        
        # Display results
        st.write(f"Chunk duration: {chunk_duration:.2f} ms")
        st.write(f"Interval between points in the computed spectrum: {freq_interval:.2f} Hz")
        st.write("Frequencies of the first few components:")
        st.write(frequencies)
        
        # Plot frequencies
        fig = plot_frequencies(frequencies)
        st.pyplot(fig)

##########

with st.tab("Signal Analysis"):  # Assuming you're placing this within a specific tab in Streamlit

    # Settings
    sampling_rate = 22000  # Sampling rate in Hz
    window_size = 64       # Window size in samples
    t = np.arange(window_size) / sampling_rate  # Time vector for window
    
    # Generate a signal (sine wave + noise)
    frequency = 1000  # Frequency of the sine wave
    signal = 0.5 * np.sin(2 * np.pi * frequency * t) + 0.5 * np.random.normal(size=window_size)
    
    # Perform FFT
    fft_result = fft(signal)
    frequencies = np.linspace(0, sampling_rate, window_size, endpoint=False)  # Frequency vector
    
    # Plotting
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    
    # Time-domain plot
    axs[0].plot(t * 1000, signal, label='Signal')  # Plot in milliseconds
    axs[0].set_title('Time Domain Signal')
    axs[0].set_xlabel('Time (ms)')
    axs[0].set_ylabel('Amplitude')
    axs[0].grid(True)
    
    # Frequency-domain plot
    magnitude = np.abs(fft_result)[:window_size // 2]  # Magnitude of the FFT
    axs[1].stem(frequencies[:window_size // 2], magnitude, 'b', markerfmt=" ", basefmt="-b")
    axs[1].set_title('Frequency Domain Spectrum')
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Magnitude')
    axs[1].grid(True)
    
    plt.tight_layout()
    
    # Display the plot in Streamlit
    st.pyplot(fig)


##########
with tab7:
    st.write("### ✏Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)

