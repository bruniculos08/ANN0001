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
#   (viii) Fk+1(h) = (2^k).(Fk(h/2) - Fk(h))/[(2^k) - 1] :. k > 0 e k ∈ N
#
# Essa fórmula pode ser usada para aproximar M e o erro nessa aproximação é de O(h^k+1).
#
# A expressão (viii) é a expressão que caracteriza o método de Extrapolação de Richardson.
#
# Para não ter que se utilizar o método de maneira recursiva (o que é computacionalmente...
# ... custoso) podemos utilizar uma tabela:

from math import *
import numpy as np

def richardson(f, x0, h, k):
    table = []
    for i in range(k):
        item = F1(f, x0, h/(2**i))
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((2**(i+1))*table[j+1] - table[j])/(2**(i+1) - 1)
            table[j] = new_item

    return table[0] 

def F1(f, x0, h):
    return (f(x0+h) - f(x0))/h

def richardson_alternative(approximations, k):
    table = []
    for i in range(k):
        item = approximations[i]
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((2**(i+1))*table[j+1] - table[j])/(2**(i+1) - 1)
            table[j] = new_item

    return table[0]

if __name__ == '__main__':

    # Exemplo 01:
    x0 = 1.43264
    h = 0.36328
    orders = [4, 5, 6, 7, 8]
    def f(x): 
        return x**(x**(-x))   
    
    for k in orders:
        print(f"F{k}(h) = {richardson(f, x0, h, k)}")
    
    # Exemplo 02:
    x0 = 2.86789
    approximations = [-0.04249709218965991, -0.015945425841985106, -0.002944796743266309, 0.0034766767766925, 0.006666521347625576, 0.008256077439526166]
    k = 6
    def f(x): 
        return (x**2)*(e**(-x))*cos(x) + 1 
    
    print(f"F{k}(h) = {richardson_alternative(approximations, k)}") 