import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


x =[1,2,3,4,5]
y =[3,7,3,4,2]
z= [2,5,9,2,4]

#plt.plot(x,y)
#plt.plot(x,z)
#plt.legend(["this is y", "this is z"])
#plt.title('Test Plot')
#plt.xlabel('x')
#plt.ylabel('y')
# plt.show()

google = pd.read_csv('M:\Gordon\A Projects 2020\PYTHON TEMP\GOOGL.csv') # Creates pandas.core.frame.DataFrame object
google.info()
print(google.head())
print()

# Selections
x1 = google.Date; y1 = google.Close # creates 2 panda.core.series.Series  objects
x2 = google['Date']                # as an array instead of a series objexr
z1 = google.Close.iloc[5]           # pick cell object.column.iloc[index]
print(z1)
# z2 = google.Close.iloc[5:3]         # selects  range of cells in column as annray

#plt.plot(x,y)
#plt.title('GOOGL Stock Price 2020')
#plt.xlabel('Date')
#plt.ylabel('Close')
#plt.show()


world = pd.read_csv( 'M:\Gordon\A Projects 2020\PYTHON TEMP\WPP2019_TotalPopulationBySex.csv ')
print(world.head())
world.info()
print(world.describe())


# filter rows where columns = Loction


uganda = world[world.Location == 'Uganda']

kenya = world[world.Location == 'Kenya']  # use '&'and '|" for or

australia = world[world.Location == 'Australia']


kenya.reset_index() # reset indices if required, drops old index
uganda.reset_index()
australia.reset_index()

kenya_list = kenya[kenya.Time < 2031]
uganda_list =uganda[uganda.Time <2031]
australia_list =australia[australia.Time <2031]

kenya_list.to_csv("M:\Gordon\A Projects 2020\PYTHON TEMP\Kenya.csv") # Save filtered file
print(uganda_list.head())
print(kenya_list.info())
print ()
print(uganda_list.head())
print(kenya_list.info())

a = kenya_list.Time
b = uganda_list.Time
f = australia_list.Time
c = kenya_list.PopTotal
d = uganda_list.PopTotal
e = australia_list.PopTotal

#plt.plot(a,c/1000)
plt.plot(a,c/1000)
plt.plot(b,d/1000)
plt.plot(f,e/1000)
plt.legend(["Kenya", "Uganda", "Australia"])
plt.title('Population')
plt.xlabel('Year')
plt.ylabel('Population (Millions)')
plt.show()
#uganda.PopTotal.hist.(bins=50) #Draw a histogram of the series

#-------------------------------------------------------------------------------------------------------------
#                       3D PLOTTING
#-------------------------------------------------------------------------------------------------------------

#from mpl_toolkits.mplot3d import Axes3D



