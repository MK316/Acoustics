import streamlit as st



tab1, tab2 = st.tabs(["Padlet", "Others"])

with tab1:
    st.markdown("#### Access to Padlet")
    st.markdown("[Padlet](https://padlet.com/mirankim316/acoustics): Padlet to share files")
    
    # Button to open GitHub ID page
    if st.button("Open Padlet"):
       st.markdown(f'<meta http-equiv="refresh" content="0;url=https://padlet.com/mirankim316/acoustics">', unsafe_allow_html=True)
    
with tab2:
    st.markdown("#### Other Resources")
    st.write("This section can contain other links or information.")
