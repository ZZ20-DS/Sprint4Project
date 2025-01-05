import streamlit as st

import pandas as pd

import plotly.express as px

 

df = pd.read_csv('vehicles_us.csv')

 

st.header("Vehicle Data Dashboard")

 

st.write("The following shown here are a collection of graphs and charts featuring the data shown in the vehicle dataset here.")

 

fig_histogram = px.histogram(df, x='price', title='Distribution of Vehicle Prices')

st.plotly_chart(fig_histogram)

 

show_expensive_cars = st.checkbox('Show only cars priced above $20,000')

 

if show_expensive_cars:

    filtered_df = df[df['price'] > 20000]

    fig = px.histogram(filtered_df, x='type', title='Stock of Car Type', labels={'type':'Car Type'})

    fig.update_layout(yaxis_title="Amount in Stock")

    st.plotly_chart(fig)

else:

    fig = px.histogram(df, x='type', title='Stock of Car Type', labels={'type':'Car Type'})

    fig.update_layout(yaxis_title="Amount in Stock")

    st.plotly_chart(fig)

st.write(filtered_df)




 