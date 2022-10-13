# Para uma determinada lista de pontos:
# (x1, y1), (x2, y2), ..., (xn, yn)
# queremos uma reta, ou seja, uma função da forma:
# p(x) = a0 + a1.x
# que se aproxime ao máximo dos pontos dados, assim note que, o erro da reta em relação aos pontos é dado por:
# E(a0, a1) = d1² + d2² + ... + dn-1² + dn²
# onde, para i > 0 e i <= n:
# di = yi - p(xi)
# sendo assim, temos:
# E(a0, a1) = ∑ [yi - p(xi)]²
# E(a0, a1) = ∑ [yi - a0 - a1.xi]²
# para diminuir tal erro note que devemos ter que
#  (i) dE  = 0   e  (ii) dE  = 0 
#      da0               da1
# de (i) teremos a seguinte equação:
#   0 = d∑ [yi - a0 - a1.xi]²
#       da0
#   0 = ∑ d[yi - a0 - a1.xi]²
#         da0
#   0 = ∑ 2[yi - a0 - a1.xi].d(yi - a0 - a1.xi)
#                           da0
#   0 = ∑ 2[yi - a0 - a1.xi].(-1)
#   0 = ∑ 2[a0 + a1.xi - yi]
#   0 = ∑ [a0 + a1.xi - yi]
#   0 = ∑a0 + ∑a1.xi - ∑yi
#   ∑yi = ∑a0 + ∑a1.xi   
#   ∑yi = a0.n + a1.∑xi
# e de (ii) temos a seguinte equação:
#   0 = d∑ [yi - a0 - a1.xi]²
#       da0                     