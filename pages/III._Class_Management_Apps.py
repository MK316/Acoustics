import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from wordcloud import WordCloud
import streamlit.components.v1 as components  # For embedding YouTube videos
from gtts import gTTS
import io

# Function to create word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Streamlit tabs
tabs = st.tabs(["📈 QR", "⏳ Timer", "👥 Grouping", "🐤 Github IDs","🔊 Text-to-Speech", "🎱 Calculator", "⛅ Word Cloud"])

# QR Code tab
with tabs[0]:
    st.subheader("QR Code Generator")
    qr_link = st.text_input("Enter a link to generate a QR code:")
    caption = st.text_input("Enter a caption for your QR code:")  # Allows user to type a caption

    # Adding a 'Generate QR Code' button
    generate_qr_button = st.button("Generate QR Code")
    
    if generate_qr_button and qr_link:
        # Generate the QR code only when the button is clicked
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_link)
        qr.make(fit=True)

        qr_img = qr.make_image(fill='black', back_color='white')

        # Convert the QR code image to RGB format and resize
        qr_img = qr_img.convert('RGB')  # Convert to RGB to be compatible with st.image
        qr_img = qr_img.resize((600, 600))  # Resize the image

        # Display the resized image with the user-provided caption
        st.image(qr_img, caption=caption, use_container_width=False, width=300)

# Timer tab
with tabs[1]:
    # Embed the Hugging Face space as an iframe
    huggingface_space_url = "https://MK-316-mytimer.hf.space"
    
    # Use Streamlit components to embed the external page
    st.components.v1.html(f"""
        <iframe src="{huggingface_space_url}" width="100%" height="600px" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    """, height=600)

# Grouping tab
with tabs[2]:
    st.subheader("👥 Grouping Tool")

    # Upload file section
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    
    # User input for group size
    members_per_group = st.number_input("Members per Group", min_value=1, value=5)
    
    # Input for fixed groups (optional)
    fixed_groups_input = st.text_input("Fixed Groups (separated by semicolon;)", placeholder="Name1, Name2; Name3, Name4")

    # Submit button to trigger grouping process
    if st.button("Submit"):
        if uploaded_file is not None:
            # Function to group names
            def group_names(file, members_per_group, fixed_groups_input):
                # Read the CSV file
                df = pd.read_csv(file)

                # Parse fixed groups input
                fixed_groups = [group.strip() for group in fixed_groups_input.split(';') if group.strip()]
                fixed_groups_df_list = []
                remaining_df = df.copy()

                # Process fixed groups and create a list for additional members to be added
                for group in fixed_groups:
                    group_names = [name.strip() for name in group.split(',') if name.strip()]
                    # Find these names in the DataFrame
                    matched_rows = remaining_df[remaining_df['Names'].isin(group_names)]
                    fixed_groups_df_list.append(matched_rows)
                    # Remove these names from the pool of remaining names
                    remaining_df = remaining_df[~remaining_df['Names'].isin(group_names)]

                # Shuffle the remaining DataFrame
                remaining_df = remaining_df.sample(frac=1).reset_index(drop=True)
                
                # Adjusting fixed groups to include additional members if they're under the specified group size
                for i, group_df in enumerate(fixed_groups_df_list):
                    while len(group_df) < members_per_group and not remaining_df.empty:
                        group_df = pd.concat([group_df, remaining_df.iloc[[0]]])
                        remaining_df = remaining_df.iloc[1:].reset_index(drop=True)
                    fixed_groups_df_list[i] = group_df  # Update the group with added members

                # Grouping the remaining names
                groups = fixed_groups_df_list  # Start with adjusted fixed groups
                for i in range(0, len(remaining_df), members_per_group):
                    groups.append(remaining_df[i:i + members_per_group])

                # Determine the maximum group size
                max_group_size = max(len(group) for group in groups)
                
                # Creating a new DataFrame for grouped data with separate columns for each member
                grouped_data = {'Group': [f'Group {i+1}' for i in range(len(groups))]}
                # Add columns for each member
                for i in range(max_group_size):
                    grouped_data[f'Member{i+1}'] = [group['Names'].tolist()[i] if i < len(group) else "" for group in groups]

                grouped_df = pd.DataFrame(grouped_data)
                
                return grouped_df

            # Call the group_names function and display the grouped names
            grouped_df = group_names(uploaded_file, members_per_group, fixed_groups_input)
            
            # Display the grouped names
            st.write(grouped_df)
            
            # Option to download the grouped names as CSV
            csv = grouped_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Grouped Names as CSV",
                data=csv,
                file_name='grouped_names.csv',
                mime='text/csv',
            )

        else:
            st.error("Please upload a CSV file before submitting.")

