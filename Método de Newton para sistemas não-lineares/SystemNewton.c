#include <math.h>
#include <stdio.h>

// Algoritmo do método de Newton para sistemas não-lineares 2x2 (2 variáveis)
// Note que as funções são escritas na forma: z = f(x, y)

double f1(double x, double y){
    return;
}

double f1x(double x, double y){
    return;
}

double f1y(double x, double y){
    return;
}

double f2(double x, double y){
    return;
}

double f2x(double x, double y){
    return;
}

double f2y(double x, double y){
    return;
}

// A generalização do método de Newton para n variáveis, sendo X_k uma matriz na k-ésima iteração do algoritmo...
// ... (note que X é maiúsculo) é dada na forma:

// X_k+1 = X_k - [1/F'(X_k)]*F(X_k)

// Onde F(X_k) é a uma matriz (coluna) de funções (cada linha possui um elemento f_i(x, y))

// Tal método surge, assim como do método de Newton para 1 variável, da fórmula de aproximação linear, porém neste...
// ... caso para funções de mais de uma variável:

// z = f(x0, y0) + fx(x0, y0)(x-x0) + fy(x0, y0)(y-y0)

// Assumindo que z = 0 tem-se:

// (1) 0 = f(x0, y0) + fx(x0, y0)(x-x0) + fy(x0, y0)(y-y0)

// (2) -f(x0, y0) =  fx(x0, y0)(x-x0) + fy(x0, y0)(y-y0)

// (3) fx(x0, y0)(x-x0) + fy(x0, y0)(y-y0) = -f(x0, y0)

// Escrevendo tal equação com matrizes teremos:

// (4) [fx(x0, y0), fy(x0, y0)] . [x] +  [fx(x0, y0), fy(x0, y0)] . [-x0] = [-f(X0, y0)]
//                                [y]                               [-y0]

// (5) [fx(x0, y0), fy(x0, y0)] . ([x] - [x0]) = [-f(X0, y0)]
//                                ([y] - [y0]) 

// (6) ([x] - [x0]) = [-f(X0, y0)]*[fx(x0, y0), fy(x0, y0)]-¹
//     ([y] - [y0]) 

// (7) [x] = [x0] + [-f(x0, y0)]*[fx(x0, y0), fy(x0, y0)]-¹
//     [y]   [y0]


double newton(double **matrix){

}