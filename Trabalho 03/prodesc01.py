from math import *

"""
Métodos de integração:
"""
def trapeze_sum(f, a, b, n):
    sum = f(a)/2 + f(b)/2
    base = (b-a)/n
    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += f(a + k*base)
    area = base*sum
    return area


"""
Função que retorna <f(x), g(x)> para um espaço vetorial de funções C[a,b], ou seja, que 
retorna o produto escalar entre duas funções f(x) e g(x) no intervalo [a,b]:
"""
def prod_esc(w, f, g, a, b, n):
    return trapeze_sum(lambda x: w(x)*f(x)*g(x), a, b, n)

if __name__ == '__main__':

    w = lambda x: e**(-x)
    f1 = lambda x: x**3 + 1
    f2 = lambda x: 1 + sin(3*x - 1)

    a, b = [1.494,1.255]
    n = 256
    result = prod_esc(w, f1, f2, a, b, n)
    print(result)

    pass