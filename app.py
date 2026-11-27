import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title = 'Startup Analysis')
df = pd.read_csv(r"Dataset\startup_clean.csv")

def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investment by the investors
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round']]
    st.subheader('Most Recent Investment')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1 :
    # biggest investment
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending= False).head()
        st.subheader("Biggest Investment")
        st.dataframe(big_series)
    with col2 :
        fig , ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    






st.sidebar.title("Startup Funding Analysis")

options = st.sidebar.selectbox("Select one", ['Overall Analysis', 'Startup', 'Investor'])

if options == "Overall Analysis":
    st.title("Overall Analysis")
elif options == "Startup":
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button("Find Startup Detail")
    st.title("Startup Analysis")
    

else:
    selected_investor = st.sidebar.selectbox('Select Startup', sorted(set(df['investors'].str.split(",").sum())))
    btn2 = st.sidebar.button("Find Investor Detail")
    if btn2 :
        load_investor_details(selected_investor)








