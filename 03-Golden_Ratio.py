# Calculating Euler's Constant by infinite series

from decimal2 import *
import math

# Sets decimal to n digits of precision
getcontext().prec= 100

limit=150
counter = 1
x = 1

# Recursion Function
def phi(x,counter,limit):
    if counter >= limit:
        return (0)
    else:
        x= Decimal(1 + (1/x))
        counter+=1; print (counter,x)
        return(phi(x,counter,limit))

y = phi(x,counter, limit)

# Using a for loop
ph=11

for i in range(1, limit):
    ph=Decimal(1 + 1/ph)
    print(i, ph)












