import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import io
import math
import random

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📖 Lecture slides", "🌀 App1: Simple", "🌀App2: Complex", "🌀GCD", "Quiz", "💾 Download"])

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

#################################################

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

    # Initialize complex wave
    complex_wave = np.zeros_like(t)

    # Define a color palette for different waves
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]  # Blue, Orange, Green, Red, Purple

    # Create a figure with subplots for individual waves and final wave
    fig, axes = plt.subplots(num_components + 1, 1, figsize=(6, 2 * (num_components + 1)))

    for i in range(num_components):
        # Generate each sine wave
        sine_wave = amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t)
        complex_wave += sine_wave  # Add to the complex wave
        
        # Plot individual sine wave with different colors
        axes[i].plot(t[:1000], sine_wave[:1000], color=colors[i % len(colors)], linewidth=1.5)
        axes[i].set_title(f"Sine Wave {i+1}: {frequencies[i]} Hz, Amplitude: {amplitudes[i]}", fontsize=10)
        axes[i].set_xlabel("Time (s)", fontsize=9)
        axes[i].set_ylabel("Amplitude", fontsize=9)
        axes[i].tick_params(axis='both', labelsize=8)
        axes[i].grid(True)

    # Normalize the complex wave to prevent clipping
    complex_wave /= np.max(np.abs(complex_wave))

    # Plot the final complex wave
    axes[-1].plot(t[:1000], complex_wave[:1000], color="black", linewidth=1.5)  # Final wave in black
    axes[-1].set_title("Final Complex Waveform (Sum of All Components)", fontsize=10)
    axes[-1].set_xlabel("Time (s)", fontsize=8)
    axes[-1].set_ylabel("Amplitude", fontsize=8)
    axes[-1].tick_params(axis='both', labelsize=8)
    axes[-1].grid(True)

    # Adjust spacing to prevent overlapping
    plt.subplots_adjust(hspace=0.8)

    # Display all plots
    st.pyplot(fig)

    # Save the wave as a temporary audio file
    audio_buffer = io.BytesIO()
    sf.write(audio_buffer, complex_wave, sampling_rate, format='WAV')
    audio_buffer.seek(0)

    # Provide a download button for the generated sound
    st.audio(audio_buffer, format='audio/wav')
    st.download_button(label="Download Complex Wave File", data=audio_buffer, file_name="complex_wave.wav", mime="audio/wav")

#################################################
with tab4:
    st.markdown("### 🧮 Find the Greatest Common Denominator (GCD)")

    # Number of sets and number range
    num_sets = 3
    min_val, max_val = 1, 100

    # Initialize session state for storing numbers
    if "gcd_numbers" not in st.session_state:
        st.session_state.gcd_numbers = [np.random.randint(min_val, max_val + 1, 3).tolist() for _ in range(num_sets)]
        st.session_state.gcd_answers = [None] * num_sets  # Initialize answer storage

    # Display questions and collect user input
    user_answers = []
    for i, numbers in enumerate(st.session_state.gcd_numbers):
        st.write(f"**Set {i+1}:** {numbers[0]}, {numbers[1]}, {numbers[2]}")
        user_input = st.number_input(
            f"Your GCD Answer for Set {i+1}:", 
            min_value=1, max_value=50, key=f"gcd_input_{i}", value=st.session_state.gcd_answers[i] or 1
        )
        user_answers.append(user_input)

    # Button to check answers
    if st.button("Check Answers"):
        results = []
        for i, numbers in enumerate(st.session_state.gcd_numbers):
            correct_gcd = math.gcd(math.gcd(numbers[0], numbers[1]), numbers[2])  # Compute correct GCD
            user_answer = int(user_answers[i])  # Ensure integer comparison

            if user_answer == correct_gcd:
                results.append(f"✅ **Set {i+1}:** Correct! GCD of {numbers} is **{correct_gcd}**.")
            else:
                results.append(f"❌ **Set {i+1}:** Incorrect. The correct GCD of {numbers} is **{correct_gcd}**.")

        # Display results
        for result in results:
            st.write(result)

    # Button to generate new questions
    if st.button("Generate New Questions"):
        st.session_state.gcd_numbers = [np.random.randint(min_val, max_val + 1, 3).tolist() for _ in range(num_sets)]
        st.session_state.gcd_answers = [None] * num_sets  # Reset stored answers
        st.rerun()
