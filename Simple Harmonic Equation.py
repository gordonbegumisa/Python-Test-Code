import numpy as np
from scipy.integrate  import odeint
import matplotlib.pyplot as plt

theta_0 = np.pi/180*10  # 10 Degrees
g = 9.8
L = 1

def harmonicApprox(t):
    y = theta_0*np.cos(np.sqrt(g/L)*t)
    return y

def harmonic(y,t):
    dydt =  -g*np.sin(y)/L
    return dydt

ilimit = 900
delta_t = 0.01
t0=0
t=t0
# Iterations for harmonicApprox function
for i in range(ilimit):
    plt.scatter(t,harmonicApprox(t), s = 0.2, c = 'green')
    t+= delta_t

#Intergration for harmonic function
# time points
t = np.linspace(0,9)
# solve ODE
z = odeint(harmonic,t0,t)
plt.scatter(t, z, s=0.2, c='red')

plt.savefig('harmonic.png')
plt.show()