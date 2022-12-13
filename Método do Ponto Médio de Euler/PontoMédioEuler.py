from math import *
import numpy as np
import matplotlib.pyplot as plt

def eulerPontoMedio(df, x0, y0, h, n):

    # Criando listas de coordenadas com as coordenadas iniciais:
    X = [x0]
    Y = [y0]

    for k in range(1, n):
        m1 = df(X[k-1], Y[k-1])
        m2 = df(X[k-1] + (h/2), Y[k-1] + (h/2)*m1)
        xk = x0 + k*h
        yk = Y[k-1] + h*m2
        X.append(xk)
        Y.append(yk)
    return X, Y

if __name__ == '__main__':

    # Exemplo 01:

    # Equação obtida para a derivada primeira de y na equação diferencial:
    v = 36364
    λ = 0.05206  
    def df(x, y):
        return λ*y + v
    
    # Restrição de valor inicial: 
    x0 = 0
    y0 = 1862823
    # Número de iterações(passos; para encontrar o n-énsimo valor de y são necessária n+1 iterações):
    n = int(1/0.0625) + 1
    # Tamanho de cada passo:
    h = 0.0625
        
    X, Y = eulerPontoMedio(df, x0, y0, h, n)
    # t = np.linspace(x0, n*h, 200)
    # ft = [f(ti) for ti in t]

    print(Y)

    # plt.plot(t, ft, color = "green")
    # plt.scatter(X, Y, label = "blue")
    # plt.savefig("Exemplo01.png")
    # plt.close()