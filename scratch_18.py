import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

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
sine_wave()







