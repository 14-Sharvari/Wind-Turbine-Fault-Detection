import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
file_path = "C:/Users/sharv/Downloads/wind_data.csv"
df = pd.read_csv(file_path)

# Streamlit app
st.title("Real-Time Weather Monitoring Dashboard")

# Summary statistics
st.sidebar.header("Data Summary")
st.sidebar.write(df.describe())

# Select location
location = st.selectbox("Select a Location:", df["Location"].unique())

# Filter data for the selected location
filtered_data = df[df["Location"] == location]

# Line chart for wind speed
st.subheader(f"Wind Speed Over Time for {location}")
fig = px.line(filtered_data, x="Timestamp", y="Wind Speed (m/s)", title="Wind Speed Over Time")
st.plotly_chart(fig)

# Temperature trend
st.subheader(f"Temperature Over Time for {location}")
fig_temp = px.line(filtered_data, x="Timestamp", y="Temperature (°C)", title="Temperature Over Time")
st.plotly_chart(fig_temp)

# Weather description
st.subheader(f"Weather Description Distribution for {location}")
weather_counts = filtered_data["Weather Description"].value_counts()
st.bar_chart(weather_counts)

# Wind power output estimation
st.subheader(f"Estimated Power Output Over Time for {location}")
fig_power = px.line(filtered_data, x="Timestamp", y="Estimated Power Output (W)", title="Power Output Over Time")
st.plotly_chart(fig_power)