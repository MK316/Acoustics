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
input_key = "input_box"
st.text_input("Input", value=st.session_state.calc_input, key=input_key, disabled=True)
st.text(st.session_state.result)

# Layout for number and operation buttons
buttons = [
    ("1", "2", "3", "+"),
    ("4", "5", "6", "-"),
    ("7", "8", "9", "*"),
    (".", "0", "=", "/")
]

# Display the buttons in a compact grid layout
for row in buttons:
    cols = st.columns([0.25, 0.25, 0.25, 0.25], gap="tiny")
    for i, value in enumerate(row):
        if value == "=":
            cols[i].button(value, on_click=calculate_result, key=f"btn_{value}", help=f"Calculate the result")
        else:
            cols[i].button(value, on_click=update_input, args=(value,), key=f"btn_{value}", help=f"Add '{value}'")

# Clear button in a full-width layout
st.button("Clear", on_click=clear_input, help="Clear all inputs and results")

# JavaScript for handling the Enter key to trigger "=" button click
st.markdown("""
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var inputBox = document.getElementById('""" + input_key + """');
        inputBox.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                var eqButton = document.getElementById('btn_=');
                if (eqButton) {
                    eqButton.click();
                }
            }
        });
    });
    </script>
    """, unsafe_allow_html=True)
