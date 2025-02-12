import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

tab1, tab2, tab3, tab3 = st.tabs(["📖 Lecture slides", "🌀 Quantal theory", "🌀 Apps", "💾 Download"])


with tab1:
    st.write("Other content here.")

with tab2:
    st.title("🎓 Quantal Theory of Speech Acoustics")
    st.subheader("Understanding Stability and Efficiency in Speech Production")
    
    st.markdown("""
    ### 📌 What is Quantal Theory?
    Quantal Theory, proposed by **Kenneth N. Stevens (1972, 1989)**, explains how **speech sounds are produced efficiently and remain stable** despite variability in articulation.
    
    According to this theory:
    1. **Speech articulation and acoustics have a nonlinear relationship**:
       - Small movements in the tongue, lips, or jaw **may not** cause large changes in sound.
       - However, at certain articulatory positions, **small shifts can lead to sudden and significant acoustic changes** (quantal changes).
    2. **Some articulatory regions are stable**, meaning they allow for small adjustments without drastically altering the sound.
    3. **Quantal sounds** (like /i/, /u/, /a/, /p/, /t/, /k/) are common across languages because they maximize stability and clarity.
    
    ---
    ### 📌 Why Is This Important?
    ✅ **Explains why certain sounds are universal** in human languages.  
    ✅ **Shows how speech remains stable** despite variability in articulation.  
    ✅ **Helps in phonetics, linguistics, and speech synthesis**.  
    """)
    
    
    # Quantal Theory Illustration: Nonlinear Effects
    st.markdown("## 🔊 Quantal Effect: Acoustic Nonlinearity")
    st.write("The relationship between articulation and acoustics is nonlinear. Below, see how a simple frequency change can create a large acoustic difference.")
    
    # Interactive Frequency Change Simulation
    st.markdown("### 🎵 Experiment: How Small Changes Affect Sound")
    st.write("Move the slider to change frequency and observe how a small change affects the waveform.")
    
    # User selects frequency shift
    freq1 = st.slider("Choose Base Frequency (Hz)", min_value=200, max_value=400, value=250, step=10)
    freq2 = freq1 + 20  # Simulating small shift causing quantal effect
    
    # Generate waveform
    duration = 0.05  # Short duration for display
    sampling_rate = 44100
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    wave1 = np.sin(2 * np.pi * freq1 * t)
    wave2 = np.sin(2 * np.pi * freq2 * t)
    
    # Plot waveforms
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(t[:500], wave1[:500], label=f"Base Freq: {freq1} Hz", color="blue")
    ax.plot(t[:500], wave2[:500], label=f"Shifted Freq: {freq2} Hz", color="red", linestyle="dashed")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Effect of Small Frequency Shift on Waveform")
    ax.legend()
    ax.grid(True)
    
    # Display plot
    st.pyplot(fig)
    
    # Conclusion
    st.markdown("""
    ---
    ## 🎯 Conclusion
    - **Quantal Theory explains why speech sounds remain stable** even with minor articulatory variations.
    - Some articulatory positions are **stable zones**, while others cause **quantal shifts** in acoustics.
    - This helps us understand **phonetic universals and efficient speech production**.
    
    ---
    📌 **Try adjusting the slider above** to observe quantal changes in action!
    """)

######################################################
with tab3:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
