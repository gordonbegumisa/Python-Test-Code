import random
from pylab import *
import numpy as np
from scipy.optimize import curve_fit

def randomwalk():
    N = 200 # number of steps
    # set up storage space
    x = zeros(N)
    t = range(N)
    # Do the walk
    for i in range(1,N):
        if choice(['forward','back']) == 'back':
            x[i] = x[i-1] - 1.0  # take a step back
            print('back')
        else:
            x[i] = x[i-1] + 1.0  # take a step forward
            print('forward')
        RMS = array([np.sqrt(i*i) for i in x])
        print(x[i])
    plot(t ,x, c='blue')
    plot(t ,RMS, c='red')
    show()
    return(0)

def power (x , a , b ) :
    return a*x**b

def randomwalk1() :
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
            if choice([0,1]):
                x[i] = x[i-1] - 1
            else:
                x[i] = x[i+1] + 1
        # add x , x ^2 to running sums
        for i in range(steps) :
            xsum[i] = xsum[i] + x[i]
            x2sum[i] = x2sum[i] + x[i]**2
    # rescale averages
    xavg = [float(i)/float(boys) for i in xsum]
    RMS = [sqrt(float(i)/float(boys)) for i in x2sum]
    xlabel("Time ( Step number ) ")
    ylabel("Average and RMS position ( Steps ) ")
    plot(t, xavg, c='blue')
    plot(t, RMS, c='red')

    # Check least squares fit , see what the power dependence i s .
    # I assume that the RMS displacement goes as D = A t B
    popt, pcov = curve_fit(power, t, RMS)
    print("Power  it : y ( t ) = A*t^B: ")
    print("A = %f +/- %f . " % (popt[0], np.sqrt(pcov[0, 0])))
    print("B = %f +/- %f . " % (popt[1], np.sqrt(pcov[1, 1])))

    # Plot the curve fit on top of that last graph
    plot(t, power(t, popt[0], popt[1]), c='green')
    show()
randomwalk1()





