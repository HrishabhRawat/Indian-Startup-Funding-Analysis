import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv(r"Dataset\startup_clean.csv")

st.sidebar.title("Startup Funding Analysis")

options = st.sidebar.selectbox("Select one", ['Overall Analysis', 'Startup', 'Investor'])

if options == "Overall Analysis":
    st.title("Overall Analysis")
elif options == "Startup":
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button("Find Startup Detail")
    st.title("Startup Analysis")
    

else:
    st.sidebar.selectbox('Select Startup', sorted(set(df['investors'].str.split(",").sum())))
    btn2 = st.sidebar.button("Find Investor Detail")
    st.title("Investors")







