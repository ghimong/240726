import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'daily_temp.csv'  # Update with the correct file path
data = pd.read_csv(file_path)

# Clean the data
data.columns = data.columns.str.strip()
data['날짜'] = data['날짜'].str.strip()
data['날짜'] = pd.to_datetime(data['날짜'], format='%Y-%m-%d')
data['Year'] = data['날짜'].dt.year

# Calculate the average minimum and maximum temperatures by year
avg_temps_by_year = data.groupby('Year').agg({'최저기온(℃)': 'mean', '최고기온(℃)': 'mean'}).reset_index()
avg_temps_by_year.columns = ['Year', 'Avg Min Temp (℃)', 'Avg Max Temp (℃)']

# Define a function to create line graphsdef create_line_graph(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Year'], data['Avg Min Temp (℃)'], label='Avg Min Temp (℃)', marker='o')
    plt.plot(data['Year'], data['Avg Max Temp (℃)'], label='Avg Max Temp (℃)', marker='o')
    plt.title('Average Minimum and Maximum Temperature by Year')
    plt.xlabel('Year')
    plt.ylabel('Temperature (℃)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Define a function to create bar graphsdef create_bar_graph(data):
    plt.figure(figsize=(12, 6))
    plt.bar(data['Year'] - 0.2, data['Avg Min Temp (℃)'], width=0.4, label='Avg Min Temp (℃)')
    plt.bar(data['Year'] + 0.2, data['Avg Max Temp (℃)'], width=0.4, label='Avg Max Temp (℃)')
    plt.title('Average Minimum and Maximum Temperature by Year')
    plt.xlabel('Year')
    plt.ylabel('Temperature (℃)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Streamlit app
st.title('Temperature Trends by Year')

# Radio button to choose the type of graph
graph_type = st.radio('Select Graph Type', ('Line Graph', 'Bar Graph'))

# Display the chosen graphif graph_type == 'Line Graph':
    create_line_graph(avg_temps_by_year)
else:
    create_bar_graph(avg_temps_by_year)
