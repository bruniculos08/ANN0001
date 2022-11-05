from math import *
from NodesAndWeights import *

# Constantes usadas na fórmula:
cd = 0.43
g = 9.81
m = 74.08
# Fórmula:
def v(t):
    return sqrt(g*m/cd) * tanh(sqrt(g*cd/m)*t)

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

def quadrature(f, cord, coeffs):
    sum = 0
    for xi, ci in zip(cord, coeffs):
        sum += ci*f(xi)
    return sum

def change(f, a, b):
    def g(u):
        return f((b+a)/2 + (b-a) * (u/2)) * (b-a)/2
    return g

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

if __name__ == '__main__':
    # (1) Usando o método dos trapézios:
    a, b = 0, 8.36
    n = 32
    print(f"Método dos Trapézios: Resultado = {trapeze_sum(v, a, b, n)}")

    # (2) Usando o método da regra de Simpson:
    a, b = 0, 8.36
    n = 16
    print(f"Método da Regra de Simpson: Resultado = {simpson(v, a, b, n)}")

    # (3) Usando o método de Romberg:
    a, b = 0, 8.36
    # h = (b-a)/n -> n = 10
    n = 10 
    k = 10
    print(f"Método de Romberg: Resultado = {richardson(v, a, b, n, k)}")

    # (4) Usando o método da quadratura gaussiana:
    a, b = 0, 8.36
    exact_for_degree_less_than = 10
    order = str(int(exact_for_degree_less_than/2))
    cord = locals()["raiz"+order]
    coeffs = locals()["peso"+order]
    print(f"Método da quadratura gaussiana: Resultado = {quadrature(change(v, a, b), cord, coeffs)}")
