import streamlit as st

# Calculator state initialization
if 'calc_input' not in st.session_state:
    st.session_state.calc_input = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# Function to update the calculator input
def update_input(value):
    st.session_state.calc_input += str(value)

# Function to calculate the result
def calculate_result():
    try:
        # Evaluate the mathematical expression from the input
        st.session_state.result = str(eval(st.session_state.calc_input))
        st.session_state.calc_input = st.session_state.result
    except Exception as e:
        st.session_state.result = "Error"
        st.session_state.calc_input = ""

# Function to clear the calculator input and result
def clear_input():
    st.session_state.calc_input = ""
    st.session_state.result = ""

# Display the current input and result
st.text_input("Input", st.session_state.calc_input, disabled=True)
st.text(st.session_state.result)

# Layout for number and operation buttons
col1, col2, col3, col4 = st.columns(4)
numbers = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    (".", "0", "=", "+")
]

for row in numbers:
    with col1:
        st.button(row[0], on_click=update_input, args=(row[0],))
    with col2:
        st.button(row[1], on_click=update_input, args=(row[1],))
    with col3:
        st.button(row[2], on_click=update_input, args=(row[2],))
    with col4:
        if row[3] == "=":
            st.button(row[3], on_click=calculate_result)
        else:
            st.button(row[3], on_click=update_input, args=(row[3],))

# Clear button
st.button("Clear", on_click=clear_input)