#################################################
with tab5:


    # Define glossary of terms and their definitions
    quiz_data = {
        "sound": "A vibration that propagates as an acoustic wave through a medium.",
        "acoustic medium": "A substance (e.g., air, water, or solid) that carries sound waves.",
        "acoustic waveform": "A graphical representation of sound pressure variation over time.",
        "sound wave": "A wave of compression and rarefaction through an acoustic medium.",
        "rarefaction": "The part of a sound wave where particles are spread apart.",
        "compression": "The part of a sound wave where particles are pushed together.",
        "periodic sounds": "Sounds that repeat at regular intervals over time.",
        "simple periodic wave": "A wave that repeats in a sinusoidal pattern.",
        "sine wave": "A smooth, repetitive oscillation representing a simple periodic wave.",
        "frequency": "The number of cycles of a waveform per second, measured in hertz (Hz).",
        "cycle": "One complete repetition of a periodic wave.",
        "period": "The time required to complete one cycle of a wave.",
        "hertz": "The unit of frequency, equal to one cycle per second.",
        "amplitude": "The maximum displacement of a wave from its resting position.",
        "phase": "The position of a point in the wave cycle at a given time.",
        "complex periodic wave": "A waveform composed of multiple sine waves of different frequencies.",
        "fundamental frequency": "The lowest frequency in a complex periodic wave.",
        "component waves": "Individual sine waves that make up a complex periodic wave.",
        "power spectrum": "A graph showing the intensity of different frequency components in a sound.",
        "Fourier’s theorem": "A principle stating that complex waves can be broken into sine waves.",
        "Fourier analysis": "A mathematical method to decompose complex sounds into sine waves.",
        "aperiodic sounds": "Sounds that do not repeat in a regular pattern.",
        "white noise": "A random sound containing all frequencies at equal intensity.",
        "transient": "A brief burst of sound, such as a click or a clap.",
        "impulse": "A very short, sharp sound that contains a broad range of frequencies.",
        "low-pass filter": "A filter that allows low frequencies to pass and attenuates high frequencies.",
        "pass band": "The range of frequencies that a filter allows to pass.",
        "reject band": "The range of frequencies that a filter attenuates.",
        "high-pass filter": "A filter that allows high frequencies to pass and attenuates low frequencies.",
        "filter slope": "The rate at which a filter attenuates frequencies outside the pass band.",
        "band-pass filter": "A filter that allows a specific range of frequencies to pass.",
        "center frequency": "The middle frequency of a band-pass filter.",
        "bandwidth": "The range of frequencies within the pass band of a filter."
    }
    
    # Function to initialize the quiz
    def initialize_quiz():
        """Initialize the quiz with new random questions and answer options."""
        st.session_state.quiz_questions = random.sample(list(quiz_data.items()), 5)  # Select 5 random questions
        st.session_state.quiz_options = {}  # Store answer choices
        st.session_state.quiz_answers = {}  # Store user answers
        
        for i, (correct_term, _) in enumerate(st.session_state.quiz_questions):
            # Generate 3 incorrect options
            wrong_answers = random.sample([term for term in quiz_data.keys() if term != correct_term], 3)
            options = wrong_answers + [correct_term]
            random.shuffle(options)  # Shuffle options
            st.session_state.quiz_options[f"q{i}"] = options  # Store the shuffled options
            st.session_state.quiz_answers[f"q{i}"] = None  # Initialize user answers
    
    # Ensure quiz is initialized
    if "quiz_questions" not in st.session_state:
        initialize_quiz()
    
    st.markdown("### 🎓 Acoustic Terminology Quiz")
    st.write("Select the correct answer for each definition.")
    
    # Display quiz questions
    for i, (correct_term, definition) in enumerate(st.session_state.quiz_questions):
        st.write(f"**Question {i+1}:** {definition}")
    
        # Ensure options exist before accessing
        options = st.session_state.quiz_options.get(f"q{i}", [])
    
        # Display radio button options
        st.session_state.quiz_answers[f"q{i}"] = st.radio(
            f"Select the correct term for Question {i+1}:",
            options,
            key=f"quiz_{i}",
            index=options.index(st.session_state.quiz_answers[f"q{i}"]) if st.session_state.quiz_answers[f"q{i}"] in options else None
        )
    
    # Button to check answers
    if st.button("Check Answers", key="check_answers_button"):
        results = []
        for i, (correct_term, _) in enumerate(st.session_state.quiz_questions):
            user_answer = st.session_state.quiz_answers.get(f"q{i}")
            if user_answer == correct_term:
                results.append(f"✅ **Question {i+1}:** Correct! The term is **{correct_term}**.")
            else:
                results.append(f"❌ **Question {i+1}:** Incorrect. The correct answer is **{correct_term}**.")
    
        for result in results:
            st.write(result)
    
    # Button to generate a new quiz
    if st.button("Generate New Quiz", key="generate_quiz_button"):
        initialize_quiz()
        st.rerun()

#################################################
with tab6:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
