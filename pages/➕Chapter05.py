import streamlit as st
import numpy as np
import soundfile as sf
from io import BytesIO


tab1, tab2, tab3 = st.tabs(["📖 Lecture slides", "🌀 Apps", "💾 Download"])

# ✅ Function to generate a stereo pure tone with a delay
def generate_stereo_tone(frequency1, frequency2, duration, delay_ms, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generate the two pure tones
    tone1 = 0.5 * np.sin(2 * np.pi * frequency1 * t)  # First frequency (Left Channel)
    tone2 = 0.5 * np.sin(2 * np.pi * frequency2 * t)  # Second frequency (Right Channel)

    # Convert delay from milliseconds to samples
    delay_samples = int((delay_ms / 1000) * sample_rate)

    # Apply the delay by shifting the second tone
    if delay_samples > 0:
        tone2 = np.concatenate((np.zeros(delay_samples), tone2[:-delay_samples]))

    # Create a stereo waveform: Left (tone1), Right (tone2 with delay)
    stereo_waveform = np.vstack((tone1, tone2)).T  # Stack as [Left, Right]

    # Save the waveform to a BytesIO buffer
    audio_buffer = BytesIO()
    sf.write(audio_buffer, stereo_waveform, sample_rate, format="WAV")
    audio_buffer.seek(0)

    return audio_buffer


with tab1:
    st.write("To be updated in time.")

with tab2:
    # User input for frequencies and delay
    col1, col2 = st.columns(2)
    with col1:
        frequency1 = st.number_input("Enter Frequency 1 (Hz)", min_value=20, max_value=20000, value=500)
        duration = st.number_input("Duration (seconds)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    
    with col2:
        frequency2 = st.number_input("Enter Frequency 2 (Hz)", min_value=20, max_value=20000, value=1500)
        delay_ms = st.number_input("Delay Time (ms)", min_value=0, max_value=500, value=20)
    
    # Generate the audio when the button is clicked
    if st.button("🎧 Generate and Play Sound"):
        audio_file = generate_stereo_tone(frequency1, frequency2, duration, delay_ms)
        st.audio(audio_file, format="audio/wav")
        
with tab3:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
