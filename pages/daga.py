import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# GitHub raw URLs for the audio files
audio_urls = [
    "https://github.com/MK316/Acoustics/raw/main/praat/bada1.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada2.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada3.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada4.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada5.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada6.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada7.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada8.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada9.wav",
    "https://github.com/MK316/Acoustics/raw/main/praat/bada10.wav"
]

st.title("Da-Ga Perception Test")

st.write("Listen to each sound and select whether you hear 'da' or 'ga'.")

# Dictionary to store responses
responses = {}

# Display audio files with choice buttons
for i, url in enumerate(audio_urls, start=1):
    st.audio(url, format="audio/wav")
    responses[f"stimulus_{i}"] = st.radio(f"Stimulus {i}", ["da", "ga"], index=None)

# Submit button
if st.button("Submit"):
    # Convert responses to DataFrame
    df = pd.DataFrame(list(responses.items()), columns=["Stimulus", "Response"])
    df["Stimulus"] = df["Stimulus"].apply(lambda x: int(x.split("_")[1]))  # Extract stimulus number

    # Count occurrences of "da" and "ga"
    counts = df.groupby(["Stimulus", "Response"]).size().unstack(fill_value=0)

    # Plot results
    fig, ax = plt.subplots()
    counts.plot(kind="bar", stacked=True, ax=ax, color=["blue", "red"])
    ax.set_xlabel("Stimulus")
    ax.set_ylabel("Count")
    ax.set_title("Da-Ga Perception Results")
    ax.legend(["Da", "Ga"])

    st.pyplot(fig)
