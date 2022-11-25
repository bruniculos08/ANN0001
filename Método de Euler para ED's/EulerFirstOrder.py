from math import *
import numpy as np
import matplotlib.pyplot as plt

def euler(f, x0, y0, h, n):
    X = [x0]
    Y = [y0]
    for k in range(1, n):
        x = x0 + k*h
        y_k = Y[k-1] + f(X[k-1], Y[k-1])*h
        X.append(x)
        Y.append(y_k)
    return X, Y

if __name__ == '__main__':
    
    def f(x, y):
        return e**x
    
    x0 = 0
    y0 = 1    
    n = 700
    h = 0.1
        
    X, Y = euler(f, x0, y0, h, n)

    # plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, label = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()
