import scipy.stats as sct
import random
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

V = 100.00       # initial price ($100)

g_sd =1   # standard deviation from the companies history is 1%
r = 0.1         # rate of return
v=0.25

data = [] # List

for i in range(10000):
    g = sct.norm.ppf(random.uniform(0, 1), loc=.01, scale=g_sd) # normal distribution
    V = V*(1 + v*g)
    data.append(V)

print(data)


sns.distplot(data)
plt.ylabel("Price")
plt.xlabel("time")
plt.show()


