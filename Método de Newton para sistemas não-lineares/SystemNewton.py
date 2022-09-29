import numpy as np

# Tentativa de fazer o método de Newton para sistemas não lineares em python

# Função que recebe lista de funções e de valores e monta a matriz F:
def build_F(functions, A):
    F = []
    for f in functions:
        row = [f(A)]
        F.append(row)
    return F

# Função que recebe lista de derivadas e valores e monta a matriz de derivadas F' (Jacobiano) invertida:
def build_J_inverse(derivatives, A):
    J = []
    for i, num in enumerate(derivatives):
        row = []
        for d in derivatives[i]:
            row.append(d(A))
        J.append(row)
    return np.linalg.inv(J)

def iterations(A, J_inverse, F):
    B = -np.dot(J_inverse, F)
    X = A - B
    return X


# Note que A é a solução inicial:
if __name__ == '__main__':

    def f1(X):
        return X[0]*X[0] + X[1]*X[1] - 5

    def f1x0(X):
        return 2*X[0]

    def f1x1(X):
        return 2*X[1]

    def f2(X):
        return X[0]*X[0] + X[0]*X[1]*X[1]*X[1] - 3    

    def f2x0(X):
        return 2*X[0] + X[1]*X[1]*X[1]    

    def f2x1(X):
        return 3*X[0]*X[1]*X[1]

    functions = [f1, f2]
    derivatives = [[f1x0, f1x1], [f2x0, f2x1]]
    initial_solution = [[-1.6257], [1.4687]]

    F = build_F(functions, initial_solution)
    J_inverse = build_J_inverse(derivatives, initial_solution)

    n = 2
    X = initial_solution
    for i in range(n):
        X = iterations(X, J_inverse, F)
        print(X)
        print()

