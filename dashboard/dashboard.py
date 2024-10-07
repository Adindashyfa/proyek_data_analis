import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Load the data from the CSV file
file_path = 'dashboard/all_data.csv'

# Check if the file exists
if os.path.exists(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    season_mapping = {
        1.0: 'spring',
        2.0: 'summer',
        3.0: 'fall',
        4.0: 'winter'
    }
    data['season'] = data['season'].replace(season_mapping)

    weather_mapping = {
        1: 'Clear, Few clouds, Partly cloudy',
        2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds',
        3: 'Light Snow, Light Rain + Thunderstorm, Scattered clouds',
        4: 'Heavy Rain + Ice Pellets, Thunderstorm + Mist, Snow + Fog'
    }
    data['weather_condition'] = data['weathersit'].map(weather_mapping)

    holiday_mapping = {
        0.0: 'non-holiday',
        1.0: 'holiday'
    }
    data['holiday'] = data['holiday'].replace(holiday_mapping)

    # Streamlit Dashboard
    st.title('Bike Sharing Data Dashboard')

    # Show the first 5 rows of the dataset
    st.subheader('Dataset Preview')
    st.write(data.head())

    # Display basic statistics
    st.subheader('Basic Data Statistics')
    st.write(data.describe())

    # Select a column to display its total rentals
    st.subheader('Select Column for Total Rentals Plot')
    column = st.selectbox('Choose a column', ['season', 'weathersit', 'holiday'])

    # Calculate total rentals based on the selected column
    total_rentals = data.groupby(column)['cnt'].sum().reset_index()

    st.write("Keterangan Pada Weathersit:")
    st.write("1 : Clear, Few clouds, Partly cloudy")
    st.write("2 : Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds")
    st.write("3 : Light Snow, Light Rain + Thunderstorm, Scattered clouds")

    # Plot bar chart for the selected column
    st.subheader(f'Total Rentals by {column.capitalize()}')
    plt.figure(figsize=(10, 5))
    sns.barplot(x=column, y='cnt', data=total_rentals, palette='Blues_d')
    plt.title(f'Total Rentals by {column.capitalize()}', fontsize=16)
    plt.xlabel(column.capitalize(), fontsize=12)
    plt.ylabel('Total Rentals', fontsize=12)

    # Use Streamlit to display the plot
    st.pyplot(plt)

    # Clear the figure after rendering
    plt.clf()

    # Export data as CSV
    if st.button('Export Data to CSV'):
        output_path = 'dashboard/all_data.csv'
        data.to_csv(output_path, index=False)
        st.write(f'Data has been exported to {output_path}')
else:
    st.write(f"File not found at {file_path}")