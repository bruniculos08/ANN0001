from sympy import symbols
from math import *


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

def chebyRoots(n):
    """
    Retorna as n raízes do enésimo polinômio de chebyshev.
    """
    roots = []
    for k in range(1, n+1):
        x_k = cos((2*k-1)*pi/(2*n))
        roots.append(x_k)
    return roots

if __name__ == '__main__':

    x = symbols('x')
    poly = getChebyPoly(3)
    rs = chebyRoots(3)
    print(rs)

    for root in rs:
        print(poly.subs(x, root))