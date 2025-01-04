import streamlit as st

import pandas as pd

import plotly.express as px

 

df = pd.read_csv('vehicles_us.csv')

 

st.header("Vehicle Data Dashboard")

 

st.write("The following shown here are a collection of graphs and charts featuring the data shown in the vehicle dataset here.")

 

fig_histogram = px.histogram(df, x='price', title='Distribution of Vehicle Prices')

st.plotly_chart(fig_histogram)

