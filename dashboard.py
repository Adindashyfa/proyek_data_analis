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

    # Ganti keterangan pada kolom yang sesuai
    season_mapping = {
        1.0: 'winter',
        2.0: 'summer',
        3.0: 'fall',
        4.0: 'spring'
    }
    data['season'] = data['season'].replace(season_mapping)

    weathersit_mapping = {
        1.0: 'clear, few clouds, partly cloudy',
        2.0: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds',
        3.0: 'Light Snow, Light Rain + Thunderstorm, Scattered clouds'
    }
    data['weathersit'] = data['weathersit'].replace(weathersit_mapping)

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

    # Add captions
    st.caption("Keterangan:")
    st.caption("Pada season: 1.0 = winter, 2.0 = summer, 3.0 = fall, 4.0 = spring")
    st.caption("Pada weathersit: 1.0 = clear, few clouds, partly cloudy, "
               "2.0 = Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, "
               "3.0 = Light Snow, Light Rain + Thunderstorm, Scattered clouds")
    st.caption("Pada holiday: 0.0 = non-holiday, 1.0 = holiday")

    # Select a column to display its distribution
    st.subheader('Select Column for Distribution Plot')
    column = st.selectbox('Choose a column', data.columns)

    # Plot histogram for the selected column
    st.subheader(f'Histogram of {column}')
    plt.figure(figsize=(10, 5))
    sns.histplot(data[column], bins=30, color='skyblue', kde=True)
    plt.title(f'Distribution of {column}', fontsize=16)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)

    # Use Streamlit to display the plot
    st.pyplot(plt)

    # Clear the figure after rendering
    plt.clf()

    # Export data as CSV
    if st.button('Export Data to CSV'):
        output_path = 'dashboard/all_data_output.csv'  # Menggunakan string sebagai jalur file output
        data.to_csv(output_path, index=False)
        st.write(f'Data has been exported to {output_path}')
else:
    st.write(f"File not found at {file_path}")