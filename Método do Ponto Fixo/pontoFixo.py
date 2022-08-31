from cmath import sqrt

def g(x):
    # Python converte para complex ao usar raiz quadrada
    c = ((3 * pow(x, 4) + 2 * pow(x, 2) + 3) / (4 * pow(x, 3) + 4 * x - 1))
    return c

def f(x):
   return x**2

def pontoFixo(g, x, n):
    for i in range(n):
        x_n = g(x)
        x = x_n
    print("%.17f,"%(x))

x_0 = 1.09298
vetor = [1, 2, 3, 4, 5, 6, 7, 8]
for i in vetor:
    pontoFixo(g, x_0, i)