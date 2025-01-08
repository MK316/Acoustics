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
tabs = st.tabs(["🍐 Course Overview", "🍓 Schedule", "🍏 Evaluation", "🍒 Assignments", "🍋 Links", "📆 Calendar"])

# Course Overview tab
with tabs[0]:
    st.caption("🔎 Course Overview")
    st.markdown("""
    <div class="justify-text">
    **This course is designed to provide in-service English teachers with essential skills for integrating technology into language education. This course emphasizes both theoretical and practical aspects of acoustics and perception, exploring their application in teaching English pronunciation and listening comprehension.

    Participants will:
    - Explore the fundamentals of speech sounds in the context of English language learning.
    - Develop a working knowledge of experimental design in acoustics and perception studies.
    - Learn basic Praat coding skills for implementing and analyzing acoustic experiments.
    - Create experimental tools for testing pronunciation and listening skills using speech data.

    By the end of this course, participants will have the confidence to design and conduct experiments, analyze findings, and apply results to enhance their teaching practices.
    </div>
    """, unsafe_allow_html=True)
# Content for the Schedule tab
with tabs[1]:
    st.caption("Spring 2025")
    # URL of the raw markdown file on GitHub
    markdown_url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/README.md"
    
    try:
        response = requests.get(markdown_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        markdown_content = response.text
        st.markdown(markdown_content, unsafe_allow_html=True)
    except requests.exceptions.HTTPError as err:
        st.error(f"Failed to retrieve Markdown content: {err}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        
# Content for the Evaluation tab
with tabs[2]:
    st.header("Evaluation")
    st.write("This section outlines the evaluation criteria and methods, such as grading rubrics, tests, projects, and participation requirements.")

# Content for the Assignments tab
with tabs[3]:
    st.header("Assignments")
    st.write("List and detail the assignments for the course here, providing due dates, submission guidelines, and grading criteria.")

# Content for the Links tab
with tabs[4]:
    st.header("Links")
    st.write("Provide useful links here. This could include additional reading materials, online resources, and related external websites.")

# Content for the Calendar tab
with tabs[5]:
   # Dropdown for selecting a month
    month_option = st.selectbox("Select a Month", options=["March", "April", "May", "June"], index=0)
    # Dictionary to map month names to their corresponding numbers
    month_to_number = {"March": 3, "April": 4, "May": 5, "June": 6}
    # Get selected month number
    month_number = month_to_number[month_option]
    # Generate the calendar for the selected month
    year = 2025  # Define the year
    cal = calendar.monthcalendar(year, month_number)
    # Display the calendar as a table using HTML
    cal_html = "<table class='calendar-table'><thead><tr>"
    cal_html += "".join(f"<th>{day}</th>" for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    cal_html += "</tr></thead><tbody>"
    for week in cal:
        cal_html += "<tr>" + "".join(f"<td>{day if day != 0 else ''}</td>" for day in week) + "</tr>"
    cal_html += "</tbody></table>"
    st.markdown(cal_html, unsafe_allow_html=True)