from cProfile import label
import numpy as np

def spline(X, Y):
    n = len(X)

    """
    Retorna todos os coeficiente de todos os polinômios, ou seja,
    todos os ak, bk, ck, dk
    """
    # Matriz com os valores de cada ak
    A = [yi for yi in Y]
    
    # Matriz com os valores de cada hk para k = 0, 1, 2, ..., n-1
    H = []
    for i in range(n-1):
        hi = X[i+1] - X[i]
        H.append(hi)

    C_coeffs = []
    # Inserir primeiro elemento da matriz:
    C_coeffs.append([1] + [0 for i in range(n-1)])
    # Montando os itens pela forma do termo hk-1 . ck-1 + 2.(hk-1 + hk).ck + hk . ck+1
    for i in range(1, n-1):
        row = [0 for j in range(n)]
        row[i-1] = H[i-1]
        row[i] = 2*(H[i-1]+H[i])
        row[i+1] = H[i]
        C_coeffs.append(row)
    # Inserir último elemento da matriz:
    C_coeffs.append([0 for i in range(n-1)] + [1])

    C_ind = []
    # Inserir primeiro elemento da matriz:
    C_ind.append(0)
    # Montando os itens pela forma do termo (3/hk).(ak+1 - ak) - (3/hk-1).(ak - ak-1)
    for i in range(1, n-1):
        num = (3/H[i])*(A[i+1]-A[i]) - (3/H[i-1])*(A[i]-A[i-1])
        C_ind.append(num)
    # Inserir último elemento da matriz:
    C_ind.append(0)

    # Resolvendo o sistema linear que dá como resultado a matriz coluna com os valores de cada ck:
    C = np.linalg.solve(C_coeffs, C_ind)

    # Matriz com os valores bk:
    B = []
    for i in range(n-1):
        bi = (1/H[i])*(A[i+1]-A[i]) - (H[i]/3)*(2*C[i] + C[i+1])
        B.append(bi)

    # Matriz com os valores dk:
    D = []
    for i in range(n-1):
        dk = (C[i+1] - C[i])/(3*H[i])
        D.append(dk)

    return A, B, C, D

def build_poly_dict(A, B, C, D, X):
    poly_dict = {}
    n = len(X)
    for i in range(n-1):
        eq = f'{A[i]}{B[i]:+}*(x-{X[i]}){C[i]:+}*(x-{X[i]})**2{D[i]:+}*(x-{X[i]})**3'
        poly_dict[i] = {'eq': eq, 'domain': [X[i], X[i+1]]}
    return poly_dict

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from math import *

    # Exemplo 01:

    X = [1, 2, 4, 5]
    Y = [1, 4, 2, 3]

    A, B, C, D = spline(X, Y)
    S = build_poly_dict(A, B, C, D, X)
    print(S)
    
    for i, value in S.items():
        def s(x):
            return eval(value['eq'])
        t = np.linspace(*value['domain'], 100)
        plt.plot(t, s(t), label = f"$S_{i}(x)$")

    plt.scatter(X, Y)
    plt.legend()
    plt.savefig("Exemplo01.png")
    plt.close()

    # Exemplo 02:

    def f(x):
        return cos(x)*(e**(-x**2))

    X = [i for i in range(0, 21, 2)]
    Y = [f(xi) for xi in X]

    A, B, C, D = spline(X, Y)
    S = build_poly_dict(A, B, C, D, X)

    for i, value in S.items():
        def s(x):
            return eval(value['eq'])
        t = np.linspace(*value['domain'], 100)
        plt.plot(t, s(t), label = f"$S_{i}(x)$")

    t = np.linspace(min(X), max(X), 101)
    ft = [f(ti) for ti in t]
    plt.plot(t, ft, label = f"$f(x)$")

    plt.scatter(X, Y)
    plt.legend()
    plt.savefig("Exemplo02.png")
    plt.close()

    # Exemplo 03 (código não fixo):

    #def f(x):
    #   return 1/(1+25*x**2)

    X = [-2.93, -1.919, -1.604, -0.744, -0.244, 0.246, 0.896, 1.931, 2.3, 2.859, 3.782, 4.182]
    #Y = [2.49, 1.275, 1.532, 3.324, 4.218, 4.609, 2.929, 1.611, 2.423, 2.097, 2.344, 1.489]
    Y = [2.49, 1.275, 1.532, 3.324, 4.218, 4.609, 2.929, 1.611, 2.423, 2.097, 2.344, 1.489]

    valores = [0.371, 0.538, 2.399, 2.841, 3.233]

    A, B, C, D = spline(X, Y)
    S = build_poly_dict(A, B, C, D, X)

    for i, value in S.items():
        def s(x):
            return eval(value['eq'])
        t = np.linspace(*value['domain'], 100)
        plt.plot(t, s(t), label = f"$S_{i}(x)$")

    def sk(x):
        for i, value in S.items():
            if value['domain'][0] <= x <= value['domain'][1]:
                return eval(value['eq'])

    for valor in valores:
        print('{:.16f},'.format(sk(valor)), end=" ")

    #t = np.linspace(min(X), max(X), 101)
    #ft = [f(ti) for ti in t]
    #plt.plot(t, ft, label = f"$f(x)$")

    plt.scatter(X, Y)
    plt.legend()
    plt.savefig("Exemplo03.png")
    plt.close()

    #for i in range(len(X)-1):
    #    print(f'{A[i]}, {B[i]}, {C[i]}, {D[i]},')

    #print(A)
    #print(B)
    #print(C)
    #print(D)



