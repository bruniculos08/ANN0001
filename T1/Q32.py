from cmath import *

V = 286.6
R = 5.18

# x = lambda
def f(x):
    result = pi*(x**2)*R - (pi/3)*(x**3) - V
    return result.real

def df(x):
    result = 2*pi*x*R - pi*(x**2)
    return result.real

def falsePositionAux(f, a, b):
    fa = abs(f(a))
    fb = abs(f(b))
    return (a*fb + b*fa)/(fa + fb)

def falsePosition(f, a, b, n):
    if(f(a)*f(b) > 0): 
        return

    for i in range(n):
        x = falsePositionAux(f, a, b)
        
        if(f(a)*f(x) < 0): 
            b = x
        else: 
            a = x

    print("%.17f" %(x))

def newton(f, df, m, n):

    for i in range(n):
        if(df(m) == 0): return
        m = m - (f(m)/df(m))
    
    print(m)

def bisection(f, a, b, n):
    if(f(a)*f(b) > 0):
        return
    for i in range(n):
        m = (a+b)/2
        if(f(a)*f(m) < 0):
            b = m
        else: 
            a = m
    
    print("%.17f"%(m))

def aproximateDerivative(f, x1, x0):
    return (f(x1)-f(x0))/(x1-x0)

def secante(f, x1, x0, n):
    for i in range(n):
        x2 = x0 - f(x0)/aproximateDerivative(f, x1, x0)
        #x2 = (x0*f(x1) - x1*f(x0))/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
    print(x2)

print("\nPelo método da bisseção")
# Pelo método da bisseção:
a = 0
b = 10.36
vetor = [2, 4, 8, 12]
for n in vetor: bisection(f, a, b, n)

print("\nPelo método de Newton")
# Pelo método de Newton:
x_0 = 5.46
vetor = [1, 3, 5]
for n in vetor: newton(f, df, x_0, n)

print("\nPelo método da secante")
# Pelo método da secante:
x_0 = 0.87
x_1 = 8.29
vetor = [1, 2, 5]
for n in vetor: secante(f, x_1, x_0, n)

print("\nPelo método da posição falsa")
# Pelo método da posição falsa:
a = 0
b = 10.36
vetor = [2, 4, 7, 11]
for n in vetor: falsePosition(f, a, b, n)