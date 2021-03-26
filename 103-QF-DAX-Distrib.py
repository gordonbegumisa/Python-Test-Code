import scipy.stats as sc
import numpy as np
import random
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

import yfinance as yf # Yahoo for financial data

import quandl as qd     # Quandl for financial data
qd.ApiConfig.api_key = "VvTuDuztxrHRnWXb8QzU" # key for quadl



ind = 'WIKI/GOOGL.4'

s = '2005-01-01'
e = '2020-01-01'

# Get data over last 15 years
index = qd.get([ind], start_date=s, end_date=e)

# Create Dataframe

# Calculate Google mean &. standard deviation
#index_mean = index.mean( axis = 0, skipna = True)
#index_std = index.std( axis = 0, skipna = True)

index_mean = 4
index_std = 1
print(index_mean, index_std)

# Calculate Gaussian

gaussian = sc.norm(loc=index_mean, scale=index_std)
x = np.linspace(0.0, 8.0, 100)
y = gaussian.pdf(x)

# Plot histogram
sns.displot(index, kde = True)
sns.displot(y, kde = True)

plt.title("Google Price 2000-2020")
plt.ylabel("Frequency")
plt.xlabel("Price ($)")
# plt.savefig('101a-QF-Gordon-Model')
plt.show()

