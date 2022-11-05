from cmath import *

P_0 = 1970647
P_1 = 4214581
v = 499677

# x = lambda
def P(x):
    result = P_0*exp(x) + (v/x)*(exp(x)-1) - P_1
    return result.real

def dP(x):
    result = P_0*exp(x) + (v/x)*exp(x) - (v/(x**2))*exp(x) + v/(x**2)
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
a = 0.1
b = 1.66
vetor = [2, 4, 8, 12]
for n in vetor: bisection(P, a, b, n)

print("\nPelo método de Newton")
# Pelo método de Newton:
x_0 = 1.91
vetor = [1, 3, 5]
for n in vetor: newton(P, dP, x_0, n)

print("\nPelo método da secante")
# Pelo método da secante:
x_0 = 0.1
x_1 = 1.63
vetor = [1, 2, 5]
for n in vetor: secante(P, x_1, x_0, n)

print("\nPelo método da posição falsa")
# Pelo método da posição falsa:
a = 0.1
b = 1.99
vetor = [2, 4, 7, 11]
for n in vetor: falsePosition(P, a, b, n)