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

def richardson(f, a, b, n, k):
    # Lembre-se que h = (b-a)/n ; o valor de n é dado indiretamente nas questões...
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

def aprox_coeffs(func_list, f, a, b, n):
    A = []
    B = []
    k = 8
    # Obs.: note que a matriz A é simétrica portanto não precisamos calcular n² integrais
    for i, fi in enumerate(func_list):
        row = []
        b_i = richardson(lambda x: f(x)*fi(x), a, b, n, k)
        for j, fj in enumerate(func_list):
            """
            Note que:
            (1) a_ij = ∫ fj(x)*fi(x) dx;
            (2) visto que a matriz A é simétrica e a parte acima da diagonal é calculada primeiro,
            não é necessário calcular os elementos em que i > j.
            """
            if(i <= j):
                a_ij = richardson(lambda x: fi(x)*fj(x), a, b, n, k)
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
    func_list = [lambda x: 2, lambda x: x - 1, lambda x: x**2 + 1, lambda x: x**3 + x - 3, lambda x: 0.5 * x**4 - 3 * x**2 + 1, lambda x: x**5 - 4 * x + 2, 
        lambda x: x**7-x]

    def f(x):
        return x**2 * cos(x * sin(log(1 + x**2)))

    a = -2.11725
    b = 2.00316
    n = 10
    # Obs.: k é definido dentro da função para uso do método de Romberg (função 'Richardson').

    coeffs = aprox_coeffs(func_list, f, a, b, n)
    for ck in coeffs: 
        print(f"{ck},")

    g = build_aprox_func(func_list, coeffs)
    values = [-1.21468 , -0.40947, 0.93108]

    for xi in values:
        print(f"{g(xi)},")

    n = 256
    print(simpson(lambda x: (f(x)-g(x))**2, a, b, n))

    # t = np.linspace(a, b, 200)
    # ft = [f(ti) for ti in t]
    # gt = [g(ti) for ti in t]

    # plt.plot(t, ft, label = 'function', color = "red")
    # plt.plot(t, gt, label = 'aproximation', color = "green")
    # plt.legend()
    # plt.savefig("Otimização01.png")