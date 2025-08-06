import yfinance as yf
import streamlit as st

st.header("Stock Market Analyzer")


dd = st.text_input("Enter the stock ","AAPL")


ticker_data = yf.Ticker(dd)

import datetime

col1,col2 = st.columns(2)

with col1:
    start = st.date_input("Start date", datetime.date(2019, 1, 1))

with col2:
    end = st.date_input("End date", datetime.date(2019, 12, 31))

ticker_df = ticker_data.history(start=start, end=end)

st.dataframe(ticker_df)

st.line_chart(ticker_df["Close"])