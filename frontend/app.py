import streamlit as st
from pages import calendar, digital_wellness, entertainment, finance, health, meals, productivity

st.sidebar.title("Everydai-Hub")
page = st.sidebar.selectbox("Select a page", ["Calendar", "Digital Wellness", "Entertainment", "Finance", "Health", "Meals", "Productivity"])

if page == "Calendar":
    calendar.show()
elif page == "Digital Wellness":
    digital_wellness.show()
elif page == "Entertainment":
    entertainment.show()
elif page == "Finance":
    finance.show()
elif page == "Health":
    health.show()
elif page == "Meals":
    meals.show()
elif page == "Productivity":
    productivity.show()
