import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title(" Covid 19 all_weekly_excess_deaths") 

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    st.write("File uploaded...")
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview") 
    st.write(df.head(10))
    st.write(df.tail(10))
    
    st.subheader("Summary Statistics") 
    st.write(df.describe(include='all')) 
    # gives a summary of the statistical properties on numerical data in the df dataframe eg. count, std(spread of the data), 25% - 25% of data falls below xx value
    
    st.subheader("Filter Data")
    columns = df.columns.tolist() #get all column names from the dataframe df as a simple list or regular python list.
    selected_column = st.selectbox("Select colum to filter by", columns)

    # Filter options
    st.sidebar.header("🔍 Data Filter")
    columns = df.columns.tolist()
    selected_column = st.sidebar.selectbox("Filter by column:", columns)
    unique_values = df[selected_column].dropna().unique()
    selected_value = st.sidebar.selectbox("Value to filter:", unique_values)

    filtered_df = df[df[selected_column] == selected_value] #filter the df to show only the rows where the values in a specific column matches a certain value.
    st.subheader(f"🔎 Filtered Data: {selected_column} = {selected_value}")
    st.write(filtered_df)

    st.header("Visualization")
    x_column = st.selectbox("Select x_axis column", columns)
    y_column = st.selectbox("Select y_axis column", columns)

    if st.button("Generate Plot"):
        st.bar_chart(filtered_df.set_index(x_column)[y_column])
else: 
    st.write("waiting on file upload...")
