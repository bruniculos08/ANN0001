from cmath import *

G = 9.81
t = 7.35
L = 7.45
v = 11.18


def sech(x):
    result = 1/(cosh(x))
    return result.real

# x = lambda
def g(x):
    result = sqrt(2*G*x) * tanh(sqrt(2*G*x)*t/(2*L)) - v
    return result.real

def dg(x):
    result = (sqrt(2*G/x)/2) * tanh(sqrt(2*G*x)*t/(2*L)) + sqrt(2*G*x)*(sech(sqrt(2*G*x)*t/(2*L))**2)*(t*sqrt(2*G)/(4*L*sqrt(x)))
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
a = 0.34
b = 18.99
vetor = [2, 4, 8, 12]
for n in vetor: bisection(g, a, b, n)

print("\nPelo método de Newton")
# Pelo método de Newton:
x_0 = 1.48
vetor = [1, 3, 5]
for n in vetor: newton(g, dg, x_0, n)

#print("\nPelo método da secante")
# Pelo método da secante:
#x_0 = 1.93
#x_1 = 19.96
#vetor = [1, 2, 5]
#for n in vetor: secante(g, x_1, x_0, n)

print("\nPelo método da posição falsa")
# Pelo método da posição falsa:
a = 0.49
b = 19.01
vetor = [2, 4, 7, 11]
for n in vetor: falsePosition(g, a, b, n)