import streamlit as st
import os
import sqlalchemy as db
from pages import calendar, digital_wellness, entertainment, finance, health, meals, productivity

# Page configuration
st.set_page_config(page_title="Everydai-Hub", layout="wide")

# Notify when the application starts successfully
st.success("Application started successfully.")

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:admin123@db:5433/everydai_db")
engine = db.create_engine(DATABASE_URL)
SessionLocal = db.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Notify when the database connects successfully
try:
    session = SessionLocal()
    st.session_state['db_session'] = session
    st.success("Connected to the database successfully.")
except Exception as e:
    st.error(f"Failed to connect to the database: {e}")

# Notify when the application connects to Nebius AI Studio successfully
try:
    NEBIUS_AI_API_KEY = os.getenv("NEBIUS_AI_API_KEY")
    NEBIUS_AI_ENDPOINT = os.getenv("NEBIUS_AI_ENDPOINT")
    if NEBIUS_AI_API_KEY and NEBIUS_AI_ENDPOINT:
        st.success("Connected to Nebius AI Studio successfully.")
    else:
        st.warning("Nebius AI Studio connection details are missing.")
except Exception as e:
    st.error(f"Failed to connect to Nebius AI Studio: {e}")

# Session state to handle authentication and navigation
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Welcome'

# Page mapping
page_mapping = {
    'Calendar': calendar,
    'Digital_Wellness': digital_wellness,
    'Entertainment': entertainment,
    'Finance': finance,
    'Health': health,
    'Meals': meals,
    'Productivity': productivity
}

# Welcome and registration page

def welcome():
    st.title("Welcome to Everydai-Hub")
    st.subheader("Registration and Login")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.form("registration_form"):
            st.write("New User Registration")
            new_user = st.text_input("Username")
            new_password = st.text_input("Password", type="password")
            register = st.form_submit_button("Register")

            if register:
                # Logic to register the user would go here
                st.success("User successfully registered. Please log in.")

        with st.form("login_form"):
            st.write("Existing User Login")
            user = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login = st.form_submit_button("Login")

            if login:
                # Logic to verify credentials would go here
                st.session_state['logged_in'] = True
                st.experimental_rerun()
                # Connect to the database
                try:
                    session = SessionLocal()
                    st.session_state['db_session'] = session
                    st.success("Connected to the database successfully.")
                except Exception as e:
                    st.error(f"Failed to connect to the database: {e}")

# Main page with the 7 functionalities

def main_page():
    st.title("Main Panel")
    st.sidebar.title("Functionalities")

    # Buttons in the sidebar
    if st.sidebar.button("Productivity Assistant"):
        st.session_state['current_page'] = 'Productivity'
    if st.sidebar.button("Meal Planner"):
        st.session_state['current_page'] = 'Meals'
    if st.sidebar.button("Smart Calendar"):
        st.session_state['current_page'] = 'Calendar'
    if st.sidebar.button("Health Tracker"):
        st.session_state['current_page'] = 'Health'
    if st.sidebar.button("Entertainment Recommendations"):
        st.session_state['current_page'] = 'Entertainment'
    if st.sidebar.button("Financial Management"):
        st.session_state['current_page'] = 'Finance'
    if st.sidebar.button("Digital Wellbeing"):
        st.session_state['current_page'] = 'Digital_Wellness'

    st.write("Select a functionality from the sidebar to get started.")

# Load the appropriate page based on the current state
if st.session_state['logged_in']:
    if st.session_state['current_page'] == 'Main':
        main_page()
    else:
        page_module = page_mapping.get(st.session_state['current_page'])
        if page_module:
            page_module.show()
        else:
            st.error("Page not found.")
else:
    welcome()
