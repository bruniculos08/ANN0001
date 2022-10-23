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

def calc_pot_coeffs(X, Y):
    const_Y= min(Y)
    if(const_Y <= 0):
        const_Y = abs(const_Y) + 1
    else:
        const_Y = 0

    const_X = min(X)
    if(const_X <= 0):
        const_X = abs(const_X) + 1
    else:
        const_X = 0

    linearized_X = [log(xi + const_X, e) for xi in X]
    linearized_Y = [log(yi + const_Y, e) for yi in Y]

    coeffs = calc_coeffs(linearized_X, linearized_Y)

    # Considerando a equação exponencial na forma y = a.k^(b.x) - c
    a = e**(coeffs[0])
    b = coeffs[1]
    c = const_Y
    k = const_X

    return {'a' : a, 'b' : b, 'k' : k, 'c' : c}
    
def build_pot(coeffs):
    def f(x):
        return coeffs['a']*(x + coeffs['k'])**(coeffs['b']) - coeffs['c']
    return f

if __name__ == '__main__':

    # Exemplo 01:
    X = [0.5126, 0.573, 0.6654, 0.7057, 0.7871, 0.839, 0.8638, 0.9288, 0.9927, 1.0747, 1.1316, 1.156, 1.2296, 1.2843, 1.3793, 1.4231, 1.46, 1.563, 1.5992, 1.6487, 1.7329, 1.7565, 1.8323, 1.8917, 1.9537, 2.0237, 2.0884, 2.1108, 2.1873, 2.267, 2.3021, 2.3839, 2.4503, 2.5089, 2.5705, 2.6377, 2.6636, 2.7247, 2.7873, 2.8298, 2.9127, 2.9983]
    Y = [0.2227, 1.1283, 0.1645, 0.0203, 0.7443, 0.8442, 0.6032, 0.9433, 1.2406, 3.8341, 2.0135, 2.8183, 3.2389, 3.341, 4.6893, 5.6199, 5.4493, 7.2853, 8.3757, 8.8673, 10.8298, 10.9226, 13.956, 15.4451, 17.0213, 19.808, 22.6852, 23.4231, 27.0152, 30.3488, 32.3376, 36.9758, 41.4058, 44.8341, 49.4973, 54.9113, 56.9, 61.2, 67.2643, 71.216, 78.7952, 89.2234]
    values = [0.6996, 0.8847, 2.1356, 2.7445, 2.9708]

    coeffs = calc_pot_coeffs(X, Y)     
    f = build_pot(coeffs)

    t = np.linspace(min(X), max(X), 100)
    ft = [f(ti) for ti in t]

    print(f"function f aplied in the choosen values: {[f(value) for value in values]}")
    print(f"coeffs = {coeffs}")    

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()

    # Exemplo 01:
    X = [2, 3, 5, 7]
    Y = [7, 10, 11, 12]
    values = [1, 2, 5, 7]

    coeffs = calc_pot_coeffs(X, Y)     
    f = build_pot(coeffs)

    t = np.linspace(min(X)-1, max(X)+1, 100)
    ft = [f(ti) for ti in t]

    print(f"function f aplied in the choosen values: {[f(value) for value in values]}")
    print(f"coeffs = {coeffs}")    

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo02.png")
    plt.close()

    pass

# Como transformar uma equação do tipo y = a.(x + k)^b - c em um equação de reta que possa ser utilizada em regressão linear:
#
# (1) Realizando manipulações algébricas temos:
#
#       y + c = a.x^b
#
# (2) Aplicando logaritmo de base natural em ambos os lados:
#
#       ln(y + c) = ln(a.(x+k)^b)
#
#       ln(y + c) = ln(a) + ln((x+k)^b)
#
#       ln(y + c) = ln(a) + b.ln(x+k)
#
# Note portanto que somando c à todos os valores da lista de coordenadas Y e aplicando o logaritmos nos elementos da lista resultante...
# ... teremos uma lista na qual poderemos aplicar uma regressão linear, porém, qual valor de c devemos utilizar?
# - Visto que nos valores da lista de coordenadas será aplicado logaritimo de base k e o argumento de um logaritimo não pode ser negativo...
# ... e nem igual à 0, teremos que:
#   
#       (i) c = 0, se min(coordenadas y) > 0;
#
#       (ii) c = min(coordenadas y) + h, onde h > 0, se min(coordenadas y) <= 0;
#
# O mesmo ocorre para a lista de coordenadas X; devemos somar k a tais coordenas e então aplicar o logaritmo nos elementos da lista resultante...
# ... para termo uma lista sobre a qual podemos aplicar uma regrassão linear junto a nova lista de coordenadas Y. Portanto devido a...
# ... aplicação do logaritmo devemos selecionar k tal que:
#
#       (i) c = 0, se min(coordenadas x) > 0;
#
#       (ii) c = min(coordenadas x) + j, onde j > 0, se min(coordenadas x) <= 0;
#
# E assim a função f da pela regressão, onde u = ln(x + k), deve ser do tipo:
#
#       f(u) = ln(y+c) = a0 + a1.u
#
# Note que, para obter y podemos aplicar os dois lados da equação como expoentes de e, assim:
#
#       e^(ln(y+c)) = e^(a0 + a1.u)
#
#       y + c = (e^a0).[e^(a1.u)]
#
#       y + c = (e^a0).{[e^(u)]^a1}
#
# Note que podemos definir que e^(a0) = a e (x + k) = e^u e b = a1, assim temos:
# 
#       y + c = a.x^b
#
#       y = a.x^b - c
#
# Que por sua vez é a equação esponencial que queremos encontrar.