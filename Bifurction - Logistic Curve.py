import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)

def logistic_curve(r,x):

    a = -(r*x)
    b = np.exp(a)
    c = (1/x) - 1
    y = 1/(1 + (b*c))
    return y

n = 600; r = 1; x = .1; rate = 0.005

for i in range(n):
    x1 = logistic(r, x)
    plt.scatter(r,x, s = 0.2, c = 'black')
    r = r + rate
    x = x1

plt.title('Bifurcation Diagramme')
plt.xlabel('r')
plt.ylabel('x')
plt.savefig('bx.png')
plt.show()

t = -0.5
r = 1.6
deltaT = 0.01
deltaR = 0.3

ilimit = 1  # Number of Curves
jlimit = 200 # Iretations per curve


for i in range(ilimit):
    for j in range(jlimit):
        n = logistic_curve(r,t)
        print(r,t,n)
        plt.scatter(t,n, s = 0.2, c = 'black')
        t = t + deltaT

    r = r + 0.05

plt.title('Logistic Curve (r = 1.6) ')
plt.xlabel('t')
plt.ylabel('N')
plt.savefig('bx1.png')
plt.show()




