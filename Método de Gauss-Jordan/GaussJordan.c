#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void printMatrix(float **matrix, int rows, int cols){
    for(int i = 0; i < rows; i++){ 
        for(int j = 0; j < cols; j++){
            printf("%f ", matrix[i][j]);
        }
        printf("\n");
    }
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

// matriz com algum coeficiente 0 não está funcionando (sugestão: fazer função que troque as linhas)

void gaussJordan(float **matrix, int rows, int cols){
    // (1) A última coluna é a matriz B é tal que A.X = B, ou seja, são os valores que o sistema de equações deve satisfazer.
    for(int j = 0; j < cols-1; j++){
        for(int i = j; i < rows; i++){

            // (2) Se estivermos em uma linha cujo pivô da atual coluna seria 0, deve-se trocar essa linha com a seguinte,...
            // ... e caso isso também resulte em um pivô nulo, deve-se repetir o processo até que não se possa mais trocar...
            // ... de linhas:
            if(matrix[i][j] == 0 && i < rows-1){
                int k = i;
                while(matrix[k][j] == 0 && k < rows-1) swapLine(matrix, cols, i, i+1);
            }

            if(matrix[i][j] != 0){
                printf("dividir linha %i (pivo %f)\n", i, matrix[i][j]);
                divLine(matrix, cols, i, matrix[i][j]);
                for(int k = 0; k < rows; k++){
                    if(k != i) addLine(matrix, cols, k, i, -matrix[k][j]);
                }
                printf("\n");
                printMatrix(matrix, rows, cols);
                printf("\n");
                break;
            }
        }
    }
}

float **createMatrix(int *rows, int *cols){

    FILE *filePointer;
    filePointer = fopen("Matrix.txt", "r");
    fscanf(filePointer, "%i %i\n", rows, cols); 
    printf("%i %i \n", *rows, *cols);

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
    gaussJordan(matrix, *rows, *cols);
    //mulLine(matrix, *cols, 0, (0.5)); addLine(matrix, *cols, 2, 0, 0.2);
    printf("\n");
    printMatrix(matrix, *rows, *cols);
}
