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

if __name__ == '__main__':

    # Exemplo 01:
    X = [x for x in range(0, 100)]
    Y = [random.random()*xi for xi in X]
    values = []

    coeffs = calc_coeffs(X, Y)
    f = build_poly(coeffs)

    t = np.linspace(0, max(X), 100)
    ft = [f(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()

    # print("coeffs: ")
    # for i, coeff in enumerate(coeffs):
    #     print(f"a{i} = {coeff}")
    # print("values: ")
    # for value in values:
    #     print(f"f({value}) = {f(value)}")

    # Exemplo 02:
    X = [0.1502, 0.1874, 0.3551, 0.5194, 0.7072, 0.922, 1.1303, 1.1872, 1.4117, 1.6165, 1.7129, 1.8782]
    Y = [5.6131, 5.4874, 7.2501, 10.9598, 13.2359, 20.2362, 29.286, 34.0887, 47.7891, 68.2312, 80.6315, 107.1187]

    
    log_Y = [log(yi, e) for yi in Y]
    

    values = [0.4917, 0.9672, 1.16]

    coeffs = calc_coeffs(X, Y)
    #f = build_poly(coeffs)

    # a0 = log(a, e) <=> e^a0 = a 
    a = e**coeffs[0]
    b = coeffs[1]

    def f(x): 
        return a*e**(b*x)

    print("a = {a}, b = {b}")

    t = np.linspace(0, max(X), 100)
    ft = [f(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo02.png")
    plt.close()

    pass

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