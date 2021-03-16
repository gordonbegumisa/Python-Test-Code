import random
import sys
from pylab import *
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

def random_walk():
    N = 200 # number of steps
    # set up storage space
    x = zeros(N)
    t = range(N)
    # Do the walk
    for i in range(1, N):
        if choice(['forward', 'back']) == 'back':
            x[i] = x[i-1] - 1.0  # take a step back
            print('back')
        else:
            x[i] = x[i-1] + 1.0  # take a step forward
            print('forward')
        print(x[i])
        RMS = array([np.sqrt(i*i) for i in x])
        plt.plot(t, x, linewidth=0.2, c='blue')
        plt.plot(t, RMS, linewidth=0.2, c='red')
    plt.title('1−D Random  Walk')
    plt.xlabel('Time(Step number)')
    plt.ylabel('Displacement and RMS position (Steps)')
    plt.legend(['Random Walk', 'RMS'])
    plt.savefig('walk1.png')
    show()
    return(0)

def power (x, a, b) :
    return a*x**b

def random_walk_average() :
    steps = 200 # number of steps
    boys = 2000 # number of fratboys
    # set up storage space
    x = zeros([steps + 1])
    t = range(steps + 1)
    xsum = zeros([steps + 1])
    x2sum = zeros([steps + 1])
    # Do the walks
    for j in range(boys):
        for i in range(1, steps):
            if choice([0, 1]):
                x[i] = x[i - 1] - 1
            else:
                x[i] = x[i + 1] + 1
        # add x , x ^2 to running sums
        for i in range(steps) :
            xsum[i] = xsum[i] + x[i]
            x2sum[i] = x2sum[i] + x[i]**2
    # rescale averages
    xavg = [float(i)/float(boys) for i in xsum]
    RMS = [sqrt(float(i)/float(boys)) for i in x2sum]

    plt.plot(t, xavg, c='blue')
    plt.plot(t, RMS, c='red')
    plt.title('AVERAGE 1−D Random  Walk')
    plt.xlabel('Time (Step number)')
    plt.ylabel('Average and RMS position (Steps)')
    plt.legend(['Average','RMS'])


    # Check least squares fit , see what the power dependence is.
    # I assume that the RMS displacement goes as D = A t B
    popt, pcov = curve_fit(power, t, RMS)
    print("Power  it : y ( t ) = A*t^B: ")
    print("A = %f +/- %f . " % (popt[0], np.sqrt(pcov[0, 0])))
    print("B = %f +/- %f . " % (popt[1], np.sqrt(pcov[1, 1])))

    # Plot the curve fit on top of that last graph
    plt.plot(t, power(t, popt[0], popt[1]), c='green')
    plt.savefig('walk2.png')
    plt.show()

def diffusion():
    # Allow animation
    ion()
    # set up graph window
    figure(figsize = (10 ,10))

    # Define droplet coordinates(all droplets) to be at point 100 ,100.
    atoms = ones([400, 2 ]) * 100
    line = plot(atoms[: , 0], atoms[:, 1] , 'ro')
    xlim(0,200)
    ylim(0,200)
    draw()
    #wait = raw_input("Press return to continue ")
    # How many steps to take ?
    N = int(sys.argv[1])
    for i in range(N):
        # Go through all atoms
        for j in range(400):
            # Move each atom ( or not ) in the x and/ or y direction.
            atoms[j, 0] += randint(-1, 1)
            atoms[j, 1] += randint(-1, 1)
            # Check for boundary collision
            x,y = (atoms[j, 0], atoms[j, 1])
            if x == 200:
                atoms[j, 0] = 198
            elif x == 0:
                atoms[j, 0] = 2
            if y == 200:
                atoms[j, 1] = 198
            elif y == 0:
                atoms[j, 1] = 2
            # See how things look now.
            line.setxdata(atoms[:, 0])
            line.setydata(atoms[:, 1])
            draw()
    #wait = raw_input ("Press return to exit")

#random_walk()
#random_walk_average()
diffusion()






