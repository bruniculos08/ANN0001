import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from math import *


"""
Métodos de integração e método do de aproximação de Funções:
"""

def trapeze_sum(f, a, b, n):
    sum = f(a)/2 + f(b)/2
    base = (b-a)/n
    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += f(a + k*base)
    area = base*sum
    return area

def simpson(f, a, b, num_subintervals):

    # Obs.: num_intervals(n) é o número de subintervalos, n/2 é o número de parábolas e n+1 é o número de pontos na partição.
    h = (b-a)/num_subintervals
    sum = f(a) + f(b)

    # k varia até 2n
    for k in range(2, num_subintervals, 2):
        sum += 2*f(a + k*h)

    # k varia até 2n-1 (quando k = 2n+1 o loop para)
    for k in range(1, num_subintervals, 2):
        sum += 4*f(a + k*h)

    sum = (h/3)*sum        
    return sum

def richardson(f, a, b, n, k):
    table = []
    # Obs.: dada essa função de erro inicial tem-se que Fk(h) diminui o erro para O(h^(2*k))
    k = int(k/2)

    for i in range(k):
        item = trapeze_sum(f, a, b, (2**i)*n)
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((4**(i+1))*table[j+1] - table[j])/(4**(i+1) - 1)
            table[j] = new_item

    return table[0]

def aprox_coeffs(func_list, f, a, b, n):
    A = []
    B = []
    # Obs.: note que a matriz A é simétrica portanto não precisamos calcular n² integrais
    for i, fi in enumerate(func_list):
        row = []
        b_i = trapeze_sum(lambda x: f(x)*fi(x), a, b, n)
        for j, fj in enumerate(func_list):
            """
            Note que:
            (1) a_ij = ∫ fj(x)*fi(x) dx;
            (2) visto que a matriz A é simétrica e a parte acima da diagonal é calculada primeiro,
            não é necessário calcular os elementos em que i > j.
            """
            if(i <= j):
                a_ij = trapeze_sum(lambda x: fi(x)*fj(x), a, b, n)
                row.append(a_ij)
            else:
                row.append(A[j][i])
        B.append(b_i)
        A.append(row)
    return np.linalg.solve(A, B)

def aprox_coeffs_ort(func_list, f, a, b, n):
    coeffs = []
    for fi in func_list:
        ck = simpson(lambda x: f(x)*fi(x), a, b, n)/simpson(lambda x: fi(x)*fi(x), a, b, n)
        coeffs.append(ck)
    return coeffs

def build_aprox_func(func_list, coeffs):
    def g(x):
        return sum(ck*fk(x) for ck, fk in zip(coeffs, func_list))
    return g

# Transforma string em função:
def stringToFunc(string):
    def f(x):
        return eval(string)
    return f

"""
Funções recursivas para geração dos polinômios de Legendre (lembre-se que estes polinômios são dois a dois ortogonais,
portanto podemos utilizar o método mais eficiente para se obter os coeficientes da aproximação para uma determinar função f(x)):
(Anotação: fazer as funções de maneira não recursiva usando a biblioteca sympy)
"""

def legendre(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legendre(x, n - 1) - (n - 1) * legendre(x, n - 2)) / n

def build_legendre_polynomial(n):
    def p(x):
        return legendre(x, n)
    return p

if __name__ == '__main__':

    # Exemplo 02:

    def f(x):
        return  x * cos(10 * x**2 * exp(-x**2))

    a = -1
    b = 1
    num_of_polys = 10
    n = 256

    P = []
    for i in range(0, num_of_polys+1):
        p_n = build_legendre_polynomial(i)
        P.append(p_n)

    coeffs = aprox_coeffs_ort(P, f, a, b, n)
    g = build_aprox_func(P, coeffs)

    for ck in coeffs:
        print(f"{ck},")

    values = [-0.542, 0.141, 0.595]
    for i, xi in enumerate(values):
        print(f"g(x_{i+1}) = {g(xi)},")

    n = 10
    k = 8
    erro = richardson(lambda x: (f(x)-g(x))**2, a, b, n, k)
    print(erro)

    t = np.linspace(a, b, 200)
    ft = [f(ti) for ti in t]
    gt = [g(ti) for ti in t]

    plt.plot(t, ft, color = "green", label = "f(x)")
    plt.plot(t, gt, color = "blue", label = "g(x)")
    plt.legend(loc="upper left")
    plt.savefig("legendre02.png")
    plt.close()