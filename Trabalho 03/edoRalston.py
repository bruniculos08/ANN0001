from math import *
import numpy as np
import matplotlib.pyplot as plt

def ralston(df, x0, y0, X):

    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0] + X
    Y = [y0]
    n = len(X)

    for k in range(1, n):
        h = X[k] - X[k-1]
        m1 = df(X[k-1], Y[k-1])
        m2 = df(X[k-1] + (3/4)*h, Y[k-1] + (3/4)*h*m1)
        yk = Y[k-1] + (h/3)*(m1 + 2*m2)
        Y.append(yk)
    return Y

if __name__ == '__main__':

    # Exemplo 01:

    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return y * (2 - x) + x + 1
    
    # Restrição de valor inicial: 
    x0 = 1.20863
    y0 = 1.7484

    X = [1.24867, 1.28112, 1.31859, 1.36392, 1.44204, 1.48799, 1.54051, 1.56915, 1.62378, 1.6689, 1.74228, 1.78788, 1.81933, 1.869, 1.94182, 1.97302, 2.01548, 2.07812, 2.14105, 2.18444]

    Y = ralston(df, x0, y0, X)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    # plt.scatter(X, Y, label = "blue")
    # plt.savefig("Exemplo01.png")
    # plt.close()