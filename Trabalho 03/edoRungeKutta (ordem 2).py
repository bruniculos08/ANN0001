from math import *
import numpy as np
import matplotlib.pyplot as plt

def rungeKutta(df, x0, y0, X, b = 1):
    """""
    Método de Runge-Kutta geral de ordem 2
    Por padrão usa o método do ponto médio de Euler que corresponde a b = 1
    b = 1/2 corresponde ao método de Heun
    b = 2/3 corresponde ao método de Ralston
    """""
    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0] + X
    Y = [y0]
    n = len(X)

    a = 1 - b
    p = 1/(2*b)
    q = p

    for k in range(1, n):
        h = (X[k] - X[k-1])
        m1 = df(X[k-1], Y[k-1])
        m2 = df(X[k-1] + p*h, Y[k-1] + q*h*m1)
        yk = Y[k-1] + (a*m1 + b*m2)*h
        Y.append(yk)
    return Y

if __name__ == '__main__':
    

    # Exemplo 01:

    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return y * (1 - x) + x + 2

    # Restrição de valor inicial: 
    x0 = 1.00338
    y0 = 2.20672
    
    X = [1.0414, 1.07131, 1.13888, 1.18984, 1.21109, 1.28049, 1.32758, 1.36977, 1.44815, 1.49292, 1.52706, 1.57023, 1.62412, 1.69296, 1.73703, 1.78261, 1.81261, 1.85932, 1.93818, 1.98088]

    b = 0.65247

    Y = rungeKutta(df, x0, y0, X, b)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    # plt.scatter(X, Y, label = "blue")
    # plt.savefig("Exemplo02.png")
    # plt.close()