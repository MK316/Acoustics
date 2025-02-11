import streamlit as st



tab1, tab2 = st.tabs(["Google drive files", "Others"])

with tab1:
    st.markdown("#### Access to Shared Google Drive: Restricted list")
    st.markdown("[Google drive](https://drive.google.com/drive/folders/1f0T4-BfKIwwowVB6JMLsmDMw0w0DQyvi?usp=drive_link): Group members, Google Drive")
    
    # Button to open GitHub ID page
    if st.button("Open Google drive"):
       st.markdown(f'<meta http-equiv="refresh" content="0;url=https://drive.google.com/drive/folders/1f0T4-BfKIwwowVB6JMLsmDMw0w0DQyvi?usp=drive_link">', unsafe_allow_html=True)
    
with tab2:
    st.markdown("#### Other Resources")
    st.write("This section can contain other links or information.")
