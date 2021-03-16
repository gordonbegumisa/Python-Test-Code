from decimal import *

#Sets decimal to 50 digits of precision
getcontext().prec = 50

phi = 11.28

for i in range(1,150):
    phi = Decimal(1 + 1/phi)
    print(i, phi)
