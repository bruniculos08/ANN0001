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

void addLine(float **matrix, int cols, int resultLine, int sumLine, float resultLineMul, float sumLineMul){
    for(int i = 0; i < cols; i++) matrix[resultLine][i] = resultLineMul*matrix[resultLine][i] + sumLineMul*matrix[sumLine][i];
}

void swapLine(float **matrix, int cols, int Line1, int Line2){
    float temp;
    for(int i = 0; i < cols; i++){
        temp = matrix[Line1][i];
        matrix[Line1][i] = matrix[Line2][i];
        matrix[Line2][i] = temp;
    }
}

void saveMatrix(float **matrix, int rows, int cols){
    remove("Matrix.txt");
    FILE *filePointer;
    filePointer = fopen("Matrix.txt", "w+");
    fprintf(filePointer, "%i %i\n", rows, cols);
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            fprintf(filePointer, "%.17f ", matrix[i][j]);
        }
        fprintf(filePointer, "\n");
    }
    fclose(filePointer);
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

    int option = -1, line1, line2;
    float mult1, mult2; 
    while(option != 0){
        scanf("%i", &option);
        switch (option)
        {
        case 1:
            printf("Digite a linha de resultado: ");
            scanf("%i", &line1);
            printf("Digite a linha a se somar: ");
            scanf("%i", &line2);
            printf("Digite o multiplicador da linha 1: ");
            scanf("%f", &mult1);
            printf("Digite o multiplicador da linha 2: ");
            scanf("%f", &mult2);
            addLine(matrix, *cols, line1-1, line2-1, mult1, mult2);
            break;
        case 2:
            printf("Digite a linha a ser multiplicada: ");
            scanf("%i", &line1);
            printf("Digite o valor para se multiplicar a linha: ");
            scanf("%f", &mult1);
            mulLine(matrix, *cols, line1-1, mult1);
            break;
        case 3:
            printf("Digite a linha a ser dividida: ");
            scanf("%i", &line1);
            printf("Digite o valor para se dividir a linha: ");
            scanf("%f", &mult1);
            divLine(matrix, *cols, line1-1, mult1);
            break;
        case 4:
            saveMatrix(matrix, *rows, *cols);
            printf("A matriz foi salva.\n");
            break;
        default:
            break;
        }
        printf("\n");
        printMatrix(matrix, *rows, *cols);
    }

}
