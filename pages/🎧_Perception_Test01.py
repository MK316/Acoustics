import streamlit as st

st.title("Main Page")

# Add a button that links to another page inside the 'pages' folder
st.page_link("pages/daga.py", label="Go to Page 1", icon="📄")
