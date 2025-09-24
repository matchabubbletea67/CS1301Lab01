import streamlit as st
import info
import pandas as pd

# about me
def about_me():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
about_me()

# sidebar links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text(f"My LinkedIn: {info.my_linkedin_url}")
    st.sidebar.text(f"My Github: {info.my_github_url}")
    st.sidebar.text(f"My email address: {info.my_email_address}")
    my_linkedin_url=f'<a href={info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height = "75"></a>'
    my_github_url=f'<a href={info.my_github_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height = "75"></a>'
    my_email_address=f'<a href={info.my_email_address}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height = "75"></a>'
links_section()

# education
def education_section(education_data, course_data):
    st.header("Education 📚")
    st.subheader(f"**{education_data['Institution']}** ")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:** ")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True,
        )
    st.write("---")
    
education_section(info.education_data, info.course_data)

#Professional Experience
def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description) in experience_data.items():
        expander = st.expander(f"{job_title}")
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience_section(info.experience_data)

#Projects
def project_section (projects_data):
    st.header ("Projects 👩🏻‍🔬")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        for bullet in project_description:
            expander.write(bullet)
    st.write("---")
project_section(info.projects_data)

# Skills
def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,'')}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}: {proficiency}")
skills_section(info.programming_data, info.spoken_data)

# Activities
def activities_section(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details) in leadership_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, (details) in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    st.write("---")
activities_section(info.leadership_data, info.activity_data)
