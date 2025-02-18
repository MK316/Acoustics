import streamlit as st
import requests
import calendar
from datetime import datetime
from PIL import Image
import os


# CSS to adjust the alignment of the dropdown to match the buttons
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;  /* Adjust this value to align with the buttons */
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the path to the slides folder
slides_path = "pages/overview_lectureslides"  # Ensure this is correct relative to your app's location
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)

# Initialize session state variables if they do not exist
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0  # Start with the first slide

# Function to load and display the image based on the current index with resizing
def display_image():
    slide_path = os.path.join(slides_path, slide_files[st.session_state.slide_index])
    image = Image.open(slide_path)
    
    # Set your desired width for resizing
    desired_width = 1200  # Adjust this value as needed
    aspect_ratio = image.height / image.width
    new_height = int(desired_width * aspect_ratio)
    resized_image = image.resize((desired_width, new_height))

    st.image(resized_image, caption=f"Slide {st.session_state.slide_index + 1} of {num_slides}")


# Include custom CSS to justify text in the markdown
# Include custom CSS to justify text in the markdown
st.markdown("""
<style>
.justify-text p {
    text-align: justify;
    text-justify: inter-word;
}
.calendar-table {
    margin-left: auto;
    margin-right: auto;
    border-collapse: collapse;
}
.calendar-table td, .calendar-table th {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Create tabs for different sections of the course
tabs = st.tabs(["🍐 Course Overview", "🍒 Overview2", "💙 Materials", "🍏 Padlet", "🍋 TBA", "📆 Calendar"])


# Course Overview tab
with tabs[0]:
    st.caption("🔎 Course Overview")
    st.markdown("""
    <div class="justify-text">
    This course is tailored for English educators, introducing essential skills for integrating acoustics into language teaching. We will demystify the fundamentals of speech sounds and auditory perception, emphasizing their practical application in English pronunciation and listening comprehension.
    Students will:
    - Explore the fundamentals of speech sounds in the context of English language learning.
    - Develop a working knowledge of experimental design in acoustics and perception studies.
    - Learn basic Praat coding skills for implementing and analyzing acoustic experiments.
    - Create experimental tools for testing pronunciation and listening skills using speech data
    - _Future Coursework:_ While this course empowers you with the tools to design and initiate experiments, a subsequent course will focus on conducting detailed analyses and applying these findings to enhance teaching practices effectively. This future course will help solidify your ability to integrate research into your language teaching.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("#### Evaluation")
    st.markdown("""
    - Attendance: 10%
    - Midterm: 30%
    - Final: 30%
    - Assignments: 30%
    """)

# Content for the Assignments tab
with tabs[1]:
    st.header("Overview")
    st.write("Perspective")

    # Arrange 'Start', 'Previous', 'Next', and 'Slide Selector' in a single row
    col1, col2, col3, col4 = st.columns([1, 1, 1, 5])
    
    with col1:
        if st.button("⛳", key="start", help="Reset to the first slide"):
            st.session_state.slide_index = 0

    with col2:
        if st.button("◀️", key="previous", help="Go back to the previous slide"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1
            else:
                st.warning("This is the first slide.")

    with col3:
        if st.button("▶️", key="next", help="Go to the next slide"):
            if st.session_state.slide_index < num_slides - 1:
                st.session_state.slide_index += 1
            else:
                st.warning("END")

    with col4:
        # Display slide selector dropdown
        selected_slide = st.selectbox("",
                                      options=[f"Slide {i + 1}" for i in range(num_slides)],
                                      index=st.session_state.slide_index)

        # Update slide index if dropdown selection changes
        selected_slide_index = int(selected_slide.split()[-1]) - 1
        if selected_slide_index != st.session_state.slide_index:
            st.session_state.slide_index = selected_slide_index

    # Display the image
    display_image()
    
    st.markdown("---")
    st.markdown("#### 🎬 Watch video: Objects Under Electron Microscope!")
    
    # YouTube Video Embed
    video_url = "https://www.youtube.com/embed/yLA8dTncLXA?si=Em5LjfXG9IWVxZzj"
    # st.video(youtube_url)

    st.markdown(
        f"""
        <iframe width="560" height="315" src="{video_url}" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )


with tabs[2]:

    st.markdown("#### 📗Texbook: ")
    st.write("- Johnson, K. (2012) _Acoustics and Auditory Phonetics_ (3rd edition), Wiley-Blackwell [link](https://books.google.co.kr/books/about/Acoustic_and_Auditory_Phonetics.html?id=sKOUKJXbmYMC&redir_esc=y)")
    st.write("- Supplementary readings (TBA)")
        
    st.markdown("---")
    
    # st.markdown("""
    # #### 🔎 Software and online platforms: 
    # - Praat software: Sound handling, speech analysis, perception experiments 
    # - Paul Boersma & David Weenink (1992-2025). _Praat: doing phonetics by computer_ [Computer program]. Version 6.4.27, retrieved 23 January 2025 from https://www.praat.org.
    # - Download from [fon.hum.uva.nl](https://www.fon.hum.uva.nl/praat/)
    # """)


    st.markdown("""
    #### Key Resources:
    - **GitHub:** Data and code repository hosting. [github.com](https://github.com)
    - **Hugging Face:** Deployment of applications and AI models. [huggingface.co](https://huggingface.co)
    - **Streamlit:** Easy deployment of applications. [streamlit.app](https://streamlit.app)
    - **Google Colab:** Cloud-based Python programming. [colab.google.com](https://colab.google.com/)
    """)

      
# Content for the Evaluation tab
with tabs[3]:
    st.header("Files to share: on Padlet")
    st.write("This Padlet serves as a dynamic hub for our Acoustics course. Here, you'll find additional course materials, additional reading resources, and online tools. It's also a space for sharing files and submitting assignments.")
    st.components.v1.iframe("https://padlet.com/mirankim316/acoustics", width=800, height=600)

# Content for the Links tab
with tabs[4]:
    st.header("TBA")

# Content for the Calendar tab
with tabs[5]:
    # Dropdown for selecting a month
    month_option = st.selectbox("Select a Month", options=["March", "April", "May", "June"], index=0)
    # Dictionary to map month names to their corresponding numbers
    month_to_number = {"March": 3, "April": 4, "May": 5, "June": 6}
    # Get selected month number
    month_number = month_to_number[month_option]
    year = 2025  # Define the year

    # Define a list of holidays as tuples (day, month)
    holidays = [
        (1, 3),  # Example: March 1
        (3, 3),  # Example: May 25
        (5, 5),
        (6, 5),
        (6, 6)
        # Add more holidays as needed
    ]

    # Generate the calendar for the selected month
    cal = calendar.monthcalendar(year, month_number)

    # Display the calendar as a table using HTML
    cal_html = "<table class='calendar-table'><thead><tr>"
    cal_html += "".join(f"<th>{day}</th>" for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    cal_html += "</tr></thead><tbody>"

    for week in cal:
        cal_html += "<tr>"
        for day in week:
            if day == 0:  # Empty cell for days outside the month
                cal_html += "<td></td>"
            else:
                # Check if the day is a holiday
                if (day, month_number) in holidays:
                    cal_html += f"<td style='color: red; font-weight: bold;'>{day}</td>"
                else:
                    cal_html += f"<td>{day}</td>"
        cal_html += "</tr>"
    cal_html += "</tbody></table>"

    st.markdown(cal_html, unsafe_allow_html=True)
