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

# def calc_non_linear_coeffs(X, Y):
#     const_Y= min(Y)
#     if(const_Y <= 0):
#         const_Y = abs(const_Y) + 1
#     else:
#         const_Y = 0

#     const_X = min(X)
#     if(const_X <= 0):
#         const_X = abs(const_X) + 1
#     else:
#         const_X = 0

#     linearized_X = [1/(const_X + xi) for xi in X]
#     linearized_Y = [1/(const_Y + yi) for yi in Y]

#     coeffs = calc_coeffs(linearized_X, linearized_Y)

#     # Considerando a equação exponencial na forma y = a.k^(b.x) - c
#     a = 1/(coeffs[0])
#     b = coeffs[1]/coeffs[0]
#     c = const_Y
#     k = const_X

#     return {'a' : a, 'b' : b, 'k' : k, 'c' : c}

def calc_non_linear_coeffs_pow_x(X, Y, pot=1):
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

    linearized_X = [1/((xi + const_X)**pot) for xi in X]
    linearized_Y = [1/(yi - const_Y) for yi in Y]

    coeffs = calc_coeffs(linearized_X, linearized_Y)

    # Considerando a equação exponencial na forma y = a.k^(b.x) - c
    a = 1/(coeffs[0])
    b = coeffs[1]/coeffs[0]
    c = const_Y
    k = const_X

    return {'a' : a, 'b' : b, 'k' : k, 'c' : c, 'pot' : pot}
    
def build_non_linear(coeffs):
    def f(x):
        # y = (a.(x+k))/((x+k)+b) - c
        return coeffs['a']*(x+coeffs['k'])**coeffs['pot']/((x+coeffs['k'])**coeffs['pot'] + coeffs['b']) - coeffs['c']
    return f

if __name__ == '__main__':

    # Exemplo 01:
    X = [1.3312, 1.7481, 2.1012, 2.5289, 3.0234, 3.3364, 3.9986, 4.3035, 4.9369, 5.4698, 5.693, 6.1623, 6.6749, 6.9567, 7.4203, 7.9901, 8.5101, 8.8578, 9.4592, 10.027, 10.0991, 10.7873, 11.1146, 11.5225, 12.0229, 12.4454, 12.9252, 13.4199, 13.9274, 14.4862, 15.0232, 15.3362, 15.4886, 16.0153, 16.401, 17.0037, 17.2934, 17.815, 18.6172, 19.0669, 19.1108, 19.5719]
    Y = [0.7456, 0.8493, 0.9207, 1.003, 1.0894, 1.1599, 1.2507, 1.3055, 1.3711, 1.3712, 1.3721, 1.4181, 1.4854, 1.5204, 1.5009, 1.5196, 1.574, 1.5769, 1.5932, 1.6087, 1.655, 1.6485, 1.6935, 1.6596, 1.6944, 1.7204, 1.7011, 1.7408, 1.7502, 1.7778, 1.7451, 1.7755, 1.7659, 1.7831, 1.8648, 1.7744, 1.8255, 1.752, 1.8105, 1.8518, 1.8329, 1.7588]
    values = [1.6152, 5.3589, 6.1014, 9.253, 9.4466]

    coeffs = calc_non_linear_coeffs_pow_x(X, Y)     
    f = build_non_linear(coeffs)

    t = np.linspace(min(X)-1, max(X)+1, 100)
    ft = [f(ti) for ti in t]

    # print(f"function f aplied in the choosen values:")
    # for value in values:
    #     print(f"f({value}) = {f(value)}")

    # print(f"coeffs = {coeffs}")    

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()

    # Exemplo 02:
    X = [1.6374, 2.0354, 3.6063, 4.5715, 5.0462, 5.7868, 6.6008, 8.3248, 9.2032, 9.8237, 10.596, 11.3267]
    Y = [0.9977, 1.3019, 2.1175, 2.3617, 2.4739, 2.5782, 2.6436, 2.8851, 2.8856, 2.9274, 2.8937, 2.9073]
    values = [4.1468, 6.1112, 8.9627]

    coeffs = calc_non_linear_coeffs_pow_x(X, Y, 2)     
    f = build_non_linear(coeffs)

    t = np.linspace(min(X)-1, max(X)+1, 100)
    ft = [f(ti) for ti in t]

    print(f"function f aplied in the choosen values:")
    for value in values:
        print(f"f({value}) = {f(value)}")

    print(f"coeffs = {coeffs}")    

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo02.png")
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