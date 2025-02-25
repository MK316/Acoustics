import streamlit as st
import numpy as np
import soundfile as sf
from io import BytesIO
import matplotlib.pyplot as plt


tab1, tab2, tab3 = st.tabs(["📖 Lecture slides", "🌀 Apps", "💾 Download"])

# ✅ Function to generate a single pure tone
def generate_pure_tone(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = 0.5 * np.sin(2 * np.pi * frequency * t)  # Sine wave with amplitude scaling
    audio_buffer = BytesIO()
    sf.write(audio_buffer, waveform, sample_rate, format="WAV")
    audio_buffer.seek(0)
    return audio_buffer, t, waveform  # Return waveform for plotting

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

    return audio_buffer, t, tone1, tone2  # Return waveforms for plotting

######################


with tab1:
    st.write("To be updated in time.")

with tab2:
    st.markdown("### 1. Two pure tone playing asynchronously (Pisoni's experiment)")
    
    # User input for frequencies and delay
    col1, col2 = st.columns(2)
    with col1:
        frequency1 = st.number_input("Enter Frequency 1 (Hz)", min_value=20, max_value=20000, value=500)
        duration = st.number_input("Duration (seconds)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    
    with col2:
        frequency2 = st.number_input("Enter Frequency 2 (Hz)", min_value=20, max_value=20000, value=1500)
        delay_ms = st.number_input("Delay Time (ms)", min_value=0, max_value=500, value=20)
    
    # Generate audio previews when the button is clicked
    if st.button("🎧 Generate Audio"):
        # Generate individual pure tones
        audio_file1, t1, waveform1 = generate_pure_tone(frequency1, duration)
        audio_file2, t2, waveform2 = generate_pure_tone(frequency2, duration)
    
        # Generate combined stereo sound
        stereo_audio_file, t_combined, stereo_wave1, stereo_wave2 = generate_stereo_tone(frequency1, frequency2, duration, delay_ms)
    
        # Display and play individual pure tones
        st.subheader("🔊 Tone 1 (Left Channel)")
        st.audio(audio_file1, format="audio/wav")
    
        # Plot waveform of Tone 1
        fig, ax = plt.subplots()
        ax.plot(t1[:1000], waveform1[:1000], color="blue")  # Show first 1000 samples for clarity
        ax.set_title(f"Waveform of {frequency1} Hz (Left)")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)
        st.pyplot(fig)
    
        st.subheader("🔊 Tone 2 (Right Channel)")
        st.audio(audio_file2, format="audio/wav")
    
        # Plot waveform of Tone 2
        fig, ax = plt.subplots()
        ax.plot(t2[:1000], waveform2[:1000], color="red")  # Show first 1000 samples for clarity
        ax.set_title(f"Waveform of {frequency2} Hz (Right)")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)
        st.pyplot(fig)
    
        # Display and play combined stereo tone
        st.subheader("🎶 Combined Stereo Audio with Delay")
        st.audio(stereo_audio_file, format="audio/wav")
    
        # Plot waveform of combined stereo tones
        fig, ax = plt.subplots()
        ax.plot(t_combined[:1000], stereo_wave1[:1000], label=f"{frequency1} Hz (Left)", color="blue")
        ax.plot(t_combined[:1000], stereo_wave2[:1000], label=f"{frequency2} Hz (Right, Delayed)", color="red")
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
