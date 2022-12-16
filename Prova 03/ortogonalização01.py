from math import *
from sympy import symbols, simplify

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
Função para ortogonalizar uma lista de funções (Gran Schimidt):
Nota: lembre-se que para ortogonalizar um função f(x) em relação à outra função g(x) deve se obter então uma nova
função h(x) tal que:

    h(x) = f(x) - proj<f(x), g(x)> = f(x) - k.g(x), onde k = <f(x), g(x)>/<g(x), g(x)>, 

o que é igual a função f(x) subtraída da sua componente na mesma direção de g(x) (tratando as funções com vetores).
"""
def ortog_funcs(func_list, a, b, n):
    G = [func_list[0]]
    A = []
    G_func_list = [symbolToFunc(func_list[0])]
    for fi in func_list[1:]:
        gi = fi
        row = []
        for gj in G:
            gi -= proj_k(symbolToFunc(fi), symbolToFunc(gj), a, b, n)*gj
            row.append(proj_k(symbolToFunc(fi), symbolToFunc(gj), a, b, n))
        gi = simplify(gi)
        G.append(gi)
        A.append(row)
        G_func_list.append(symbolToFunc(gi))
    return A
"""
Obs: a função acima ('ortog_funcs') não resulta mais em erro de recursão pois agora utiliza a biblioteca sympy
na construção das funções, e portanto visto que agora tais funções são construídas algebricamente e não por meio de chamadas
de outras funções, as mesmas são agora funções folha (logo não fazem recursão ou chamada de outras funções)
"""

def stringToFunc(string):
    def f(x):
        return eval(string)
    return f

def symbolToFunc(expr):
    return stringToFunc(str(expr))


"""
Função que retorna <f(x), g(x)> para um espaço vetorial de funções C[a,b], ou seja, que 
retorna o produto escalar entre duas funções f(x) e g(x) no intervalo [a,b]:
"""
def prod_esc(f, g, a, b, n):
    return simpson(lambda x: f(x)*g(x), a, b, n)

"""
Função que retorna o resultado a constante k da projeção de f(x) em g(x), ou seja,
k = <f(x), g(x)>/<g(x), g(x)>:
"""
def proj_k(f, g, a, b, n) -> float:
    return (prod_esc(f, g, a, b, n)/prod_esc(g, g, a, b, n))


if __name__ == '__main__':

    a, b = [-1.00088, 1.30114]
    n = 500
    x = symbols('x')
    func_list = [1,  x, x**2, x**3, x**4, x**5, x**6, x**7, x**8, x**9]

    result_list = ortog_funcs(func_list, a, b, n)
    
    for row in result_list:
        # print(row)
        for a_ij in row:
            print(f"{a_ij},") 

    pass