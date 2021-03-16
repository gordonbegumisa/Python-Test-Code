import numpy as np
from scipy.integrate  import ode
from scipy.misc import derivative
import matplotlib.pyplot as plt

theta_0 = np.pi/180*10  # 10 Degrees
g = 9.8
L = 1

def harmonic(t):
    y = theta_0*np.cos(np.sqrt(g/L)*t)
    return y
def velocity(t):
    y = derivative(harmonic, t, dx=0.01, order=5)
    return y

ilimit = 200
delta_t = 0.01
t0=0
t=t0
# Iterations for harmonicApprox function
#for i in range(ilimit):
#    plt.scatter(t,harmonicApprox(t), s = 0.2, c = 'green')
 #   t+= delta_t

for i in range(ilimit):
    plt.scatter(harmonic(t), velocity(t), s=0.2, c='red')
    t += delta_t

plt.savefig('harmonic1.png')
plt.show()