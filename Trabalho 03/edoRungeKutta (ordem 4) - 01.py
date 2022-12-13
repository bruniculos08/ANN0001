from math import *
import numpy as np
import matplotlib.pyplot as plt

def rungeKutta(df, x0, y0, X):

    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0] + X
    Y = [y0]
    n = len(X)

    for k in range(1, n):
        h = X[k] - X[k-1]
        m1 = df(X[k-1], Y[k-1])
        m2 = df(X[k-1] + h/2, Y[k-1] + m1*h/2)
        m3 = df(X[k-1] + h/2, Y[k-1] + m2*h/2)
        m4 = df(X[k-1] + h, Y[k-1] + m3*h)
        yk = Y[k-1] + (1/6)*(m1 + 2*m2 + 2*m3 + m4)*h
        Y.append(yk)
    return Y

if __name__ == '__main__':
    
    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return y * (1 - x) + x + 2
    
    # Restrição de valor inicial: 
    x0 = 1.4447
    y0 = 2.4142

    X = [1.4881, 1.5071, 1.5635, 1.6, 1.6678, 1.7327, 1.7858, 1.8361, 1.871, 1.917, 1.9712, 2.0155, 2.0801, 2.1315, 2.1798, 2.2216, 2.2875, 2.3042, 2.3508, 2.4031]

    Y = rungeKutta(df, x0, y0, X)

    print(Y)