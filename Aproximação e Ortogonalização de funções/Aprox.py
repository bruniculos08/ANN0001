from math import *
import numpy as np
import matplotlib.pyplot as plt

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

# Função que retorna o produto escalar entre duas funções f(x) e g(x):
def prod_esc(f, g, a, b, n):
    return trapeze_sum(lambda x: f(x)*g(x), a, b, n)

# Função que retorna o resultado da projeção de f(x) em g(x):
def proj(f, g, a, b, n):
    def proj(x):
        return (prod_esc(f, g, a, b, n)/prod_esc(g, g, a, b, n))*g(x)
    return proj

# Função que retorna o resultado a constante k da projeção de f(x) em g(x):
def proj_k(f, g, a, b, n):
    return (prod_esc(f, g, a, b, n)/prod_esc(g, g, a, b, n))

# Função para ortogonalizar uma lista de funções (Gran Schimidt):
def ortog_funcs(func_list, a, b, n):
    G = [func_list[0]]
    for fi in func_list[1:]:
        def gi(x):
            sum = 0
            for gj in G:
                sum -= proj_k(fi, gj, a, b, n)*gj(x)
            return fi(x) + sum
        G.append(gi)
    return G
# Obs.: essa função resulta em erro de recursão.

if __name__ == '__main__':
    
    # Exemplo 01:
    def f1(x): return 1
    def f2(x): return x
    def f3(x): return x**2
    def f4(x): return x**3

    def g1(x): return f1(x)
    def g2(x): return f2(x) - proj_k(f2, g1)
    def g3(x): return f3(x) - proj_k(f3, g1)*g1(x) - proj_k(f3, g2)*g2(x)
    def g4(x): return f4(x) - proj_k(f4, g1)*g1(x) - proj_k(f4, g2)*g2(x) - proj_k(f4, g3)*g3(x)