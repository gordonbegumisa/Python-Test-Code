import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

x = np.linspace(0, 5, 50)

plt.plot(x,np.sin(x))
plt.plot(x,-np.cos(x))
plt.plot(x,-np.sin(x))

plt.title('Wave Function(x)')
plt.xlabel('x')

plt.legend(['Sin(x)', '-Cos(x)', '-Sin(x)'])
plt.show()
