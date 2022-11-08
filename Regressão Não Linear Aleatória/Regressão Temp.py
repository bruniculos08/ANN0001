import random as random
from math import *
import matplotlib.pyplot as plt
import numpy as np


def calc_coeffs(X, Y, degree = 1):
    degree += 1

    # (1) Cria a matriz do lado esquerdo da equação:
    X_matrix = []
    for i in range(degree):
        row = []
        for j in range(degree):
            sum = 0
            for xi in X: 
                sum += xi ** (i + j)
            row.append(sum)
        X_matrix.append(row)

    # (2) Cria a matriz do lado direito da equação:
    Y_matrix = []
    for i in range(degree):
        sum = 0
        for xi, yi in zip(X, Y):
            sum += yi*(xi**i)
        Y_matrix.append(sum)

    return np.linalg.solve(X_matrix, Y_matrix)

def calc_non_linear_coeffs(X, Y):
    const_Y = min(Y)
    if(const_Y <= 0):
        const_Y = abs(const_Y) + 1
    else:
        const_Y = 0

    const_X = min(X)
    if(const_X <= 0):
        const_X = abs(const_X) + 1
    else:
        const_X = 0

    linearized_X = [1/sqrt(xi + const_X) for xi in X]
    linearized_Y = [sqrt(yi + const_Y) for yi in Y]

    coeffs = calc_coeffs(linearized_X, linearized_Y, 1)

    a = coeffs[1]/coeffs[0]
    b = 1/coeffs[0]
    c = const_Y
    k = const_X

    return {'a' : a, 'b' : b, 'k' : k, 'c' : c}
    
def build_non_linear(coeffs):
    def f(x):
        return ((coeffs['a']/coeffs['b'])*(1/sqrt(x + coeffs['k'])) + 1/coeffs['b'])**2 - coeffs['c']
    return f

if __name__ == '__main__':

    # Exemplo 01:
    def f(x):
        return ((1 + sqrt(x)))**2/((1*sqrt(x)))**2

    X = [xi for xi in range(1, 100, 4)]
    Y = [f(xi) for xi in X]

    # values = [1.1859, 4.6267, 5.8824]

    coeffs = calc_non_linear_coeffs(X, Y)     
    g = build_non_linear(coeffs)

    t = np.linspace(min(X), max(X)+1, 100)
    ft = [f(ti) for ti in t]
    gt = [g(ti) for ti in t]

    # print(f"function f aplied in the choosen values:")
    # for value in values:
    #     print(f"f({value}) = {f(value)}")

    print(f"coeffs = {coeffs}")    

    plt.plot(t, ft, color = "green")
    plt.plot(t, gt, color = "orange")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()

    pass

# Como transformar uma equação do tipo y = (a.(x+k))/((x+k)+b) - c em um equação de reta que possa ser utilizada em regressão linear:
#
# (1) Realizando manipulações algébricas temos:
#
#       y + c = (a.(x+k))/((x+k)+b)
#
#       1/(y+c) = ((x+k) + b)/(a.(x+k))
#
#       1/(y+c) = 1/a + b/(a.(x+k))
#
#       1/(y+c) = 1/a + (b/a).(1/(x+k)) 
#
# (2) Fazendo a substituição u = 1/(x+k) e v = 1/(y + c) teremos:
#
#       v = 1/a + (b/a).u
#
# Que tem por sua vez a forma de uma função linear, da forma:
#
#       f(u) = a0 + a1.u
#
# Substituindo para obter y teremos:
#
#       1/(y+c) = a0 + a1.1/(x+k)
#
#       y + c = 1/(a0 + a1/(x+k))
#
# Assim teremos:
# 
#       y + c = 1/(a0.(x+k)/(x+k) + a1.1/(x+k))
#
#       y + c = 1/[(a0.(x+k) + a1)/(x+k)]
#
#       y + c = (x+k)/(a0.(x+k) + a1)
#
#       y = x/(a0.(x+k) + a1) - c
#
#       y = (1/a0).[(x+k)/((x+k) + a1/a0)] - c
#
# Logo, note que podemos definir que (1/a0) = a e a1/a0 = b, ou seja, a0 = (1/a) e portanto, a1 = (b/a), assim temos:
#
#       y = a.[(x+k)/((x+k) + b)] - c
#
# Que por sua vez é equação não linear qual queremos encontrar; note entretanto que os valores das constantes c e k devem ser...
# ... escolhidos de modo que não ocorra divisão por zero, assim teremos:
#
#       (i) c = 0, se min(coordenadas y) > 0;
#
#       (ii) c = min(coordenadas y) + h, onde h > 0, se min(coordenadas y) <= 0;
#
# e para k, teremos:
#
#       (i) k = 0, se min(coordenadas x) > 0;
#
#       (ii) k = min(coordenadas x) + j, onde j > 0, se min(coordenadas x) <= 0;