import numpy as np
from scipy.integrate  import odeint
import matplotlib.pyplot as plt

theta_0 = np.pi/180*10  # 10 Degrees
g = 9.8
L = 1

def harmonicApprox(t):
    y = theta_0*np.cos(np.sqrt(g/L)*t)
    return y

def harmonic(x,t):
    y = x[0]
    dy = x[1]
    xdot = [[], []]
    xdot[0] = dy
    xdot[1] = -g*np.sin(y)/L
    return xdot

ilimit = 1800
delta_t = 0.01
t0=0
t=t0
# Iterations for harmonicApprox function
for i in range(ilimit):
    plt.scatter(t,harmonicApprox(t), s = 0.2, c = 'green')
    t+= delta_t

# Harmonic Function
t = np.linspace(0,ilimit/100,ilimit)
z2 = odeint(harmonic,[theta_0,0],t)

plt.scatter(t,z2[:,0], s=0.2, c='red')
#plt.scatter(t,z2[:,1],s=0.2, c='blue')

plt.title('Simple Harmonic Motion - Comparason')
plt.xlabel('t')
plt.ylabel('y()')
plt.legend(["Approximation for sin(theta)=theta", "dy/dt (ODEInt Python)"])
plt.savefig('16-SHE-01-harmonic.png')
plt.show()