# Dada a seguinte lista de pontos:
#
# (x0, y0), (x1, y1), ...,  (xn-1, yn-1), (xn, yn)
#
# Assim, utilizando polinômio para iterpolar tais pontos dois à dois (um polinômio para cada par de pontos), devemos atender...
# ... as seguintes restrições, para quaisquer k ∈ [0, n-2],
#
# i) Sk(xk) = yk e Sk+1(xk+1) = yk+1
#
# ii) Sk(xk+1) = Sk+1(xk+1)
#
# iii) Sk'(xk+1) = Sk+1'(xk+1)
#
# iv) Sk''(xk+1) = Sk+1''(xk+1)
#
# Note que o polinômio de grau 3 tem forma:
#
# p(x) = a + b.x + c.x² + d.x³
#
# Porém para esse método utilizaremos o polinômio na seguinte forma:
#
# p(x) = ak + bk.(x-xk) + ck.(x-xk)² + dk.(x-xk)³
#
# Visto que nessa forma para encontrar ak basta utilizar o primeiro ponto (xk, yk) interpolado pelo polinômio, pois se:
#
# p(xk) = ak + bk.(xk-xk) + ck.(xk-xk)² + dk.(xk-xk)³
#
# p(xk) = ak + 0 + 0 + 0
#
# p(xk) = ak -> ak = yk 
#
# Portanto a0 = y0, a1 = y1, a2 = y2, ..., an-1 = yn-1 ; agora precisamos pedir que Sk(xk+1) = Sk+1(xk+1) ; antes disso, definiremos que...
# ... hk = xk+1 - xk, assim, lembre-se que:
# 
# Sk(x) = ak + bk.(x-xk) + ck.(x-xk)² + dk.(x-xk)³ 
#
# Sk+1(x) = ak+1 + bk+1.(x-xk) + ck.(x-xk)² + dk.(x-xk)³
#
# Logo, calculando em x = xk+1, temos:
# 
# Sk(xk+1) = ak + bk.(xk+1-xk) + ck.(xk+1-xk)² + dk.(xk+1-xk)³ <=> Sk(x) = ak + bk.(hk) + ck.(hk)² + dk.(hk)³
#
# Sk+1(xk+1) = ak+1 + 0 + 0 + 0
#
# Portanto:
#
# ak+1 = ak + bk.(hk) + ck.(hk)² + dk.(hk)³
#
# Agora precisamos pedir que Sk'(xk+1) = Sk+1'(xk+1) ; calculando as derivadas temos:
#
# Sk'(x) = bk + 2.ck.(x-xk) + 3.dk.(x-xk)²
#
# Sk+1'(x) = bk+1 + 2.ck+1(x-xk+1) + 3.dk+1.(x-xk+1)²
#
# logo, calculando em x = xk+1, temos:
# 
# Sk'(xk+1) = bk + 2.ck.(xk+1-xk) + 3.dk.(xk+1-xk)² <=> Sk'(xk+1) = bk + 2.ck.(hk) + 3.dk.(hk)²
#
# Sk+1'(xk+1) = bk+1 + 0 + 0
#
# Portanto:
#
# bk+1 = bk + 2.ck.(hk) + 3.dk.(hk)²
#
# Agora precisamos pedir que Sk"(xk+1) = Sk+1"(xk+1) ; calculando as segundas derivadas temos:
#
# Sk"(x) = 2.ck + 6.dk.(x-xk)
#
# Sk+1"(x) = 2.ck+1 + 6.dk+1.(x-xk+1) 
# 
# logo, calculando em x = xk+1, temos:
#
# Sk"(xk+1) = 2.ck + 6.dk.(xk+1-xk) <=> Sk"(xk+1) = 2.ck + 6.dk.(hk)
#
# Sk+1"(xk+1) = 2.ck+1 + 0
#
# Portanto:
# 
# 2.ck+1 = 2.ck + 6.dk.(hk) <=> ck+1 = ck + 3.dk.(hk) <=> dk+1 = (ck+1-ck)/(3.hk)
# 
# Substituindo a equação (3) na equação (1), obtemos:
#
# ak+1 = ak + bk.hk + ck.(hk)² + (ck+1-ck/(3.hk)).(hk)³ <=> ak+1 = ak + bk.hk + ((hk²)/3).(2.ck + ck+1)
# 
# Isolando bk obtemos:
#
# bk = (1/hk).(ak+1-ak) - (hk/3).(2.ck + ck+1)
#
# Substituindo a equação (3) na equação (2), obtemos:
#
# bk+1 = bk + 2.ck.hk + 3.((ck+1-ck)/(3.hk)).(hk)² <=> bk+1 = bk + hk.(ck+1-ck)
#
# Agora, nas equações (4) e (5), substituindo k por k-1 (shif nos índices), sabendo que tais equações agora, ao invés de serem válidas...
# ... para 0 ≤ k ≤ n-2, serão válidas para 1 ≤ k ≤ n-1, teremos:
#
# bk = bk-1 + (ck + ck-1).hk-1                                                      (6)
# 
# bk-1 = = (1/hk-1)(ak - ak-1) - [(hk-1)/3].(2.ck-1 + ck)                           (7)
#
# Substituindo as equações (4) e (7) na equação (6), obtemos:
#
# (1/hk).(ak-1 - ak) - (hk/3).(2.ck + ck+1) = (1/hk-1).(ak - ak-1) - [(hk-1)/3].(2.ck-1 + ck) + (ck - ck-1).hk-1
#
# Que é o mesmo que:
#
# hk-1 . ck-1 + 2.(hk-1 - hk).ck + hk . ck+1 = (3/hk).(ak+1 - ak) - (3/hk-1).(ak - ak-1)
#
# Sendo, assim, note que esta equação é valida para 1 ≤ k ≤ n-2, e definindo c0 = 0 e cn = 0, visto que tais valores podem aparecer...
# ... na equação (dependendo do índice k escolhido), tem-se um sistema com n - 2 equações, porém se adicionamos as seguintes restrições:
# 
# S0"(x0) = 0 -> c0 = 0
#
# Sn-1"(xn) = 0 -> cn = 0
#
# Teremos n - 2 + 2 equações, ou seja, n equações, e além disso temos n variáveis, portanto resumindo:
#
# c0 = 0, cn = 0 e para cada k = 1, 2, 3, ..., n-2, n-1 tem se:
# hk-1 . ck-1 + 2.(hk-1 - hk).ck + hk . ck+1 = (3/hk).(ak+1 - ak) - (3/hk-1).(ak - ak-1)
#
# Escrevendo tal sistema de equações na forma matricial, ou seja, A.X = B, teremos:
#
#  --                                                                         --      --  --        --                                             --
# | 1       0           0           0      ...     0            0           0  |      | c0 |        |                 0                             | 
# | h0   2(h0+h1)      h1           0      ...     0            0           0  |      | c1 |        |   (3/h1).(a2 - a1) - (3/h0).(a1 - a0)         |
# | .                                                           .           .  |      | c2 |        |   (3/h2).(a3 - a2) - (3/h1).(a2 - a1)         |
# | .                                                           .           .  |  °   | .  |    =   |                 .                             |
# | .                                                           .           .  |      | .  |        |                 .                             |
# | 0       0           0          0      ...    hn-2     2(hn-2+hn-1)    hn-1 |      | .  |        | (3/hn-1).(an - an-1) - (3/hn-2).(an-1 - an-2) |
# | 0       0           0          0      ...      0            0           1  |      | cn |        |                 0                             |
# --                                                                          --      --  --        --                                             --
#
# Juntando isso com as seguintes informações:
# 
# 1) ak = yk para k = 0, 1, 2, ..., n 
#
# 2) hk = xk+1 - xk para k = 0, 1, 2, ..., n-1
#
# 3) os valores de cada ck são dados no sistema anterior (para k = 0, 1, ..., n)
#
# 4) bk = (1/hk).(ak+1 - ak) - (hk/3).(2.ck + ck+1) para k = 0, 1, 2, ..., n-1
#
# 5) dk = (ck+1 - ck)/(3.hk)