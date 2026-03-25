"""
Script: App & BI

Description:
This code reads data from BigQuery to create a Streamlit dashboard showing:  
- The total number of users in the database
- Number of users per location
- List of all users

EDEM. Master Big Data & Cloud 2025/2026
Professor: Javi Briones & Adriana Campos
"""

""" Import Libraries """
import streamlit as st
from google.cloud import bigquery
import pandas as pd

# Configure BigQuery client
client = bigquery.Client()

# Set Streamlit page configuration
st.set_page_config(page_title="Dashboard Clients", layout="wide")
st.title("KPIs Clients Dashboard")

# Query to count distinct users
query_users = """
SELECT COUNT(DISTINCT User_ID) AS total_users
FROM `<PROJECT_ID>.<DATASET>.<TABLE_NAME_CLIENTS>`
"""

# Query to count users per location
query_location = """
SELECT Location, COUNT(User_ID) AS users_count
FROM `<PROJECT_ID>.<DATASET>.<TABLE_NAME_CLIENTS>`
GROUP BY Location
ORDER BY users_count DESC
"""

# Query to get all users
query_all_users = """
SELECT User_ID, First_Name, Last_Name, Location
FROM `<PROJECT_ID>.<DATASET>.<TABLE_NAME_CLIENTS>`
ORDER BY User_ID
"""

# Execute queries
users_df = client.query(query_users).to_dataframe()
location_df = client.query(query_location).to_dataframe()
all_users_df = client.query(query_all_users).to_dataframe()

# Display KPIs
st.metric("Total Users", users_df['total_users'][0])

# Display users per location
st.subheader("Users per Location")
st.bar_chart(location_df.set_index('Location'))

# Display full table of users
st.subheader("All Users")
st.dataframe(all_users_df)
