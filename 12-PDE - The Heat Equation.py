import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d


def sine_wave():
    xlimit = 2*np.pi
    N =  360
    delta_x = xlimit/N
    x = 0

    for i in range(0,N):
        x = x + delta_x
        y = np.sin(x)
        plt.scatter(x,y, s=0.5, c='black')

    plt.title('Sine Curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('PDE1.png')
    plt.show()

def cosine_wave():
    xlimit = 2*np.pi
    N =  360
    delta_x = xlimit/N
    x = 0

    for i in range(0,N):
        x = x + delta_x
        y = np.cos(x)
        plt.scatter(x,y, s=0.5, c='black')

    plt.title('Sine Curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('PDE1.png')
    plt.show()

def heat_curve():
    x = 0
    t = 0
    N = 50
    L = 1000
    xlimit = L
    delta_x = xlimit/N
    delta_t = 1
    alfa = 750
    ax = plt.axes(projection='3d')
    for i in range(0, N):
       for j in range(0, N):
            T = np.cos(3*x*(np.pi/L))*np.exp(-alfa*t*(3*np.pi/L)**2)
            ax.scatter(x,t,T, color='black', s=0.2)
            x = x + delta_x
       t = t + delta_t
       x = 0
    ax.set_xlabel('T')
    ax.set_ylabel('t')
    ax.set_xlabel('x')
    plt.show()

               
#sine_wave()
#cosine_wave()
heat_curve()