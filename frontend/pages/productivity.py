import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def productivity():
    st.title("Custom Productivity Wizard")
    st.write("Capture your work habits and receive personalized recommendations to improve your productivity.")

# Form to capture data
with st.form("productivity_form"):
    st.subheader("Input Data")

# Daily work hours
work_hours = st.number_input(
    "Daily work hours",
    min_value=1,
    max_value=24,
    help="Enter the number of hours you work per day."
)

# To-do tasks
to_do_tasks = st.text_area(
    "To-do tasks (comma-separated)",
    help="List your to-do tasks, separated by commas."
)

# Break preferences
st.subheader("Break Preferences")
break_duration = st.number_input(
    "Duration of each break (minutes)",
    min_value=5,
    max_value=60,
    value=15,
    help="Duration in minutes of each break."
)
break_frequency = st.number_input(
    "Break frequency (every X hours)",
    min_value=1,
    max_value=8,
    value=2,
    help="How many hours do you prefer to take a break?"
)

# Daily/Weekly Goals
st.subheader("Goals")
daily_goals = st.text_area(
    "Daily goals (comma-separated)",
    help="List your daily goals, separated by commas."
)
weekly_goals = st.text_area(
    "Weekly goals (comma-separated)",
    help="List your weekly goals, separated by commas."
)

# Button to submit the form
submit = st.form_submit_button("Generate Recommendations")

# Process the data and display results
if submit:
    st.success("Generated Recommendations:")

# Example data for visualizations
tasks = to_do_tasks.split(",")
priorities = ["High", "Medium", "Low"]
priority_distribution = [len(tasks) // 3, len(tasks) // 3, len(tasks) - 2 * (len(tasks) // 3)]

# Bar chart: Distribution of work and rest hours
st.subheader("Distribution of Work and Rest Hours")
fig, ax = plt.subplots()
ax.bar(["Work", "Rest"], [work_hours, break_duration * (work_hours // break_frequency)], color=['skyblue', 'lightgreen'])
ax.set_xlabel("Activity")
ax.set_ylabel("Hours/Minutes")
ax.set_title("Distribution of Work and Break Hours")
st.pyplot(fig)

# Pie chart: Proportion of tasks by priority
st.subheader("Proportion of Tasks by Priority")
fig, ax = plt.subplots()
ax.pie(priority_distribution, labels=priorities, autopct='%1.1f%%', colors=['lightcoral', 'lightblue', 'lightgreen'])
ax.set_title("Distribution of Tasks by Priority")
st.pyplot(fig)

# Pending tasks table
st.subheader("Pending Tasks")
df_tasks = pd.DataFrame({
    "Task": tasks,
    "Priority": priorities[:len(tasks)]
})
st.table(df_tasks)

# Productivity Recommendations
st.subheader("Productivity Recommendations")
st.write(f"- **Prioritize tasks:** {tasks[0]}, {tasks[1]}")
st.write(f"- **Focus Block:** Work in blocks of {break_frequency} hours with breaks of {break_duration} minutes.")
st.write(f"- **Daily Goals:** Focus on completing {daily_goals.split(',')[0]} today.")
st.write(f"- **Weekly Goals:** Plan time for {weekly_goals.split(',')[0]} this week.")

# Run the productivity spreadsheet
if __name__ == "__main__":
    productivity()