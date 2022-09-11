#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void printMatrix(float **matrix, int rows, int cols){
    for(int i = 0; i < rows; i++){ 
        for(int j = 0; j < cols; j++){
            printf("%.17f ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void mulLine(float **matrix, int cols, int resultLine, float mult){
    for(int i = 0; i < cols; i++) matrix[resultLine][i] = matrix[resultLine][i]*mult; 
}

void divLine(float **matrix, int cols, int resultLine, float divisor){
    for(int i = 0; i < cols; i++) matrix[resultLine][i] = matrix[resultLine][i]/divisor; 
}

void addLine(float **matrix, int cols, int resultLine, int sumLine, float sumLineMul){
    for(int i = 0; i < cols; i++) matrix[resultLine][i] = matrix[resultLine][i] + sumLineMul*matrix[sumLine][i];
}

void swapLine(float **matrix, int cols, int Line1, int Line2){
    float temp;
    for(int i = 0; i < cols; i++){
        temp = matrix[Line1][i];
        matrix[Line1][i] = matrix[Line2][i];
        matrix[Line2][i] = temp;
    }
}

float **createMatrix(int *rows, int *cols){

    FILE *filePointer;
    filePointer = fopen("Matrix.txt", "r");
    fscanf(filePointer, "%i %i\n", rows, cols); 
    printf("\nMatriz de %i linhas e %i colunas. \n\n", *rows, *cols);

    // (1) Alocando os ponteiros para as linhas da matriz:
    // - o ponteiro de ponteiro aponta para um espaço a partir de onde há um número rows de ponteiros para int's
    float **matrix = (float **)malloc((*rows)*sizeof(float*));

    // (2) Alocando os ponteiros para as colunas da matriz:
    // - cada ponteiro para int aponta para um espaço a partir de onde há um número columns de int's
    for(int i=0; i<(*rows); i++){
        matrix[i] = (float *)malloc((*cols)*sizeof(float));

        // (2.1) Setando os elementos da matriz iguais à zero para inserção (por meio de adição) das arestas na função createGraph:
        for(int j=0; j<(*cols); j++) fscanf(filePointer, "%f ", &matrix[i][j]);
        //fscanf(filePointer, "\n");
    }
    return matrix;
}

int main(){
    int *rows;
    rows = malloc(sizeof(int));
    int *cols;
    cols = malloc(sizeof(int));
    
    float **matrix = createMatrix(rows, cols);

    printMatrix(matrix, *rows, *cols);

    // Operação 1:
    // 1/2⋅L1 + L2 → L2
    addLine(matrix, *cols, 1, 0, 0.5);

    printMatrix(matrix, *rows, *cols);
    // Operação 2:
    addLine(matrix, *cols, 2, 0, 1.75);

    // Operação 3:
    addLine(matrix, *cols, 3, 0, -1.5);

    // Operação 4:
    addLine(matrix, *cols, 2, 1, 1.25);

    // Operação 5:
    addLine(matrix, *cols, 3, 1, 0.83333333333333333);

    // Operação 6:
    addLine(matrix, *cols, 3, 2, 0.90909090909090909090909090909091);

    printMatrix(matrix, *rows, *cols);
}
