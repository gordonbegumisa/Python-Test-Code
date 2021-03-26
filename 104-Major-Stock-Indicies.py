import numpy as np
import pandas as pd
import yfinance as yf

# Retrieving List of World Major Stock Indices from Yahoo! Finance
df_list = pd.read_html('https://finance.yahoo.com/world-indices/')
majorStockIdx = df_list[0]
print(majorStockIdx.head(10))

# ^GSPC is the symbol of S&P 500 in Yahoo! Finance
tickerData = yf.Ticker('^GSPC')
tickerDf1 = tickerData.history(period='1d', start='2000-1-1', end='2020-10-1')