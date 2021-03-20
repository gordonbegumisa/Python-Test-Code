import random
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.stats import norm

d0 = 163            # historical dividend last year
gL_mean = 0.025     # average GDP growth rate
gL_sd = 0.00001     # standard deviation

gS_mean = 0.0       # over next year Zero grow
gS_sd = 0.00001     # standard deviation

r = 0.08            # historical rate of return
t = 1               # 1 year short-term growth rate
H = t/2

data = [] # List

for i in range(10000):
    gL = norm.ppf(random.uniform(0, 1), loc=gL_mean, scale=gL_sd)
    gS = norm.ppf(random.uniform(0, 1), loc=gS_mean, scale=gS_sd)
    v = ((d0*H*(gS-gL)) + (d0*(1+gL)))/(r-gL) # H - Growth Model
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

