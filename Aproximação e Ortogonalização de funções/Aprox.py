from math import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify

# Métodos de integração (necessários para solução do sistema de equações):
def trapeze_sum(f, a, b, n):
    sum = f(a)/2 + f(b)/2
    base = (b-a)/n
    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += f(a + k*base)
    area = base*sum
    return area


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

"""
Observe que são calculadas n integrais na diagonal + [(n-1) + (n-2) + ... + 2 + 1] integrais das diagonais acima + n integras das integrais
na matriz B, o que resulta em n(n+1)/2 + n = (n² + 3n)/2 integrais, o que é mesmo assim uma valor O(n²) apesar da otimização em relação aos
elementos iguais (pela simetria da matriz).
"""

def aprox_coeffs_ort(func_list, f, a, b, n):
    coeffs = []
    for fi in func_list:
        ck = trapeze_sum(lambda x: f(x)*fi(x), a, b, n)/trapeze_sum(lambda x: fi(x)*fi(x), a, b, n)
        coeffs.append(ck)
    return coeffs

"""
Observe que nesta outra função, dado que estamos considerando que 'func_list' é uma lista de funções duas à duas ortogonais, precisamos apenas
calcular os n elementos da diagonal da matriz A + os n elementos da matriz coluna B, assim temos que calcular 2n integrais apenas, e portanto,
agora temos um problema de complexidade O(n).
"""

def build_aprox_func(func_list, coeffs):
    def g(x):
        return sum(ck*fk(x) for ck, fk in zip(coeffs, func_list))
    return g

"""
Função que retorna <f(x), g(x)> para um espaço vetorial de funções C[a,b], ou seja, que 
retorna o produto escalar entre duas funções f(x) e g(x) no intervalo [a,b]:
"""
def prod_esc(f, g, a, b, n):
    return trapeze_sum(lambda x: f(x)*g(x), a, b, n)

"""
Função que retorna (<f(x), g(x)>/<g(x), g(x)>).g(x), ou seja, o resultado da projeção de f(x) em g(x):
"""
def proj(f, g, a, b, n):
    def proj(x):
        return (prod_esc(f, g, a, b, n)/prod_esc(g, g, a, b, n))*g(x)
    return proj

"""
Função que retorna o resultado a constante k da projeção de f(x) em g(x), ou seja,
k = <f(x), g(x)>/<g(x), g(x)>:
"""
def proj_k(f, g, a, b, n) -> float:
    return (prod_esc(f, g, a, b, n)/prod_esc(g, g, a, b, n))


"""
Função para ortogonalizar uma lista de funções (Gran Schimidt):
Nota: lembre-se que para ortogonalizar um função f(x) em relação à outra função g(x) deve se obter então uma nova
função h(x) tal que:

    h(x) = f(x) - proj<f(x), g(x)> = f(x) - k.g(x), onde k = <f(x), g(x)>/<g(x), g(x)>, 

o que é igual a função f(x) subtraída da sua componente na mesma direção de g(x) (tratando as funções com vetores).
"""
def ortog_funcs(func_list, a, b, n):
    G = [func_list[0]]
    G_func_list = [symbolToFunc(func_list[0])]
    for fi in func_list[1:]:
        gi = fi - sum(proj_k(symbolToFunc(fi), symbolToFunc(gj), a, b, n)*gj for gj in G)
        gi = simplify(gi)
        G.append(gi)
        G_func_list.append(symbolToFunc(gi))
    return G_func_list
"""
Obs: a função acima ('ortog_funcs') não resulta mais em erro de recursão pois agora utiliza a biblioteca sympy
na construção das funções, e portanto visto que agora tais funções são construídas algebricamente e não por meio de chamadas
de outras funções, as mesmas são agora funções folha (logo não fazem recursão ou chamada de outras funções)
"""

def stringToFunc(string):
    def f(x):
        return eval(string)
    return f

def symbolToFunc(expr):
    return stringToFunc(str(expr))

if __name__ == '__main__':
    
    # Exemplo 01:
    a = -1
    b = 1
    n = 256

    def f1(x): return 1
    def f2(x): return x
    def f3(x): return x**2
    def f4(x): return x**3

    def g1(x): return f1(x)

    a_21 =  proj_k(f2, g1, a, b, n)
    def g2(x): return f2(x) - a_21*g1(x)
    
    a_31 = proj_k(f3, g1, a, b, n)
    a_32 = proj_k(f3, g2, a, b, n)
    def g3(x): return f3(x) - a_31*g1(x) - a_32*g2(x)
    
    a_41 = proj_k(f4, g1, a, b, n)
    a_42 = proj_k(f4, g2, a, b, n)
    a_43 = proj_k(f4, g3, a, b, n)
    def g4(x): return f4(x) - a_41*g1(x) - a_42*g2(x) - a_43*g3(x)

    func_list = [g1, g2, g3, g4]

    # Função para aproximar g(x):
    def f(x): 
        return log(x+5, e) + cos(x)*x**2

    coeffs = aprox_coeffs_ort(func_list, f, a, b, n)
    g = build_aprox_func(func_list, coeffs)

    t = np.linspace(a, b, 200)
    ft = [f(ti) for ti in t]
    gt = [g(ti) for ti in t]

    plt.plot(t, ft, label = 'function', color = "red")
    plt.plot(t, gt, label = 'aproximation', color = "green")
    plt.legend()
    plt.savefig("Exemplo01.png")

    # Exemplo 02:
    a = -1
    b = 1
    n = 256

    x = symbols('x')
    func_list = [1, x, x**2, x**3]
    orto_func_list = ortog_funcs(func_list, a, b, n)

    # Função para aproximar g(x):
    def f(x): 
        return log(x+5, e) + cos(x)*x**2

    coeffs = aprox_coeffs_ort(orto_func_list, f, a, b, n)
    g = build_aprox_func(orto_func_list, coeffs)

    t = np.linspace(a, b, 200)
    ft = [f(ti) for ti in t]
    gt = [g(ti) for ti in t]

    plt.plot(t, ft, label = 'function', color = "red")
    plt.plot(t, gt, label = 'aproximation', color = "green")
    plt.legend()
    plt.savefig("Exemplo02.png")