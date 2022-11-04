# Método de Richardson considerando um função de erro incial de O(h²):
def richardson(f, a, b, n, k):
    table = []
    # Obs.: dada essa função de erro inicial tem-se que Fk(h) diminui o erro para O(h^(2*k))
    k = int(k/2)

    for i in range(k):
        item = trapeze_sum(f, a, b, (2**i)*n)
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((4**(i+1))*table[j+1] - table[j])/(4**(i+1) - 1)
            table[j] = new_item

    return table[0]

# Método da soma dos trapézios (qual por sua vez possui erro O(h²)):
def trapeze_sum(f, a, b, n):

    sum = f(a)/2 + f(b)/2
    base = (b-a)/n

    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += f(a + k*base)
    
    area = base*sum

    return area

if __name__ == '__main__':

    from math import *

    # Exemplo 01:
    a = 0.213
    b = 1.213
    k = 10
    n = 3
    def f(x):
        return exp(x)*sin(x)/(1+x**2)
    
    # Obs.: dada a função de erro inicial O(h²) tem-se que Fk(h) muda a função de erro para O(h^(2*k))
    print(f"Area = {richardson(f, a, b, n, k)}")
    
    pass