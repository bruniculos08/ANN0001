from math import *
import numpy as np
import matplotlib.pyplot as plt

def rungeKutta(df, x0, y0, h, n, b = 1):
    """""
    Método de Runge-Kutta geral de ordem 2
    Por padrão usa o método do ponto médio de Euler que corresponde a b = 1
    b = 1/2 corresponde ao método de Heun
    b = 2/3 corresponde ao método de Ralston
    """""
    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0]
    Y = [y0]

    a = 1 - b
    p = 1/(2*b)
    q = p

    for k in range(1, n):
        m1 = df(X[k-1], Y[k-1])
        m2 = df(X[k-1] + p*h, Y[k-1] + q*h*m1)
        xk = X[k-1] + h
        yk = Y[k-1] + (a*m1 + b*m2)*h
        X.append(xk)
        Y.append(yk)
    return X, Y

if __name__ == '__main__':
    

    # Exemplo 01:

    # Equação obtida para a derivada primeira de y na equação diferencial:
    a = 9.94668
    
    def df(x, y):
        return -y/sqrt(a**2 - y**2)
    
    # Restrição de valor inicial: 
    x0 = 1.02787
    y0 = 4.8879
    # Número de iterações(passos):
    n = 101
    # Tamanho de cada passo:
    h = 0.06334
    # Peso:
    b = 0.96169
        
    X, Y = rungeKutta(df, x0, y0, h, n, b)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    # plt.scatter(X, Y, label = "blue")
    # plt.savefig("Exemplo01.png")
    # plt.close()

    # Exemplo 02 para y'(x) = cos(x):

    # Equação obtida para a derivada primeira de y na equação diferencial:
    def df(x, y):
        return cos(x)

    # Restrição de valor inicial: 
    x0, y0 = 0, 0
    # Número de iterações(passos):
    n = 700
    # Tamanho de cada passo:
    h = 0.1

    X, Y = rungeKutta(df, x0, y0, h, n)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    # plt.scatter(X, Y, label = "blue")
    # plt.savefig("Exemplo02.png")
    # plt.close()