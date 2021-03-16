import numpy as np
from matplotlib import pyplot as plt

def golden(x):
    y = 1 + 1 / x
    return(y)

# Initial Conditions
xlimit = np.pi
N =  80
delta_x = xlimit/N
x = 0.5

#Iterate
for i in range(0,N):
    x = x + delta_x
    y = golden(x)
    y1 = x
    plt.scatter(x,y, s=0.2, c='black')
    plt.scatter(x, y1, s=0.2, c='green')

plt.title('Golden Ratio')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('golden.png')
plt.show()








