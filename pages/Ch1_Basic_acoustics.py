import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit app
st.caption("Ch.1 Basic acoustics & acoustic filters")

# Create tabs
tab1, tab2, tab3 = st.tabs(["EX1-4", "Tab 2", "Tab 3"])

# Tab 1: Sine Wave Plot
with tab1:
    st.header("Sine Wave Plot")
    
    # Generate degrees and amplitudes
    degrees = np.arange(0, 721, 45)
    radians = np.radians(degrees)
    amplitudes = np.sin(radians)

    # Plot the sine wave
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(degrees, amplitudes, marker='o', linestyle='-', label="Sine Wave")
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Center line
    ax.set_xticks(degrees)
    ax.set_yticks(np.arange(-1, 1.5, 0.5))
    ax.set_title("Sine Wave Plot (0° to 720°)")
    ax.set_xlabel("Degrees")
    ax.set_ylabel("Amplitude")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)

# Tab 2: Placeholder for future content
with tab2:
    st.header("Tab 2 Content")
    st.write("This is where you can add content for the second tab.")

# Tab 3: Placeholder for future content
with tab3:
    st.header("Tab 3 Content")
    st.write("This is where you can add content for the third tab.")
