import streamlit as st
import pandas as pd
import plotly.express as px
st.title("DRIVING FORCES: Key Factors That Influence Car Sales and Pricing")
st.markdown("This dashboard is a Streamlit dashboard that can be used to analyze the driving forces behind car sales and pricing.")
# read the data from the csv file
df = pd.read_csv("vehicles_us.csv")
#show the data in the app
st.write(df)
st.subheader("Histogram: Analysis of Price")

# Price Histogram Analysis
fig_price = px.histogram(
    df, 
    x='price', 
    nbins=100, 
    range_x=(0, 100000),
    title='Price of vehicles: frequency distribution'
)
fig_price.update_layout(
    xaxis_title='Price',
    yaxis_title='Number of Vehicles'
)
st.plotly_chart(fig_price)

# Scatter Plot: Price vs Model Year
st.subheader('Scatter Plot: Price vs Model Year')
fig_scatter = px.scatter(
    df,
    x='model_year',
    y='price',
    title='Price vs Model Year',
    labels={'model_year': 'Model Year', 'price': 'Price (USD)'},
    color_discrete_sequence=['blue'],
    opacity=0.5
)
fig_scatter.update_layout(
    xaxis_title='Model Year',
    yaxis_title='Price (USD)',
    template='plotly_white'
)
st.plotly_chart(fig_scatter)

# Checkbox to Filter Data
filter_data = st.checkbox("Show only vehicles from 2015 onwards")

# Apply filter if the checkbox is checked
if filter_data:
    df = df[df['model_year'] >= 2015]

# Histogram: Price Distribution
st.subheader('Histogram of Vehicle Prices')
fig_price = px.histogram(
    df, 
    x='price', 
    nbins=100, 
    range_x=(0, 100000),
    title='Price of Vehicles: Frequency Distribution'
)
fig_price.update_layout(
    xaxis_title='Price',
    yaxis_title='Number of Vehicles'
)
st.plotly_chart(fig_price, key='price_histogram')  # Added unique key

# Scatter Plot: Price vs Model Year
st.subheader('Scatter Plot: Price vs Model Year')
fig_scatter = px.scatter(
    df,
    x='model_year',
    y='price',
    title='Price vs Model Year',
    labels={'model_year': 'Model Year', 'price': 'Price (USD)'},
    color_discrete_sequence=['blue'],
    opacity=0.5
)
fig_scatter.update_layout(
    xaxis_title='Model Year',
    yaxis_title='Price (USD)',
    template='plotly_white'
)
st.plotly_chart(fig_scatter, key='scatter_plot')