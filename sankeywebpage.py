import streamlit as st
import requests
import streamlit.components.v1 as components

# Set the title of the Streamlit app
st.title("Sankey Diagram Viewer")

# URL to the HTML file in the GitHub repository
html_file_path = "https://github.com/jtferri/public-repository"

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as html_file:
	html_content = html_file.read()

# Display the HTML file in the Streamlit app
components.html(html_content, height=2000, width=2000)
