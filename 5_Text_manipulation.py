import streamlit as st

# Text input for course title
course_title = st.text_input("Course Title", "")

# Number input for maximum corrector
max_corrector = st.number_input("Maximum Corrector", min_value=0, max_value=100, value=50)

# Text area for course description
course_description = st.text_area("Course Description", "")

# Text input for user input
user_input = st.text_input("User Input", "")

# Display the inputs
st.write(f"Course Title: {course_title}")
st.write(f"Maximum Corrector: {max_corrector}")
st.write(f"Course Description: {course_description}")
st.write(f"User Input: {user_input}")
