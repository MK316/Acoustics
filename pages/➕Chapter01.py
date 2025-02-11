import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import io

tab1, tab2, tab3, tab4 = st.tabs(["📖 Lecture slides", "🌀 App1: Simple", "App2: Complex","💾 Download"])

with tab1:
    st.write("Other content here.")

with tab2:
    st.markdown("### 🎵 1. Generate a Simple Periodic Wave")

    # User input for frequency, amplitude, and phase shift
    frequency = st.number_input("Enter Frequency (Hz)", min_value=1, max_value=5000, value=440, step=1)
    amplitude = st.slider("Set Amplitude", min_value=0.1, max_value=1.0, value=0.5, step=0.05)
    phase_shift = st.slider("Phase Shift (degrees)", min_value=0, max_value=360, value=0, step=10)
    
    duration = 1.0  # Fixed duration of 1 second
    sampling_rate = 44100  # Standard audio sampling rate

    # Generate time values
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Convert phase shift from degrees to radians
    phase_rad = np.deg2rad(phase_shift)
    
    # Generate sine wave with phase shift
    wave = amplitude * np.sin(2 * np.pi * frequency * t + phase_rad)

    # Plot the waveform
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(t[:1000], wave[:1000])  # Show only first 1000 points for clarity
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Waveform (Freq: {frequency} Hz, Amp: {amplitude}, Phase: {phase_shift}°)")
    ax.grid(True)
    
    # Display the waveform
    st.pyplot(fig)

    # Save the wave as a temporary audio file
    audio_buffer = io.BytesIO()
    sf.write(audio_buffer, wave, sampling_rate, format='WAV')
    audio_buffer.seek(0)

    # Provide a download button for the generated sound
    st.audio(audio_buffer, format='audio/wav')
    st.download_button(label="Download Wave File", data=audio_buffer, file_name="generated_wave.wav", mime="audio/wav")
    st.markdown("---")
    # ---------- Phase Shift Comparison App ----------
    st.markdown("### 🔄 2. Phase Shift Visualization")
    st.write("This section compares how the waveform changes with different phase shifts.")

    # Generate three example waves with different phase shifts (0°, 90°, 180°)
    phase_shifts = [0, 90, 180]
    fig, ax = plt.subplots(figsize=(6, 3))

    for phase in phase_shifts:
        phase_rad = np.deg2rad(phase)
        shifted_wave = amplitude * np.sin(2 * np.pi * frequency * t + phase_rad)
        ax.plot(t[:1000], shifted_wave[:1000], label=f"{phase}°")

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Comparison of Phase-Shifted Waves")
    ax.legend()
    ax.grid(True)

    # Display phase shift comparison plot
    st.pyplot(fig)

with tab3:
    st.markdown("### 🎶 Create a Complex Wave")

    # User selects number of sine wave components
    num_components = st.number_input("Number of sine waves to combine", min_value=1, max_value=5, value=2)

    frequencies = []
    amplitudes = []

    # User inputs for multiple frequencies and amplitudes
    for i in range(num_components):
        col1, col2 = st.columns(2)
        with col1:
            freq = st.number_input(f"Frequency {i+1} (Hz)", min_value=1, max_value=5000, value=440 if i == 0 else 880, step=1)
            frequencies.append(freq)
        with col2:
            amp = st.slider(f"Amplitude {i+1}", min_value=0.1, max_value=1.0, value=0.5, step=0.05)
            amplitudes.append(amp)

    duration = 1.0  # Fixed duration of 1 second
    sampling_rate = 44100  # Standard audio sampling rate

    # Generate time values
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    # Generate complex wave by summing multiple sine waves
    complex_wave = np.zeros_like(t)
    for i in range(num_components):
        complex_wave += amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t)

    # Normalize the wave to avoid clipping
    complex_wave /= np.max(np.abs(complex_wave))

    # Plot the waveform
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(t[:1000], complex_wave[:1000])  # Show only first 1000 points for clarity
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Complex Waveform")
    ax.grid(True)

    # Display the waveform
    st.pyplot(fig)

    # Save the wave as a temporary audio file
    audio_buffer = io.BytesIO()
    sf.write(audio_buffer, complex_wave, sampling_rate, format='WAV')
    audio_buffer.seek(0)

    # Provide a download button for the generated sound
    st.audio(audio_buffer, format='audio/wav')
    st.download_button(label="Download Complex Wave File", data=audio_buffer, file_name="complex_wave.wav", mime="audio/wav")


with tab4:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
