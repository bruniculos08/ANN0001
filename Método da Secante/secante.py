from math import *

def f(x): 
    return pi*x - exp(x)
    
def aproximateDerivative(x1, x0):
    return (f(x1)-f(x0))/(x1-x0)

def secante(x1, x0, n):
    for i in range(n):
        x2 = x0 - f(x0)/aproximateDerivative(x1, x0)
        #x2 = (x0*f(x1) - x1*f(x0))/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
    print(x2)

vetor = [1, 3, 5]
x0 = 0.83824
x1 = 2.05516
for n in vetor:
    secante(x1, x0, n)