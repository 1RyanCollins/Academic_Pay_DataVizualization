import pandas as pd
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/1RyanCollins/Academic_Pay_DataVizualization/main/Academic_Data.csv")
st.title("Adjunct & PhD Student Data Visualization Project")
st.write(df)  # visualize my dataframe in the Streamlit app



















