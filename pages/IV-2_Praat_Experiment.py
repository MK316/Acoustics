import streamlit as st

st.caption("Perception experiment using Praat MFC")

# Define the tabs
tabs = st.tabs(["Praat manual", "Exp 1 sample", "Exp 2", "Exp 3"])

# Embed a webpage in the first tab
with tabs[0]:
    st.header("Praat Manual")
    # Replace the URL below with the actual URL you want to embed
    st.components.v1.iframe("https://www.fon.hum.uva.nl/praat/manual/ExperimentMFC.html", width=700, height=800)

# Content for Experiment 1
with tabs[1]:
    st.header("Experiment 1")
    st.write("Content for Experiment 1 will be updated here.")

# Content for Experiment 2
with tabs[2]:
    st.header("Experiment 2")
    st.write("Content for Experiment 2 will be updated here.")

# Content for Experiment 3
with tabs[3]:
    st.header("Experiment 3")
    st.write("Content for Experiment 3 will be updated here.")
