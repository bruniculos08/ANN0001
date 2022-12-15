import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, simplify
from math import *
from NodesAndWeights import *

"""
Método de interpolação para ser usado nas raízes do polinômio de Chebyshev:
"""
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

"""
Métodos de integração e de aproximação de funções para serem utilizados em conjunco com polinômios 
de Chebyshev:
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

def aprox_coeffs(func_list, f, a, b, cord_quadrature, coeffs_quadrature):
    A = []
    B = []
    # Obs.: note que a matriz A é simétrica portanto não precisamos calcular n² integrais
    for i, fi in enumerate(func_list):
        row = []
        b_i = quadrature(lambda x: f(x)*fi(x), a, b, cord_quadrature, coeffs_quadrature)
        for j, fj in enumerate(func_list):
            """
            Note que:
            (1) a_ij = ∫ fj(x)*fi(x) dx;
            (2) visto que a matriz A é simétrica e a parte acima da diagonal é calculada primeiro,
            não é necessário calcular os elementos em que i > j.
            """
            if(i <= j):
                a_ij = quadrature(lambda x: fi(x)*fj(x), a, b, cord_quadrature, coeffs_quadrature)
                row.append(a_ij)
            else:
                row.append(A[j][i])
                
        B.append(b_i)
        A.append(row)
    return np.linalg.solve(A, B)

def build_aprox_func(func_list, coeffs):
    def g(x):
        return sum(ck*fk(x) for ck, fk in zip(coeffs, func_list))
    return g

"""
Dentre todos os polinômios de grau n que interpolam y = f(x) numa lista de n+1 pontos no intervalo [-1, 1],
aquele que interpola nas raízes do polinômio T_n+1(x) é o polinômio que melhor se aproxima da função y = f(x),
ou seja, esse polinômio minimiza a seguinte função erro:

    erro(P) = max|f(x)-P(x)| para -1 <= x <= 1, sendo P um polinômio

"""

def changeToChebyInterval(f, a, b):
    def F(u):
        return f(((b-a)/2) * u + (a+b)/2)
    return F

def changeFromChebyInterval(g, a, b):
    def G(u):
        return g((2/(b-a)) * u - (a+b)/(a-b))
    return G

def getChebyPoly(n):
    """
    Retorna o e-nésimo polinômio de chebyshev como um objeto de expressão
    da biblioteca sympy (o que é diferente e melhor que um função recursiva
    com complexidade O(2^n)).
    """
    x = symbols('x')
    t_n = 1
    T = [1, x]
    for _ in range(1, n):
        t_n = 2*T[1]*x - T[0]
        T = [T[1], t_n]
    return t_n

def getChebyPolyList(n):
    """
    Retorna a lista do n (note que começa do 0-ésimo e vai até o (n-1)-ésimo) primeiros polinômios de chebyshev como objetos de expressão
    da biblioteca sympy (o que é diferente e melhor que um função recursiva com complexidade O(2^n)).
    """
    x = symbols('x')
    t_n = 1
    T = [1, x]
    T_func_list = [lambda x: 1, lambda x: x] 
    for i in range(2, n):
        t_n = 2*T[i-1]*x - T[i-2]
        t_n = simplify(t_n)
        T.append(t_n)
        T_func_list.append(symbolToFunc(t_n))
    return T_func_list

def chebyRoots(n):
    """
    Retorna as n raízes do e-nésimo polinômio de chebyshev.
    """
    roots = []
    for k in range(1, n+1):
        x_k = cos((2*k-1)*pi/(2*n))
        roots.append(x_k)
    return roots

def stringToFunc(string):
    def f(x):
        return eval(string)
    return f

def symbolToFunc(expr):
    return stringToFunc(str(expr))

if __name__ == '__main__':

    # Exemplo 01:

    def f(x):
        return log(1 + x**2, e)*sin(10*x)

    a = -1
    b = 1
    exact_for_degree_less_than = 26
    last_poly_num = 21

    order = str(int(exact_for_degree_less_than/2))    
    lists_names = ['raiz'+order, 'peso'+order]
    cord_quadrature = locals()[lists_names[0]]
    coeffs_quadrature= locals()[lists_names[1]]
    print(cord_quadrature, coeffs_quadrature)

    # f_cheby = changeToChebyInterval(f, a, b)
    f_cheby = f
    cheby_polynomials = getChebyPolyList(last_poly_num+1)
    coeffs = aprox_coeffs(cheby_polynomials, f_cheby, a, b, cord_quadrature, coeffs_quadrature)
    p = build_aprox_func(cheby_polynomials, coeffs)
    # g = changeFromChebyInterval(p, a, b)
    g = p

    """
    Printando as respostas:
    """
    for ci in coeffs:
        print(f"{ci},")

    values = [-0.581, -0.152, 0.734]
    for i, x_i in enumerate(values):
        print(f"g(x_{i}) = {g(x_i)},")

    n = 4096
    erro = trapeze_sum(lambda x: (f(x)-g(x))**2, a, b, n)
    print(erro)

    """
    Plotando Gráfico:
    """

    t = np.linspace(a, b, 200)
    ft = [f(ti) for ti in t]
    gt = [g(ti) for ti in t]

    plt.plot(t, ft, color = "green", label = "f(x)")
    plt.plot(t, gt, color = "blue", label = "g(x)")
    plt.legend()
    # plt.savefig("cheby04.png")
    plt.close()