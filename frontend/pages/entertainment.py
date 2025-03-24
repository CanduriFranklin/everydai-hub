import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

def show():
    entertainment()

def entertainment():
    st.title("Entertainment Recommendations")
    st.write("Receive personalized movie, TV, book, or music recommendations based on your mood and preferences.")

# Form to capture data
with st.form("entertainment_form"):
    st.subheader("Entertainment Preferences")

# Mood
mood_mood = st.selectbox(
    "Mood",
    options=["Happy", "Sad", "Relaxed", "Energetic"],
    help="Select your current mood."
)

# Entertainment Preferences
preferences = st.text_area(
    "Preferences (e.g., movie genre, favorite authors)",
    help="Describe your entertainment preferences."
)

# Preferred Time
preferred_time = st.selectbox(
    "Preferred time",
    options=["Morning", "Afternoon", "Evening"],
    help="Select your preferred time to enjoy entertainment."
)

# Entertainment type
entertainment_type = st.multiselect(
    "Entertainment type",
    options=["Movies", "TV Shows", "Books", "Music"],
    help="Select your preferred type of entertainment."
)

# Button to submit the form
submit = st.form_submit_button("Generate Recommendations")

# Process the data and display results
if submit:
    # Make API call to backend
    response = requests.post("http://backend:8000/api/entertainment", json={
        "preferences": preferences.split(",")
    })
    if response.status_code == 200:
        recommendations = response.json().get("recommendations", [])
        st.success("Generated recommendations:")
        for recommendation in recommendations:
            st.write(f"- {recommendation}")
    else:
        st.error("Failed to generate recommendations. Please try again.")

# Example data for visualizations
recommendations = {
    "Type": ["Movies", "TV Shows", "Books", "Music"],
    "Recommendation": [
        f"Movie: 'Spirited Away' (Mood: {mood_mood})",
        f"Series: 'Stranger Things' (Time: {preferred_time})",
        f"Book: 'One Hundred Years of Solitude' (Preferences: {preferences})",
        f"Music: Relaxing Jazz Playlist (Mood: {mood_mood})"
    ]
}
df_recommendations = pd.DataFrame(recommendations)

# Bar Chart: Distribution of Recommendations by Type
st.subheader("Distribution of Recommendations by Type")
type_counts = df_recommendations['Type'].value_counts()
fig, ax = plt.subplots()
ax.bar(type_counts.index, type_counts.values, color=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
ax.set_xlabel("Type of Entertainment")
ax.set_ylabel("Number of Recommendations")
ax.set_title("Distribution of Recommendations by Type")
st.pyplot(fig)

# Pie chart: Proportion of recommendations by mood
st.subheader("Proportion of Recommendations by Mood")
estado_counts = df_recommendations['Recommendation'].apply(lambda x: mood_mood if mood_mood in x else "Other").value_counts()
fig, ax = plt.subplots()
ax.pie(estado_counts, labels=estado_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'lightblue', 'gold'])
ax.set_title("Proportion of Recommendations by Mood")
st.pyplot(fig)

# Recommendations table
st.subheader("Personalized Recommendations")
st.table(df_recommendations)

# Run the entertainment sheet
if __name__ == "__main__":
    show()