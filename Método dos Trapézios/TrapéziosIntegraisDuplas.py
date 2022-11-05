# Método dos Trapézios para integrais duplas:
from math import *

def trapeze_double_sum(f, a, b, c, d, m, n):
    # Bases dos trapézios (subintervalos) nas direções de x e de y respectivamente:
    h1 = (b-a)/m
    h2 = (d-c)/n

    # Somatórios da fórmula:
    sum_corners = 0
    sum_const_Y_edges = 0
    sum_const_X_edges = 0
    sum_inside = 0

    # Calculando sum_corners:
    for y in [c, d]:
        for x in [a, b]:
            sum_corners += f(x, y)

    # Calculando sum_const_Y_edges:
    for y in [c, d]:
        for i in range(1, m):
            xi = a + i*h1
            sum_const_Y_edges += f(xi, y)

    # Calculando sum_const_X_edges:
    for x in [a, b]:
        for j in range(1, n):
            yj = c + j*h2
            sum_const_X_edges += f(x, yj)
                
    # Calculando sum_inside:
    for j in range(1, n):
        yj = c + j*h2
        for i in range(1, m):
            xi = a + i*h1
            sum_inside += f(xi, yj)

    sum = (h1*h2/4)*(sum_corners + 2*(sum_const_Y_edges + sum_const_X_edges) + 4*(sum_inside))
    return sum

if __name__ == '__main__':

    # Exemplo 01:
    a, b = [-1.09, 1.498]
    c, d = [-1.514, 1.33]
    m = 256
    n = 128
    def f(x, y):
        return sqrt(e**(-(x**2)*(y**2)) + 1)
    
    print(f"Resultado (volume): {trapeze_double_sum(f, a, b, c, d, m, n)}")

    pass