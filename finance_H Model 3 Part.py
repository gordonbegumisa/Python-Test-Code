#! FinQuest - Financial Modelling Using Monte Caro Simulation
import random
import numpy as np
import seaborn as sns
from scipy.stats import norm
from matplotlib import pyplot as plt


d0 = 163            # historical dividend last year
gL_mean = 0.025     # average GDP growth rate
gL_sd = 0.00001     # standard deviation

gM_mean = 0.005       # over next year -ve growth
gM_sd = 0.00001     # standard deviation

gS_mean = 0.025       # over next year 15% grow
gS_sd = 0.00001     # standard deviation

r = 0.08            # historical rate of return
t = 1               # 1 year short-term growth rate
H = t/2

data = [] # List

for i in range(10000):
    gL = norm.ppf(random.uniform(0, 1), loc=gL_mean, scale=gL_sd)
    gM = norm.ppf(random.uniform(0, 1), loc=gM_mean, scale=gM_sd)
    gS = norm.ppf(random.uniform(0, 1), loc=gS_mean, scale=gS_sd)

    d1 = d0*(1+gM)
    v1 = d1/(1+r)
    v2 = ((d1*H*(gS-gL))/(r-gL) + (d1*(1+gL))/(r-gL))/(1+r)
    v = v1 + v2
    data.append(v)


print('Mean Price', np.mean(data))
print('Median Price', np.median(data))
print('STD', np.std(data))
print('Min Price', np.min(data))
print('Max Price', np.max(data))

sns.distplot(data)
plt.ylabel("Frequency")
plt.xlabel("Market Value")
plt.show()

