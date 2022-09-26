#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void printVetor(double *vetor, int rows){
    for(int i = 0; i < rows; i++){ 
        //printf("x_%i = %.17f\n", i+1, vetor[i]);
        printf("%.7f, ", vetor[i]);
    }
    printf("\n");
}

void printMatrix(double **matrix, int rows, int cols){
    for(int i = 0; i < rows; i++){ 
        for(int j = 0; j < cols; j++){
            printf("%lf ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void swapLine(double **matrix, int cols, int Line1, int Line2){
    double temp;
    for(int i = 0; i < cols; i++){
        temp = matrix[Line1][i];
        matrix[Line1][i] = matrix[Line2][i];
        matrix[Line2][i] = temp;
    }
}

void jacobi(double **matrix, int rows, int cols, double *vetor, int n){
    for(int k = 0; k < n; k++){
        double tempVetor[rows];
        for(int i = 0; i < rows; i++){
            double temp = 0; 
            for(int j = 0; j < cols; j++){
                if(j != i && j != cols-1) temp += (-matrix[i][j]*vetor[j])/matrix[i][i];
                else if(j == cols-1) temp += ((matrix[i][j])/matrix[i][i]);
                // Não pode ficar somando em vetor, tem que criar uma variável temporária
            }
            tempVetor[i] = temp;
        }
        // O vetor de solução só pe atualizado depois de uma iteração completa (diferente do método de Seidel)
        for(int i = 0; i < rows; i++) vetor[i] = tempVetor[i]; 

        //printf("%i iteracoes:\n", k+1);
        //printVetor(vetor, rows);
    }
    //printf("%i iteracoes:\n", n);
    printVetor(vetor, rows);
}

double **createMatrix(int *rows, int *cols){

    FILE *filePointer;
    filePointer = fopen("Matrix.txt", "r");
    fscanf(filePointer, "%i %i\n", rows, cols); 
    printf("\nMatriz de %i linhas e %i colunas. \n\n", *rows, *cols);


    // (1) Alocando os ponteiros para as linhas da matriz:
    // - o ponteiro de ponteiro aponta para um espaço a partir de onde há um número rows de ponteiros para int's
    double **matrix = (double **)malloc((*rows)*sizeof(double*));

    // (2) Alocando os ponteiros para as colunas da matriz:
    // - cada ponteiro para int aponta para um espaço a partir de onde há um número columns de int's
    for(int i=0; i<(*rows); i++){
        matrix[i] = (double *)malloc((*cols)*sizeof(double));

        // (2.1) Setando os elementos da matriz iguais à zero para inserção (por meio de adição) das arestas na função createGraph:
        for(int j=0; j<(*cols); j++) fscanf(filePointer, "%lf ", &matrix[i][j]);
        //fscanf(filePointer, "\n");
    }
    return matrix;
}

int main(){
    int *rows;
    rows = malloc(sizeof(int));
    int *cols;
    cols = malloc(sizeof(int));

    double **matrix = createMatrix(rows, cols);
    
    double *vetor;
    vetor = malloc((*rows)*sizeof(double));

    //for (int i = 0; i < *rows; i++) vetor[i] = 0;
    // Obs.: o vetor deveria ser resetado dentro do loop, por isso o exercício deu errado
    //vetor[0] = -0.95;
    //vetor[1] = 1.09;
    //vetor[2] = 3.46;

    int rodadas[] = {3 , 6, 8, 10, 11, 15, 16, 19, 23, 24, 26, 29 };

    printVetor(vetor, *rows);
    printMatrix(matrix, *rows, *cols);
    for(int i = 0; i < sizeof(rodadas)/sizeof(int); i++){ 
        vetor[0] = -4.14;
        vetor[1] = 0.89;
        vetor[2] = -2.64;
        vetor[3] = -1.23;
        jacobi(matrix, *rows, *cols, vetor, rodadas[i]);
    }
    //printVetor(vetor, *rows);

}
