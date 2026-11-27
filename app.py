import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title = 'Startup Analysis')
df = pd.read_csv(r"Dataset\startup_clean.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
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
        fig , ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    # pie chart in which sector a particular investor invested in 
    with col2:
        sectors = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested in ')
        fig1 , ax1 = plt.subplots()
        ax1.pie(sectors, labels = sectors.index, autopct="%0.01f%%")
        st.pyplot(fig1)


    # Year on Year investment of the particualr investor
    st.subheader("Year on Year Investment")
    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    fig2, ax2= plt.subplots()
    ax2.plot(year_series.index, year_series.values)
    st.pyplot(fig2)
    

def load_overall_analysis():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        total = round(df['amount'].sum())
        st.metric("Total", str(total) + ' Indian Rupees')
    with col2:
        max_total = round(df.groupby('startup')['amount'].max().sort_values(ascending = False).head(1).values[0])
        st.metric('Max' , str(max_total) + ' Indian Rupees')
    with col3:
        avg_funding = round(df.groupby('startup')['amount'].sum().mean())
        st.metric('Average', str(avg_funding) + " Indian Rupees")
    with col4:
        total_startup = df['startup'].nunique()
        st.metric("Funded Startup", total_startup)




st.sidebar.title("Startup Funding Analysis")

options = st.sidebar.selectbox("Select one", ['Overall Analysis', 'Startup', 'Investor'])

if options == "Overall Analysis":
    st.title("Overall Analysis")
    btn0 = st.sidebar.button("Show Overall Analysis")
    if btn0:
        load_overall_analysis()

elif options == "Startup":
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button("Find Startup Detail")
    st.title("Startup Analysis")
    

else:
    selected_investor = st.sidebar.selectbox('Select Startup', sorted(set(df['investors'].str.split(",").sum())))
    btn2 = st.sidebar.button("Find Investor Detail")
    if btn2 :
        load_investor_details(selected_investor)








