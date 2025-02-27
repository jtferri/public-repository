import streamlit as st
import os

# Display title of webpage
st.title('Sankey Graphic')

# Load the HTML file
html_file_path = r"/Users/jacquelineferri/public-repository/sankey.html"

# Check if the file exists before displaying it
if os.path.exists(html_file_path):
    st.components.v1.html(open(html_file_path).read(), height=600)
else:
    st.error("Plot HTML file not found!")