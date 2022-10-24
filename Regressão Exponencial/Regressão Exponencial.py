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

def calc_exp_coeffs(X, Y, expoent):
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

def build_exp(coeffs):
    def f(x):
        return coeffs['a']*coeffs['k']**(coeffs['b']*x) - coeffs['c']
    return f

def calc_exp_coeffs_inverse(X, Y, expoent):
    const = min(X)
    if(const <= 0):
        const = abs(const) + 1
    else:
        const = 0

    linearized_X = [log(xi + const, expoent) for xi in X]
    coeffs = calc_coeffs(linearized_X, Y)

    b = coeffs[0]
    a = coeffs[1]
    m = expoent
    k = const

    return {'a' : a, 'b' : b, 'm' : m, 'k' : k}

def build_exp_inverse(coeffs):
    def f(x):
        return coeffs['b'] + coeffs['a']*log(x+coeffs['k'], coeffs['m'])
    return f

if __name__ == '__main__':

    # Exemplo 01:
    X = [0.0202, 0.0914, 0.1416, 0.1667, 0.2266, 0.3154, 0.335, 0.4089, 0.4679, 0.5171, 0.5905, 0.6387, 0.7131, 0.7527, 0.8102, 0.8425, 0.8921, 0.9473, 1.0221, 1.0796, 1.1121, 1.1826, 1.2454, 1.3067, 1.3656, 1.4166, 1.4982, 1.5326, 1.5562, 1.6396, 1.7149, 1.7656, 1.8161, 1.8879, 1.9055, 1.9838]
    Y = [4.397, 5.1077, 6.5344, 7.5504, 4.8005, 5.7035, 5.1387, 5.9875, 6.831, 7.3067, 7.7048, 7.2332, 8.953, 9.0576, 10.0124, 9.405, 11.3052, 12.3553, 13.0991, 12.6969, 13.5873, 15.7953, 15.1653, 16.9946, 18.6564, 18.8157, 21.0904, 21.7505, 22.4597, 24.6642, 25.8545, 27.892, 30.2306, 34.2837, 33.172, 36.0403]
    values = [0.2608, 0.3236, 0.5979, 1.9546, 1.96]
    expoent = 2

    coeffs = calc_exp_coeffs(X, Y, expoent)     
    f = build_exp(coeffs)

    t = np.linspace(min(X), max(X), 100)
    ft = [f(ti) for ti in t]

    #print(f"function f aplied in the choosen values: {[f(value) for value in values]}")
    #print(f"coeffs = {coeffs}")    

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()

    # Exemplo 02:
    X = [1.3496, 1.9498, 3.1147, 3.6402, 4.66, 5.3863, 5.5916, 6.5049, 7.6301, 8.0992, 8.5171, 9.6802]
    Y = [5.4398, 6.3005, 7.3701, 7.692, 8.4826, 8.6278, 8.7415, 9.0914, 9.3739, 9.5324, 9.7319, 10.0403]
    values = [2.847, 4.2114, 7.6937]
    expoent = e

    coeffs = calc_exp_coeffs_inverse(X, Y, expoent)     
    f = build_exp_inverse(coeffs)

    t = np.linspace(min(X), max(X), 100)
    ft = [f(ti) for ti in t]

    print(f"function f aplied in the choosen values: {[f(value) for value in values]}")
    print(f"coeffs = {coeffs}")    

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo02.png")
    plt.close()

    pass

# Como transforma uma equação do tipo y = a.k^(b.x) - c em um equação de reta que possa ser utilizada em regressão linear:
#
# (1) Realizando manipulações algébricas para facilitar a resolução do problema (algo que solucionará o problema para caso de valores...
# ... negativos existentes na lista de coordenadas Y):
#
# y + c = a.k^(b.x)
#
# (2) Aplicando logaritmo (de base k) em ambos os lados temos:
#
#   log(y + c) = log(a.k^(b.x))
#
#   log(y + c) = log(a) + log(k^(b.x))
#
#   log(y + c) = log(a) + b.x.log(k)
# 
#   log(y + c) = log(a) + b.x
# 
# Note portanto que somando c à todos os valores da lista de coordenadas Y e aplicando o logaritmos nos elementos da lista resultante...
# ... teremos uma lista na qual poderemos aplicar uma regressão linear, porém, qual valor de c devemos utilizar?
# - Visto que nos valores da lista de coordenadas será aplicado logaritimo de base k e o argumento de um logaritimo não pode ser negativo...
# ... e nem igual à 0, teremos que:
#
#       (i) c = 0, se min(coordenadas y) > 0;
#
#       (i) c = min(coordenadas y) + h, onde h > 0, se min(coordenadas y) <= 0;
#
# E assim função f dada pela regressão deve ser do tipo:
#
#       f(x) = log(y + c) = a0 + a1.x 
#
# Note que, para obter y podemos aplicar os dois lados da equação como expoentes de k, assim:
#
#       k^[log(y + c)] = k^(a0 + a1.x)
#
#       y + c = [k^(a0)].[k^(a1.x)]
#
# Note que podemos definir que k^(a0) = a e b = a1, assim temos:
#
#       y + c = a.k^(b.x)
#
#       y = a.k^(b.x) - c
#
# Que é por sua vez a equação exponencial desejada inicialmente.