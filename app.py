import streamlit as st
import pandas as pd
import plotly.express as px

st.title("DRIVING FORCES: Key Factors That Influence Car Sales and Pricing")
st.markdown("This dashboard is a Streamlit dashboard that can be used to analyze the driving forces behind car sales and pricing.")

# Read the data from the CSV file
try:
    df = pd.read_csv("vehicles_us.csv")
except FileNotFoundError:
    st.error("Error: The file 'vehicles_us.csv' was not found.")
    st.stop()
# Fill missing values or drop rows as needed
df['model_year'] = df['model_year'].fillna(0).astype(int)  # Replace NaN with 0 for visualization
df['cylinders'] = df['cylinders'].fillna(0).astype(int)  # Replace NaN with 0
df['odometer'] = df['odometer'].fillna(df['odometer'].mean()).astype(int)  # Fill with mean
df['paint_color'] = df['paint_color'].fillna("unknown")  # Replace NaN with "unknown"
df['is_4wd'] = df['is_4wd'].fillna(0).astype(int)  # Treat NaN as 0 (not 4WD)

# Check for unique values in object columns
for col in ['model', 'condition', 'fuel', 'transmission', 'type', 'paint_color']:
    st.write(f"Unique values in {col}:", df[col].unique())
import pyarrow as pa

try:
    pa_table = pa.Table.from_pandas(df)
    st.write("PyArrow conversion successful!")
except Exception as e:
    st.error(f"PyArrow conversion failed: {e}")
    st.stop()
# Display cleaned dataset
st.write("Cleaned Dataset:")
st.write(df.head())
# Histogram: Analysis of Price
st.subheader("Histogram: Analysis of Price")
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

 
