# PANDA TIME SERIES
# https://campus.datacamp.com/courses/manipulating-time-series-data-in-python/working-with-time-series-in-pandas?ex=3
#

import pandas as pd  # assumed imported going forward
from datetime import datetime  # To manually create dates
import numpy as np
import matplotlib.pyplot as plt
import quandl as qd
qd.ApiConfig.api_key = 'VvTuDuztxrHRnWXb8QzU' # key for quadl

def introduction():
    # ------------------------------------------------------------------------------------------------------------
    #                               P A R T I
    #                     Time        Series         Intro
    # ---------------------------------------------------------------------------------------------------------------
    #   Time stamps
    #   Time Periods
    #   Calculations
    #   Indexes
    #   Data Frames
    # write your thread 1 code here

    # create timestamp
    time_stamp = pd.Timestamp(datetime(2017, 1, 1))
    print("Timestamp Created: ",time_stamp)

    # retreive the year: time_stamp.year ie 2007
    # retreive the weekday:  time_stamp.weekday_name ie 'Sunday'
    print("Timestamp Year Retrieved) : ",time_stamp.year)
    print("Timestamp Day Retrieved) : ",time_stamp.weekday())
    print()

    # PERIODS

    period = pd.Period('2017-01','M')   # default: month-end
    print(period)

    period.asfreq('D')  # convert to daily
    print(period)

    period = period.to_timestamp().to_period('M')  # convert to monthly
    print(period)
    print()
    period = period + 2

    #  --------------------------INDEXES-------------------------------------------------------------

    index = pd.date_range(start='2017-1-1', periods=12, freq='M')
    print(index)
    period = index.to_period()

    print(period)
    print()

    # -----------------------DATA FRAMES----------------------------------------------------------

    #   pd.DataFrame({'data': index}).info()
    #   RRangeIndex: 12 entries, 0 to 11
    #   ta columns (total 1 columns):
    #   data    12 non-null datetime64[ns]
    #   dtypes: datetime64[ns](1)
    #   np.random.random:
    #   Random numbers: [0,1]
    #   12 rows, 2 columns

    data = np.random.random(size=(12,2))
    pd.DataFrame(data=data, index=index).info() # display class infor
    print(data)
    print()
    return(0)

