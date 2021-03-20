# Fourier Series to Approximate the Step Function

import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
sns.set()

x = np.linspace(-1, 1, 500)

y1 = (4*(np.sin(np.pi*x) + np.sin(3*np.pi*x)/3 + np.sin(5*np.pi*x)/5 + np.sin(7*np.pi*x)/7 + np.sin(9*np.pi*x)/9))/np.pi
y2 = y1 + 4*(np.sin(11*np.pi*x)/11 + np.sin(13*np.pi*x)/13 + np.sin(15*np.pi*x)/15 + np.sin(17*np.pi*x)/17)/np.pi

plt.plot(x, y1)
plt.plot(x, y2)

plt.title('Fourier Series to Approximate the Step Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x) ', 'f(x) with more accuracy'])
plt.savefig('05-Fourier Series.png')
plt.show()
