import streamlit as st
import os

# Display title of webpage
st.title('Sankey Graphic')

# Path to the HTML file
html_file_path = r"/Users/jacquelineferri/public-repository/sankey.html"

# Check if the file exists before displaying it
if os.path.exists(html_file_path):
    # Open the HTML file and read its contents
    with open(html_file_path, 'r') as file:
        plot_html = file.read()
    
    # Display the HTML content in Streamlit
    st.components.v1.html(plot_html, height=600)  # Adjust the height as needed
else:
    # Show an error message if the file is not found
    st.error("HTML file not found!")