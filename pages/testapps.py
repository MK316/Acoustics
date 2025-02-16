import streamlit as st

# Initialize calculator input and result
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
    except Exception as e:
        st.session_state.result = "Error"

# Function to clear the calculator input and result
def clear_input():
    st.session_state.calc_input = ""
    st.session_state.result = ""

# Display the calculator input and result
input_box = st.text_input("Input", value=st.session_state.calc_input, disabled=True)
st.text(st.session_state.result)

# Layout for number and operation buttons
buttons = [
    ("1", "2", "3", "+"),
    ("4", "5", "6", "-"),
    ("7", "8", "9", "*"),
    (".", "0", "=", "/")
]

# Display the buttons in a grid layout
for row in buttons:
    cols = st.columns(4)
    for i, value in enumerate(row):
        if value == "=":
            cols[i].button(value, on_click=calculate_result, key=f"btn_{value}")
        else:
            cols[i].button(value, on_click=update_input, args=(value,), key=f"btn_{value}")

# Clear button
st.button("Clear", on_click=clear_input)

# JavaScript for handling the Enter key to trigger "=" button click
st.markdown("""
    <script>
    const inputBox = document.getElementById('""" + st.session_state.input_box + """');
    inputBox.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            const eqButton = document.getElementById('btn_=');
            if (eqButton) {
                eqButton.click();
            }
        }
    });
    </script>
    """, unsafe_allow_html=True)
