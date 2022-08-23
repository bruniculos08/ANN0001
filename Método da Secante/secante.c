#include <math.h>
#include <stdio.h>
#include <locale.h>

double function(double x){
    return sqrt(x)-cos(x);
}

double aproximateDerivative(double a, double b){ // <- Aproximação da derivada (coeficiente angular da reta que passa...
    return (function(b)-function(a))/(b-a);      // ... pelos ponto P0(x0, f(x0)) e P1(x1, f(x1))).
}

// Obs.: a única diferença entre o método da secante e método de Newton é que nesse não utilizamos a derivada da função...
// ... e sim um aproximação da mesma.

// Note que para uma função f(x), de derivada f'(x), a reta tangente a um ponto (c, f(c)) quaisquer é...
// ... dada por y = f(c) + f'(c)(x-c) 

// Geometricamente pode se notar quando y = 0, ou seja, quando a reta mencionada cruza o eixo x, teremos...
// ... 0 = f(c) + f'(c)(x-c) -> x = c - f(c)/f'(c)

// Logo temos o valor para o qual a reta cruza o eixo x, que é um valor mais próximo ao valor qual f(x) cruza o eixo x,...
// ... e assim podemos repetir a aproximação calculando uma nova reta tangente obtendo uma aproximação ainda melhor.

// Para obter cada novo ponto de aproximação deve-se faze x = c - f(c)/f'(c) e c = x, repetindo o processo.


void secante(double (*f)(double), double(*df)(double, double), double x0, double x1, double tolerance){
    while(fabs(f(x1)) > tolerance){
        
        //x1 = x0 - f(x0)/aproximateDerivative(x0, x1);
        
        x1 = (x0*f(x1) - x1*f(x0))/(f(x1)-f(x0)); // Essa equação é igual à da linha comentada acima!
        
        printf("m = %.17f\n", x1);                      
        //Obs.: Note que o primeiro print será de x2
    }
}


int main(){
    setlocale(LC_ALL, "");
    double (*f)(double);
    double (*df)(double, double);
    f = function;
    df = aproximateDerivative;
    double x0 = 0.32056;
    double x1 = 1.22067;
    secante(f, df, x0, x1, 0.00000000000001);
}