#import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv', engine='c')

df['price'] = pd.to_numeric(df['price'], errors='coerce')  
df = df.dropna(subset=['price'])  
df['price'] = df['price'].astype(int)  

st.header("Vehicle Data Dashboard")

st.write("The following are a collection of graphs and charts featuring the data shown in the vehicle dataset.")

fig_histogram = px.histogram(df, x='price', title='Distribution of Vehicle Prices')
st.plotly_chart(fig_histogram)

show_expensive_cars = st.checkbox('Show only cars priced above $20,000')

if show_expensive_cars:
    filtered_df = df[df['price'] > 20000]
    fig = px.histogram(filtered_df, x='type', title='Stock of Car Type (Price > $20,000)', labels={'type': 'Car Type'})
    fig.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig)

    # Display filtered dataframe
    st.write("Filtered Dataframe (Cars priced above $20,000):")
    st.write(filtered_df)
else:
    fig = px.histogram(df, x='type', title='Stock of Car Type', labels={'type': 'Car Type'})
    fig.update_layout(yaxis_title="Amount in Stock")
    st.plotly_chart(fig)

    # Display unfiltered dataframe
    st.write("Unfiltered Dataframe:")
    st.write(df)








 


 