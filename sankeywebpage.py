import streamlit as st

import streamlit.components.v1 as components

# Set the title of the Streamlit app
st.title("Sankey Diagram Viewer")

# Path to the HTML file
html_file_path = "/Users/jacquelineferri/public-repository/sankey.html"

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Display the HTML file in the Streamlit app
components.html(html_content, height=800)