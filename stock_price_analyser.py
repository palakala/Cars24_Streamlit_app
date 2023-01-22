import pandas as pd
import streamlit as st
import yfinance as yf
import datetime


st.write(

    """
    # Stock Price Analyser

    Show are the Apple stock
    """
)

# ticker_symbol = "AAPL"

ticker_symbol = st.text_input(
                            "Enter the Stock Symbol",
                            "AAPL",
                            key = "Placeholder"

)

ticker_data = yf.Ticker(ticker_symbol)

col1, col2 = st.columns(2)


with col1:
    start_date = st.date_input(
        "From date",
        datetime.date(2019,1,1))
with col2:
    end_date = st.date_input(
        "End date",
        datetime.date(2022,12,31)
    )

ticker_df = ticker_data.history(period = "1d",
                                start = f"{start_date}",
                                end = f"{end_date}")

st.write(f"### {ticker_symbol}'s EOD Prices")

st.dataframe(ticker_df)


st.write("""

## Daily closing price chart
""")

st.line_chart(ticker_df.Close)

st.write("""
## Volume of shares traded each day
""")

st.line_chart(ticker_df.Volume)
