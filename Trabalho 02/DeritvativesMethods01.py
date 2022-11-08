# Métodos para derivadas:
import matplotlib.pyplot as plt
import numpy as np
from math import *

# Método das diferenças finitas(cálculo dos coeficientes):
def diff_fin(X, x0, k):
    n = len(X)
    A = []
    B = []

    for i in range(n):
        row = []
        for xi in X:
            row.append(xi**i)
        A.append(row)
        if i < k:
            B.append(0)
        else:
            # como i varia de 0 até n-1 e não de 1 até n tem-se:
            b = (factorial(i)/factorial(i-k))*(x0**(i-k))
            B.append(b)

    return np.linalg.solve(A, B)

# Método das diferenças finitas(cálculo da aproximação da derivada de acordo com os coeficientes encontrados...
# ... pela função anterior):
def get_aprox(X, coeffs, f):
    sum = 0
    for xi, ci in zip(X, coeffs):
        sum += ci*f(xi)
    return sum

# Contrução da fórmula de Taylor para n:
def build_taylor(X, x0, f, n):
    def p(x):
        poly = f(x0)
        for i in range(n):
            coeffs = diff_fin(X, x0, i+1)
            poly += get_aprox(X, coeffs, f) * (x - x0)**(i+1) / factorial(i+1)
        return poly
    return p

# Método de extrapolação de Richardson:
def richardson(f, x0, h, k):
    table = []
    for i in range(k):
        item = F1(f, x0, h/(2**i))
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((2**(i+1))*table[j+1] - table[j])/(2**(i+1) - 1)
            table[j] = new_item

    return table[0]

# Função usada no método de extrapolação de Richardson:
def F1(f, x0, h):
    return (f(x0+h) - f(x0))/h

# Método de extrapolação de Richardson usando:
def richardson_alternative(approximations, k):
    # Note que aproximantion[i] é a função F1 calculada na linha i do método, ou seja, com F1(h/2**i):
    table = []
    for i in range(k):
        item = approximations[i]
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((2**(i+1))*table[j+1] - table[j])/(2**(i+1) - 1)
            table[j] = new_item

    return table[0]

if __name__ == '__main__':

    # # Exemplo 01 - Método das diferenças finitas:
    # X = [7.1146, 7.1457, 7.3827]
    # x0 = 7.223
    # # k-ésima derivada:
    # k = 2
    # def f(x): 
    #     return exp(cos(x)**2) + exp(-x**2) + log(x)
    
    # coeffs = diff_fin(X, x0, k)
    # string = "'"*k
    # print(f"f{string}({x0}) ~ {get_aprox(X, coeffs, f)}")

    # # Exemplo 02 - Polinômio de Taylor pelo método das difereças finitas:
    # X = [0.1933, 0.2334, 0.2667, 0.3575, 0.3771, 0.4527, 0.491, 0.5263, 0.5926, 0.6308]
    # x0 = 0.408
    # n = 5
    # def f(x):
    #     return x**2 * cos(x - 1) * exp(-3 * x ** 2)

    # taylor = build_taylor(X, x0, f, n)
    # values = [0.3402, 0.344, 0.3911, 0.3923, 0.4879]

    # for value in values:
    #     #print(f"p({value}) = {taylor(value):.10e}")
    #     print(f"{taylor(value):.10e}, {abs(f(value)-taylor(value)):.10e},")
    #     #print(f"|f({value})-p({value})| = {abs(f(value)-taylor(value)):.10e}")

    # Exemplo 03 - Método de extrapolação de Richardson:
    x0 = 1.43264
    h = 0.36328
    # A ordem é o expoente da função de erro O(h^k)
    orders = [4, 5, 6, 7, 8]
    def f(x): 
        return x**(x**(-x))   
    
    for k in orders:
        print(f"F{k}(h) = {richardson(f, x0, h, k)}")

    angular_coeff = richardson(f, x0, h, max(orders))
    def df(x):
        return angular_coeff*(x-x0) + f(x0)

    t = np.linspace(x0 - 4, x0 + 4, 100)
    ft = [f(ti) for ti in t]
    dt = [df(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.plot(t, dt, color = "orange")
    plt.scatter(x0, f(x0), label = "blue")
    plt.savefig("Exemplo03 - DerivativesMethods01.png")
    plt.close()

    # Exemplo 04 - Método de extrapolação de Richardson utilizando aproximações para cada F1(h/(2^k)), ou seja, sem...
    # ... utilizar a fórmula de F1(h):
    x0 = 2.86789
    approximations = [-0.04249709218965991, -0.015945425841985106, -0.002944796743266309, 0.0034766767766925, 0.006666521347625576, 0.008256077439526166]
    k = 6
    def f(x): 
        return (x**2)*(e**(-x))*cos(x) + 1 
    
    angular_coeff = richardson_alternative(approximations, k)
    print(f"F{k}(h) = {richardson_alternative(approximations, k)}") 

    def df(x):
        return angular_coeff*(x-x0) + f(x0)

    # Obs.: Neste modelo do método, tanto x0, quanto a função f são irrelevantes.

    t = np.linspace(x0 - 4, x0 + 4, 100)
    ft = [f(ti) for ti in t]
    dt = [df(ti) for ti in t]

    plt.plot(t, ft, color = "green")
    plt.plot(t, dt, color = "orange")
    plt.scatter(x0, f(x0), label = "blue")
    plt.savefig("Exemplo04 - DerivativesMethods01.png")
    plt.close()
