# This code plots a simple bifurcation diagram for the logistic map using a recursion

import matplotlib.pylab as plt

limit = 4.0
r = 1.0
x =0.01
delta_r = 0.005

def chaos(x,r,limit):
    if r >= limit:
        return(0)
    else:
        n = r*x*(1-x)
        x = n
        r += delta_r
        print(r, x)
        plt.scatter(r,x, color='black', s=0.1)
        return (chaos(x,r,limit))

z = chaos(x,r,limit)
plt.show()