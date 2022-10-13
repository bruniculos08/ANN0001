import random as random
from math import *
import matplotlib.pyplot as plt
import numpy as np

def calc_coeffs(X, Y, degree):
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

def build_poly(coeffs):
    def func(x):
        result = 0
        for i, ci in enumerate(coeffs):
            result += ci*(x**i)
        return result
    return func

if __name__ == '__main__':
    X = [float(x) for x in range(0, 200)]
    Y = [xi**2 for xi in X]
    coeffs = calc_coeffs(X, Y, 5)
    f = build_poly(coeffs)
    print(coeffs)

    t = np.linspace(0, max(X), 100)
    ft = [f(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")


# Para uma determinada lista de pontos:
# (x1, y1), (x2, y2), ..., (xn, yn)
# queremos uma reta, ou seja, uma função da forma:
# p(x) = a0 + a1.x
# que se aproxime ao máximo dos pontos dados, assim note que, o erro da reta em relação aos pontos é dado por:
# E(a0, a1) = d1² + d2² + ... + dn-1² + dn²
# onde, para i > 0 e i <= n:
# di = yi - p(xi)
# sendo assim, temos:
# E(a0, a1) = ∑ [yi - p(xi)]²
# E(a0, a1) = ∑ [yi - a0 - a1.xi]²
# para diminuir tal erro note que devemos ter que
#  (i) dE  = 0   e  (ii) dE  = 0 
#      da0               da1
# de (i) teremos a seguinte equação:
#   0 = d∑ [yi - a0 - a1.xi]²
#       da0
#   0 = ∑ d[yi - a0 - a1.xi]²
#         da0
#   0 = ∑ 2[yi - a0 - a1.xi].d(yi - a0 - a1.xi)
#                           da0
#   0 = ∑ 2[yi - a0 - a1.xi].(-1)
#   0 = ∑ 2[a0 + a1.xi - yi]
#   0 = ∑ [a0 + a1.xi - yi]
#   0 = ∑a0 + ∑a1.xi - ∑yi
#   ∑yi = ∑a0 + ∑a1.xi   
#   ∑yi = a0.n + a1.∑xi
# e de (ii) temos a seguinte equação:
#   0 = d∑ [yi - a0 - a1.xi]²
#       da1                     
#   0 = ∑ d[yi - a0 - a1.xi]²
#         da1
#   0 = ∑ 2[yi - a0 - a1.xi].d(yi - a0 - a1.xi)
#                            da1
#   0 = ∑ 2[yi - a0 - a1.xi].(-xi)
#   0 = ∑ 2[a0 + a1.xi - yi].(xi)
#   0 = ∑ [a0 + a1.xi - yi].(xi)
#   0 = ∑ [a0.xi + a1.xi² - yi.xi]
#   0 = ∑a0.xi + ∑a1.xi² - ∑yi.xi
#   0 = a0.∑xi + a1.∑xi² - ∑yi.xi
#   ∑yi.xi = a0.∑xi + a1.∑xi²
# logo temos de resolver o seguinte sistema de equações:
#   ∑yi = a0.n + a1.∑xi
#   ∑yi.xi = a0.∑xi + a1.∑xi²
# escrevendo na forma matricial temos:
#   --                  -- --    --      --
#   |  n     ∑xi   | . | a0 |    | ∑yi    |
#   |  ∑xi   ∑xi²  |   | a1 |  = | ∑yi.xi |
#   --                 -- --     --      --  