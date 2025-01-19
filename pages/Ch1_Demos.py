import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit app
st.caption("Ch.1 Basic acoustics & acoustic filters")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Links", "Tab 2", "EX1-4"])

# Tab 1: Links with two sections of buttons
with tab1:
    st.header("Links")
    
    # First section: st.write and 2 buttons
    st.write("Visit these websites for additional resources:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Open Website 1"):
            st.markdown("[Visit Website 1](https://www.example.com)", unsafe_allow_html=True)
    with col2:
        if st.button("Open Website 2"):
            st.markdown("[Visit Website 2](https://www.example.org)", unsafe_allow_html=True)
    
    st.write("---")  # Divider for separation

    # Second section: st.write and 3 buttons
    st.write("Explore more tools and examples:")
    col3, col4, col5 = st.columns(3)
    with col3:
        if st.button("Tool 1"):
            st.markdown("[Open Tool 1](https://www.tool1.com)", unsafe_allow_html=True)
    with col4:
        if st.button("Tool 2"):
            st.markdown("[Open Tool 2](https://www.tool2.com)", unsafe_allow_html=True)
    with col5:
        if st.button("Tool 3"):
            st.markdown("[Open Tool 3](https://www.tool3.com)", unsafe_allow_html=True)

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
