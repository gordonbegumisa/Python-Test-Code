import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(x,t):
    y = x[0]
    dy = x[1]
    K = 30
    xdot = [[], []]
    xdot[0] = dy
    xdot[1] = - (0.9 + 0.7 * t) * dy - K * y
    return xdot


t = np.linspace(0, 2, 100)
z2 = odeint(model, [2, -1], t)

plt.plot(t, z2[:, 0], 'g:')
plt.plot(t, z2[:, 1], 'k-.')
plt.title('Plots Using ODEInt() Python')
plt.legend(["y", "dy/dt"])
plt.xlabel('t')
plt.savefig('17-SHE-02.png')
plt.show()