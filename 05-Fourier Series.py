import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
sns.set()

x = np.linspace(-2, 2, 400)
y = (4*(np.sin(np.pi*x)) + (np.sin(3*np.pi*x))/3 + (np.sin(5*np.pi*x))/5 + np.sin(7*np.pi*x))/np.pi
y1 = y + 4*((np.sin(11*np.pi*x))/11 + (np.sin(13*np.pi*x))/13 + (np.sin(15*np.pi*x))/15 + (np.sin(17*np.pi*x))/17)/np.pi
plt.plot(x, y);plt.plot(x, y1)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(['a','b'])
plt.savefig('05-Fourier Series.png')
plt.show()