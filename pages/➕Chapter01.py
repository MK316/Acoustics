import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import io
import math
import random
import os
from PIL import Image

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["📖 Lecture slides", "🌀 App1: Simple", "🌀App2: Complex", "🌀GCD", "💦 Quiz", "🌀 Videos", "💾 Download"])

# CSS to adjust the alignment of the dropdown to match the buttons
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;  /* Adjust this value to align with the buttons */
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the path to the slides folder
slides_path = "pages/AAP01/"  # Ensure this is correct relative to your app's location
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)

# Initialize session state variables if they do not exist

# Initialize session state variables if they do not exist
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0  # Start with the first slide

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
    st.caption("Introduction: Slides 1~8")
    st.caption("Chapter 01: Slides 9~52")
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
    
    # Initialize session state variables safely
    if "quiz_count" not in st.session_state:
        st.session_state.quiz_count = 1  # Start at quiz 1
    
    if "remaining_terms" not in st.session_state:
        st.session_state.remaining_terms = list(quiz_data.items())  # Store all terms initially
    
    # Function to initialize the quiz
    def initialize_quiz():
        """Selects new questions from remaining words until all are asked."""
        num_questions = min(5, len(st.session_state.remaining_terms))  # Take up to 5 remaining questions
        st.session_state.quiz_questions = random.sample(st.session_state.remaining_terms, num_questions)
    
        # Remove selected terms from remaining pool
        st.session_state.remaining_terms = [item for item in st.session_state.remaining_terms if item not in st.session_state.quiz_questions]
    
        # Store answer choices and reset user answers
        st.session_state.quiz_options = {}
        st.session_state.quiz_answers = {}
    
        for i, (correct_term, _) in enumerate(st.session_state.quiz_questions):
            wrong_answers = random.sample([term for term in quiz_data.keys() if term != correct_term], 3)
            options = wrong_answers + [correct_term]
            random.shuffle(options)
            st.session_state.quiz_options[f"q{i}"] = options
            st.session_state.quiz_answers[f"q{i}"] = None
    
    # Ensure quiz is initialized
    if "quiz_questions" not in st.session_state:
        initialize_quiz()
    
    st.markdown(f"### 🎓 Lesson 1: Terminology Quiz (Set {st.session_state.quiz_count})")
    st.write(f"📌 **Remaining Questions: {len(st.session_state.remaining_terms)}**")
    
    # Display quiz questions
    for i, (correct_term, definition) in enumerate(st.session_state.quiz_questions):
        st.write(f"**Question {i+1}:** {definition}")
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
    
    
    # Button to continue to the next quiz set
    if st.session_state.remaining_terms:
        if st.button("Next Quiz Set", key="next_quiz_button"):
            st.session_state.quiz_count += 1  # Increment quiz count
            initialize_quiz()  # Get a new quiz set
            st.rerun()
    else:
        st.write("🎉 **All questions have been asked! Great job completing the quiz!**")

#################################################
with tab6:
    video_url = "https://www.youtube.com/embed/XLfQpv2ZRPU?si=5zKkYufSdvLbsCp3"

    st.markdown("#### 1. Video: Understanding physical aspect of sound")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )

    

    video_url2 = "https://www.youtube.com/embed/rYrdiQckGhw?si=nod5AuttYchOzH5X"

    st.markdown("#### 2. Fun experiments with sound")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url2}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )

    

    video_url3 = "https://www.youtube.com/embed/wvJAgrUBF4w?si=KxaZ-caUSgWc2noQ"

    st.markdown("#### 3. Sound resonance experiment")
    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url3}" 
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
    if st.button("Download PDF (No need) 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
