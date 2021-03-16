import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g = 9.8
L = 2
mu = .01

THETA_0 = np.pi/3 #60 degrees
THETA_DOT_0 = 0 # No initual angular velocity

#Definition of ODE
def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g/L) *np.sin(theta)


#Solution tothe differential equation
def theta(t):
    # Initialize changing values
    theta = THETA_0
    theta_dot = THETA_DOT_0
    delta_t = 0.01
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot+= theta_double_dot * delta_t
    return theta

tlimit=500
t=0
t1=.1
for i in range(tlimit):
    y = theta(t)
    plt.scatter(t,y)
    t+=t1
plt.show()