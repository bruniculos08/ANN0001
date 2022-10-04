

def diff_div(X, Y):
    # Esta cópia de Y irá mudar a cada iteração:
    Y_table = [yi for yi in Y]  

    # Sabemos que o primeiro coeficiente, a0, é sempre igual a y0, assim temos:
    coeffs = [Y[0]] + [0 for yi in Y[1:]]   
    
    n = len(coeffs)
    
    # Para cada coluna (lembrando que a 1º coluna já é dada):
    for i in range(n-1):

        # Para cada elemento da coluna (lembrando que a0 já foi calculcado):
        for j in range(n - i - 1):
            num = Y_table[j+1] - Y_table[j]
            denom = X[j+1+i] - X[j]
            Y_table[j] = num/denom

        # Como Y_table a cada "for" se torna outra coluna da tabela, lembre-se...
        # ... que sempre o primeiro elemento de uma coluna k equivale ao coeficiente ak:
        coeffs[i+1] = Y_table[0]

    return coeffs

def build_poly(X, coeffs):
    def func(x):
        sum = 0
        for i, ci in enumerate(coeffs):
            prod = ci
            # Se i = 0 o loop não itera:
            for j in range(i):
                prod *= (x - X[j])
            sum += prod
        return sum
    return func


if __name__ == '__main__': 

    import numpy as np
    import matplotlib.pyplot as plt
    from math import *

    # Exemplo 01:

    X = [1, 2, 3, 4]
    Y = [2, 5, 1, 3]

    coeffs = diff_div(X,Y)
    p = build_poly(X, coeffs)

    #print(coeffs)
    #for xi in X: print(f'{p(xi)}')

    t = np.linspace(min(X), max(X), 100)
    pt = [p(ti) for ti in t]

    plt.plot(t, pt, color = "orange")
    plt.scatter(X, Y, color = "blue")
    plt.savefig("Exemplo01.png")
    plt.close()

    # Exemplo 02

    def f(x):
        return e**(-x**2)

    X = [-4, -3, -2, -1, 1, 2, 3, 4]
    Y = [f(xi) for xi in X]

    coeffs = diff_div(X,Y)
    p = build_poly(X, coeffs)

    #print(coeffs)
    #for xi in X: print(f'{p(xi)}')

    t = np.linspace(min(X)-1, max(X)+1, 100)
    pt = [p(ti) for ti in t]
    ft = [f(ti) for ti in t]

    plt.plot(t, pt, color = "orange")
    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, color = "blue")
    plt.savefig("Exemplo02.png")
    plt.close()

    # Exemplo 03 (código não fixo):

    def f(x):
        return x**5 - 4*(x**2) + 2*(sqrt(x + 1)) + cos(x)

    X = [-0.481, -0.331, -0.252, -0.096, -0.029, 0.055, 0.207, 0.315, 0.428, 0.469, 0.584, 0.676, 0.797, 0.956, 1.022, 1.13, 1.25, 1.353, 1.419]
    Y = [f(xi) for xi in X]

    coeffs = diff_div(X,Y)
    p = build_poly(X, coeffs)

    for ci in coeffs: print(f'{ci:.20f},')
    #for xi in X: print(f'{p(xi)}')

    t = np.linspace(min(X), max(X), 100)
    pt = [p(ti) for ti in t]
    ft = [f(ti) for ti in t]

    plt.plot(t, pt, color = "orange")
    plt.plot(t, ft, color = "green")
    plt.scatter(X, Y, color = "blue")
    plt.savefig("Exemplo03.png")
    plt.close()

# Esse método se baseia em, para a seguinte lista (geral) de pontos:
#
# (x1, y1), (x2, y2), ..., (xn, yn)
#
# Utilizar tais pontos para encontrar cada coeficiente do polinômio na...
# ... forma:
#
# p(x) = a0 + a1.(x-x1) + a2.(x-x1).(x-x2) + ... + an-1.(x-x1)...(x-xn-1)
#
# Note que...
# Para o ponto (x1, y1) temos que:
#
# y1 = p(x1)
# y1 = a0 + 0 + 0 + ... + 0
# y1 = a0 
#
# Para o ponto (x2, y2) temos que:
#
# y2 = p(x2)
# y2 = a0 + a1.(x2-x1) + 0 + 0 + ... + 0
# y2 = y1 + a1.(x2-x1)
# a1.(x2-x1) = y2-y1
# a1 = (y2-y1)/(x2-x1)
#
# Para o ponto (x3, y3) temos que:
#
# y3 = p(x3)
# y3 = a0 + a1.(x3-x1) + a2.(x3-x1).(x3-x2) + 0 + ... + 0
# y3 = y1 + (y2-y1).(x3-x1)/(x2-x1) + a2.(x3-x1).(x3-x2)
# y3-y2 = y1-y2 + (y2-y1).(x3-x1)/(x2-x1) + a2.(x3-x1).(x3-x2)
# (y3-y2)(x3-x2)/(x3-x2) = -(y1-y2)(x2-x1)/(x2-x1) + (y2-y1).(x3-x1)/(x2-x1) + a2.(x3-x1).(x3-x2)
# (y3-y2)(x3-x2)/(x3-x2) = (y1-y2)(x3-x2)/(x2-x1) + a2.(x3-x1).(x3-x2)
# a2.(x3-x1)(x3-x2) = (y3-y2)(x3-x2)/(x3-x2) - (y1-y2)(x3-x2)/(x2-x1)
# a2.(x3-x1) = (y3-y2)/(x3-x2) - (y1-y2)/(x2-x1)
# a2 = [(y3-y2)/(x3-x2) - (y1-y2)/(x2-x1)]/(x3-x1)
#
# Fazendo o mesmo processo para cada coeficiente teremos algo bem complicado...
# ... porém há uma tabela que pode auxiliar...