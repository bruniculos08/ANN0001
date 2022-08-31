#include <math.h>
#include <stdio.h>
#include <locale.h>

double function(double x){
    return x*x - 3;
}

double functionDerivative(double x){
    return 2*x;
}

// Note que para uma função f(x), de derivada f'(x), a reta tangente a um ponto (c, f(c)) quaisquer é...
// ... dada por y = f(c) + f'(c)(x-c) 

// Geometricamente pode se notar quando y = 0, ou seja, quando a reta mencionada cruza o eixo x, teremos...
// ... 0 = f(c) + f'(c)(x-c) -> x = c - f(c)/f'(c)

// Logo temos o valor para o qual a reta cruza o eixo x, que é um valor mais próximo ao valor qual f(x) cruza o eixo x,...
// ... e assim podemos repetir a aproximação calculando uma nova reta tangente obtendo uma aproximação ainda melhor.

// Para obter cada novo ponto de aproximação deve-se faze x = c - f(c)/f'(c) e c = x, repetindo o processo.


void newton(double (*f)(double), double(*df)(double), double m, double tolerance){
    while(fabs(f(m)) > tolerance){
        if(df(m) == 0) return;
        m = m - (f(m)/df(m));
        printf("m = %.17f\n", m);
    }
}


int main(){
    setlocale(LC_ALL, "");
    double (*f)(double);
    double (*df)(double);
    f = function;
    df = functionDerivative;
    double m = 2;
    newton(f, df, m, 0.00000000001);
}