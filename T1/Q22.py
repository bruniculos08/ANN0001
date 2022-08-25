from math import *

def function(x):
    return exp(5*x)-2

def falsePositionAux(f, a, b):
    fa = abs(f(a))
    fb = abs(f(b))
    return (a*fb + b*fa)/(fa + fb)

def falsePosition(f, a, b, n):
    if(f(a)*f(b) > 0): return
    i = 1

    while(1):
        x = falsePositionAux(f, a, b)
        #print("x = %.17f na %i iteração" % (x, i))

        if(i >= n): 
            break
        
        if(f(a)*f(x) < 0): 
            b = x
        else: 
            a = x
        i+=1
        
    print("%.17f," % (x))
        
vetor = [1 , 25, 50, 100, 200, 400, 800, 1600, 3200, 4800, 6400, 8000, 10000]
for i in vetor:
    falsePosition(function, -0.993624, 1.9528124, i)