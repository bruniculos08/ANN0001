from math import *
import numpy as np
import matplotlib.pyplot as plt

def ralston(df, x0, y0, h, n):

    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0]
    Y = [y0]

    for k in range(1, n):
        m1 = df(X[k-1], Y[k-1])
        m2 = df(X[k-1] + (3/4)*h, Y[k-1] + (3/4)*h*m1)
        xk = x0 + k*h
        yk = Y[k-1] + (h/3)*(m1 + 2*m2)
        X.append(xk)
        Y.append(yk)
    return X, Y

if __name__ == '__main__':

    # Exemplo 01:

    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return y * (2 - x) + x + 1
    
    # Restrição de valor inicial: 
    x0 = 1.65934
    y0 = 2.59428
    # Número de iterações(passos):
    n = 16
    # Tamanho de cada passo:
    h = 0.12139
        
    X, Y = ralston(df, x0, y0, h, n)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    # plt.scatter(X, Y, label = "blue")
    # plt.savefig("Exemplo01.png")
    # plt.close()