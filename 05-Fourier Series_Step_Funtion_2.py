# Fourier Series to Approximate the Step Function

import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
sns.set()

x = np.linspace(-1, 1, 500)
y = 0
i = 1
limit = 32

while i < limit:
    y += 4*np.sin(i*np.pi*x)/(i*np.pi)
    i += 2
    col = (np.random.random(), np.random.random(), np.random.random())
    plt.plot(x, y, color=col)

plt.title('Fourier Series to Approximate the Step Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig('05-Fourier Series2.png')
plt.show()
