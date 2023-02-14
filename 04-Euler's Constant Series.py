# calculates Euler's constant (also known as e) using an infinite series. The code sets the precision of Decimal objects to 50 decimal places using the getcontext().prec method, and then iteratively calculates the value of e using the formula e = 1 + 1/1! + 1/2! + 1/3! + ....
#The code then compares the calculated value of e to the value of e calculated using the exp() function from the NumPy library, which is a more precise way of calculating e. The difference between these two values is then printed as the error.


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




