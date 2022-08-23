from math import *

def f(x): 
    return sqrt(x)-cos(x)

def aproximateDerivative(x1, x0):
    return (f(x1)-f(x0))/(x1-x0)

def secante(x1, x0, n):
    for i in range(n):
        #x1 = x0 - f(x0)/aproximateDerivative(x1, x0)
        x1 = (x0*f(x1) - x1*f(x0))/(f(x1)-f(x0))
    print(x1)

vetor = [1, 2, 3, 4, 5]
x0 = 0.05656
x1 = 1.32765
for n in vetor:
    secante(x1, x0, n)