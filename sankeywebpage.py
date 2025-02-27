import streamlit as st
import os

# Display title of webpage
st.title('Sankey Graphic')

# Load the HTML file
html_file_path = r"/Users/jacquelineferri/public-repository/sankey.html"

st.components.v1.html(f"""
    <div id="sankey"></div>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script>
        var plotData = {plot_data};
        Plotly.newPlot('sankey', plotData.data, plotData.layout);
    </script>
""", height=600)