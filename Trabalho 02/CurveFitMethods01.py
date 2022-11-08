# Métodos de ajuste de curvas para regressão linear e linearização:
import matplotlib.pyplot as plt
import numpy as np
from math import *

# Obs.: se nenhum grau for passado à função, o grau padrão será 1, ou seja, se terá uma reta e portanto...
# ... uma regressão linear.
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

# A função build coeffs da maneira que está definida aqui serve tanta para regressão linear quanto polinômial:
def build_poly(coeffs):
    def func(x):
        result = 0
        for i, ci in enumerate(coeffs):
            result += ci*(x**i)
        return result
    return func

def calc_non_linear_coeffs(X, Y):

    # Traslação do gráfico sobre o eixo Y:
    const_Y = min(Y)
    if(const_Y < 0):
        const_Y = abs(const_Y) + 1
    else:
        const_Y = 0

    # Traslação do gráfico sobre o eixo X:
    const_X = min(X)
    if(const_X < 0):
        const_Y = abs(const_X) + 1
    else:
        const_X = 0

    linearized_X = [1/sqrt(xi + const_X) for xi in X]    
    linearized_Y = [sqrt(yi + const_Y) for yi in Y]
    coeffs = calc_coeffs(linearized_X, linearized_Y)

    a = coeffs[1]/coeffs[0]
    b = 1/coeffs[0]
    c = const_Y
    k = const_X
    return {'a' : a, 'b' : b, 'k' : k, 'c' : c}
    
# Função que constrói a função de regressão considerando que esta não será um polinômio:
def build_non_linear(coeffs):
    def func(x):
        return ((coeffs['a']/coeffs['b'])*(1/sqrt(x + coeffs['k'])) +  1/coeffs['b'])**2 - coeffs['c']
    return func

if __name__ == '__main__':
    
    # Exemplo 01:
    X = [0.7708, 1.6674, 2.3526, 2.9878, 4.1301, 4.6131, 5.6179, 6.3146, 7.0627, 8.0253, 8.8753, 9.421]
    Y = [6.6604, 3.6621, 2.7577, 2.3334, 1.8311, 1.6729, 1.4886, 1.3931, 1.2011, 1.2012, 1.206, 1.0941]
    values = [1.1859, 4.6267, 5.8824]

    coeffs = calc_non_linear_coeffs(X, Y)
    f = build_non_linear(coeffs)

    print(coeffs)

    t = np.linspace(min(X), max(X)+1, 100)
    ft = [f(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01 - CurveFitMethods.png")
    plt.close()

    pass