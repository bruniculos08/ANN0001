#include <math.h>
#include <stdio.h>

// Algoritmo do método de Newton para sistemas não-lineares 2x2 (2 variáveis)
// Note que as funções são escritas na forma: z = f(x, y)

double f1(double x, double y){
    return x*x + y*y - 5;
}

double f1x(double x, double y){
    return 2*x;
}

double f1y(double x, double y){
    return 2*y;
}

double f2(double x, double y){
    return x*x + x*y*y*y - 3;
}

double f2x(double x, double y){
    return 2*x + y*y*y;
}

double f2y(double x, double y){
    return 3*x*y*y;
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

// (8) [x] = [x0] - [f(x0, y0)]*[fx(x0, y0), fy(x0, y0)]-¹
//     [y]   [y0]

// note que é necessário mais de uma equação visto que a matriz [fx(x0, y0), fy(x0, y0)] não é inversível, assim supondo que tivéssimos...
// ... mais uma equação além desta, teriámos também de ter essa matriz multiplicando do lado esquerdo:


// (9) X = X_0 - F(X_0)*[F'(X_0)]-¹

// Eis a fórmula da aproximação de newton para 3 variáveis (e seguindo o mesmo padrão tem-se para n variáveis)

double newton(double x0, double y0, int n){
    for(int i = 0; i < n; i++){
        double F[] = {f1(x0, y0), f2(x0, y0)};
        double det = f1x(x0, y0)*f2y(x0, y0) - f1y(x0, y0)*f2x(x0, y0);
        double dF_inv[2][2] = {{f2y(x0, y0)/det, -f1y(x0, y0)/det}, {-f2x(x0, y0)/det, f1x(x0, y0)/det}};
        x0 = x0 - (F[0]*dF_inv[0][0] + F[1]*dF_inv[0][1]);
        y0 = y0 - (F[0]*dF_inv[1][0] + F[1]*dF_inv[1][1]);
    }
    printf("x = %.17f, y = %.17f para %i iteracoes.\n", x0, y0, n);
}

int main(){
    int vetor[] = {1, 2, 3, 4, 5};
    double x0 = -1.6257;
    double y0 = 1.4687;
    for(int i = 0; i < sizeof(vetor)/sizeof(vetor[0]); i++){
        newton(x0, y0, vetor[i]);
    }
}