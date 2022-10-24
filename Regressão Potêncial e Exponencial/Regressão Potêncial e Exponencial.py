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

def calc_non_linear_coeffs(X, Y, base):
    const_Y= min(Y)
    if(const_Y <= 0):
        const_Y = -1*(abs(const_Y) + 1)
    else:
        const_Y = 0

    const_X = min(X)
    if(const_X <= 0):
        const_X = abs(const_X) + 1
    else:
        const_X = 0

    linearized_X = X
    linearized_Y = [log(yi - const_Y) - log(xi + const_X) for xi, yi in zip(X, Y)]

    coeffs = calc_coeffs(linearized_X, linearized_Y)

    # Considerando a equação exponencial na forma y = a.k^(b.x) - c
    a = base**(coeffs[0])
    b = coeffs[1]
    c = const_Y
    k = const_X

    return {'a' : a, 'b' : b, 'k' : k, 'c' : c, 'm' : base}
    
def build_non_linear(coeffs):
    def f(x):
        # y = a.(x+k).[m^(b.x)]
        return coeffs['a']*(x+coeffs['k'])*(coeffs['m'])**(coeffs['b']*x)
    return f

if __name__ == '__main__':

    # Exemplo 01:
    X = [0.133, 1.1277, 1.8076, 2.7734, 3.9582, 4.3861, 5.8489, 6.6472, 7.4997, 7.6521, 8.6918, 9.5471]
    Y = [0.6338, 4.0986, 5.5934, 6.7477, 7.2089, 7.1567, 6.6551, 6.2211, 5.7261, 5.5752, 4.9273, 4.367]
    values = [1.528, 8.3326, 8.454]
    base = e

    coeffs = calc_non_linear_coeffs(X, Y, base)     
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
    X = [0.2156, 0.4668, 0.7006, 0.8844, 1.12, 1.31, 1.6984, 1.7818, 2.0398, 2.3288, 2.5648, 2.7907, 3.1119, 3.3013, 3.5441, 3.7199, 3.9947, 4.1341, 4.429, 4.7367, 4.8657, 5.177, 5.4504, 5.6574, 5.8663, 6.1771, 6.2764, 6.6626, 6.7474, 7.0353, 7.2356, 7.4475, 7.7872, 7.9192, 8.2978, 8.4943, 8.8131, 8.9043, 9.2165, 9.3417, 9.7426, 9.7694]
    Y = [0.8117, 1.6458, 2.3001, 2.7664, 3.414, 3.7525, 4.4355, 4.5254, 4.9759, 5.2498, 5.4947, 5.7059, 5.8145, 5.8937, 6.1502, 6.0444, 6.0755, 6.1134, 6.229, 6.0928, 6.1364, 5.9942, 5.9281, 5.8757, 5.7802, 5.6901, 5.6268, 5.507, 5.5222, 5.3159, 5.1873, 5.1702, 4.9304, 4.8555, 4.6829, 4.6146, 4.3877, 4.3636, 4.2787, 4.1716, 3.9343, 3.9048]
    values = [2.3656, 4.7113, 6.0035, 7.1615, 9.5641]
    base = e

    coeffs = calc_non_linear_coeffs(X, Y, base)     
    f = build_non_linear(coeffs)

    t = np.linspace(min(X)-1, max(X)+1, 100)
    ft = [f(ti) for ti in t]

    # print(f"function f aplied in the choosen values:")
    # for value in values:
    #     print(f"f({value}) = {f(value)}")

    # print(f"coeffs = {coeffs}")    

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo02.png")
    plt.close()

# Como transformar uma equação do tipo y = a.(x+k).m^(b.x) - c em um equação de reta que possa ser utilizada em regressão linear:
#
# (1) Realizando manipulações algébricas temos:
#
#       y = a.(x+k).m^(b.x) - c
# 
#       y + c = a.(x+k).m^(b.x)
#
# (2) Aplicando logaritmo de base m em ambos os lados da equação temos:
#
#       log(y+c) = log(a.(x+k).m^(b.x)) 
#
#       log(y+c) = log(a) + log(x+k) + log(m^(b.x))
# 
#       log(y+c) = log(a) + log(x+k) + b.log(m^x)
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
#       (i) k = 0, se min(coordenadas x) > 0;
#
#       (ii) k = min(coordenadas x) + p, onde p > 0, se min(coordenadas x) <= 0;
#
# E assim, sendo v = log(y+c) e u = log(x+k) + b.log(m^x), a função f dada pela regressão deve ser do tipo:
#
#       f(u) = log(a) + b.u
#
# Assim para realizar tal linearização devemos aplicar log(y+c) em cada elemento da lista de coordenadas Y e aplicar u = log((x+k))/b + log(m^x) em...
# ... cada um dos elementos da lista de coordenadas X ; a equação que queremos:
#
#       f(u) = a0 + a1.u 
#
#       log(y+c) = a0 + a1.u
#
# Substituindo u par obter y teremos:
#
#       log(y+c) = a0 + a1.[log(x+k) + b.log(m^x)]
#
# Aplicando ambos os lados como expoentes de m teremos:
#
#       m^[log(y+c)] = m^{a0 + a1.[log(x+k) + b.log(m^x)]}
#
#       y + c = (m^a0).m^{a1.[log(x+k) + b.log(m^x)]}
#
#       y + c = (m^a0).m^[log((x+k)^a1) + b.log(m^(x.a1))]
#
#       y + c = (m^a0).m^[log((x+k)^a1) + b.log(m^(x.a1))]
#
#       y + c = (m^a0).m^[log((x+k)^a1)].m^[b.log(m^(x.a1))]
#
#       y + c = (m^a0).[(x+k)^a1].(m^b).m^(x.a1)
#
#       y + c = (m^a0).[(x+k)^a1].(m^b).m^(x.a1)