def tranformation():
    #   --------------------------------------------------------------------------------------------------------------
    #                               P A R T II
    #                        Time    series      transformation
    #   ------------------------------------------------------------------------------------------------------------
    #   Basic time series transformations include:
    #   Parsing string dates and convert to datetime64
    #   Selecting & slicing for specific subperiods
    #   Setting & changing DateTimeIndex frequency
    #   Upsampling vs Downsampling

    print('---------------------GOOGLE STOCK PRICES-------------------------------------------------')
    #   -------------------------Example Getting GOOGL stock prices-----------------------------
    google = pd.read_csv('M:\Gordon\A Projects 2020\Python\Time Series Practise\GOOGL.csv') # Autoloads as a data DataFrame object 'pandas.core.frame.DataFrame'
    google.info()

    google.Date = pd.to_datetime(google.Date)    # converts string dates to datetime64 pd.to_datetime() within the google object
    google.info()
    print(google.head())
    print()

    google.set_index('Date', inplace=True) # set repaired column as index
    google.info()

    print(google.head())

    # Plot the index
    google.Close.plot(title='Google Stock Price')
    plt.tight_layout(); plt.show()

    # ----Selecting Data-----------------------------------------------------------------
    print('---------------------SELECTING DATA-------------------------------------------------')
    rawData= google.values                                  #Select raw data: Result, number, string.
    print(); print('RAW DATA');print(rawData)

    dataPoint = google.iloc[3,3]                             #Select point by Reference/index.Result:Series Select point by row use nesting
    print(); print('Data Point'); print(dataPoint);

    data.iloc[0:5]  # first five rows of dataframe
    data.iloc[:, 0:2]  # first two columns of data frame with all rows
    data.iloc[[0, 3, 6, 24], [0, 5, 6]]  # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
    data.iloc[0:5, 5:8]  # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).

    # Change the first name of all rows with an ID greater than 2000 to "John"
    data.loc[data['id'] > 2000, "first_name"] = "John"

    # Change the first name of all rows with an ID greater than 2000 to "John"
    data.loc[data['id'] > 2000, "first_name"] = "John"

    dataRow = google.iloc[3]                                 #Select row by index (row 1 is indexed as 0. Result: Series
    print(); print('Row'); print(dataRow)



    dataRow1 = google[google.index =='2020-01-01']          # Select Row. Result: series
    print(); print('Row 1'); print(dataRow1)

    columnNames = google.columns # retrieve column names
    print(); print('Column Names'); print(columnNames)

    dataIndex = google.index
    print(); print('Index'); print(dataIndex)

    dataColumn = google['Open']                             # Select a column: series
    print(); print('Column 1'); print(dataColumn)           # Automatic -  includes index

    dataColumns = google[['Open', 'Close']]                  #Select Multiple Columns
    print(); print('Multiple Columns'); print(dataColumns)
    print()

    #dataRowRange = google[google.between('2020-1-1', '2020-2-2', inclusive=False)] # endpoints are included
    #print(); print('Column Range'); print(dataRowRange)

    # ------Characterics -------------------------------------------------------
    print()
    print('-----------------------CHARACTERISTICS---------------------------------------')
    print('NUMBER OF Elements'); print (google.size); print()       # Returns no of elements
    print('Info'); print (google.info());  print()     # Object Information
    print('Description'); print (google.describe());print()  # Descriptive Data

    #------------------CHANGES TO DATA-----------------------------------------------------

    # ------------ADD-----------------------------------------
    # Add a Column and populate with data
    # df['Col'] = [data, data, data, .........]

    # Add a Row
    #
    # Add Data
    #
    # ----------DELETE---------------------------------------
    # Delete Data

    #   Delete Rows
        #   df.drop(['index1', 'index2',......])   # Drop a Row
        #   df([1,2])                             # Drop  rows 2 and 3
        # df[df.Name != 'Alisa']        # Drop a row by condition
        # df.drop(df.index[2])          # Drop a row by index
        # df[:-3]                       #Drop bottom 3 rows

    # Delete Columns
        #   df.drop('reports', axis=1) Note: axis=1 denotes that we are referring to a column, not a row
               # del df[#ColumnName] # Delete a Column by came

    #-------------RENAME------------------------------------------
    # # Rename columns using a dictionary to map values

    # # Rename the Area columnn to 'place_name'
    # data = data.rename(columns={"Area": "place_name"}inplace = True))

    # # Again, the inplace parameter will change the dataframe without assignment
    # data.rename(columns={"Area": "place_name"}, inplace=True)

    # # Rename multiple columns in one go with a larger dictionary
    # data.rename(
    #     columns={
    #         "Area": "place_name",
    #         "Y2001": "year_2001"
    #     },
    #     inplace=True
    # )

    # # Rename all columns using a function, e.g. convert all column names to lower case:
    # data.rename(columns=str.lower)

    # Frequency Changes--------------------------------------------------------------------------
    google.asfreq('D')  # set calendar day frequency. Higher frequency implies new dates => missing data (Called UpSampling)
    google.asfreq('B') # Convert DateTimeIndex to business day frequency
    #   ---------------------------REPLACE--------------------------------------

    # REPLACE https: // www.python - course.eu / pandas_replacing_values.php
    #
    #
    return(0)

def calculations():

    # -----------------------------------------------------------------------------------------------------------------
    #                       TIME SERIES CALCLUATIONS
    # -----------------------------------------------------------------------------------------------------------------
    # Shift or lag values back or forward back in time
    # Get the difference in value for a given time period
    # Compute the percent change over any number of periods

    #   Let pd.read_csv() do the parsing for you

    #   Methods:
    #       .shift() 	    Moving data between past & future
    #       .div()		    % change between 2   columns
    #       .change()
    #       .diff 		    difference in value for 2 adjacent periods
    #       .pct_change()   built-in time-series % change

    google = pd.read_csv('M:\Gordon\A Projects 2020\Python\Time Series Practise\GOOGL.csv', parse_dates=['Date'], index_col='Date')
    print(); print(google.info()); print(google.head(5))

    # shift(): Moving data between past & future defaults to periods=1 1 period into future.
    google['ShiftedClose'] = google.Close.shift() # default: periods=1 # creates  new column with shifted daates
    google['LaggedClose'] = google.Close.shift(periods=-1)
    print(); print(google[['Close', 'ShiftedClose', 'LaggedClose']].tail(3))

    #Calculate one-period percent change
    google['Change'] = google.Close.div(google.ShiftedClose)
    print(); google[['Close', 'ShiftedClose', 'Change']].head(3)

    #      Calculate one-period percent change
    google['Return'] = google.Change.sub(1).mul(100)
    print(); print(google[['Close', 'ShiftedClose', 'Change', 'Return']].head(3))

    #   diff(): built-in time-series change
    #   Difference in value for two adjacent periods
    google['Difference'] = google.Close.diff()
    print(); print(google[['Close', 'Difference']].head(3))

    #   .pct_change(): built-in time-series % change
    #   Percent change for two adjacent periods
    google['PChange'] = google.Close.pct_change().mul(100)
    print(); print(google[['Close', 'Return', 'PChange']].head(3))

    #   Looking ahead: Get multi-period returns
    google['Return_3d'] = google.Close.pct_change(periods=3).mul(100)
    print(); print(google[['Close', 'Return_3d']].head())
    #-------------------------------------------------------------------------------------------------------------------
    return (0)

