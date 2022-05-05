# Fourier Series to Approximate the Step Function

import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
sns.set()

x = np.linspace(-1, 1, 500)
y = 1
i = 1

while i < 31:
    y += 4*np.sin(i*np.pi*x)/i
    col = (np.random.random(), np.random.random(), np.random.random())
    plt.plot(x, y, color=col)
    i += 2

plt.title('Fourier Series to Approximate the Step Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig('05-Fourier Series2.png')
plt.show()
