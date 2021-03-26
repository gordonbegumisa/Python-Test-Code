# This code plots a simple bifurcation diagram for the logistic map using a while loop

import matplotlib.pyplot as plt
import numpy as np


def logistic(rn, xn):
    return rn * xn * (1 - xn)

r = 1
x = 0.1
r_limit = 4
r_points = 5000

r = np.linspace(r, r_limit, r_points)
x = logistic(r, x)
plt.scatter(r, x, s=0.2, c='black')

plt.title('Bifurcation Diagram')
plt.xlabel('r')
plt.ylabel('x')
plt.show()
