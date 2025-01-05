import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('vehicles_us.csv')

# Ensure 'price' and 'days_listed' columns have correct types
df['price'] = df['price'].astype(float)
df['days_listed'] = df['days_listed'].astype(float)  # Convert to float if necessary

# Streamlit app setup
st.header("Vehicle Data Dashboard")
st.write("The following shown here are a collection of graphs and charts featuring the data shown in the vehicle dataset here.")

# Checkbox to toggle between different types of charts
show_price_histogram = st.checkbox('Show Price Histogram')
show_car_type_bar_chart = st.checkbox('Show Car Type Bar Chart')

# Show price histogram if checkbox is checked
if show_price_histogram:
    fig_histogram = px.histogram(df, x='price', title='Distribution of Vehicle Prices')
    st.plotly_chart(fig_histogram)

# Show car type bar chart if checkbox is checked
if show_car_type_bar_chart:
    fig_car_type = px.histogram(df, x='type', title='Stock of Car Type', labels={'type': 'Car Type'})
    fig_car_type.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig_car_type)

# Checkbox for filtering expensive cars
show_expensive_cars = st.checkbox('Show only cars priced above $20,000')

# If checkbox is checked, filter and show expensive cars
if show_expensive_cars:
    filtered_df = df[df['price'] > 20000]
    fig = px.histogram(filtered_df, x='type', title='Stock of Car Type for Expensive Cars', labels={'type': 'Car Type'})
    fig.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig)
    st.dataframe(filtered_df)  # Show filtered data when checkbox is checked
else:
    # Display default graph for all cars
    fig = px.histogram(df, x='type', title='Stock of Car Type', labels={'type': 'Car Type'})
    fig.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig)



 


 