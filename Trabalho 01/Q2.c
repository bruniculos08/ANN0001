#include <math.h>
#include <stdio.h>
#include <locale.h>

double function(double x){
    return M_PI*x - pow(M_E, x);
}

void bisectionRecursive(double (*f)(double), double a, double b, double tolerance){
    if(f(a)*f(b) > 0){
        printf("Esse intervalo não pode ser utilizado.\n");
        return;
    }

    if(fabs(f(a)) < tolerance){
        printf("x = %.17f é uma raiz da função.\n", a);
        return;
    }

    if(fabs(f(b)) < tolerance){
        printf("x = %.17f é uma raiz da função.\n", b);
        return;
    }

    double m = (a+b)/2;
    printf("m = %.17f\n", m);

    if(f(a)*f(m) < 0) bisectionRecursive(f, a, m, tolerance);
    else bisectionRecursive(f, m, b, tolerance);

}

void bisection(double (*f)(double), double a, double b, double tolerance){
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
    int iterations = 0;
    while(fabs(f(m)) >= tolerance)
    {
        m = (a+b)/2;
        iterations++;
        printf("m = %.17f\n", m);
        if(f(m)*f(a) > 0) a = m; // Não esquecer que a condição é f(m).f(a) e não a.m
        else b = m;
    }

    printf("x = %.17f é uma raiz da função (%i iterações).\n", m, iterations);    
}


int main(){
    setlocale(LC_ALL, "");
    double (*f)(double);
    f = function;
    double a = 0.332586, b = 1.210148;
    
    bisection(f, a, b, 3.4173*pow(10, -12));
}