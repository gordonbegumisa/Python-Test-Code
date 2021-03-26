import scipy.stats as sct
import random
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

import quandl as qd
qd.ApiConfig.api_key = 'VvTuDuztxrHRnWXb8QzU' # key for quadl



d_0 = 100
data = []

d0 = 100  # Dividend ($100)
g_mean = 0.05  # average growth rate from the company’s history is 5%
g_sd = 0.01  # standard deviation from the company’s history is 1%
r = 0.1  # rate of return

for i in range(10000):
    g = sct.norm.ppf(random.uniform(0, 1), loc=g_mean, scale=g_sd)  # normal distribution of growth rate
                                                                    # with g_mean & g_sd stardard deviation
    v = d_0 * (1 + g) / (r - g)  # Gordon Growth Model Formula
    data.append(v)

sns.distplot(data)
plt.title("Present Stock Value Using the Gordon Model")
plt.ylabel("Frequency")
plt.xlabel("Value($)")
plt.savefig('101a-QF-Gordon-Model')
plt.show()

