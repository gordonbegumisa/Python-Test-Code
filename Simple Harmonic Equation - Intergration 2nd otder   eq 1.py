import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(x,t):
    y = x[0]
    dy=x[1]
    K=.05
    xdot=[[],[]]
    xdot[0] = dy
    xdot[1] = -(K*dy) - np.sin(y)
    return xdot

y0= 10*np.pi/180
t = np.linspace(0, 100, 800)
z2 = odeint(model, [0,y0], t)

plt.plot(t,z2[:,0])
plt.plot(t,z2[:,1])
plt.title('Damped Pendulum Motion .ODEInt()')
plt.legend(["y", "dy/dt"])
plt.xlabel('t')
plt.savefig('harmonic3.png')
plt.show()

#Plot Phase-Space
plt.plot(z2[:,0],z2[:,1])
plt.title('Damped Pendulum Motion in Phase Space')
plt.xlabel('y')
plt.ylabel('dy/dt')
plt.savefig('harmonic4.png')
plt.show()