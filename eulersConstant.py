import math

def  eulerConstant(n):
    e = (1+((complex(0,1)*math.pi)/n))**n
    return e

for n in range(1,200,20):
    print("n= ",n, " (1 + i*pi/n)**n = ", eulerConstant(n))