def comparasons():
    #Stock price series: hard to compare at different levels
    #   Simple solution: normalize price series to start at 100
    #   Divide all prices by first in series, multiply by 100
    #   Same starting point
    #   All prices relative to starting point
    #   Difference to starting point in percentage points

    #Download data
    google = pd.read_csv('M:\Gordon\A Projects 2020\Python\Time Series Practise\GOOGL.csv', parse_dates=['Date'], index_col='Date')
    print(); print(google.info()); print(google.head(5))

    # NORMALISING SINGLE SERIES

    first_price = google.Close.iloc[0]  # 1st price data is the base price ie 1339.39
    print(); print('first price as base:', first_price )

    normalized = google.Close.div(first_price).mul(100) # Divide all prices by first in series, multiply by 100
    print(); print('normalized prices'); print(normalized.head(5))

    normalized.plot(title='Google Normalized Series')
    plt.show()

    # NORMALISING MULTIPLE SERIES
    # 1ST STEP IS WRANGLE THE DATA AND STORE INTO 1 DATAFRAME

    # Retrieve Google, Apple, Yahoo & SP500 stock data from Quandl
    google = qd.get('WIKI/GOOGL')
    apple = qd.get('WIKI/AAPL')
    yahoo = qd.get('WIKI/YHOO') # sp500= qd.get('WIKI/SP500');

    print('GOOGL PRICES FROM QUANDL');print(); print(google.info()); print(); print(google.head(5));

    # Perse Index to Date Column
    google['DateAdd'] = google.index  # Create a year column
    google.reset_index(level=0, inplace=True )  # Take Dates from index and move to Date column

    apple['DateAdd'] = apple.index
    apple.reset_index(level=0, inplace=True)

    yahoo['DateAdd'] = yahoo.index
    yahoo.reset_index(level=0, inplace=True)

    print('GOOGL PRICES FROM QUANDL');print(); print(google.info()); print(); print(google.head(5))

    # Filter for Close prices only
    google_prices = google[['Date','Close','DateAdd']]
    apple_prices = apple[['Date','Close','DateAdd']]
    yahoo_prices = yahoo[['Date','Close','DateAdd']]
    # print();print(google_prices.head(5));print();print(apple_prices.head(5));print();print(yahoo_prices.head(5))

    # Rename Columns

    google_prices.rename(columns={'Close':'GOOGL'}, inplace = True)
    apple_prices.rename(columns={'Close':'AAPL'}, inplace = True)
    yahoo_prices.rename (columns={'Close':'YHOO'}, inplace = True)

    print(); print(google_prices.head(5)); print(); print(apple_prices.head(5));  print(); print(yahoo_prices.head(5))

    # Merge Datasets according to date, use inner for only dates are common for comparason.

    stockDataTwo= pd.merge(google_prices, apple_prices, on = 'DateAdd', how = 'inner')
    stockDataSet= pd.merge(stockDataTwo, yahoo_prices, on ='DateAdd', how = 'inner')

    print(); print ('MERGED STOCK DATA'); print(); print(stockDataSet.info()); print(stockDataSet.head(5))

    # Simply the Database

    # Filter for prices only
    stockDataSet = stockDataSet[['Date_x','GOOGL', 'AAPL', 'YHOO']]

    print(); print('MERGED STOCK DATA'); print(); print(stockDataSet.info()); print(stockDataSet.head(5))

    # Set Index as timestamp

    stockDataSet.set_index('Date_x', drop=True, inplace=True)  # set repaired column as index
    stockDataSet.index.rename('Date', inplace=True)

    print(); print('MERGED STOCK DATA'); print(); print(stockDataSet.info()); print(stockDataSet.head(5))

    # NORMALISE

    basePrices = stockDataSet.iloc[0]
    print(basePrices)

    normalized = 100*stockDataSet.div(stockDataSet.iloc[0])   # .div():automatic alignment of Series index & dataFrame columns
    print(); print('normalized prices');print(normalized)

    normalized.plot(title='Google Normalized Series')
    plt.show()

    return(0)


#introduction()
#tranformation()
#calculations()
comparasons()


