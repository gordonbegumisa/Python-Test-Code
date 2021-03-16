import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

L=25

def wave(x,n):
    w = (np.sqrt(2/L)*np.cos(np.pi*n*x/L))**2
    return w

x = np.linspace(-L, L, L*8)
plt.xlim(-L/2, L/2)
plt.plot(x,wave(x,1))
plt.plot(x,wave(x,3))
plt.plot(x,wave(x,5))

plt.title('Probability Distributions (x)')
plt.xlabel('x')

plt.legend(['n=1', 'n=3', 'n=5'])
plt.show()