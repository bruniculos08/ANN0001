#include <math.h>
#include <stdio.h>
#include <locale.h>

double function(double x){
    return pow(x, 2) - 3;
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
    double a = 0.72217, b = 2.38122;
    int vetor[] = {2, 4, 5, 6, 11, 12, 13, 16, 21, 22, 23, 24, 28, 29, 31, 33, 35, 36, 37, 38};
    for(int i = 0; i < sizeof(vetor)/sizeof(vetor[0]); i++) bisection(f, a, b, vetor[i]);
}