# Comparason of Caclulating pi
from decimal import *
import math
import numpy as np

#Sets decimal to 50 digits of precision
getcontext().prec = 50

def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)

def chudnovskyBig(n): #http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi

def gordon(n):
    x = math.radians(n)
    pi = math.radians(180)*np.sin(x)/(x*np.sin(math.radians(90)-(x/2)))
    return pi

#print ("\t\t\t Plouff \t\t Bellard \t\t\t Chudnovsky")
print ("\t\t\t Gordon \t\t \t\t\t Chudnovsky")
n = 0.001
for i in range(1,20):
    #print("Iteration number ",i, " ", plouffBig(i), " " , bellardBig(i)," ", chudnovskyBig(i))
    print("Iteration number ", i, " ", n, Decimal(gordon(n)), " ", chudnovskyBig(i))
    # print(n, Decimal(gordon(n)))
    n = n * 0.00001

error = Decimal(chudnovskyBig(i)) - Decimal(gordon(n))
print(error)