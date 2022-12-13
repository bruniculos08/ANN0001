from math import *
import numpy as np
import matplotlib.pyplot as plt

def rungeKutta(df, x0, y0, h, n):

    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0]
    Y = [y0]

    for k in range(1, n):
        m1 = df(x0, y0)
        m2 = df(x0 + h/2, y0 + m1*h/2)
        m3 = df(x0 + h/2, y0 + m2*h/2)
        m4 = df(x0 + h, y0 + m3*h)
        x0 += h
        y0 += (1/6)*(m1 + 2*m2 + 2*m3 + m4)*h  
        X.append(x0)
        Y.append(y0)
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
        
    X, Y = rungeKutta(df, x0, y0, h, n)
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

    X, Y = rungeKutta(df, x0, y0, h, n)
    t = np.linspace(x0, n*h, 200)
    ft = [f(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo02.png")
    plt.close()