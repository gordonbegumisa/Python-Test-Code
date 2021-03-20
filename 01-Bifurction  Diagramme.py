# This code plots a simple bifurcation diagram for the logistic map using a while loop

import matplotlib.pyplot as plt


def logistic(rn, xn):
    return rn * xn * (1 - xn)


r = 1
x = 0.1
r_limit = 4
r_points = 5000
r_rate = (r_limit - r)/r_points

while r < r_limit:
    x = logistic(r, x)
    plt.scatter(r, x, s=0.2, c='black')
    r = r + r_rate

plt.title('Bifurcation Diagram')
plt.xlabel('r')
plt.ylabel('x')
plt.savefig('01-Bifurcation.png')
plt.show()
