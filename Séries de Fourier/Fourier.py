import matplotlib.pyplot as plt
import numpy as np
from math import *

def trapeze_sum(f, a, b, n):
    sum = f(a)/2 + f(b)/2
    base = (b-a)/n
    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += f(a + k*base)
    area = base*sum
    return area

def fourier_coeffs(f, num_coeffs, num_intervals):
    """
    Retorna os coeficientes a_n's, b_n's e c da série de fourier 
    para uma determinada função f(x)
    """   
    a = -pi
    b = pi
    A = []
    B = []

    c = (1/(2*pi))*trapeze_sum(f, a, b, num_intervals)

    for m in range(1, num_coeffs+1):
        a_m = (1/pi)*trapeze_sum(lambda x: f(x)*cos(m*x), a, b, num_intervals)
        b_m = (1/pi)*trapeze_sum(lambda x: f(x)*sin(m*x), a, b, num_intervals) 
        A.append(a_m)
        B.append(b_m)

    return A, B, c

def build_fourier(A, B, c):
    """
    Monta a série de fourier a partir dos coeficientes a_n's, b_n's e c
    calculados para um determinada função f(x)
    """
    def f(x):
        return c + sum(a_n*cos(n*x) + b_n*sin(n*x) for n, (a_n, b_n) in enumerate(zip(A, B), 1))
    return f

if __name__ == "__main__":
    
    def f(x):
        if x < 0:
            return 3 + x / pi
        return 1 + x / pi

    num_intervals = 256

    A, B, c = fourier_coeffs(f, 10, num_intervals)
    g = build_fourier(A, B, c)

    print(A, B, c)

    t = np.linspace(-pi, pi, 200)
    ft = [f(ti) for ti in t]
    gt = [g(ti) for ti in t]

    plt.plot(t, ft, color='green', label='f(x)')
    plt.plot(t, gt, color='blue', label='Fourier Serie for f(x)')
    plt.legend()
    plt.savefig("Exemplo01.png")
    plt.close()