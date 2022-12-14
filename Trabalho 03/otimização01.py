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

def build_aprox_func(func_list, coeffs):
    def g(x):
        return sum(ck*fk(x) for ck, fk in zip(coeffs, func_list))
    return g

if __name__ == '__main__':
    
    # Exemplo 01:
    func_list = [lambda x: 1, lambda x: x, lambda x: x**2, lambda x: x**3, lambda x: x**4, lambda x: x**5, 
        lambda x: x**6, lambda x: x**7, lambda x: x**8]

    def f(x):
        return  x**2 * exp(x) * sqrt(log(2 + cos(-x**2)))

    a = -2.10778
    b = 0.84568
    n = 256

    coeffs = aprox_coeffs(func_list, f, a, b, n)
    for ck in coeffs: 
        print(f"{ck},")

    g = build_aprox_func(func_list, coeffs)
    values = [-0.27657 , 0.84128, 1.79411]

    for xi in values:
        print(f"{g(xi)},")

    n = 512
    print(trapeze_sum(lambda x: (f(x)-g(x))**2, a, b, n))

    # t = np.linspace(a, b, 200)
    # ft = [f(ti) for ti in t]
    # gt = [g(ti) for ti in t]

    # plt.plot(t, ft, label = 'function', color = "red")
    # plt.plot(t, gt, label = 'aproximation', color = "green")
    # plt.legend()
    # plt.savefig("Otimização01.png")