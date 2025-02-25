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

    # Encode categorical responses for plotting
    response_mapping = {"da": 1, "ga": 2}  # Encode 'da' as 1, 'ga' as 2
    df["Response_Num"] = df["Response"].map(response_mapping)

    # Create the plot
    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(df["Stimulus"], df["Response_Num"], marker="o", linestyle="-", color="black")

    # Set y-axis to categorical labels
    ax.set_yticks([1, 2])
    ax.set_yticklabels(["Da", "Ga"])  # Show "Da" and "Ga" instead of numbers

    ax.set_xticks(df["Stimulus"])  # Set x-ticks to be only stimulus values
    ax.set_xlabel("Stimulus")
    ax.set_ylabel("Response")
    ax.set_title("Da-Ga Perception Results")

    # Display the plot in Streamlit
    st.pyplot(fig)
