import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt



# plt.style.use('')
st = dt.datetime(2020, 1, 18)
en = dt.datetime(2020, 6, 18)

prices = web.get_data_yahoo(['AAPL'], start=st, end=en)['Close']
returns = prices.pct_change()

last_price = prices.iloc[-1]

sims = 100
days = 252
sim_df = pd.DataFrame()

volitility = 0.25/days

for i in range(sims):
    count = 0
    st_dev = returns.std()

    price_series = []

    price = last_price * (1 + np.random.normal(0, volitility))
    price_series.append(price)

    for j in range(days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, volitility))
        price_series.append(price)
        count += 1

    sim_df[i] = price_series


fig = plt.figure()
plt.plot(sim_df)
#plt.plot(last_price, color='r', linestyle='-')
plt.show()





