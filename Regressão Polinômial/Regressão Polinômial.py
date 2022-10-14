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
    # Note: o número de pontos do polinômio deve ser estritamente maior que o grau do polinômio, caso contrário...
    # ... haverão infinitas soluções

    # Exemplo 01:
    X = [float(x) for x in range(0, 3)]
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
#
# (x1, y1), (x2, y2), ..., (xn, yn)
#
# queremos uma reta, ou seja, uma função da forma:
#
# p(x) = a0 + a1.x + a2.x² + ... + ak.x^k
#
# que se aproxime ao máximo dos pontos dados, assim note que, o erro da reta em relação aos pontos é dado por:
#
# E(a0, a1) = d1² + d2² + ... + dn-1² + dn²
#
# onde, para i > 0 e i <= n:
#
# di = yi - p(xi)
#
# sendo assim, temos:
#
# E(a0, ..., ak) = ∑ [yi - p(xi)]²
# E(a0, ..., ak) = ∑ (yi - a0 - a1.xi - a2.xi² - ... - ak.xi^k)²
# E(a0, ..., ak) = ∑ (yi - ∑ aj.xi^j)²
#
# para diminuir tal erro note que devemos ter que:
#
#  dE  = 0 , dE  = 0, ... , dE = 0 
#  da0       da1            dak
#
# Note que para tal ponto crítico existem k+1 equações, então, calculando dE/dal = 0, onde 0 <= l <= k, temos:
#
#  dE  =  d[∑ (yi - ∑ aj.xi^j)²]
#  dal    dal
    
#  dE  =  ∑d(yi - ∑ aj.xi^j)²]
#  dal     dal
    
#  dE  =  ∑[2.(yi - ∑ aj.xi^j).d(yi - ∑ aj.xi^j)]
#  dal                         dal
    
#  dE  =  ∑2.[yi - ∑(aj.xi^j)].[-∑d(aj.xi^j)]
#  dal                           dal
    
#  dE  =  ∑2.[yi - ∑(aj.xi^j)].[-∑d(aj.xi^j)]
#  dal                           dal

#  dE  =  ∑2.[yi - ∑(aj.xi^j)].(-xi^l)
#  dal                           

#  0  =  ∑2.[yi - ∑(aj.xi^j)].(-xi^l) 

#  0  =  ∑[yi - ∑(aj.xi^j)].(-xi^l)

#  0  =  (∑yi.-xi^l) + ∑(∑aj.xi^(j+l))

# (∑yi.xi^l) = ∑(∑aj.xi^(j+l))

# (∑yi.xi^l) = ∑a0.xi^l + ∑a1.xi^(l+1) + ... + ∑ak.xi^(l+k)
    
# (∑yi.xi^l) = a0.∑xi^l + a1.∑xi^(l+1) + ... + ak.∑xi^(l+k)
    
# Note que, por este resultado, dado que l = 0, 1, 2, ..., k-1, k, temos k equações da forma:
#
#    l = 0 -> a0.n + a1.(∑xi¹) + a2.(∑xi²) + ... + ak.(∑xi^k) = ∑yi
#    l = 1 -> a0.(∑xi¹) + a1.(∑xi²) + a2.(∑xi³) + ... + ak.(∑xi^(k+1)) = (∑yi.xi¹)
#    .
#    .
#    . 
#    l = k -> a0.(∑xi^k) + a1.(∑xi^(k+1)) + a2.(∑xi^(k+2)) + ... + ak.(∑xi^(2.k)) = (∑yi.xi^k) 
#
# Escrevendo o sistema de equações na forma matricial:
#    ____                                             ____       __    __      __            __
#   |   n         ∑xi        ∑xi²      ...     ∑xi^k     |      |   a0  |     |   ∑yi         |
#   |   ∑xi       ∑xi²       ∑xi³      ...     ∑xi^(k+1) |      |   a1  |     |   ∑yi.xi¹     |
#   |   ∑xi²      ∑xi³       ∑xi^4     ...     ∑xi^(k+2) |      |   .   |     |     .         |
#   |   .                                           .    |   °  |   .   |  =  |     .         |
#   |   .                                           .    |      |   .   |     |     .         |
#   |   .                                           .    |      |  ak-1 |     |  ∑yi.xi^(k-1) |   
#   |   ∑xi^k  ∑xi^(k+1)    ∑xi^(k+2)  ...     ∑xi^(2.k) |      |  ak   |     |  ∑yi.xi^k     |
#   |____                                            ____|      |__   __|     |__           __|
#
# Resolvendo tal sistema obtemos os resultado para os coeficientes a0, a1, ..., ak, e então temos o polinômio que...
# ... mais se aproxima dos pontos