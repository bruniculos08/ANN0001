#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void printVetor(float *vetor, int rows){
    for(int i = 0; i < rows; i++){ 
        printf("x_%i = %f\n", i+1, vetor[i]);
    }
    printf("\n");
}

void printMatrix(float **matrix, int rows, int cols){
    for(int i = 0; i < rows; i++){ 
        for(int j = 0; j < cols; j++){
            printf("%f ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void swapLine(float **matrix, int cols, int Line1, int Line2){
    float temp;
    for(int i = 0; i < cols; i++){
        temp = matrix[Line1][i];
        matrix[Line1][i] = matrix[Line2][i];
        matrix[Line2][i] = temp;
    }
}

void seidel(float **matrix, int rows, int cols, float *vetor, int n){
    for(int k = 0; k < n; k++){
        for(int i = 0; i < rows; i++){
            float temp = 0; 
            for(int j = 0; j < cols; j++){
                if(j != i && j != cols-1) temp += (-matrix[i][j]*vetor[j])/matrix[i][i];
                else if(j == cols-1) temp += ((matrix[i][j])/matrix[i][i]);
                // Não pode ficar somando em vetor, tem que criar uma variável temporária
            }
            vetor[i] = temp;
        }
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
    
    float *vetor;
    vetor = malloc((*rows)*sizeof(float));

    for (int i = 0; i < *rows; i++) vetor[i] = 0;

    int n = 10;

    printVetor(vetor, *rows);
    printMatrix(matrix, *rows, *cols);
    seidel(matrix, *rows, *cols, vetor, n);
    printVetor(vetor, *rows);

}
