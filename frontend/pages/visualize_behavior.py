import streamlit as st
import pandas as pd
import sqlalchemy as db

# Database connection
engine = db.create_engine('sqlite:///path_to_your_database.db')
connection = engine.connect()
metadata = db.MetaData()
app_behavior = db.Table('app_behavior', metadata, autoload=True, autoload_with=engine)

# Streamlit app
st.title('Application Behavior Logs')

# Query the database
query = db.select([app_behavior])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

# Convert to DataFrame
columns = result_set[0].keys()
df = pd.DataFrame(result_set, columns=columns)

# Display the DataFrame
st.write(df)

# Display the DataFrame with real-time updates
st.dataframe(df)

# Display charts
st.line_chart(df.set_index('timestamp'))
