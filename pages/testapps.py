import streamlit as st

# Create tabs
tab1, tab2 = st.tabs(["Calculator", "Other Features"])

# Code for the calculator within the first tab
with tab1:
    st.markdown("### 🔢 Calculator")
    # Initialize calculator input and result
    if 'calc_input' not in st.session_state:
        st.session_state.calc_input = ""
    if 'result' not in st.session_state:
        st.session_state.result = ""

    # Function to update the calculator input
    def update_input(value):
        # Mapping from Unicode symbols to standard operators
        symbol_map = {"➕": "+", "➖": "-", "✖️": "*", "➗": "/"}
        # Replace the symbol with its corresponding operator if it's a special symbol
        value = symbol_map.get(value, value)
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
        ("1", "2", "3", "➕"),
        ("4", "5", "6", "➖"),
        ("7", "8", "9", "✖️"),
        (".", "0", "=", "➗")
    ]

    # Adjusting button widths and font size via columns and markdown
    button_style = """
    <style>
    div.stButton > button:first-child {
        font-size: 18px; /* Increase font size */
        height: 3em; /* Increase height */
        width: 100%; /* Attempt to adjust width */
        margin: 0.25em; /* Tight margin to reduce space */
    }
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    for row in buttons:
        cols = st.columns(4)
        for i, value in enumerate(row):
            button_label = f"{value}"  # Ensures symbols are displayed
            if value == "=":
                cols[i].button(button_label, on_click=calculate_result, key=f"btn_{value}")
            else:
                cols[i].button(button_label, on_click=update_input, args=(value,), key=f"btn_{value}")

    # Clear button in a full-width layout
    st.button("Clear", on_click=clear_input)

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

# Second tab for other features or content
with tab2:
    st.write("Here you can add other features or additional content.")

