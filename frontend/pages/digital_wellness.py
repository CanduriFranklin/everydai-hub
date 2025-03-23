import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def digital_wellbeing():
	st.title("Digital Wellbeing")
	st.write("Monitor your digital usage and receive recommendations to promote healthy digital habits.")

# Form to capture data
with st.form("digital_wellbeing_form"):
	st.subheader("Digital Usage")

# Time on social media
social_time = st.number_input(
	"Time on social media (hours/day)",
	min_value=0,
	max_value=24,
	help="Enter the time you spend on social media each day."
)

# Time on productivity apps
productivity_time = st.number_input(
	"Time on productivity apps (hours/day)",
	min_value=0,
	max_value=24,
	help="Enter the time you spend on productivity apps every day."
)

# Notification Frequency
notification_frequency = st.selectbox(
	"Notification Frequency",
	options=["High", "Medium", "Low"],
	help="Select the frequency of notifications you receive."
)

# Digital Wellbeing Goals
st.subheader("Digital Wellbeing Goals")
wellbeing_goals = st.multiselect(
	"Digital Wellbeing Goals",
	options=["Reduce time on social media", "Limit notifications", "Increase time on productivity"],
	help="Select your digital wellbeing goals."
)

# Button to submit the form
submit = st.form_submit_button("Generate Recommendations")

# Process the data and display results
if submit:
	st.success("Recommendations generated:")

# Example data for visualizations
digital_usage_data = {
	"Activity": ["Social Media", "Productivity"],
	"Time (hours)": [social_time, productivity_time]
}
df_digital_use = pd.DataFrame(digital_usage_data)

# Bar chart: Distribution of digital time
st.subheader("Distribution of Digital Time")
fig, ax = plt.subplots()
ax.bar(df_digital_use['Activity'], df_digital_use['Time (hours)'], color=['skyblue', 'lightgreen'])
ax.set_xlabel("Activity")
ax.set_ylabel("Time (hours)")
ax.set_title("Distribution of Digital Time")
st.pyplot(fig)

# Pie chart: Proportion of digital use
st.subheader("Proportion of Digital Use")
fig, ax = plt.subplots()
ax.pie(df_digital_use['Time (hours)'], labels=df_digital_use['Activity'], autopct='%1.1f%%', colors=['lightcoral', 'lightblue'])
ax.set_title("Proportion of Digital Use")
st.pyplot(fig)

# Personalized Recommendations
st.subheader("Personalized Recommendations")
if social_time > 2:
	st.write("- **Social Media:** Limit your time on social media to 2 hours a day.")
if productivity_time < 4:
	st.write("- **Productivity:** Increase your time on productivity apps to at least 4 hours a day.")
if notification_frequency == "High":
	st.write("- **Notifications:** Reduce the frequency of notifications to minimize distractions.")
if "Reduce time on social media" in wellbeing_goals:
	st.write("- **Goal:** Set reminders to take breaks from social media.")
if "Limit notifications" in wellbeing_goals:
	st.write("- **Goal:** Turn off non-essential notifications on your device.")

# Run the Digital Wellness Sheet
if __name__ == "__main__":
	digital_wellbeing()