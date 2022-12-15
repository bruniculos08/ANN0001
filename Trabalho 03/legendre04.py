import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify
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

def quadrature(f, a, b, cord_quadrature, coeffs_quadrature):
    g = changeToQuadratureInterval(f, a, b)
    sum = 0
    for xi, ci in zip(cord_quadrature, coeffs_quadrature):
        sum += ci*g(xi)
    return sum

def changeToQuadratureInterval(f, a, b):
    """
    Muda uma função do intervalo [a, b] para o intervalo [-1, 1].
    Obs.: Note que nesta transformação a função também é multiplicada, isto pois ao se realizar a substituição de x pela nova variável t no
    intervalo [a, b] deve-se fazer a substituição dx = (dt/dx)dt.
    """
    def g(u):
        return f((b+a)/2 + (b-a) * (u/2)) * (b-a)/2
    return g

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

def aprox_coeffs_ort(func_list, f, a, b, cord_quadrature, coeffs_quadrature):
    coeffs = []
    for fi in func_list:
        ci = quadrature(lambda x: f(x)*fi(x), a, b, cord_quadrature, coeffs_quadrature)/quadrature(lambda x: fi(x)*fi(x), a, b, cord_quadrature, coeffs_quadrature)
        coeffs.append(ci)
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

def symbolToFunc(expr):
    return stringToFunc(str(expr))
    

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

def optimized_legendre(n):
    """
    Função que gera a lista do primeiro até o e-nésimo polinômio de Legendre de maneira iterativa
    Obs.: x deve ser um elemento da classe symbol da biblioteca sympy.
    """
    x = symbols('x')
    P = [1, x]
    P_func_list = [lambda x: 1, lambda x: x]
    for i in range(2, n+1):
        p_i = ((2 * i - 1) * x * P[1] - (i - 1) * P[0]) / i
        p_i = simplify(p_i)
        P.pop(0)
        # print(p_i, "\n\n")
        P.append(p_i)
        P_func_list.append(symbolToFunc(p_i))
    return P_func_list


def build_legendre_polynomial(n):
    def p(x):
        return legendre(x, n)
    return p

if __name__ == '__main__':

    """
    Exemplo 02:
    Não está funcionando (nota 7,71 na questão 10)
    """

    def f(x):
        return log(1 + x**2) * sin(10 * x)

    a = -1
    b = 1
    num_of_polys = 50
    exact_for_degree_less_than = 24

    P = optimized_legendre(num_of_polys)

    from NodesAndWeights import *
    order = str(int(exact_for_degree_less_than/2))    
    lists_names = ['raiz'+order, 'peso'+order]
    cord_quadrature = locals()[lists_names[0]]
    coeffs_quadrature= locals()[lists_names[1]]

    coeffs = aprox_coeffs_ort(P, f, a, b, cord_quadrature, coeffs_quadrature)
    g = build_aprox_func(P, coeffs)

    for ck in coeffs:
        print(f"{ck},")

    values = [-0.837, 0.254, 0.915]
    for i, xi in enumerate(values):
        print(f"g(x_{i+1}) = {g(xi)},")

    n = 1024
    erro = trapeze_sum(lambda x: (f(x)-g(x))**2, a, b, n)
    print(erro)

    t = np.linspace(a, b, 200)
    ft = [f(ti) for ti in t]
    gt = [g(ti) for ti in t]

    plt.plot(t, ft, color = "green", label = "f(x)")
    plt.plot(t, gt, color = "blue", label = "g(x)")
    plt.legend(loc="upper left")
    plt.savefig("legendre04.png")
    plt.close()