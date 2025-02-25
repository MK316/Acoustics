import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# GitHub raw URLs for the audio files
audio_urls = [
    "https://github.com/MK316/Acoustics/raw/main/praat/bada1.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada3.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada5.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada7.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada9.wav"
]

st.title("Da-Ga Perception Test")

st.write("Listen to each sound and select whether you hear 'da' or 'ga'.")

# Dictionary to store responses
responses = {}

# Display audio files with radio buttons for selection
for i, url in enumerate(audio_urls, start=1):
    st.audio(url, format="audio/wav")
    responses[f"stimulus_{i}"] = st.radio(f"Stimulus {i}", ["da", "ga"], index=None, horizontal=True)

# Submit button
if st.button("Submit"):
    # Convert responses to DataFrame
    df = pd.DataFrame(list(responses.items()), columns=["Stimulus", "Response"])
    df["Stimulus"] = df["Stimulus"].apply(lambda x: int(x.split("_")[1]))  # Extract stimulus number

    # Map categorical labels to numeric positions for plotting
    response_map = {"da": "Da", "ga": "Ga"}
    df["Response"] = df["Response"].map(response_map)

    # Define categorical order for y-axis
    category_order = ["Ga", "Da"]

    # Plot results as a line-dot plot with categorical y-axis
    fig, ax = plt.subplots()
    ax.plot(df["Stimulus"], df["Response"], marker="o", linestyle="-", color="black")

    # Adjust y-axis for categorical labels
    ax.set_yticks(category_order)
    ax.set_yticklabels(category_order)

    ax.set_xticks(df["Stimulus"])  # Set x-ticks to be only stimulus values
    ax.set_xlabel("Stimulus")
    ax.set_ylabel("Response")
    ax.set_title("Da-Ga Perception Results")

    st.pyplot(fig)
