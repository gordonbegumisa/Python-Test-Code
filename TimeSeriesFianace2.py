import pandas as pd  # assumed imported going forward
from datetime import datetime  # To manually create dates
import numpy as np
import matplotlib.pyplot as plt
import quandl as qd
qd.ApiConfig.api_key = 'VvTuDuztxrHRnWXb8QzU' # key for quadl


# Import Data
#google = pd.read_csv('M:\Gordon\A Projects 2020\Python\Time Series Practise\GOOGL.csv', parse_dates=['Date'], index_col='Date')

#----------------------------------------------------------------------------------------
#                        RE-SAMPLING DATA
#-----------------------------------------------------------------------------------------

# UPSAMPLING: Fill-in Logic or Interpolatipn

# ffill() is applied across the index then any missing value is filled based on the corresponding value in the previous row.
# bfill() When axis='rows', then value in current na cells are filled from the corresponding value in the next row.
# when axis='columns', then the current na cells will be filled from the value present in the next column in the same row.
# https://www.geeksforgeeks.org/python-pandas-dataframe-bfill/


# Set start and end dates
start = '2016-1-1'
end = '2016-2-29'

# Create monthly_dates here
monthly_dates = pd.date_range(start=start, end=end, freq='M')
# Create and print monthly here

monthly = pd.Series(data=[1,2], index=monthly_dates)
print(monthly)

# Create weekly_dates here
weekly_dates = pd.date_range(start=start, end=end, freq='W')

# Print monthly, reindexed using weekly_dates
print(monthly.reindex(weekly_dates))

print(monthly.reindex(weekly_dates, method='bfill'))

print(monthly.reindex(weekly_dates, method='ffill'))

