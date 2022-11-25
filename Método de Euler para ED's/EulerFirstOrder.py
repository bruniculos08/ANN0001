from math import *
import numpy as np
import matplotlib.pyplot as plt

def euler(f, x0, y0, h, n):
    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0]
    Y = [y0]

    for k in range(1, n):
        # Calculando x_k+1:
        x = x0 + k*h
        # Calculando y_k:
        y_k = Y[k-1] + f(X[k-1], Y[k-1])*h

        X.append(x)
        Y.append(y_k)
    
    return X, Y

if __name__ == '__main__':
    

    # Exemplo 01 para y'(x) = e**x:

    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return e**x

    # Solução da equação diferencial:
    def f(x):
        return e**x
    
    # Restrição de valor inicial: 
    x0, y0 = 0, 1
    # Número de iterações(passos):
    n = 700
    # Tamanho de cada passo:
    h = 0.1
        
    X, Y = euler(df, x0, y0, h, n)
    t = np.linspace(x0, n*h, 200)
    ft = [f(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()

    # Exemplo 02 para y'(x) = cos(x):

    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return cos(x)
    
    # Solução da equação diferencial:
    def f(x):
        return sin(x)

    # Restrição de valor inicial: 
    x0, y0 = 0, 0
    # Número de iterações(passos):
    n = 700
    # Tamanho de cada passo:
    h = 0.1

    X, Y = euler(df, x0, y0, h, n)
    t = np.linspace(x0, n*h, 200)
    ft = [f(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo02.png")
    plt.close()