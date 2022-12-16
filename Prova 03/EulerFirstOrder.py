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
    a = 8.78623
    def df(x, y):
        return -y/sqrt(a**2 -y**2)
    
    # Restrição de valor inicial: 
    x0, y0 = 1.99943, 5.90312
    # Número de iterações(passos):
    n = 101
    # Tamanho de cada passo:
    h = 0.08774
        
    X, Y = euler(df, x0, y0, h, n)
    t = np.linspace(x0, n*h, 200)

    print(Y)

    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()
