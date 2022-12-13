from math import *
import numpy as np
import matplotlib.pyplot as plt

def euler(df, x0, y0, X):
    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0] + X
    Y = [y0]
    n = len(X)

    for k in range(1, n):
        h = X[k] - X[k-1]

        # Calculando y_k:
        y_k = Y[k-1] + df(X[k-1], Y[k-1])*h

        Y.append(y_k)
    
    return Y

if __name__ == '__main__':
    

    # Exemplo 01 para y'(x) = e**x:

    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return y*(1-x) + x + 2

    # Solução da equação diferencial:
    # def f(x):
    #     return e**x
    
    # Restrição de valor inicial: 
    x0 = 0.35051
    y0 = 2.44976    

    X = [0.36573, 0.44019, 0.47016, 0.53561, 0.5954, 0.62351, 0.69233, 0.72972, 0.7712, 0.82678, 0.87487, 0.90885, 0.96612, 1.03758, 1.06427, 1.12513, 1.16983, 1.22741, 1.27631, 1.32534]

    Y = euler(df, x0, y0, X)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    # plt.scatter(X, Y, label = "blue")
    # plt.savefig("Exemplo01.png")
    # plt.close()