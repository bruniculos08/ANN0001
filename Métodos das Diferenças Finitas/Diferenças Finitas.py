# Note que pela fórmula de Taylor temos que:
#
# (i) para polinômios de grau menor igual à 1 tem-se:
#
#    f'(x0) = (1/h).f(x0+h) - (1/h).f(x0) ou f'(x0) = (1/h).f(x0) - (1/h).f(x0-h)
#
# (ii) para polinômios de grau menor igual à 2 tem-se:
#
#    f'(x0) = (1/(2.h)).f(x0+h) + 0.f(x0) - (1/(2.h)).f(x0-h)
#
# (iii) para polinômios de grau menor igual à 3 tem-se:
#
#   f''(x0) = (1/h²).f(x0-h) - (2/h²).f(x0) + (1/h²).f(x0+h)
#  
# Note que nas respectivas fórmulas estamos atribuindo pesos para valores da função calculados em determinados pontos, assim pode ser possível...
# ... determinar uma fórmula do tipo:
#
#   f'k(x0) ~ c1.f(x1) + c2.f(x2) + ... + cn.f(xn)
#   
# tal que essa expressão seja exata em polinômios de grau menor igual à n-1. Em particular essa fórmula será exata

from math import *
import numpy as np

def diff_fin(X, x0, k):
    n = len(X)
    A = []
    B = []

    for i in range(n):
        row = []
        for xi in X:
            row.append(xi**i)
        A.append(row)
        if i < k:
            B.append(0)
        else:
            # como i varia de 0 até n-1 e não de 1 até n tem-se:
            b = (factorial(i)/factorial(i-k))*(x0**(i-k))
            B.append(b)

    return np.linalg.solve(A, B)

def get_aprox(X, coeffs, f):
    sum = 0
    for xi, ci in zip(X, coeffs):
        sum += ci*f(xi)
    return sum

def build_taylor(X, x0, f, n):
    def p(x):
        poly = f(x0)
        for i in range(n):
            coeffs = diff_fin(X, x0, i+1)
            poly += get_aprox(X, coeffs, f) * (x - x0)**(i+1) / factorial(i+1)
        return poly
    return p

if __name__ == '__main__':

    # Exemplo 01:
    X = [7.1146, 7.1457, 7.3827]
    x0 = 7.223
    k = 2
    def f(x): 
        return exp(cos(x)**2) + exp(-x**2) + log(x)
    

    coeffs = diff_fin(X, x0, k)
    string = "'"*k
    #print(f"f{string}({x0}) ~ {get_aprox(X, coeffs, f)}")

    # Exemplo 02:
    X = [-1.57, -1.5414, -1.5003, -1.4799, -1.437, -1.4016, -1.3725, -1.3408, -1.2835, -1.2723, -1.2221, -1.1958, -1.1529, -1.1314, -1.1017]
    x0 = -1.3311
    k = 5
    def f(x):
        return x**2 * exp(-x) * cos(x) + 1

    
    coeffs = diff_fin(X, x0, k)
    string = "'"*k
    #print(f"f{string}({x0}) ~ {get_aprox(X, coeffs, f)}")

    
    # Exemplo 3:
    X = [0.1933, 0.2334, 0.2667, 0.3575, 0.3771, 0.4527, 0.491, 0.5263, 0.5926, 0.6308]
    x0 = 0.408
    n = 5
    def f(x):
        return x**2 * cos(x - 1) * exp(-3 * x ** 2)

    taylor = build_taylor(X, x0, f, n)
    values = [0.3402, 0.344, 0.3911, 0.3923, 0.4879]

    for value in values:
        #print(f"p({value}) = {taylor(value):.10e}")
        print(f"{taylor(value):.10e}, {abs(f(value)-taylor(value)):.10e},")
        #print(f"|f({value})-p({value})| = {abs(f(value)-taylor(value)):.10e}")

    pass