import streamlit as st
from PIL import Image
import json

# Setting the page configuration
st.set_page_config(page_title="My Portfolio", layout="centered", initial_sidebar_state="expanded")

st.button("Current mode")

# Sidebar with styled title
st.sidebar.markdown("<h1 style='color: white; font-size: 36px;'>Welcome to My Portfolio</h1>", unsafe_allow_html=True)

st.sidebar.image("image.ico", use_column_width=True) 

# Custom CSS for theme
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #f3f4f7, #ffffff);
        font-family: Arial, sans-serif;
    }
    .main-header h1 {
        color: #1a73e8;
        font-size: 2.5em;
        text-align: center;
    }
    h2, h3 {
        color: #0d47a1;
    }
    h3 {
        font-size: 1.7em;
    }
    .stButton>button {
        background-color: #1a73e8;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #0057d9;
    }
    .stProgress .stMarkdown {
        font-size: 14px;
        font-weight: 500;
    }
    .project-box {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
        width: 350px;
        height: 350px;
        border: 1px solid #dfe1e5;
        border-radius: 16px;
        margin: 10px;
        background: #ffffff;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    }
    .project-box h3 {
        margin: 0 0 10px;
    }
    a {
        color: #1a73e8;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

from theme import init_themes, change_theme

# Initialize themes
init_themes()

# Theme toggle button
ms = st.session_state
btn_face = ms.themes[ms.themes["current_theme"]]["button_face"]
st.button(btn_face, on_click=change_theme)

# Refreshing if needed
if ms.themes["refreshed"] == False:
    ms.themes["refreshed"] = True
    st.rerun()

#st.title("Welcome to My Personal Portfolio")

# Initializing the session state for navigation
if 'section' not in st.session_state:
    st.session_state.section = 'Home'

def home():
    st.title("Home")
    st.markdown("""
        <div style='text-align: justify;'>
        <span style='font-size: 40px;'>Hi!</span><br><br>
        <span style='font-size: 38px;'>I'm Muhammad Azhar</span><br><br>
        <span style='font-size: 24px;'>A Data Science student</span><br><br>
        ------ This portfolio highlights my projects, skills, and professional background.------
        </div>
    """, unsafe_allow_html=True)

import streamlit as st

def about_me():
    st.header("About Me")
    st.markdown("""
        <div style='
            padding: 15px; 
            background-color: #e6f7ff;  /* Light blue background */
            border-radius: 8px; 
            border: 1px solid #b3d9ff;
            font-family: Arial, sans-serif;
            text-align: justify;
        '>
            I have a keen interest in developing machine learning models, working on real-world datasets, 
            and using data-driven insights to solve problems. I also enjoy learning cloud technologies, 
            big data tools, and working on group projects. <br><br>

            When I'm not coding or analyzing data,
                                 I like playing Mobile Games
                                                  editing videos, 
                                                          and exploring new tech trends.
        </div>
    """, unsafe_allow_html=True)

    # Link to my CV
    st.markdown("""
        <div style='text-align: justify;'>
        You can view and download my CV by clicking the link below:
        </div>
    """, unsafe_allow_html=True)

    st.button("Download")
    st.markdown("[Download My CV](https://docs.google.com/document/d/1kUvcpyjDPqq-qmw1DklP1Lki6hWClF5z/edit?usp=sharing&ouid=104362434502810120258&rtpof=true&sd=true)", unsafe_allow_html=True)

    st.subheader("Skills")
    skills = {
        "Python": 85,
        "Machine Learning": 75,
        "Data Visualization": 80,
        "SQL": 70,
        "Web Development": 60
    }
    for skill, level in skills.items():
        st.write(f"**{skill}:**")
        st.progress(level)

def projects():
    st.header("Projects")
    try:
        with open("project.json") as f:
            projects_data = json.load(f)

        for project in projects_data:
            st.markdown(f"""
                <div style="
                    display: flex; 
                    flex-direction: column; 
                    justify-content: center; 
                    align-items: center; 
                    padding: 15px; 
                    width: 340px; 
                    border: 2px solid #ddd; 
                    border-radius: 12px; 
                    margin: 20px auto; 
                    background-color: #f9f9f9; 
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
                    <h3 style="color: #007acc; font-size: 20px; margin-bottom: 10px; text-align: center;">
                        {project["title"]}
                    </h3>
                    <p style="font-size: 14px; color: #555; text-align: center;">
                        {project["description"]}
                    </p>
                    <p style="font-size: 14px; text-align: center;">
                        <strong>Technologies Used:</strong> {', '.join(project['technologies'])}
                    </p>
                    <div style="display: flex; justify-content: space-between; width: 80%;">
                        <a href="{project['source_code']}" target="_blank" style="color: #007acc; font-size: 14px; text-decoration: none;">
                            Source Code
                        </a>
                        <a href="{project['live_demo']}" target="_blank" style="color: #007acc; font-size: 14px; text-decoration: none;">
                            Live Demo
                        </a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("Error loading project data. Please check the file path.")

def contact():
    st.header("Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(f"Thank you, {name}! I will get back to you soon.")

# Layout for navigation button
col1, col2 = st.columns([1, 6])
with col2:
    section = st.selectbox(
        "Navigate to", 
        options=['Home', 'About Me', 'Projects', 'Contact'], 
        key="nav_select",
        help="Choose a section to navigate"
    )

# Rendering the selected section
if section == 'Home':
    home()
elif section == 'About Me':
    about_me()
elif section == 'Projects':
    projects()
elif section == 'Contact':
    contact()
