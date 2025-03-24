import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def comidas():
    st.title("Meal Planner & Grocery Management")
    st.write("Capture your dietary preferences and pantry inventory to receive recipe recommendations and shopping lists.")

    # Form to capture data
    with st.form("comidas_form"):
        st.subheader("Dietary Preferences")

        # Dietary preferences
        preferences = st.multiselect(
            "Dietary Preferences",
            options = ["Vegan", "Vegetarian", "Gluten-Free", "Low-Carb", "Keto", "Dairy-Free"],
            help="Select your dietary preferences."
        )

        # Allergies or dietary restrictions
        allergies = st.text_input(
            "Allergies or dietary restrictions",
            help="Enter any Food allergy or restriction (e.g., nuts, shellfish)."
        )

        # Pantry Inventory
        st.subheader("Pantry Inventory")
        inventory = st.text_area(
            "Available ingredients (separated by commas)",
            help="List the ingredients you have in your pantry."
        )

        # Health Goals
        st.subheader("Health Goals")
        health_goals = st.selectbox(
            "Health Goals",
            options=["Lose Weight", "Maintain Weight", "Gain Muscle Mass", "Improve Overall Health"],
            help="Select your primary health goal."
        )

        # Number of Daily Meals
        num_meals = st.number_input(
            "Number of Daily Meals",
            min_value=1,
            max_value=6,
            value=3,
            help="Enter the number of meals you want to plan per day."
        )

        # Submit Button the form
        submit = st.form_submit_button("Generate Recommendations")

    # Process the data and display results
    if submit:
        st.success("Generated recommendations:")

        # Example data for visualizations
        missing_ingredients = ["Tomatoes", "Onion", "Chickpeas", "Olive Oil"]
        suggested_recipes = [
            {"Recipe": "Quinoa Salad", "Type": "Vegan"},
            {"Recipe": "Chickpea Curry", "Type": "Vegetarian"},
            {"Recipe": "Fruit Smoothie", "Type": "Gluten-Free"},
        ]
        df_recipes = pd.DataFrame(suggested_recipes)

        # Bar chart: Missing ingredients
        st.subheader("Missing Ingredients")
        fig, ax = plt.subplots()
        ax.bar(missing_ingredients, [5, 3, 4, 2], color='skyblue')
        ax.set_xlabel("Ingredients")
        ax.set_ylabel("Missing Amount")
        ax.set_title("Distribution of Missing Ingredients")
        st.pyplot(fig)

        # Pie chart: Proportion of recipes by type
        st.subheader("Proportion of Recipes by Type")
        recipe_type = df_recipes['Type'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(recipe_type, labels=recipe_type.index, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'lightblue'])
        ax.set_title("Distribution of Recipes by Type")
        st.pyplot(fig)

        # Table of suggested recipes
        st.subheader("Suggested Recipes")
        st.table(df_recipes)

        # Automatic shopping list
        st.subheader("Automatic Shopping List")
        st.write(f"- **Missing ingredients:** {', '.join(missing_ingredients)}")

# Run the food spreadsheet
if __name__ == "__main__":
    comidas()