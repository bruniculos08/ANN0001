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
    coeffs = calc_coeffs(X, Y)
    f = build_poly(coeffs)

    t = np.linspace(0, max(X), 100)
    ft = [f(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()

    # Exemplo 02:
    X = [0.0472, 0.588, 0.8306, 0.9416, 1.3687, 1.6071, 2.1113, 2.3487, 2.6205, 2.8916, 3.3605, 3.5383, 4.0572, 4.0883, 4.6103, 4.8969, 5.3019, 5.5072, 5.7727, 5.9827, 6.4492, 6.6631, 6.9284, 7.4766, 7.5325, 7.9474, 8.3881, 8.4975, 8.9937, 9.1914, 9.59, 9.8857]
    Y = [1.6419, 2.8969, 3.8245, 4.2689, 5.4957, 6.0326, 7.4508, 8.565, 8.9236, 9.6319, 11.0012, 11.4891, 13.0284, 13.0854, 14.4487, 15.273, 16.4422, 17.0173, 17.74, 17.4706, 19.6981, 20.0275, 21.0917, 22.5734, 22.8609, 23.2017, 25.3521, 25.6713, 27.3512, 27.6621, 28.707, 29.5817]
    values = [1.4212, 1.6509, 3.8148, 7.0385, 8.1816]
    coeffs = calc_coeffs(X, Y)
    f = build_poly(coeffs)

    t = np.linspace(0, max(X), 100)
    ft = [f(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo02.png")
    plt.close()

    print("coeffs: ")
    for i, coeff in enumerate(coeffs):
        print(f"a{i} = {coeff}")
    print("values: ")
    for value in values:
        print(f"f({value}) = {f(value)}")
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