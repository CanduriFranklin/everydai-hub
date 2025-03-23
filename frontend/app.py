import streamlit as st
import os

# Page configuration
st.set_page_config(page_title="Everydai-Hub", layout="wide")

# Session state to handle authentication and navigation
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Welcome'

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
        page_module = __import__(f"pages.{st.session_state['current_page'].lower()}", fromlist=['show'])
        page_module.show()
else:
    welcome()
