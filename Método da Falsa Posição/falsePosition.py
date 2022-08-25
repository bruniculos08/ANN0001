from math import *

def function(x):
    return pi*x-exp(x)

def falsePositionAux(f, a, b):
    fa = abs(f(a))
    fb = abs(f(b))
    return (a*fb + b*fa)/(fa + fb)

def falsePosition(f, a, b, tol):
    if(f(a)*f(b) > 0): return
    i = 1

    while(1):
        x = falsePositionAux(f, a, b)
        print("x = %.17f na %i iteração" % (x, i))

        if(abs(f(x) < tol)): 
            break
        
        if(f(a)*f(x) < 0): 
            b = x
        else: 
            a = x
        i+=1
        

falsePosition(function, 0.1246, 0.9406, 0.00000000000001)