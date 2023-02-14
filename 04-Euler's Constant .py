# Calculating Euler's Constant by infinite series

from m3-cdecimal import *
import math

# Sets decimal to n digits of precision
getcontext().prec = 50

e = 1

for n in range (1,50):
    e = cdecimal(e + 1/Decimal(math.factorial(n)))
    print(n, e)