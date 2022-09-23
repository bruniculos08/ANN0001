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
#  --                                                                         --      --  --
# | 1       0           0           0      ...     0            0           0  |      | c0 |
# | h0   2(h0+h1)      h1           0      ...     0            0           0  |      | c1 |
# | .                                                           .           .  |      | c2 |
# | .                                                           .           .  |  °   | .  |
# | .                                                           .           .  |      | .  |
# | 0       0           0          0      ...    hn-2     2(hn-2+hn-1)    hn-1 |      | .  |
# | 0       0           0          0      ...      0            0           1  |      | cn |
# --                                                                          --      --  --