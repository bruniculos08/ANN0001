#include <math.h>
#include <stdio.h>
#include <locale.h>

double function(double x){
    return log(pow(x, 2)) - 0.7; // ou 2*log(x) - 0.7
    // A solução desta equação (log(x²) -0.7 = 0) é também a solução de log(x²) = 0.7
}

void bisection(double (*f)(double), double a, double b, int iterations){
    if(f(a)*f(b) > 0){
        printf("Esse intervalo não pode ser utilizado.\n");
        return;
    }

    if(f(a) == 0){
        printf("x = %.17f é uma raiz da função.\n", a);
        return;
    }

    if(f(b) == 0){
        printf("x = %.17f é uma raiz da função.\n", b);
        return;
    }
    
    double m;
    for(int i = 0; i < iterations; i++){
        m = (a+b)/2;
        //printf("m = %.17f\n", m);
        if(f(m)*f(a) > 0) a = m;
        else b = m;
    }

    printf("x = %.17f é uma raiz da função (%i iterações).\n", m, iterations);    
}


int main(){
    setlocale(LC_ALL, "");
    double (*f)(double);
    f = function;
    double a = 1.0635, b = 5.894;
    int vetor[] = {2, 3, 6, 7, 8, 9, 10, 15, 16, 19, 22, 23, 27, 28, 29, 30, 32, 36, 38, 39};
    for(int i = 0; i < sizeof(vetor)/sizeof(vetor[0]); i++) bisection(f, a, b, vetor[i]);
}