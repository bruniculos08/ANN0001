import numpy as np

def lagrange(x,y):
	num = len(x)
	coefs = []
	for i in range(num):
		prod = 1
		for j in range(num):
			if i != j:
				prod *= (x[i] - x[j])
		ci = y[i] / prod
		coefs.append(ci)
	return coefs

def plLagr(t: float,x: list[float], coefs: list[float]) -> float:
	soma = 0
	num = len(coefs)
	for i in range(num):
		prod = 1
		for j in range(num):
			if i != j:
				prod*=(t-x[j])
		prod *= coefs[i]
		soma += prod
	return soma

def polyLagr(x, coefs):
	def f(t):
		return plLagr(t,x, coefs)
	return f

if __name__ == '__main__':

    # Exemplo 1
    # Exemplo 2

    # Exemplo 3 

