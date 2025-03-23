import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def health():
	st.title("Health and Wellness Tracker")
	st.write("Capture your health habits and receive personalized insights to improve your well-being.")

	# Form to capture data
	with st.form("health_form"):
		st.subheader("Health Data")

		# Hours of sleep
		hours_sleep = st.number_input(
			"Hours of sleep",
			min_value=0,
			max_value=24,
			help="Enter the number of hours you slept last night."
		)

		# Minutes of daily exercise
		exercise = st.number_input(
			"Minutes of daily exercise",
			min_value=0,
			max_value=240,
			help="Enter the minutes of exercise you performed today."
		)

		# Habits Nutritional Information
		st.subheader("Eating Habits")
		balanced_meals = st.selectbox(
			"Did you have balanced meals today?",
			options=["Yes", "No"],
			help="Select if you had balanced meals today."
		)
		water_consumption = st.number_input(
			"Glasses of water consumed",
			min_value=0,
			max_value=20,
			help="Enter the number of glasses of water you consumed today."
		)

		# Health Goals
		st.subheader("Health Goals")
		health_goals = st.selectbox(
			"Health Goals",
			options=["Lose Weight", "Improve Fitness", "Maintain Overall Health"],
			help="Select your main health goal."
		)

		# Button to submit the form
		submit = st.form_submit_button("Generate Insights")

	# Process the data and display results
	if submit:
		st.success("Insights generated:")

		# Example data for visualizations
		health_data = {
			"Category": ["Sleep", "Exercise", "Water"],
			"Value": [hours_sleep, exercise, water_consumption]
		}
		health_df = pd.DataFrame(health_data)

		# Bar chart: Health habits summary
		st.subheader("Health Habits Summary")
		fig, ax = plt.subplots()
		ax.bar(health_df['Category'], health_df['Value'], color=['skyblue', 'lightgreen', 'lightcoral'])
		ax.set_xlabel("Category")
		ax.set_ylabel("Value")
		ax.set_title("Health Habits Summary")
		st.pyplot(fig)

		# Pie chart: Proportion of healthy habits
		st.subheader("Proportion of Healthy Habits")
		healthy_habits = [hours_sleep >= 7, exercise >= 30, water_consumption >= 8]
		labels = ["Adequate Sleep", "Sufficient Exercise", "Sufficient Water"]
		fig, ax = plt.subplots()
		ax.pie(healthy_habits, labels=labels, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'lightblue'])
		ax.set_title("Proportion of Healthy Habits")
		st.pyplot(fig)

		# Personalized recommendations
		st.subheader("Personalized Recommendations")
		if hours_sleep < 7:
			st.write("- **Sleep:** Try to sleep at least 7 hours each night.")
		if exercise < 30:
			st.write("- **Exercise:** Get at least 30 minutes of exercise daily.")
		if water_consumption < 8:
			st.write("- **Water:** Drink at least 8 glasses of water a day.")
		if balanced_meals == "No":
			st.write("- **Nutrition:** Include balanced meals in your diet.")

# Run the health sheet
if __name__ == "__main__":
	health()