# Logistic Curves vs R values
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# initialise data of lists.
data = {'t': [0.000,0.000], 'r': [0.000,0000],  'N1': [0.000,000]}  #data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}

# Creates pandas DataFrame.
logistic = pd.DataFrame(data)

print (logistic.head())


def logistic_curve(r,x):
    y = 1 / (1 + ((1 / x) - 1)*np.exp(-r * x))
    return y

# Generate Data

t = -0.5
startR = 1.0
deltaT = 0.01
deltaR = 0.3


jlimit = 200 # Iterations per curve
klimit = 5  # Number of Curves



for j in range(jlimit):
    logistic.loc[j, 't'] = t
    counter = 0
    r = startR
    for k in range(klimit):
        n = logistic_curve(r,t)
        logistic.loc[j, 1 + k] = r
        logistic.loc[j, 10 + k] = n
        r = r + deltaR
        #print(t,r,n)
    t = t + deltaT

print(logistic.head(5))
logistic.to_csv('07-logisticCurve.csv')

# gca stands for 'get current axis'
ax = plt.gca()

#   Plot Data
logistic.plot(x ='t', y=10, kind = 'line', ax=ax)
logistic.plot(x ='t', y=11, kind = 'line', ax=ax)
logistic.plot(x ='t', y=12, kind = 'line', ax=ax)
logistic.plot(x ='t', y=13, kind = 'line', ax=ax)
logistic.plot(x ='t', y=14, kind = 'line', ax=ax)

plt.title('Logistic Curves vs R values')
plt.legend(["r = 1.0", "r = 1.3", "r = 1.6", "r = 1.9" , "r = 2.2"])
plt.xlabel('t')
plt.ylabel('N')
plt.savefig('07-Logistic Curves R.png')
plt.show()




