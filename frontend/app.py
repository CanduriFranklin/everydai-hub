import streamlit as st

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
                st.session_state['current_page'] = 'Main'
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
        st.session_state['current_page'] = 'Wellbeing'

    st.write("Select a functionality from the sidebar to get started.")

# Functionality 1: Personalized Productivity Assistant

def productivity():
    st.title("Personalized Productivity Assistant")
    st.write("Capture your work habits and receive personalized recommendations.")

    with st.form("productivity_form"):
        work_hours = st.number_input("Daily work hours", min_value=1, max_value=24)
        pending_tasks = st.text_area("Pending tasks (separated by commas)")
        submit = st.form_submit_button("Generate Recommendations")

        if submit:
            # Simulation of recommendations (real logic would go here)
            st.success("Recommendations generated:")
            st.write("- Prioritize tasks: Task 1, Task 2")
            st.write("- Focus block: 2 hours in the morning")
            st.write("- Breaks: 5 minutes every 25 minutes")

# Functionality 2: Meal Planner and Grocery Management

def meals():
    st.title("Meal Planner and Grocery Management")
    st.write("Capture your preferences and receive recipe suggestions.")

    with st.form("meals_form"):
        preferences = st.text_input("Dietary preferences (e.g., vegan, gluten-free)")
        inventory = st.text_area("Pantry inventory (available ingredients)")
        submit = st.form_submit_button("Generate Recipes")

        if submit:
            # Simulation of recommendations (real logic would go here)
            st.success("Suggested recipes:")
            st.write("- Quinoa salad with vegetables")
            st.write("- Chickpea curry")
            st.write("- Shopping list: tomatoes, onion, chickpeas")

# Functionality 3: Smart Calendar

def calendar():
    st.title("Smart Calendar")
    st.write("Sync your events and receive schedule suggestions.")

    with st.form("calendar_form"):
        events = st.text_area("Events and tasks (format: event, date, time)")
        submit = st.form_submit_button("Optimize Schedule")

        if submit:
            # Simulation of recommendations (real logic would go here)
            st.success("Optimized schedule:")
            st.write("- Work meeting: 10:00 - 11:00")
            st.write("- Important task: 14:00 - 15:00")
            st.write("- Break: 16:00 - 16:15")

# Functionality 4: Health and Wellness Tracker

def health():
    st.title("Health and Wellness Tracker")
    st.write("Capture your health habits and receive personalized insights.")

    with st.form("health_form"):
        sleep_hours = st.number_input("Sleep hours", min_value=0, max_value=24)
        exercise = st.text_input("Daily exercise minutes")
        submit = st.form_submit_button("Generate Insights")

        if submit:
            # Simulation of recommendations (real logic would go here)
            st.success("Insights generated:")
            st.write("- Improve your sleep: Try to sleep 8 hours")
            st.write("- Exercise: Increase to 30 minutes daily")

# Functionality 5: Entertainment Recommendations

def entertainment():
    st.title("Entertainment Recommendations")
    st.write("Capture your preferences and receive personalized recommendations.")

    with st.form("entertainment_form"):
        mood = st.selectbox("Mood", ["Happy", "Sad", "Relaxed", "Energetic"])
        preferences = st.text_area("Preferences (e.g., movie genres, favorite authors)")
        submit = st.form_submit_button("Generate Recommendations")

        if submit:
            # Simulation of recommendations (real logic would go here)
            st.success("Recommendations generated:")
            st.write("- Movie: 'Spirited Away'")
            st.write("- Book: 'One Hundred Years of Solitude'")
            st.write("- Music: Relaxing jazz playlist")

# Functionality 6: Personalized Financial Management

def finance():
    st.title("Personalized Financial Management")
    st.write("Capture your expenses and receive saving tips.")

    with st.form("finance_form"):
        income = st.number_input("Monthly income", min_value=0)
        expenses = st.text_area("Monthly expenses (category, amount)")
        submit = st.form_submit_button("Generate Tips")

        if submit:
            # Simulation of recommendations (real logic would go here)
            st.success("Tips generated:")
            st.write("- Reduce food expenses: Save $200 per month")
            st.write("- Suggested budget: $500 for leisure")

# Functionality 7: Digital Wellbeing

def wellbeing():
    st.title("Digital Wellbeing")
    st.write("Capture your digital usage and receive recommendations for healthy habits.")

    with st.form("wellbeing_form"):
        social_media_time = st.number_input("Time on social media (hours/day)", min_value=0)
        notifications = st.selectbox("Notification frequency", ["High", "Medium", "Low"])
        submit = st.form_submit_button("Generate Recommendations")

        if submit:
            # Simulation of recommendations (real logic would go here)
            st.success("Recommendations generated:")
            st.write("- Limit social media time to 1 hour daily")
            st.write("- Disable non-essential notifications")

# Navigation between pages
if st.session_state['logged_in']:
    if st.session_state['current_page'] == 'Main':
        main_page()
    elif st.session_state['current_page'] == 'Productivity':
        productivity()
    elif st.session_state['current_page'] == 'Meals':
        meals()
    elif st.session_state['current_page'] == 'Calendar':
        calendar()
    elif st.session_state['current_page'] == 'Health':
        health()
    elif st.session_state['current_page'] == 'Entertainment':
        entertainment()
    elif st.session_state['current_page'] == 'Finance':
        finance()
    elif st.session_state['current_page'] == 'Wellbeing':
        wellbeing()
else:
    welcome()
