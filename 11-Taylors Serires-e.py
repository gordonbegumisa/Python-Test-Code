import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
sns.set()


x = np.linspace(-2, 2, 100)
y = np.exp(-x**2)
y1 = 1 - x**2
y2 = y1 + (0.5*x**4)

plt.figure()
plt.plot(x, y); plt.plot(x, y1); plt.plot(x, y2)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(['y = e^-(x^2)','y = 1 - x^2', 'y = 1 - x^2 + (x^4)/2'])

x = np.linspace(-5, 5, 100)
y = np.exp(x)
y1 = 1 + x
y2 = y1 + (x**2)/2
y3 = y2 + (x**3)/6

plt.figure()
plt.plot(x, y); plt.plot(x, y1); plt.plot(x, y2)
plt.xlabel('x');plt.ylabel('y')
plt.legend(['y = e^x','y = 1 + x', 'y = 1 + x^2/2 + (x^3)/6'])
plt.show()