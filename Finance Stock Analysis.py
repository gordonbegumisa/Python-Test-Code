import random
import pandas as pd
import datetime
import numpy as np
import matplotlib.pylab as plt
# from numpy.linagl import cholesky
import seaborn as sns
import quandl as qd     #Quandl for financial qd data
qd.ApiConfig.api_key = 'VvTuDuztxrHRnWXb8QzU' # key for quadl


#Chacshe data for this period
all_data_start, all_data_end = '2016-01-01', '2019-10-01'

#By default work with data in this period
default_start, default_end = '2016-01-01', '2019-10-01'


# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call

data = qd.get_table('WIKI/PRICES', ticker=['AAPL', 'MSFT', 'WMT'],
                        qopts={'columns': ['ticker', 'date', 'adj_close']},
                        date ={'gte': '2015-01-01', 'lte': '2016-01-01'},
                        paginate=True)

# create a new dataframe with 'date' column as index
new = data.set_index('date')

# use pandas pivot function to sort adj_close by tickers
historical = new.pivot(columns='ticker')
print(historical.head())

plt.plot(historical)
plt.show()

# returns  relative to the initial price = relative changes in price. ie divide all
# prices by the first.

returns = (historical/historical.iloc[0])
returns.plot(); plt.show()

# If I buy and equal amount of shares for all stocks -> portfolio
N = 3
#returns['Portfolio'] = returns.iloc[:, 0:N], sum(axis=1)) / N

# Calculate the risk by volitiliy
daily_pct_change = np.log(returns.pct_change() +1)
vol = daily_pct_change.std()*np.sqrt(252)
print(vol)


