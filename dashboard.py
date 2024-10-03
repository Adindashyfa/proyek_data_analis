import pandas as pd
import streamlit as st
import os

# Load the data from the CSV file
file_path = 'C:/Users/hp/ProyekAnalisisData/all_data.csv'

# Check if the file exists
if os.path.exists(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Streamlit Dashboard
    st.title('Bike Sharing Data Dashboard')

    # Show the first 5 rows of the dataset
    st.subheader('Dataset Preview')
    st.write(data.head())

    # Display basic statistics
    st.subheader('Basic Data Statistics')
    st.write(data.describe())

    # Select a column to display its distribution
    st.subheader('Select Column for Distribution Plot')
    column = st.selectbox('Choose a column', data.columns)

    # Plot histogram for the selected column
    st.subheader(f'Histogram of {column}')
    st.bar_chart(data[column])

    # Export data as CSV
    if st.button('Export Data to CSV'):
        output_path = 'C:/Users/hp/ProyekAnalisisData/all_data_output.csv'
        data.to_csv(output_path, index=False)
        st.write(f'Data has been exported to {output_path}')
else:
    st.write(f"File not found at {file_path}")
