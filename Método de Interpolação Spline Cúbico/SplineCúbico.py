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
