from math import *
import numpy as np
import matplotlib.pyplot as plt

def eulerPontoMedio(df, x0, y0, X):

    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0] + X
    Y = [y0]
    n = len(X)

    for k in range(1, n):
        h = X[k] - X[k-1]
        m1 = df(X[k-1], Y[k-1])
        m2 = df(X[k-1] + (h/2), Y[k-1] + (h/2)*m1)
        yk = Y[k-1] + h*m2
        Y.append(yk)
    return Y

if __name__ == '__main__':

    # Exemplo 01:

    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return y * (2 - x) + x + 1
    
    # Restrição de valor inicial: 
    x0 = 0.879
    y0 = 1.07304
    # Número de iterações(passos):
    n = 16
    # Tamanho de cada passo:
    h = 0.12139

    X = [0.90462, 0.93778, 1.01841, 1.0618, 1.10124, 1.17281, 1.20933, 1.25026, 1.31627, 1.3385, 1.40881, 1.46647, 1.5057, 1.54598, 1.6099, 1.65657, 1.69699, 1.76334, 1.7967, 1.84303]

    Y = eulerPontoMedio(df, x0, y0, X)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    # plt.scatter(X, Y, label = "blue")
    # plt.savefig("Exemplo01.png")
    # plt.close()