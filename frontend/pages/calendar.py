import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests

def calendar():
	st.title("Smart Calendar")
	st.write("Synchronize your events, tasks, and commitments, and receive suggestions for optimal schedules.")

	# Form to capture data
	with st.form("calendario_form"):
		st.subheader("Events and Tasks")

		# Events and tasks
		events = st.text_area(
			"Events and tasks (format: name, date YYYY-MM-DD, time HH:MM, priority)",
			help="Enter your events and tasks in the format: name, date, time, priority (high, medium, low)."
		)

		# Estimated duration of each event
		event_duration = st.number_input(
			"Estimated duration of each event (minutes)",
			min_value=15,
			max_value=240,
			value=60,
			help="Enter the estimated duration of each event in minutes."
		)

		# Schedule Preferences
		st.subheader("Schedule Preferences")
		schedule_preferences = st.multiselect(
			"Schedule Preferences",
			options=["Morning", "Afternoon", "Evening"],
			help="Select your preferred times for important events."
		)

		# Button to submit the form
		submit = st.form_submit_button("Generate Agenda")

	# Process the data and display results
	if submit:
		# Make API call to backend
		response = requests.post("http://backend:8000/api/calendar", json={
			"events": events,
			"event_duration": event_duration,
			"schedule_preferences": schedule_preferences
		})
		if response.status_code == 200:
			agenda = response.json().get("agenda", [])
			st.success("Generated Agenda:")
			for item in agenda:
				st.write(f"- {item}")
		else:
			st.error("Failed to generate agenda. Please try again.")

		# Process entered events
		events_list = [event.strip() for event in events.split("\n") if event.strip()]
		events_data = []
		for event in events_list:
			name, date, time, priority = event.split(",")
			events_data.append({
				"Name": name.strip(),
				"Date": datetime.strptime(date.strip(), "%Y-%m-%d"),
				"Time": time.strip(),
				"Priority": priority.strip(),
				"Duration (min)": event_duration
			})

		# Create a DataFrame of events
		df_events = pd.DataFrame(events_data)

		# Bar chart: Distribution of events by priority
		st.subheader("Distribution of Events by Priority")
		priority_counts = df_events['Priority'].value_counts()
		fig, ax = plt.subplots()
		ax.bar(priority_counts.index, priority_counts.values, color=['lightcoral', 'lightblue', 'lightgreen'])
		ax.set_xlabel("Priority")
		ax.set_ylabel("Number of Events")
		ax.set_title("Distribution of Events by Priority")
		st.pyplot(fig)

		# Pie chart: Proportion of events by schedule
		st.subheader("Proportion of Events by Schedule")
		schedules = ["Morning" if int(event['Schedule'].split(":")[0]) < 12 else "Afternoon" if int(event['Schedule'].split(":")[0]) < 18 else "Night" for event in events_data]
		schedule_counts = pd.Series(schedules).value_counts()
		fig, ax = plt.subplots()
		ax.pie(schedule_counts, labels=schedule_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'lightblue'])
		ax.set_title("Event Distribution by Schedule")
		st.pyplot(fig)

		# Events table
		st.subheader("Scheduled Events")
		st.table(df_events)

		# Optimal schedule suggestions
		st.subheader("Optimal Schedule Suggestions")
		st.write(f"- **Preferred schedule:** {schedule_preferences[0] if schedule_preferences else 'Not specified'}")
		st.write(f"- **Most important event:** {df_events.loc[df_events['Priority'] == 'high', 'Name'].values[0]}")
		st.write(f"- **Total event duration:** {df_events['Duration (min)'].sum()} minutes")

# Run the calendar sheet
if __name__ == "__main__":
	calendar()