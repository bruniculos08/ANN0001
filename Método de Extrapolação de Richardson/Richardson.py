# Método da Extrapolação de Richardson
#
# Suponha que F1(h) seja uma fórmula que pode ser usada para aproximar um certo número M, e que o erro da aproximação seja O(h), ou seja,...
# ... suponha que:
#
#   (i)  M = F1(h) + k1.h + k2.h² + k3.h³ + k4.h^4 + ...
#
# trocando h por h/2 na expressão acima considerando que h seja suficiente pequeno de modo que a igualdade (aproximação) se mantém...
# ... obtemos:
#
#   (ii) M = F1(h/2) + k1.h/2 + k2.h²/4 + k3.h³/8 + ...
#
# Se multiplicarmos (2) por 2 e subtrair com (1), obtemos:
#
#   (iii) 2.M - M = M = F(h/2) - F(h) - k2.h²/2 - k3.(3/4).h³ - ...
#
# A expressão (3) diz que M pode ser aproximádo por:
#
#   (iv) F2(h) = 2.F1(h/2) - F1(h) 
#
# e que o erro desta aproximação é O(h²). Trocando h por h/2 na expressão (iv), obtemos:
#
#   (v) M = F2(h/2) - k2.(h²/8) - k3.(h³/32) - ...
#
# multiplicando (v) por 4 e subtraindo (iv) obtemos: 
#
#   (vi) 3.M = 4.F2(h/2) - F2(h) + (3/8).k3.h² + ... 
#
#        M = (1/3).(4.F2(h/2) - F2(h)) + (1/8).k3.h² + ... 
#
# A expressão (vi) nos diz que M pode ser aproximado por:
#
#   (vii) F3(h) = (1/3).(4.F2(h/2) - F2(h)) 
#
# e que o erro nessa aproximação é O(h³). Repetindo esse procedimento k vezes obtemos:
#
#   Fk+1(h) = (2^k).(Fk(h/2) - Fk(h))/[(2^k) - 1] :. k > 0 e k ∈ N
#
# Essa fórmula pode ser usada para aproximar M e o erro nessa aproximação é de O(h^k+1).

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