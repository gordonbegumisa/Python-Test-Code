import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# initialise data of lists.
data = {'t': [0.000,0.000], 'r': [0.000,0000],  'N': [0.000,000]}  #data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}

# Creates pandas DataFrame.
logisticObj = pd.DataFrame(data)

def logistic_curve(l,k,r,t):
    n = l/(l+((k-l)*(math.exp(-r*t))))
    #print(n)
    return n

# Generate Data

t = 0.1
deltaT = 0.05
startR = 1.3
deltaR = 0.8
l = 1000000
k = 3*l

ylimit = 120 # Iterations per curve
zlimit = 6  # Number of Curves


for y in range(ylimit):
    logisticObj.loc[y,'t'] = t
    r = startR
    for z in range(zlimit):
        n = logistic_curve(l,k,r,t)
        logisticObj.loc[y, 1 + z] = r
        logisticObj.loc[y, 10 + z] = n
        print(y,z,t,l,k,r,n)
        r = r + deltaR

    t = t + deltaT

print(logisticObj.head(50))
logisticObj.to_csv('logisticCurve.csv')

# gca stands for 'get current axis'
ax = plt.gca()

#   Plot Data
for z in range(zlimit):
    logisticObj.plot(x ='t', y=(z+10), kind = 'line', ax=ax)



#   logisticObj.plot(x ='t', y=11, kind = 'line', ax=ax)
#   logisticObj.plot(x ='t', y=12, kind = 'line', ax=ax)
#logisticObj.plot(x ='t', y=13, kind = 'line', ax=ax)
#logisticObj.plot(x ='t', y=14, kind = 'line', ax=ax)

plt.title('Logistic Curves')
plt.legend(["r = 1.3", "r = 1.3 +.6", "r = 1.6 + 1.2 ", "r = 1.6 +1.5" , "r = 1.6 + 1.8"])
plt.xlabel('t')
plt.ylabel('N')
plt.savefig('bx3.png')
plt.show()




