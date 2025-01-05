import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('vehicles_us.csv')

# Check and fix missing or invalid column names
df.columns = [col if col != '' else f'Unnamed_{i}' for i, col in enumerate(df.columns)]

# Ensure 'price' and 'days_listed' columns have correct types (convert to float if necessary)
df['price'] = df['price'].astype(float, errors='ignore')
df['days_listed'] = df['days_listed'].astype(float, errors='ignore')

# Title of the app centered
st.title('DRIVING FORCES: What affects Car Sales and Pricing')

st.write("The following shown here are a collection of graphs and charts featuring the data shown in the vehicle dataset here.")

# Show price histogram
fig_histogram = px.histogram(df, x='price', title='Distribution of Vehicle Prices')
st.plotly_chart(fig_histogram)

# Checkbox for filtering expensive cars
show_expensive_cars = st.checkbox('Show only cars priced above $20,000')

if show_expensive_cars:
    filtered_df = df[df['price'] > 20000]
    fig = px.histogram(filtered_df, x='type', title='Stock of Car Type (Expensive Cars)', labels={'type': 'Car Type'})
    fig.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig)
    
    # Display filtered data
    st.dataframe(filtered_df)  # Use dataframe to display the filtered DataFrame
else:
    # Show car type distribution for all cars
    fig = px.histogram(df, x='type', title='Stock of Car Type', labels={'type': 'Car Type'})
    fig.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig)