# Github

with tabs[3]:
    st.markdown("#### Github IDs")
    st.markdown("[Github IDs](https://docs.google.com/spreadsheets/d/1z2uYvH-foo3BZ6a4_T80TK7HOQbIJIYIUe5SWOEaGyk/edit?usp=sharing): Group members, Google Drive")

    # Button to open GitHub ID page
    if st.button("Open GitHub ID Page"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://docs.google.com/spreadsheets/d/1z2uYvH-foo3BZ6a4_T80TK7HOQbIJIYIUe5SWOEaGyk/edit?usp=sharing">', unsafe_allow_html=True)


# Text-to-Speech tab
with tabs[4]:
    st.subheader("Text-to-Speech Converter (using Google TTS")
    text_input = st.text_area("Enter the text you want to convert to speech:")
    language = st.selectbox("Choose a language: 🇰🇷 🇺🇸 🇬🇧 🇷🇺 🇫🇷 🇪🇸 🇯🇵 ", ["Korean", "English (American)", "English (British)", "Russian", "Spanish", "French", "Japanese"])

    tts_button = st.button("Convert Text to Speech")
    
    if tts_button and text_input:
        # Map human-readable language selection to language codes and optionally to TLDs for English
        lang_codes = {
            "Korean": ("ko", None),
            "English (American)": ("en", 'com'),
            "English (British)": ("en", 'co.uk'),
            "Russian": ("ru", None),
            "Spanish": ("es", None),
            "French": ("fr", None),
            "Japanese": ("ja", None)
        }
        language_code, tld = lang_codes[language]

        # Assuming you have a version of gTTS that supports tld or you have modified it:
        # This check ensures that the tld parameter is only used when not None.
        if tld:
            tts = gTTS(text=text_input, lang=language_code, tld=tld, slow=False)
        else:
            tts = gTTS(text=text_input, lang=language_code, slow=False)
        
        speech = io.BytesIO()
        tts.write_to_fp(speech)
        speech.seek(0)

        # Display the audio file
        st.audio(speech.getvalue(), format='audio/mp3')

# Code for the calculator within the first tab
with tabs[5]:
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

    # # Display the calculator input and result
    input_key = "input_box"
    st.text_input("Input", value=st.session_state.calc_input, key=input_key, disabled=True)
    # st.text(st.session_state.result)

    # Custom CSS to adjust the font size of the result text
    result_style = """
    <style>
    div[data-testid="stText"] {
        font-size: 24px; /* Larger font size for the result */
    }
    </style>
    """
    st.markdown(result_style, unsafe_allow_html=True)
    st.text("💎 The result is: " + st.session_state.result)

 
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


# Word Cloud tab
with tabs[6]:
    st.subheader("🌌 Word Cloud Generator")

    # Input text for generating the word cloud
    user_input = st.text_area("Enter text to generate a word cloud:")

    # Button to generate the word cloud
    if st.button("Generate Word Cloud"):
        if user_input.strip():
            # Generate word cloud only when there is valid input
            wordcloud = create_wordcloud(user_input)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.warning("Please enter some text to generate a word cloud.")
