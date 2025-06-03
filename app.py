import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset here
@st.cache_data
def load_data():
    df = pd.read_csv('your_dataset.csv')  # Replace with your actual file path
    df['MSRP'] = df['MSRP'].str.replace('[$,]', '', regex=True).astype('int64')
    return df

# Load data
df = load_data()

# App title
st.title("Car MSRP Visualization App")

# Brand selection
brands = df['Make'].unique()
brand = st.selectbox("Select a car brand", sorted(brands))

# Filter data for selected brand
filtered_df = df[df['Make'] == brand]

# Plotting
if not filtered_df.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Model', y='MSRP', data=filtered_df, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)
else:
    st.warning("No data found for the selected brand.")
