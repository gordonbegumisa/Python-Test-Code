import numpy as np
import matplotlib.pyplot as plt

def logistic_curve(r,x):
    return 1/(1 + (np.exp(-r * x)*((1/x) - 1)))

t_start = -0.5; t_end = 1.5; t_points = 50; r = 1.6

t = np.linspace(t_start,t_end,t_points)
plt.plot(t,logistic_curve(r,t), color = 'black')

plt.title('Logistic Curve (r = 1.6) ')
plt.xlabel('Time (t)')
plt.ylabel('Population (y)')
plt.savefig('02-Logistic Curve.png')
plt.show()




