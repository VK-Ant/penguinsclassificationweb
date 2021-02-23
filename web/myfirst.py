import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple stock price app


shown are the stock closing price and volume of Gooogle!

""")


tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'Id', start = '2010-5-31', end = '2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)