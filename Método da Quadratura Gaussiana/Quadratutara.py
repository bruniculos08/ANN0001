
# Obs.: as listas de coeficientes são predefinidas.
def quadrature(f, cord, coeffs):
    sum = 0
    for xi, ci in zip(cord, coeffs):
        sum += ci*f(xi)
    return sum


# Transforma string em função:
def stringToFunc(string):
    def f(x):
        return eval(string)
    return f

# Mudança de variável na função f para se encaixar nos limites de integração [-1, 1]:
def change(f, a, b):
    def g(u):
        return f((b+a)/2 + (b-a) * (u/2)) * (b-a)/2
    return g

if __name__ == '__main__':

    import math as math
    # Listas de pontos e pesos para quadratura gaussiana:
    from NodesAndWeights import *
    
    # Exemplo 01:
    funcs = ['math.exp(-x**2)', 'math.exp(x)*math.sin(x)/(1+x**2)', 'math.cos(-x**2/3)', 'math.log(math.sqrt(1+x**2))', '(x+1/x)**2']
    a = [-1.443, 0.291, -1.509, 1.112, 0.525]
    b = [0.598, 2.602, 1.075, 3.701, 2.48]
    exact_for_degree_less_than = [4, 12, 6, 8, 10]

    for i, string in enumerate(funcs):
        # Obs.: order é o número de raízes (lembrando que o número de raízes é a metade do número de pontos no intervalo):
        order = str(int(exact_for_degree_less_than[i]/2))    
        lists_names = ['raiz'+order, 'peso'+order]

        # Listas de pontos e pesos para quadratura gaussiana:
        cord = locals()[lists_names[0]]
        coeffs = locals()[lists_names[1]]
        # Obs.: a função locals() transforma as variáveis definidas em arquivos locais (mesma pasta do código em que está...
        # ... sendo executada) em itens de um dicionário cujas os índices são os nomes das variáveis.
                
        # Função após troca de variável:
        g = change(stringToFunc(funcs[i]), a[i], b[i])
        result = quadrature(g, cord, coeffs)

        #print(f"Resultado = {result}")

    pass