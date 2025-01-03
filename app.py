import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# Title of the app centered
st.title('DRIVING FORCES: Key Factors that Impact Car Sales and Pricing')


# Load and clean the dataset
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    df = df.drop(df.columns[0], axis=1)  # Drop the first column
    return df

# Main function for the Streamlit app
def main():
    st.title("Car Model Frequency App")

    # Load the data
    df = load_data()

    # Count the frequency of each model
    model_counts = df['model'].value_counts()

    # Display the top 10 models
    st.write("Top 10 Models by Frequency:")
    st.table(model_counts.head(10))

    # Create a histogram for the top 10 models
    st.write("Histogram: Top 10 Most Frequent Car Models")
    fig, ax = plt.subplots()
    model_counts.head(10).plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title("Most Frequent Car Models")
    ax.set_xlabel("Car Model")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
     # Data for top 5 popular car colors
    paint_colors = {
        'white': 10029,
        'black': 7692,
        'silver': 6244,
        'grey': 5037,
        'blue': 4475
    }

    colors = list(paint_colors.keys())
    frequencies = list(paint_colors.values())

    # Create a scatter plot for top 5 popular car colors
    st.write("Scatter Plot: Top 5 Popular Car Colors")
    fig, ax = plt.subplots()
    ax.scatter(colors, frequencies, color='green', s=100)
    ax.set_title("Top 5 Popular Car Colors")
    ax.set_xlabel("Car Colors")
    ax.set_ylabel("Frequency")
    for i, txt in enumerate(frequencies):
        ax.annotate(txt, (colors[i], frequencies[i]), textcoords="offset points", xytext=(0,10), ha='center')
    st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    main()

 