from hashlib import new

def f(x):
    return x*(x-1)*(x-2) + 0.42

def df(x):
    return 3*(x**2) - 6*x + 2

def newton(f, df, c, iterations):
    x = c
    for i in range(iterations):
        x = x - f(x)/df(x)
    # Naprint("x = ", x," para ", iterations," iterações")
    print("%.10f,"%x)


        # Equação da reta tangente à P(c, f(c)) é dada por: y = f(c) + df(c)(x-c)
        # Na interceção da reta com o eixo x temos:
        # 0 = f(c) + df(c)(x-c) 
        # -> x-c = - f(c)/df(c) 
        # -> x = c - f(c)/df(c)

c = 2.65161653
vetor = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
for iterations in vetor:
    newton(f, df, c, iterations)