import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def finanzas():
	st.title("Personalized Financial Management")
	st.write("Capture your income and expenses, and receive recommendations to improve your financial situation.")

# Form to capture data
with st.form("finanzas_form"):
	st.subheader("Financial Data")

# Monthly income
income = st.number_input(
	"Monthly income",
	min_value=0,
	help="Enter your monthly income."
)

# Monthly expenses
st.subheader("Monthly Expenses")
expenses = st.text_area(
	"Monthly expenses (format: category, amount)",
	help="Enter your monthly expenses in the format: category, amount (e.g., Food, 200)."
)

# Financial goals
st.subheader("Financial Goals")
financial_goals = st.selectbox(
	"Financial Goals",
	options=["Save for Vacation", "Pay Off Debt", "Invest", "Maintain Budget"],
	help="Select your main financial goal."
)

# Button to submit the form
submit = st.form_submit_button("Generate Recommendations")

# Process the data and display results
if submit:
	st.success("Generated Recommendations:")

# Process entered expenses
gastos_lista = [gasto.strip() for gasto in expenses.split("\n") if gasto.strip()]
gastos_data = []
for gasto in gastos_lista:
	categoria, cantidad = gasto.split(",")
	gastos_data.append({
		"Category": categoria.strip(),
		"Amount": float(cantidad.strip())
	})

# Create an expense data frame
df_expenses = pd.DataFrame(gastos_data)

# Calculate total expenses and remaining balance
total_expenses = df_expenses['Amount'].sum()
remaining_balance = income - total_expenses

# Bar chart: Distribution of expenses by category
st.subheader("Distribution of Expenses by Category")
fig, ax = plt.subplots()
ax.bar(df_expenses['Category'], df_expenses['Amount'], color=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
ax.set_xlabel("Category")
ax.set_ylabel("Amount ($)")
ax.set_title("Distribution of Expenses by Category")
st.pyplot(fig)

# Pie chart: Proportion of income and expenses
st.subheader("Income to Expense Ratio")
labels = ["Income", "Expenses"]
sizes = [income, total_expenses]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
ax.set_title("Income to Expense Ratio")
st.pyplot(fig)

# Expense table
st.subheader("Expense Summary")
st.table(df_expenses)

# Personalized recommendations
st.subheader("Personalized Recommendations")
if remaining_balance < 0:
	st.write("- **Attention:** Your expenses exceed your income. Consider cutting back on non-essential spending.")
else:
	st.write(f"- **Remaining balance:** ${remaining_balance:.2f}")
	st.write(f"- **Suggested savings:** ${remaining_balance * 0.2:.2f} (20% of your remaining balance)")
if financial_goals == "Save for Vacation":
	st.write("- **Tip:** Allocate a fixed monthly amount for your vacation fund.")
elif financial_goals == "Pay Off Debt":
	st.write("- **Tip:** Prioritize paying off higher-interest debts.")

# Run the finance spreadsheet
if __name__ == "__main__":
	finanzas()