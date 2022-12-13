from math import *
import numpy as np
import matplotlib.pyplot as plt

def heun(df, x0, y0, h, n):

    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0]
    Y = [y0]

    for k in range(1, n):
        m1 = df(X[k-1], Y[k-1])
        m2 = df(X[k-1] + h, Y[k-1] + m1*h)
        xk = x0 + k*h
        yk = Y[k-1] + (h/2)*(m1 + m2)
        X.append(xk)
        Y.append(yk)
    return X, Y

if __name__ == '__main__':

    # Exemplo 01:

    # Equação obtida para a derivada primeira de y na equação diferencial:

    k = 0.0544*pi

    def E(t):
        return e**(-k*t) * sin(2*t - pi)

    def dE(t):
        return e**(-k*t) * (-k*sin(2*t - pi) + 2*cos(2*t - pi))

    def ddE(t):
        return (-4*k*pi*cos(2*t - pi) + (-4 + k**2)*sin(2*t - pi)) * (e**(-k*t))

    C = 0.2225
    R = 1.2407
    L = 1.5192

    def df(x, y):
        return C*ddE(x) + (1/R)*dE(x) + (1/L)*E(x)
    
    # Restrição de valor inicial: 
    x0 = 0
    y0 = 0
    # Número de iterações(passos; para encontrar o e-nésimo valor de y deve-se fazer n+1 iterações):
    n = 151
    # Tamanho de cada passo:
    h = 0.1608
        
    X, Y = heun(df, x0, y0, h, n)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exercício23 (corrente).png")
    # plt.close()