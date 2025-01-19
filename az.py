import streamlit as st
from PIL import Image
import json

# Setting the page configuration
st.set_page_config(page_title="My Portfolio", layout="wide")

st.title("Welcome to My Personal Portfolio")

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


def about_me():
    st.header("About Me")
    st.markdown("""
        <div style='text-align: justify;'>
        I am passionate about data science, AI, and building innovative software solutions. 
        I’m currently pursuing a **BS in Data Science**.
        </div>
    """, unsafe_allow_html=True)
    
    # Link to my CV
    st.markdown("""
        <div style='text-align: justify;'>
        You can view and download my CV by clicking the link below:
        </div>
    """, unsafe_allow_html=True)
    

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

        # Using markdown to create box layout for each project
        for project in projects_data:
            st.markdown(f"""
                <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin-bottom: 20px; background-color: #fff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                    <h3 style="color: #007acc; font-size: 20px; margin-bottom: 10px;">{project["title"]}</h3>
                    <p style="font-size: 16px; color: #555;">{project["description"]}</p>
                    <p><strong>Technologies Used:</strong> {', '.join(project['technologies'])}</p>
                    <div style="display: flex; justify-content: space-between;">
                        <a href="{project['source_code']}" target="_blank" style="color: #007acc; font-size: 16px; text-decoration: none;">Source Code</a>
                        <a href="{project['live_demo']}" target="_blank" style="color: #007acc; font-size: 16px; text-decoration: none;">Live Demo</a>
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

# Render selected section
if section == 'Home':
    home()
elif section == 'About Me':
    about_me()
elif section == 'Projects':
    projects()
elif section == 'Contact':
    contact()
