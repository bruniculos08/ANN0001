from math import *
from NodesAndWeights import *

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

def trapeze_sum_alternative(X, Y):
    n = len(X)-1
    sum = Y[0]/2 + Y[-1]/2
    base = (X[-1]-X[0])/n
    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += Y[k]
    area = base*sum
    return area

def simpson_alternative(X, Y):
    num_subintervals = len(X)-1
    # Obs.: num_intervals(n) é o número de subintervalos, n/2 é o número de parábolas e n+1 é o número de pontos na partição.
    h = (X[-1]-X[0])/num_subintervals
    sum = Y[0] + Y[-1]
    # k varia até 2n
    for k in range(2, num_subintervals, 2):
        sum += 2*Y[k]
    # k varia até 2n-1 (quando k = 2n+1 o loop para)
    for k in range(1, num_subintervals, 2):
        sum += 4*Y[k]
    sum = (h/3)*sum        
    return sum

if __name__ == '__main__':
    n = 16
    X = [i*0.75 for i in range(n+1)]
    R_values = [9.82, 9.33, 8.81, 8.7, 8.07, 7.87, 7.19, 6.96, 6.53, 6.04, 5.74, 5.28, 4.81, 4.34, 3.88, 3.67, 3.14]
    print(X)

    # (1) Usando o método dos trapézios:
    print(f"Método dos Trapézios: Resultado = {trapeze_sum_alternative(X, R_values)}")

    # (2) Usando o método da regra de Simpson:
    print(f"Método da Regra de Simpson: Resultado = {simpson_alternative(X, R_values)}")
