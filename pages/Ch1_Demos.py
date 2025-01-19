import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit app
st.caption("Ch.1 Basic acoustics & acoustic filters")

# Create tabs
tab1, tab2, tab3 = st.tabs(["👀 Links", "🌀 Apps", "🌱EX1-4"])

# Tab 1: Links with colorful buttons, descriptions, and links
with tab1:
    st.caption("Here you will find links to useful online resources related to lectures and course materials.")
    
    # First section: Colorful buttons with descriptions and links
    st.write("1. Visit these websites for additional resources:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <a href="https://www.google.com" target="_blank">
                <button style="background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; border-radius: 5px;">Open Website 1</button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Description: Access an introductory resource for acoustic phonetics.")
    with col2:
        st.markdown(
            """
            <a href="https://www.example.org" target="_blank">
                <button style="background-color: #2196F3; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; border-radius: 5px;">Open Website 2</button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.write("Description: Explore advanced examples in speech science.")
 
    with col3:
        st.markdown(
            """
            <a href="https://www.tool1.com" target="_blank">
                <button style="background-color: #000066; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; border-radius: 5px;">Tool 1</button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.write("Description: A tool for analyzing sound waveforms.")
        
    st.write("---")  # Divider for separation

    # Second section: More colorful buttons
    st.write("2. Explore more tools and examples:")
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown(
            """
            <a href="https://www.tool2.com" target="_blank">
                <button style="background-color: #FF9800; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; border-radius: 5px;">Tool 2</button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.write("Description: Simulate acoustic filters with this tool.")
    with col5:
        st.markdown(
            """
            <a href="https://www.tool3.com" target="_blank">
                <button style="background-color: #9C27B0; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; border-radius: 5px;">Tool 3</button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.write("Description: Visualize speech data and patterns.")

    with col6:
        st.markdown(
            """
            <a href="https://www.tool3.com" target="_blank">
                <button style="background-color: #660000; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px; border-radius: 5px;">Tool 3</button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.write("Description: Visualize speech data and patterns.")


# Tab 2: Placeholder for future content
with tab2:
    st.header("Tab 2 Content")
    st.write("This is where you can add content for the second tab.")

# Tab 3: Sine Wave Plot
with tab3:
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
