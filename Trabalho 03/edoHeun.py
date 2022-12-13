from math import *
import numpy as np
import matplotlib.pyplot as plt

def heun(df, x0, y0, X):

    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0] + X
    Y = [y0]
    n = len(X)

    for k in range(1, n):
        h = X[k] - X[k-1]
        m1 = df(X[k-1], Y[k-1])
        m2 = df(X[k-1] + h, Y[k-1] + m1*h)
        yk = Y[k-1] + (h/2)*(m1 + m2)
        Y.append(yk)
    return Y

if __name__ == '__main__':

    # Exemplo 01:

    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return y * (2 - x) + x + 1
    
    # Restrição de valor inicial: 
    x0 = 0.25964
    y0 = 0.99219
    
    X = [0.29566, 0.33624, 0.39496, 0.44545, 0.49735, 0.51941, 0.60283, 0.64264, 0.69308, 0.72683, 0.76571, 0.81599, 0.88288, 0.93736, 0.97332, 1.03157, 1.06834, 1.11582, 1.18832, 1.24488]

    Y = heun(df, x0, y0, X)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    # plt.scatter(X, Y, label = "blue")
    # plt.savefig("Exemplo01.png")
    # plt.close()