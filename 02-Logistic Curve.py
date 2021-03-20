# This code plots a simple logistic curve for a growing population of N
# and an r value of 1.6

import numpy as np
import matplotlib.pyplot as plt


def logistic_curve(r, x):
    return 1/(1 + (np.exp(-r * x)*((1/x) - 1)))


t_start = -0.5
t_end = 1.5
t_points = 50
rr = 1.6

t = np.linspace(t_start, t_end, t_points)
plt.plot(t, logistic_curve(rr, t), color='black')

plt.title('Logistic Curve (r = 1.6) ')
plt.xlabel('Time (t)')
plt.ylabel('Population (N)')
plt.savefig('02-Logistic Curve.png')
plt.show()




