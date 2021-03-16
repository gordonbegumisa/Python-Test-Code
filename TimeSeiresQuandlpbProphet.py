# PANDA TIME SERIES
# https://campus.datacamp.com/courses/manipulating-time-series-data-in-python/working-with-time-series-in-pandas?ex=3
#

import pandas as pd  # assumed imported going forward
from datetime import datetime  # To manually create dates
import numpy as np
import matplotlib.pyplot as plt

import quandl as qd     #   Quandl for financial qd data
qd.ApiConfig.api_key = 'VvTuDuztxrHRnWXb8QzU' # key for quadl

import fbprophet as fp  #   Facebooks Prophet

def tesla_gm_test_data():



    # Retrieve Tesla stock data from Quandl
    tesla = qd.get('WIKI/TSLA')

    # Retrieve the General Motors stock data from Quandl
    gm = qd.get('WIKI/GM')

    print(gm.info());print();print(gm.head(5));print();print(gm.tail());print()

    # The adjusted close accounts for stock splits, so that is what we should graph.
    # gm.index is the dataframe index value ie date index


    #plt.plot(gm.index, gm['Adj. Close'])
   #plt.title('GM Stock Price')
    #plt.ylabel('Price ($)');
    #plt.show()
    #plt.savefig('M:\Gordon\A Projects 2020\PYTHON TEMP\GmGraph.png')
   # plt.close('all')

   #plt.plot(tesla.index, tesla['Adj. Close'], 'r')
    #plt.title('Tesla Stock Price')
    #plt.ylabel('Price ($)');
    #plt.show();
    #plt.savefig('M:\Gordon\A Projects 2020\PYTHON TEMP\TeslaGraph.png')
    #plt.close('all')

    # Yearly average number of shares outstanding for Tesla and GM
    tesla_shares = {2018: 168e6, 2017: 162e6, 2016: 144e6, 2015: 128e6, 2014: 125e6, 2013: 119e6, 2012: 107e6,
                    2011: 100e6, 2010: 51e6}
    gm_shares = {2018: 1.42e9, 2017: 1.50e9, 2016: 1.54e9, 2015: 1.59e9, 2014: 1.61e9, 2013: 1.39e9, 2012: 1.57e9,
                 2011: 1.54e9, 2010: 1.50e9}

    # TESLA
    # --------------------------------------------------------------------------------------------
    tesla['Year'] = tesla.index.year  # Create a year column
    tesla.reset_index(level=0, inplace=True)  # Take Dates from index and move to Date column
    tesla['Cap'] = 0  # Create cap column = 0

    # Calculate market cap for all years
    for i, year in enumerate(tesla['Year']):
        shares = tesla_shares.get(year)  # Retrieve the shares for the year from Set
        tesla.loc[i, 'Cap'] = shares * tesla.loc[i, 'Close'] / 1e9  # Update the cap column to shares times the price in Billions

    print(tesla.head())

    # GM
    # ---------------------------------------------------------------------------
    gm['Year'] = gm.index.year  # Create a year columngm.reset_index(level=0, inplace=True)  # Take Dates from index and move to Date column
    gm.reset_index(level=0, inplace=True)  # Take Dates from index and move to Date column
    gm['Cap'] = 0  # Create cap column = 0

     # Calculate market cap for all years
    for i, year in enumerate(gm['Year']):
        shares = gm_shares.get(year)  # Retrieve the shares for the year from Set
        gm.loc[i, 'Cap'] = shares * gm.loc[i, 'Close'] / 1e9  # Update the cap column to shares times the price in Billions

    print(gm.head())
    # --------------------------------------------------------------------
    # MERGE The concat method; combine DataFrames vertically.
    # https: // chrisalbon.com / python / data_wrangling / pandas_join_merge_dataframe /

    cars = pd.merge(tesla, gm, on = 'Date');
    # cars.rename(columns={'Cap_x': 'gm_cap', 'Cap_y': 'tesla_cap'}, inplace=True)
    print(); print(cars.info()); print(cars.head())

    plt.figure(figsize=(10, 8))
    plt.plot(cars['Date'], cars['Cap_x'], 'b-', label = 'Tesla')
    plt.plot(cars['Date'], cars['Cap_y'], 'r-', label = 'GM')
    plt.ylabel(' (Amount ($ Billion)'); plt.title('GM & Tesla Comparative Capatilisation')
    plt.legend()
    plt.show()
    plt.savefig('M:\Gordon\A Projects 2020\PYTHON TEMP\Tesla_vs_GMGraph.png')
    plt.close('all')
    # Find the first and last time Tesla was valued higher than GM
    first_date = cars.ix[np.min(list(np.where(cars['Cap_y'] > cars['Cap_x'])[0])), 'Date']
    last_date = cars.ix[np.max(list(np.where(cars['Cap_yx'] > cars['Cap_x'])[0])), 'Date']
    print("Tesla was valued higher than GM from {} to {}.".format(first_date.date(), last_date.date()))

    return(0)

def prophet_test():

    print();  print('---------------------------------------------------------')
    print('PROPHET STARTS HERE'); print('---------------------------------------------------------')

    # Prophet requires columns ds (Date) and y (value)
    gm = gm.rename(columns={'Date': 'ds', 'cap': 'y'})

    # Put market cap in billions
    # gm['y'] = gm['y'] / 1e9

    # Make the prophet model and fit on the data
    gm_prophet = fp.Prophet(changepoint_prior_scale=0.15)
    gm_prophet.fit(gm)

    # Make a future dataframe for 2 years
    gm_forecast = gm_prophet.make_future_dataframe(periods=365 * 2, freq='D')

    # Make predictions
    gm_forecast = gm_prophet.predict(gm_forecast)

    gm_prophet.plot(gm_forecast, xlabel='Date', ylabel='Market Cap (billions $)')
    plt.title('Market Cap of GM')

    print('Tesla change Points:'); print((tesla_prophet.changepoints[:10]))

    return (0)

testal_gm_test_data()
prophet_test()