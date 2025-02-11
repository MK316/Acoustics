import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

tab1, tab2, tab3 = st.tabs(["📖 Lecture slides", "🌀 Apps", "💾 Download"])


with tab1:
    st.write("Other content here.")

with tab2:
    st.markdown("### 🎵 Generate a Simple Periodic Wave")

    # User input for frequency and amplitude
    frequency = st.number_input("Enter Frequency (Hz)", min_value=1, max_value=5000, value=440, step=1)
    amplitude = st.slider("Set Amplitude", min_value=0.1, max_value=1.0, value=0.5, step=0.05)
    duration = 1.0  # Fixed duration of 1 second
    sampling_rate = 44100  # Standard audio sampling rate

    # Generate time and wave signal
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)

    # Plot the waveform
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(t[:1000], wave[:1000])  # Show only first 1000 points for clarity
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Waveform (Frequency: {frequency} Hz, Amplitude: {amplitude})")
    ax.grid(True)
    
    # Display the waveform
    st.pyplot(fig)

    # Generate and play the sound
    import soundfile as sf
    import io

    # Save the wave as a temporary audio file
    audio_buffer = io.BytesIO()
    sf.write(audio_buffer, wave, sampling_rate, format='WAV')
    audio_buffer.seek(0)

    # Provide a download button for the generated sound
    st.audio(audio_buffer, format='audio/wav')
    st.download_button(label="Download Wave File", data=audio_buffer, file_name="generated_wave.wav", mime="audio/wav")
    
with tab3:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)









