import scipy.stats as sct
import random
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# SNP 500
d0 = 163
gL_mean = 0.05 # average growth rate from the company history is 5%
gL_sd = 0.01     # standard deviation from the companies history is 1%

gS_mean = 0.05 # average growth rate from the company history is 5%
gLSsd = 0.01     # standard deviation from the companies history is 1%

r = 0.08
n = 5
H = n/2

data = [] # List

for i in range(10000):
    gL = sct.norm.ppf(random.uniform(0, 1), loc=g_mean, scale=g_sd)
    gS = sct.norm.ppf(random.uniform(0, 1), loc=g_mean, scale=g_sd)
    v = (d0*H*(gS-gL))/(r-gL) + (d0*(1+gL))/(r-gL) # H Growth Model
    data.append(v)

print ('Mean Price', np.mean(data))
print ('Median Price', np.median(data))
print ('STD', np.std(data))
print ('Min Price', np.min(data))
print ('Max Price', np.max(data))

sns.distplot(data)
plt.ylabel("Frequency")
plt.xlabel("Market Value")
plt.show()

