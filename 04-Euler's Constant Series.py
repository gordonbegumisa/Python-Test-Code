# Calculating Euler's Constant by infinite series
# Have concluded that this formula has a precision limited to 16 decimal places.

from decimal import *
import math
import numpy as np

limit = 50
getcontext().prec = limit # Sets decimal to n digits of precision
e = 1

for n in range(1, limit*2):
    e = Decimal(e + 1/Decimal(math.factorial(n)))
    print('n =\t', n,  '\te =\t', e)
enp = Decimal(np.exp(1))
error = Decimal(enp - e)

print('\ne (numpy) =\t\t', enp)
print('\nerror =\t\t\t ', error)




