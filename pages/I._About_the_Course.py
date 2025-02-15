import streamlit as st
import requests
import calendar
from datetime import datetime

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
tabs = st.tabs(["🍐 Course Overview", "💙 Materials", "🍏 Evaluation", "🍒 Assignments", "🍋 Links", "📆 Calendar"])

# Course Overview tab
with tabs[0]:
    st.caption("🔎 Course Overview")
    st.markdown("""
    <div class="justify-text">
    This course is designed to provide students with essential skills for integrating technology into language education. This course emphasizes both theoretical and practical aspects of acoustics and perception, exploring their application in teaching English pronunciation and listening comprehension.<br><br>

    Students will:
    - Explore the fundamentals of speech sounds in the context of English language learning.
    - Develop a working knowledge of experimental design in acoustics and perception studies.
    - Learn basic Praat coding skills for implementing and analyzing acoustic experiments.
    - Create experimental tools for testing pronunciation and listening skills using speech data.

    By the end of this course, participants will have the knowledge and skills to design and conduct experiments. (+ analyze findings, and apply results to enhance their teaching practices.)
    </div>
    """, unsafe_allow_html=True)

with tabs[1]:

    st.markdown("""#### 📗Texbook: 
    - Johnson, K. (2012) _Acoustics and Auditory Phonetics_ (3rd edition), Wiley-Blackwell [link](https://books.google.co.kr/books/about/Acoustic_and_Auditory_Phonetics.html?id=sKOUKJXbmYMC&redir_esc=y))
    - Supplementary readings (TBA)
    
    st.markdown("---")
    
    st.markdown("""
    #### 🔎 Software and online platforms:
    - Praat software: Sound handling, speech analysis, perception experiments 
    - Paul Boersma & David Weenink (1992-2025). _Praat: doing phonetics by computer_ [Computer program]. Version 6.4.27, retrieved 23 January 2025 from https://www.praat.org.
    - Download from [fon.hum.uva.nl](https://www.fon.hum.uva.nl/praat/)
    """)


    # st.markdown("🔎Github: data and code storage") 
    # st.markdown("- https://github.com")

    # st.markdown("🔎Higgingface: deploy applications, machine learning, AI models") 
    # st.markdown("- https://huggingface.co")

    # st.markdown("🔎Streamlit: application deploy") 
    # st.markdown("- https://streamlit.app")

    # st.markdown("🔎Colab: Python coding via clouding") 
    # st.markdown("- https://colab.google/")
      
# Content for the Evaluation tab
with tabs[2]:
    st.header("Evaluation")
    st.markdown("""
    - Attendance: 10%
    - Midterm: 30%
    - Final: 30%
    - Assignments: 30%
    """)

# Content for the Assignments tab
with tabs[3]:
    st.header("Assignments")
    st.write("Detailed assignments for the course will be updated here in time. Stay tuned!")

# Content for the Links tab
with tabs[4]:
    st.header("Links")
    st.write("Useful links will be updated here. This could include additional reading materials, online resources, and related external websites.")

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
