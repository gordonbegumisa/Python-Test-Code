import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

plot.close('all') # Clear memory
world = pd.read_csv( 'M:\Gordon\A Projects 2020\PYTHON TEMP\WPP2019_TotalPopulationBySex.csv ') # Import data

print(world.head())
world.info()
print(world.describe())

# sort, filter and standardise data required data rows where columns = Location

uganda = world[world.Location == 'Uganda']
kenya = world[world.Location == 'Kenya']  # use '&'and '|" for or
rwanda = world[world.Location == 'Rwanda']
#burundi = world[world.Location == 'Burundi']
southsudan = world[world.Location == 'South Sudan']
tanzania = world[world.Location == 'United Republic of Tanzania']
australia = world[world.Location == 'Australia']

kenya.reset_index() # reset indices if required, drops old index
uganda.reset_index()
rwanda.reset_index()
#burudi.reset_index()
southsudan.reset_index()
tanzania.reset_index()
australia.reset_index()

print(); print(kenya.head())
print(uganda.head())
print(rwanda.head())
print(southsudan.head())
print(tanzania.head())
print(australia.head())

# create single shared time axis as series
a = kenya.Time

# create population series for each country
fr=1000
aa = kenya.PopTotal/fr
bb = uganda.PopTotal/fr
cc = rwanda.PopTotal/fr
#dd = burundi.PopTotal/fr
ee = southsudan.PopTotal/fr
ff = tanzania.PopTotal/fr
eastafrica = aa + bb + cc +ee + ff

# australia as a control
x = australia.PopTotal/fr
xx = australia.PopTotal/fr

#format the page
plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

plt.title('Population Growth Projections Across East Africa 1950-2070')
plt.xlabel('Source: UN - Department of Economic and Social Affairs - World Population Prospects 2019')
plt.ylabel('Population (Millions)')
plt.xlim(1950,2070)
plt.ylim(0,100)

#plot graph
plt.plot(a,aa)
plt.plot(a,bb)
plt.plot(a,cc)
#plt.plot(a,dd)
plt.plot(a,ee)
plt.plot(a,ff)
plt.plot(eastafrica)
plt.plot(a,xx)

plt.legend(["Kenya", "Uganda",  "Rwanda", "South Sudan", "Tanzania", "Regional","Australia"])

#plt.text('Source: UN - Department of Economic and Social Affairs - World Population Prospects 2019')
plt.show()
#plt.savefig('M:\Gordon\A Projects 2020\PYTHON TEMP\xx.jpg')

#uganda.PopTotal.hist.(bins=50) #Draw a histogram of the series

#-------------------------------------------------------------------------------------------------------------
#                       3D PLOTTING
#-------------------------------------------------------------------------------------------------------------

#from mpl_toolkits.mplot3d import Axes3D



