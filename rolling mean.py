import numpy as np
import pandas as pd
#import pandas.io.data as web
import pandas_datareader as web

goog = web.DataReader('GOOG', data_source='yahoo', start='3/14/2009', end='4/14/2014')
print(goog.tail())

goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))

#goog['Volatility'] = pd.rolling(goog['Log_Ret'], window=252).mean() * np.sqrt(252)

goog['Volatility'] = goog[['Log_Ret']].rolling( window=252).mean() * np.sqrt(252)
