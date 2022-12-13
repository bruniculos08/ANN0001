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
    for fi in func_list:
        row = []
        b_i = trapeze_sum(lambda x: f(x)*fi(x), a, b, n)
        for fj in func_list:
            # Note que a_ij = ∫ fj(x)*fi(x) dx
            a_ij = trapeze_sum(lambda x: fi(x)*fj(x), a, b, n)
            row.append(a_ij)
        B.append(b_i)
        A.append(row)
    return np.linalg.solve(A, B)

def build_aprox_func(func_list, coeffs):
    def g(x):
        return sum(ck*fk(x) for ck, fk in zip(coeffs, func_list))
    return g

if __name__ == '__main__':
    
    # Exemplo 01:
    func_list = [lambda x: sin(x), lambda x: cos(x), lambda x: e**x, lambda x: x]

    def f(x):
        return log(x, e) + cos(x) + x

    a = 1
    b = 6
    n = 256

    coeffs = aprox_coeffs(func_list, f, a, b, n)
    g = build_aprox_func(func_list, coeffs)

    t = np.linspace(a, b, 200)
    ft = [f(ti) for ti in t]
    gt = [g(ti) for ti in t]

    plt.plot(t, ft, label = 'function', color = "red")
    plt.plot(t, gt, label = 'aproximation', color = "green")
    plt.legend()
    plt.savefig("Exemplo01.png")