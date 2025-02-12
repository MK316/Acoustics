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
    
    ### 🎥 Pitch Hearing Demonstration
    Watch this video to understand **how small changes in articulation can lead to major acoustic effects**.
    
    """)
    st.markdown("[🎥 Watch the video on YouTube](https://www.youtube.com/watch?v=QFq9ywKuCYo)")
   
    # Embed YouTube video using <iframe>
    video_url = "https://www.youtube.com/embed/PM4WSBZanQQ?si=WCErVnSrSjeLkme2"
    
    st.markdown(
        f"""
        <iframe width="700" height="400" src="{video_url}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )

    ---
    ### 🎵 Interactive: Simulating Quantal vs. Non-Quantal Effects
    Try adjusting the **articulatory position** (simulated as tongue height) and observe:
    - **Stable Regions**: Small articulation changes **do not** significantly affect the waveform.
    - **Unstable Regions**: Small articulation changes **cause a major waveform shift**.
    
    Move the slider and see how quantal effects work!
    """)
    
    # User selects "articulatory position" (simulated tongue height)
    articulation_position = st.slider("Select an Articulatory Position (Simulated Tongue Height)", 
                                      min_value=1, max_value=100, value=50, step=1)
    
    # Simulating Quantal & Non-Quantal Zones
    if 10 <= articulation_position <= 40:
        frequency = 300  # Stable zone (like vowel /i/)
    elif 41 <= articulation_position <= 59:
        frequency = 300 + (articulation_position - 40) * 8  # Non-quantal zone (unstable transition)
    elif 60 <= articulation_position <= 90:
        frequency = 450  # Stable zone (like vowel /a/)
    
    # Generate waveform
    duration = 0.05  # Short duration for display
    sampling_rate = 44100
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * t)
    
    # Plot waveform
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(t[:500], waveform[:500], color="blue", linewidth=2)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Waveform at Articulatory Position {articulation_position} (Frequency: {frequency} Hz)")
    ax.grid(True)
    
    # Display plot
    st.pyplot(fig)
    
    # Explanation of the effect
    if 10 <= articulation_position <= 40 or 60 <= articulation_position <= 90:
        st.success("✅ **You are in a Quantal Zone!** Small changes in articulation do NOT drastically change acoustics.")
    else:
        st.warning("⚠ **You are in a Non-Quantal Zone!** Small articulation changes cause a BIG acoustic shift.")
    
    st.markdown("""
    ---
    ## 🎯 Key Takeaways
    - **Quantal Zones (Stable Regions)**: Articulatory adjustments do not drastically affect the sound.
    - **Non-Quantal Zones (Unstable Regions)**: Small articulation changes lead to **big** acoustic differences.
    - **This is why languages prefer quantal sounds**, ensuring **clear and stable communication**.
    
    ---
    **Try adjusting the slider above** and observe the effects in action!
    """)

######################################################
with tab3:
    st.write("### Download Lecture Slides")

    # GitHub raw file URL (replace with your actual link)
    pdf_url = "https://github.com/MK316/Acoustics/raw/main/data/test.pdf"

    # Create a button that triggers download
    if st.button("Download PDF 📥"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={pdf_url}">', unsafe_allow_html=True)
