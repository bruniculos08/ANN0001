# Método dos Trapézios para integração:
#
# Considere um trapézio de altura h1 e h2 e base b; sua área é dada por:
#
#   A = b.(h1+h2)/2
# 
# Note que dada uma função f e um intervalor [a, b] separado em n+1 pontos tal que:
#
#   a = x0 < x1 < x2 < x3 < x4 < ... < xn-1 < xn = b
#
# Tem-se que:
#
#   a-b ∫ f(x) dx ≅ ∑ Tk
#
# Onde, definindo-se que, para 1 ≤ k ≤ n:
#
#   xk - xk-1 = (b-a)/n
#
# Tk é dado por:
#
#   Tk = [(b-a)/n]*[f(xk-1) + f(xk)]/2, com 1 ≤ k ≤ n
#
# Porém note que quando fizermos isso para obter a aproximação da integral da função teremos:
#
#   ∑ Tk = [(b-a)/n]*[f(x0) + f(x1)]/2 + [(b-a)/n]*[f(x1) + f(x2)]/2 + ... + [(b-a)/n]*[f(xn-2) + f(xn-1)]/2 + [(b-a)/n]*[f(xn-1) + f(xn)]/2
#
#   ∑ Tk = [(b-a)/n]*{[(f(x0) + f(x1)]/2 + [f(x1) + f(x2)]/2 + ... + [f(xn-2) + f(xn-1)]/2 + [f(xn-1) + f(xn)]/2}
#
#   ∑ Tk = [(b-a)/n]*{[(f(x0) + f(x1)]/2 + [f(x1) + f(x2)]/2 + ... + [f(xn-2) + f(xn-1)]/2 + [f(xn-1) + f(xn)]/2}
#
#   ∑ Tk = [(b-a)/n]*[f(x0)/2 + f(x1) + f(x2) + ... + f(xn-2) + f(xn-1) + f(xn)/2}
#
# Está última fórmula simplifica a execução do algoritmo.

def trapeze_sum(f, a, b, n):
    sum = f(a)/2 + f(b)/2
    base = (b-a)/n

    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += f(a + k*base)
    
    area = base*sum

    return area

def trapeze_sum_variable_subinterval(f, X):
    n = len(X)
    sum = 0

    for k in range(1, n):
        base = X[k] - X[k-1]
        sum += base*(f(X[k]) + f(X[k-1]))/2

    return sum


if __name__ == '__main__':

    from math import *

    # Exemplo 01:
    def f(x):
        return cos(x)
    a = 0
    b = 2
    n = 2000
    #print(f"Área = {trapeze_sum(f, a, b, n)}")

    # Exemplo 02:
    def f(x):
        return sin(x/(sqrt(x**2 + 1))) + 1
    a, b = -1.682, 1.618
    n_subintervalos = [2, 17, 45, 61, 84, 143, 162, 254, 525, 813, 4256, 5057]

    # for n in n_subintervalos:
    #     #print(f"Área = {trapeze_sum(f, a, b, n)} para n = {n};")
    #     print(f"{trapeze_sum(f, a, b, n)},")

    # Exemplo 03:
    X = [0.332, 0.351, 0.354, 0.368, 0.425, 0.437, 0.468, 0.507, 0.512, 0.572, 1.021, 1.039, 1.254, 1.315, 1.322, 1.501, 1.783, 2.118, 2.229, 2.253, 2.333, 2.385, 2.4, 2.476, 2.735, 2.903, 2.912, 3.001, 3.149, 3.234, 3.263, 3.268, 3.272, 3.356, 3.401, 3.443, 3.453, 3.484, 3.651, 3.849, 4.079, 4.246, 4.296, 4.336, 4.395, 4.464, 4.74]
    Y = [2.352, 2.41, 2.419, 2.46, 2.614, 2.643, 2.714, 2.791, 2.8, 2.892, 2.818, 2.798, 2.528, 2.452, 2.444, 2.246, 2.047, 2.014, 2.052, 2.064, 2.111, 2.148, 2.159, 2.225, 2.514, 2.728, 2.739, 2.843, 2.969, 2.999, 3.0, 2.999, 2.999, 2.964, 2.924, 2.872, 2.857, 2.807, 2.404, 1.726, 1.075, 1.055, 1.152, 1.265, 1.48, 1.79, 2.941]
    def f(x):
        i = X.index(x)
        return Y[i]
    
    print(f"Área = {trapeze_sum_variable_subinterval(f, X)}")

    pass