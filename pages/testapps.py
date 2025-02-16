import streamlit as st

# Calculator state initialization
if 'calc_input' not in st.session_state:
    st.session_state.calc_input = ""

# Function to update the calculator input
def update_input(number):
    st.session_state.calc_input += str(number)

# Function to clear the calculator input
def clear_input():
    st.session_state.calc_input = ""

# Display the current input
st.text_input("Input", st.session_state.calc_input, disabled=True)

# Number buttons
col1, col2, col3 = st.columns(3)
with col1:
    st.button("1", on_click=update_input, args=(1,))
    st.button("4", on_click=update_input, args=(4,))
    st.button("7", on_click=update_input, args=(7,))

with col2:
    st.button("2", on_click=update_input, args=(2,))
    st.button("5", on_click=update_input, args=(5,))
    st.button("8", on_click=update_input, args=(8,))
    st.button("0", on_click=update_input, args=(0,))

with col3:
    st.button("3", on_click=update_input, args=(3,))
    st.button("6", on_click=update_input, args=(6,))
    st.button("9", on_click=update_input, args=(9,))

# Clear button
st.button("Clear", on_click=clear_input)
