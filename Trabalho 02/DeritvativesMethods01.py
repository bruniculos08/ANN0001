# Métodos para derivadas:
import matplotlib.pyplot as plt
import numpy as np
from math import *

# Método das diferenças finitas(cálculo dos coeficientes):
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

# Método das diferenças finitas(cálculo da aproximação da derivada de acordo com os coeficientes encontrados...
# ... pela função anterior):
def get_aprox(X, coeffs, f):
    sum = 0
    for xi, ci in zip(X, coeffs):
        sum += ci*f(xi)
    return sum

# Contrução da fórmula de Taylor para n:
def build_taylor(X, x0, f, n):
    def p(x):
        poly = f(x0)
        for i in range(n):
            coeffs = diff_fin(X, x0, i+1)
            poly += get_aprox(X, coeffs, f) * (x - x0)**(i+1) / factorial(i+1)
        return poly
    return p

# Método de extrapolação de Richardson:
def richardson(f, x0, h, k):
    table = []
    for i in range(k):
        item = F1(f, x0, h/(2**i))
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((2**(i+1))*table[j+1] - table[j])/(2**(i+1) - 1)
            table[j] = new_item

    return table[0]

# Função usada no método de extrapolação de Richardson:
def F1(f, x0, h):
    return (f(x0+h) - f(x0))/h

# Método de extrapolação de Richardson usando:
def richardson_alternative(approximations, k):
    # Note que aproximantion[i] é a função F1 calculada na linha i do método, ou seja, com F1(h/2**i):
    table = []
    for i in range(k):
        item = approximations[i]
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((2**(i+1))*table[j+1] - table[j])/(2**(i+1) - 1)
            table[j] = new_item

    return table[0]

