#include <math.h>
#include <stdio.h>
#include <locale.h>

double function(double x){
    return x*(x-1)*(x-2) + 0.42;
}

double functionDerivative(double x){
    return 3*x*x - 6*x + 2;
}

// Obs.: a função log() usa base e (número de euler).

// Note que para uma função f(x), de derivada f'(x), a reta tangente a um ponto (c, f(c)) quaisquer é...
// ... dada por y = f(x) + f'(x)(x-c) 

// Geometricamente pode se notar quando y = 0, ou seja, quando a reta mencionada cruza o eixo x, teremos...
// ... 0 = f(x) + f'(x)(x-c) -> x = c - f(x)/f'(x)

// Logo temos o valor para o qual a reta cruza o eixo x, que é um valor mais próximo ao valor qual f(x) cruza o eixo x,...
// ... e assim podemos repetir a aproximação calculando uma nova reta tangente obtendo uma aproximação ainda melhor.

// Para obter cada novo ponto de aproximação deve-se faze x = c - f(x)/f'(x) e c = x, repetindo o processo.


void newton(double (*f)(double), double(*df)(double), double m, int iterations){
    for(int i = 0; i < iterations; i++){
        //if(df(m) == 0) return;
        m = m - (f(m)/df(m));
    }
    printf("m = %.17f para %i iterações\n", m, iterations);
    //printf("%.7f;\n", m);
}


int main(){
    setlocale(LC_ALL, "");
    double (*f)(double);
    double (*df)(double);
    f = function;
    df = functionDerivative;
    double m = 2.92952751;
    int vetor[] = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195};
    for(int i = 0; i < sizeof(vetor)/sizeof(vetor[0]); i++) newton(f, df, m, vetor[i]);
}

// Avisar para o professor que o código está convergindo para a raiz antes do que o gabarito do exercício apresenta