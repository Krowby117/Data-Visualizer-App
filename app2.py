import streamlit as st
import pandas as pd

from tabs.distroTab import show_dist
from tabs.dataTab import show_data
from tabs.relaTab import show_rela
from tabs.cleaningTab import show_cleaning

st.title("A Simple CSV Visualizer")

file = st.file_uploader("Upload a CSV file", type="csv")


if file:
    data = pd.read_csv(file).dropna()
    data = data.convert_dtypes()
    if data.empty:
        st.warning("The dataset is empty after removing rows with missing values. Please upload a CSV with more complete data or adjust missing value handling.")
    else:
        numeric_data = data.select_dtypes(include="number").columns.tolist()
        nonNumeric_data = data.select_dtypes(include="object").columns.tolist()

        ## --- main app tabs ---
        dataTab, cleanTab, distTab, relTab= st.tabs(["Data", "Cleaning", "Distributions", "Relationships"])

        with dataTab:
            show_data(data)

        with cleanTab:
            show_cleaning(numeric_data, data)

        with distTab:
            show_dist(numeric_data, nonNumeric_data, data)

        with relTab:
            show_rela(numeric_data, nonNumeric_data, data)
