import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
sns.set()


x = np.linspace(-2, 2, 100)
y = np.sin(x)
y1 = x - (x**3)/3
y2 = y1 + (x**5)/5

plt.figure()
plt.plot(x, y); plt.plot(x, y1); plt.plot(x, y2)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(['sine(x)','x - (x^3)/3', 'x + (x^5)/5'])
plt.show()