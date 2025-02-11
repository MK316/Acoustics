import streamlit as st



tabs = st.tabs(["Google drive files", "Others"])

with tabs[0]:
    st.markdown("#### Access to Shared Google Drive: Restricted list")
    st.markdown("[Google drive](https://drive.google.com/drive/folders/1f0T4-BfKIwwowVB6JMLsmDMw0w0DQyvi?usp=drive_link): Group members, Google Drive")
    
    # Button to open GitHub ID page
    if st.button("Open Google drive"):
       st.markdown(f'<meta http-equiv="refresh" content="0;url=https://drive.google.com/drive/folders/1f0T4-BfKIwwowVB6JMLsmDMw0w0DQyvi?usp=drive_link">', unsafe_allow_html=True)
    
with tabs[1]:


if __name__ == "__main__":
    main()
