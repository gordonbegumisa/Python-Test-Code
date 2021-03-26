import random
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

d0 = 100
data = []

for i in range(10000):
    g = random.uniform(0.05, 0.08)
    r = random.uniform(0.09, 0.10)
    v = d0 * (1 + g)/(r - g) # Gordon Growth Model Formula
    data.append(v)

print ('Mean Price ($)', np.mean(data))
print ('Median Price ($)', np.median(data))
print ('STD ($)', np.std(data))
print ('Min Price ($)', np.min(data))
print ('Max Price ($)', np.max(data))

sns.distplot(data)
plt.title("Present Stock Value Using the Gordon Model")
plt.ylabel("Frequency")
plt.xlabel("Value($)")
plt.savefig('101-QF-Gordon-Model')
plt.show()

