import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(x,t):
    y = x[0]
    dy = x[1]
    xdot = [[], []]
    xdot[0] = dy
    xdot[1] = -np.sin(y) - (0.5*dy) + 1.5*np.cos(0.9*t)
    return xdot


y0 = 80*np.pi/180
t = np.linspace(-30, 70, 1200)
z2 = odeint(model, [-1, y0], t)

plt.scatter(t, z2[:, 0], s=0.5 )
plt.scatter(t, z2[:, 1], s=0.5)
plt.title('Damped Driven Pendulum Motion .ODEInt()')
plt.legend(["y", "dy/dt"])
plt.xlabel('t')
plt.savefig('20-SHE-07.png')
plt.show()

# Plot Phase-Space
plt.scatter (z2[:, 0], z2[:, 1], s=0.5, c='blue')
plt.title('Damped Driven Pendulum Motion in Phase Space')
plt.xlabel('Angle (y)')
plt.ylabel('Angular Velocity (dy/dt)')
plt.savefig('21-SHE-08.png')
plt.show()