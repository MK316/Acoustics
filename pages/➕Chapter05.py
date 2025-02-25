import streamlit as st
import numpy as np
import soundfile as sf
from io import BytesIO
import matplotlib.pyplot as plt


tab1, tab2, tab3 = st.tabs(["📖 Lecture slides", "🌀 Apps", "💾 Download"])

# ✅ Function to generate a pure tone
def generate_pure_tone(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = 0.5 * np.sin(2 * np.pi * frequency * t)  # Sine wave
    return t, waveform

# ✅ Function to generate a stereo pure tone with delay
def generate_stereo_tone(frequency1, frequency2, duration, delay_ms, sample_rate=44100):
    t, tone1 = generate_pure_tone(frequency1, duration, sample_rate)
    _, tone2 = generate_pure_tone(frequency2, duration, sample_rate)

    # Convert delay from milliseconds to samples
    delay_samples = int((delay_ms / 1000) * sample_rate)

    # Apply delay by shifting tone2
    if delay_samples > 0:
        delayed_tone2 = np.concatenate((np.zeros(delay_samples), tone2[:-delay_samples]))
    else:
        delayed_tone2 = tone2

    # Combine stereo: Left = tone1, Right = delayed_tone2
    stereo_waveform = np.vstack((tone1, delayed_tone2)).T

    # Save stereo audio to buffer
    audio_buffer = BytesIO()
    sf.write(audio_buffer, stereo_waveform, sample_rate, format="WAV")
    audio_buffer.seek(0)

    return audio_buffer, t, tone1, delayed_tone2  # Return both waveforms


######################


with tab1:
    st.write("To be updated in time.")

with tab2:
    st.markdown("### 1. Two pure tone playing asynchronously (Pisoni's experiment)")
    
    # User input
    col1, col2 = st.columns(2)
    with col1:
        frequency1 = st.number_input("Enter Frequency 1 (Hz)", min_value=20, max_value=20000, value=500)
        duration = st.number_input("Duration (seconds)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    
    with col2:
        frequency2 = st.number_input("Enter Frequency 2 (Hz)", min_value=20, max_value=20000, value=1500)
        delay_ms = st.number_input("Delay Time (ms)", min_value=0, max_value=500, value=20)
    
    # Generate audio and waveform when clicked
    if st.button("🎧 Generate Audio"):
        # Generate stereo sound
        stereo_audio_file, t_combined, stereo_wave1, stereo_wave2 = generate_stereo_tone(frequency1, frequency2, duration, delay_ms)
    
        # Display combined audio
        st.subheader("🎶 Combined Stereo Audio with Delay")
        st.audio(stereo_audio_file, format="audio/wav")
    
        # ✅ Plot overlay of waveforms (first 50ms for better visualization)
        time_limit = 0.05  # Show first 50ms
        sample_limit = int(time_limit * 44100)
    
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(t_combined[:sample_limit], stereo_wave1[:sample_limit], label=f"{frequency1} Hz (Left)", color="blue")
        ax.plot(t_combined[:sample_limit], stereo_wave2[:sample_limit], label=f"{frequency2} Hz (Right, Delayed)", color="red")
    
        ax.set_title(f"Waveforms of {frequency1} Hz (Left) and {frequency2} Hz (Right) with {delay_ms} ms Delay")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)


with tab3:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
