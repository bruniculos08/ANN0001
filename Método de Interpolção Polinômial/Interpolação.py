import numpy as np


# Função que gera a matriz de Vandermonde do sistema linear...
# ... do método de interpolação polinômial
def vandermonde(coords_X, coords_Y):
    X = []
    Y = coords_Y
    n = len(coords_X)

    for xi in coords_X:
        # Cada linha é formada da seguinte forma: 1 + xi**1 + xi**2 + ... + xi**(n-1)
        row = [1] + [xi**k for k in range(1, n)]
        # Obs.: lembre-se que a função range começa no elemento esquerdo do argumento mas...
        # ... termina no elemento direito do argumento - 1.
        X.append(row)
        # A cada iteração construímos uma linha da matriz e adicionamos à mesma
    return np.linalg.solve(X, Y)
    # O método "linalg.solve" multiplica a matriz de coeficientes (X nesse caso) por uma matriz coluna de variáveis...
    # ... e resolve o sistema linear para estas variáveis retornando um vetor com o valor de cada.

# Note que o sistema de equações a ser resolvido para se obter...
# ... os coeficientes do polinômio interpolador é:
#
# a0 + a1.x1 + a2.x1**2 + ... an-1.x1**(n-1) = y1
# a0 + a1.x2 + a2.x2**2 + ... an-1.x2**(n-1) = y2
#  .     .        .                 .
#  .     .        .                 .
#  .     .        .                 .
# a0 + a1.xn + a2.xn**2 + ... an-1.xn**(n-1) = yn
# 
# Esse sistema pode ser transformado na forma matricial da...
# ... seguinte maneira:
# X.A = Y
# Note que A é a matriz coluna das incógnitas quais queremos...
# ... obter o valor.

# Função que monta o polinômio:
def build_poly(coeffs):
    def func(x):
        soma = coeffs[0]                         # soma = a0
        for i, ci in enumerate(coeffs[1:], 1):   # coeffs[1:] pois já adicionamos o elemento a0*x**0
            soma += ci*x**i                      # enumerate permite usar o índice do elemento no "for" junto ao próprio elemento...
        return soma                              # ... e setamos tal contador pra começar em 1 (por isso "(coeffs[1:], 1)", para...
    return func                                  # ... usar i como expoente).

# Apesar de lembrar a função "main" de python, a seguinte função separa um pedaço do código em que, caso todo o código seja...
# ... importado para outro arquivo, este pedaço não será importado:
if __name__ == '__main__':

    # Exemplo 1 com lista de coordenadas (1,2) e (3, -1):
    X = [-10, -1, 1, 3]
    Y = [9, 4, 2, -1]
    
    coeffs = vandermonde(X, Y)
    
    p = build_poly(coeffs)
    # Note que p será o polinômio interpolador (pois build_poly retorna uma função)

    # Verificando:
    # print(f'{p(1) = } e {p(3) = }')
    # Se o resulta de p(xi) = yi o polinômio está correto

    # Para visualização:
    import matplotlib.pyplot as plt

    # Esta biblioteca para plotar o gráfico pede um domínio (uma lista coordenadas X),...
    # ... uma divisão para o intervalo, e uma lista de coordenadas Y, e usando isso irá...
    # ... ligar os pontos vias seguimentos de reta para formar o gráfico:

    t = np.linspace(-10, 4, 100) # Isto é, t é a lista de coordenadas X de -1 até 4, dividida em 100 pontos
    pt = [p(ti) for ti in t]    # Isto é, pt é a lista de coordenadas Y calculadas aplicando o polinômio...
                                # ... em cada uma das coordenadas (x) da lista t
                
    plt.plot(t, pt, color = "red")    # Plota o gráfico da maneira comentada anteriormente
    plt.scatter(X, Y, color = "blue") # Plota pontos apenas
 
    plt.savefig("Exemplo01.png")
    plt.close()
    # O comando close() "limpa" o gráfico (para não ficar plotando um em cima do outro).


    # Exemplo 2 com uma lista de coordenadas baseada em uma função para então comparar o gráfico do...
    # ... polinômio com o gráfico da função:
    
    from math import *

    # Note que basta trocar a função f(x) para se obter uma interpolação totalmente diferente para a função que se queira.
    def f(x):
        return exp(-(x**2))

    # É necessário forçar o valor de cada xi em X à ser um float (sem isso pode ocorrer erro na função "vandermonde").
    X = [float(n) for n in range(-10, 11, 1)]
    Y = [f(xi) for xi in X]

    coeffs = vandermonde(X, Y)

    p = build_poly(coeffs)

    t = np.linspace(-5, 5, 50)
    pt = [p(ti) for ti in t]
    ft = [f(ti) for ti in t]

    plt.plot(t, pt, color = "red")
    plt.scatter(X, Y, color = "blue")
    plt.plot(t, ft, color = "green")

    plt.savefig("Exemplo02.png")
    plt.close()

    # Exemplo 3 (exemplo dos exercício, ou seja, código não fixo):

    def g(x):
        return sin(sqrt(1+tan(x)))

    X = [3.196, 3.804, 4.113]
    Y = [g(xi) for xi in X]

    coeffs = vandermonde(X, Y)
    
    # Printando coeficientes:
    # for i, ci in enumerate(coeffs): print(f'a{i} = {ci}')
    # for ci in coeffs: print(f'{ci:.20f},')
    # Este último "for" usa um "print" de tal modo que a notação científica é suprimida.

    p = build_poly(coeffs)

    # Printando o erro absoluto para as coordenas em "values":
    values = [3.511, 3.585]
    for xi in values: 
        diff = abs(g(xi)-p(xi))
        print(f'{diff},')

    # Cálculos de pontos xi em p(x):
    # values = [0.036, 1.248, 1.434, 1.591]
    # for xi in values: 
    #    print(f'{p(xi)},')
    #    plt.scatter([xi], [p(xi)], color = "purple")

    t = np.linspace(min(X), max(X), 100)
    pt = [p(ti) for ti in t]
    gt = [g(ti) for ti in t]

    plt.plot(t, pt, color = "red")
    plt.plot(t, gt, color = "green")
    plt.scatter(X, Y, color = "blue")
    plt.savefig("Exemplo03.png")

