# Método de Simpson



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

def simpson_alternative(X, Y):
    n = len(X)
    sum = 0

    for k in range(2, n, 2):
        sum += (X[k-1] - X[k-2])/3 * (Y[k-2] + 4*Y[k-1] + Y[k])

    return sum


if __name__ == '__main__':

    from math import *

    # Exemplo 01:
    a = -1.078
    b = 1.412
    subintervals = [6, 20, 40, 72, 88, 104, 146, 168, 186, 226, 302]
    def f(x):
        return sqrt(sin(cos(log(x**2 + 1, e) + 2) + 3) + 4)

    for n in subintervals:
        #print(f"Área aproximada pela regra de simpson = {simpson(f, a, b, m)}")
        print(f"{simpson(f, a, b, n)},")

    # Exemplo 02:
    X = [0.004, 0.114, 0.224, 0.244, 0.264, 0.291, 0.318, 0.371, 0.424, 1.1265, 1.829, 1.837, 1.845, 1.969, 2.093, 2.2665, 2.44, 2.448, 2.456, 2.473, 2.49, 2.637, 2.784, 2.8145, 2.845, 2.9585, 3.072, 3.108, 3.144, 3.157, 3.17, 3.2085, 3.247, 3.264, 3.281, 3.304, 3.327, 3.421, 3.515, 3.574, 3.633, 4.095, 4.557, 4.7355, 4.914]
    Y = [1.254, 1.596, 1.987, 2.058, 2.128, 2.219, 2.307, 2.469, 2.611, 2.691, 2.029, 2.027, 2.024, 2.001, 2.009, 2.071, 2.192, 2.199, 2.206, 2.222, 2.238, 2.395, 2.577, 2.616, 2.655, 2.795, 2.912, 2.942, 2.966, 2.973, 2.98, 2.994, 3.0, 3.0, 2.998, 2.992, 2.982, 2.901, 2.749, 2.616, 2.457, 1.052, 2.252, 2.932, 2.804]

    print(f"Área aproximada pela regra de simpson = {simpson_alternative(X, Y)}")

    pass