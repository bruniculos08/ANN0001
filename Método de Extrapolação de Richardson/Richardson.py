# Método da Extrapolação de Richardson
#
# Suponha que F(h) seja uma fórmula que pode ser usada para aproximar um certo número M, e que o erro da aproximação seja O(h), ou seja,...
# ... suponha que:
#
#   M = F(h) + k1.h + k2.h² + k3.h³ + k4.h^4 + ...
#
# trocando h por h/2 na expressão acima considerando que h seja suficiente pequeno de modo que a igualdade (aproximação) se mantém...
# ... obtemos:
#
#   M = F(h/2) + k1.h/2 + k2.h²/4 + k3.h³/8 + ...

from math import *
import numpy as np

def richardson():
    return


if __name__ == '__main__':

    # Exemplo 01:
    X = [7.1146, 7.1457, 7.3827]
    x0 = 7.223
    k = 2
    def f(x): 
        return exp(cos(x)**2) + exp(-x**2) + log(x)
    
    string = "'"*k
    #print(f"f{string}({x0}) ~ {get_aprox(X, coeffs, f)}")

    pass