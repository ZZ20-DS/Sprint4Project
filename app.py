import streamlit as st

import pandas as pd

import plotly.express as px

 

df = pd.read_csv('vehicles_us.csv')

 

st.header("Vehicle Data Dashboard")

 # Streamlit app
st.title('Vehicle Model Year Analysis')

# Checkbox to filter vehicles older than 2007
filter_older = st.checkbox('Show only vehicles older than 2007')

# Filter the DataFrame based on the checkbox
if filter_older:
    filtered_df = df[df['model_year'] < 2007]
else:
    filtered_df = df

# Show the filtered DataFrame (optional, can be useful for debugging or analysis)
st.write("Filtered Dataset", filtered_df)

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(filtered_df['model_year'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Vehicle Model Years')
plt.xlabel('Model Year')
plt.ylabel('Count')
plt.grid(True)

# Display the histogram in Streamlit
st.pyplot(plt)

# Scatter plot for popular colors (black, white, silver)
popular_colors = ['black', 'white', 'silver']

# Filter for rows where color is one of the popular colors
filtered_colors_df = filtered_df[filtered_df['color'].isin(popular_colors)]

# Show the filtered dataset for popular colors
st.write("Filtered Dataset for Popular Colors (Black, White, Silver):", filtered_colors_df)

# Scatter plot for each of the popular colors
for color in popular_colors:
    color_df = filtered_colors_df[filtered_colors_df['color'] == color]
    
    if 'price' in color_df.columns:  # Replace 'price' with any numeric column in your dataset
        st.write(f"Scatter Plot of Model Year vs. Price for {color.capitalize()} Cars")
        
        # Plotting the scatter plot for each color
        plt.figure(figsize=(10, 6))
        plt.scatter(color_df['model_year'], color_df['price'], alpha=0.5, label=f'{color.capitalize()} Cars')
        plt.title(f'Scatter Plot of Model Year vs. Price for {color.capitalize()} Cars')
        plt.xlabel('Model Year')
        plt.ylabel('Price')
        plt.grid(True)
        plt.legend()
        
        # Display the scatter plot for each color in Streamlit
        st.pyplot(plt)
    else:
        st.write(f"No 'price' column found for {color.capitalize()} cars.")

  



 