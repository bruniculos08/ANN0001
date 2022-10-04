# Essa função recebe a lista de coordenadas X e Y, e devolve uma lista dos coeficientes do polinômio:
def lagrange(X, Y):
	num = len(X)
	# num é o número de pontos
	coeffs = []
	for i in range(num):
		prod = 1
		for j in range(num):
			if(i != j): 
				prod *= (X[i]-X[j])
		ci = Y[i]/prod
		coeffs.append(ci)
	return coeffs

# Essa função constrói e retorna o polinômio de langrange:
def build_poly(X, coeffs):
	def func(x):
		soma = 0
		for i, ci in enumerate(coeffs):
			prod = ci
			for j in range(len(coeffs)):
				if(i != j): prod *= (x-X[j])
			soma += prod
		return soma
	return func

# Apesar de lembrar a função "main" de python, a seguinte função separa um pedaço do código em que, caso todo o código seja...
# ... importado para outro arquivo, este pedaço não será importado:
if __name__ == "__main__":

	import numpy as np
	import matplotlib.pyplot as plt
	from math import *

	# Exemplo 1:
	X = [2.728, 2.937, 3.202, 3.478, 3.698, 4.069, 4.308, 4.536]
	Y = [0.681, 0.777, 0.857, 0.918, 0.956, 0.999, 0.967, 0.54]

	coeffs = lagrange(X, Y)
	p = build_poly(X, coeffs)

	#for ci in coeffs: print(f'{ci:.20f},') 
	# for xi in X: print(f'{p(xi)}')

	t = np.linspace(min(X), max(X), 100)
	pt = [p(ti) for ti in t]

	plt.plot(t, pt, color = "red")
	plt.scatter(X, Y, color = "blue")
	plt.savefig("Exemplo01.png")
	plt.close()

	# Exemplo 2:

	def f(x):
		return e**(cos(x)**2) + e**(-x**2) + log(x, e)

	X = [2.603, 5.325, 7.733]
	Y = [f(xi) for xi in X]

	coeffs = lagrange(X, Y)
	p = build_poly(X, coeffs)

	#for ci in coeffs: print(f'{ci:.20f},') 
	# for xi in X: print(f'{p(xi)}')

	t = np.linspace(min(X), max(X), 100)
	pt = [p(ti) for ti in t]
	ft = [f(ti) for ti in t]

	plt.plot(t, pt, color = "red")
	plt.plot(t, ft, color = "green")
	plt.scatter(X, Y, color = "blue")
	plt.savefig("Exemplo02.png")
	plt.close()

	# Exemplo 03 (código não fixo):

	def f(x):
		return cos(x + sqrt(log(x**2, e)))

	X = [1.493, 1.665, 1.875, 2.035, 2.141, 2.283, 2.456, 2.641, 2.825, 3.023, 3.268, 3.363, 3.561, 3.728, 3.861, 4.104, 4.256, 4.383, 4.533, 4.682, 4.935]
	Y = [f(xi) for xi in X]

	coeffs = lagrange(X, Y)
	p = build_poly(X, coeffs)

	for ci in coeffs: print(f'{ci:.20f},') 
	# for xi in X: print(f'{p(xi)}')

	t = np.linspace(min(X), max(X), 100)
	pt = [p(ti) for ti in t]
	#ft = [f(ti) for ti in t]

	plt.plot(t, pt, color = "red")
	#plt.plot(t, ft, color = "green")
	plt.scatter(X, Y, color = "blue")
	plt.savefig("Exemplo03.png")
	plt.close()


# Neste método de interpolação, para uma lista de pontos (geral): 
#
# (x0, y0), (x1, y1), ..., (xn-1, yn-1)
#
# Temos um polinômio da seguinte forma:
#
# p(x) = y0.L0(x) + y1.L1(x) + ... + yn-1.Ln-1(x)
#
# Onde:
#
# Li(x) = 1, se x = xi
# 		= 0, se x ≠ xi
#
# Montando esse polinômio, note que, para 0 ≤ i  ≤ n-1, temos:
#
# Li(x) = (x-x0).(x-x1)...(x-xi-1).(x-xi+1)...(x - xn-1) / (xi-x0).(x-x1)...(xi-xi-1).(xi-xi+1)...(xi - xn-1)
#
# Ou seja, Li(x) pode ser definido pelo seguinte produtório:
#
# Li(x) = ∏	(x-xj)/(xi-xj) para 0 ≤ j ≤ n-1 e j ≠ i
