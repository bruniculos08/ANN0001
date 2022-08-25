#include <math.h>
#include <stdio.h>
#include <locale.h>

double function(double x){
    return x*x - 2;
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
    
    double m = (a+b)/2;
    while(fabs(f(m)) >= tolerance)
    {
        printf("m = %.17f\n", m);
        if(f(m)*f(a) > 0) a = m;
        else b = m;
        m = (a+b)/2;
    }

    printf("x = %.17f é uma raiz da função.\n", m);    
}


int main(){
    setlocale(LC_ALL, "");
    double (*f)(double);
    f = function;
    double a = 1, b = 2;
    bisection(f, a, b, 0.000000000000001);
}