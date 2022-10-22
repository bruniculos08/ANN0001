import random as random
from math import *
import matplotlib.pyplot as plt
import numpy as np


def calc_coeffs(X, Y):

    # (1) Cria a matriz do lado esquerdo da equação:
    X_matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            sum = 0
            for xi in X: 
                sum += xi ** (i + j)
            row.append(sum)
        X_matrix.append(row)

    # (2) Cria a matriz do lado direito da equação:
    

    Y_matrix = []
    for i in range(2):
        sum = 0
        for xi, yi in zip(X, Y):
            sum += yi*(xi**i)
        Y_matrix.append(sum)

    return np.linalg.solve(X_matrix, Y_matrix)

def build_poly(coeffs):
    def func(x):
        result = 0
        for i, ci in enumerate(coeffs):
            result += ci*(x**i)
        return result
    return func

def calc_pot_coeffs(X, Y, expoent):
    const = min(Y)
    if(const <= 0):
        const = abs(const) + 1
    else:
        const = 0

    linearized_Y = [log(yi + const, expoent) for yi in Y]
    coeffs = calc_coeffs(X, linearized_Y)

    # Considerando a equação exponencial na forma y = a.k^(b.x) - c
    a = expoent**(coeffs[0])
    b = coeffs[1]
    k = expoent
    c = const

    return {'a' : a, 'b' : b, 'k' : k, 'c' : c}
    
def build_pot(coeffs):
    def f(x):
        return coeffs['a']*coeffs['k']**(coeffs['b']*x) - coeffs['c']
    return f

if __name__ == '__main__':

    # Exemplo 01:
    X = [0.0202, 0.0914, 0.1416, 0.1667, 0.2266, 0.3154, 0.335, 0.4089, 0.4679, 0.5171, 0.5905, 0.6387, 0.7131, 0.7527, 0.8102, 0.8425, 0.8921, 0.9473, 1.0221, 1.0796, 1.1121, 1.1826, 1.2454, 1.3067, 1.3656, 1.4166, 1.4982, 1.5326, 1.5562, 1.6396, 1.7149, 1.7656, 1.8161, 1.8879, 1.9055, 1.9838]
    Y = [4.397, 5.1077, 6.5344, 7.5504, 4.8005, 5.7035, 5.1387, 5.9875, 6.831, 7.3067, 7.7048, 7.2332, 8.953, 9.0576, 10.0124, 9.405, 11.3052, 12.3553, 13.0991, 12.6969, 13.5873, 15.7953, 15.1653, 16.9946, 18.6564, 18.8157, 21.0904, 21.7505, 22.4597, 24.6642, 25.8545, 27.892, 30.2306, 34.2837, 33.172, 36.0403]
    values = [0.2608, 0.3236, 0.5979, 1.9546, 1.96]
    expoent = 2

    coeffs = calc_pot_coeffs(X, Y, expoent)     
    f = build_pot(coeffs)

    t = np.linspace(min(X), max(X), 100)
    ft = [f(ti) for ti in t]

    print(f"function f aplied in the choosen values: {[f(value) for value in values]}")
    print(f"coeffs = {coeffs}")    

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()

    pass

# Como transforma uma equação do tipo y = a.x^b - c em um equação de reta que possa ser utilizada em regressão linear:
#
# (1) Realizando manipulações algébricas temos:
#
#       y + c = a.x^b
#
# (2) Aplicando logaritmo de base natural em ambos os lados:
#
#       ln(y + c) = ln(a.x^b)
#
#       ln(y + c) = ln(a) + ln(x^b)
#
#       ln(y + c) = ln(a) + b.ln(x)