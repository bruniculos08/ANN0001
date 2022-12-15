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

def quadrature(f, a, b, cord_quadrature, coeffs_quadrature):
    g = changeToQuadratureInterval(f, a, b)
    sum = 0
    for xi, ci in zip(cord_quadrature, coeffs_quadrature):
        sum += ci*g(xi)
    return sum

def changeToQuadratureInterval(f, a, b):
    def g(u):
        return f((b+a)/2 + (b-a) * (u/2)) * (b-a)/2
    return g

"""
Função que retorna <f(x), g(x)> para um espaço vetorial de funções C[a,b], ou seja, que 
retorna o produto escalar entre duas funções f(x) e g(x) no intervalo [a,b]:
"""
def prod_esc(w, f, g, a, b, cord_quadrature, coeffs_quadrature):
    return quadrature(lambda x: w(x)*f(x)*g(x), a, b, cord_quadrature, coeffs_quadrature)

if __name__ == '__main__':

    w = lambda x: e**(-x)
    f1 = lambda x: x**3 + 1
    f2 = lambda x: 1 + sin(3*x - 1)

    from NodesAndWeights import *
    exact_for_degree_less_than = 16
    order = str(int(exact_for_degree_less_than/2))    
    lists_names = ['raiz'+order, 'peso'+order]
    cord_quadrature = locals()[lists_names[0]]
    coeffs_quadrature = locals()[lists_names[1]]

    a, b = [-1.494,1.255]
    result = prod_esc(w, f1, f2, a, b, cord_quadrature, coeffs_quadrature)
    print(result)

    pass