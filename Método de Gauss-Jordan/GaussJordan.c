#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void printMatrix(double **matrix, int rows, int cols){
    for(int i = 0; i < rows; i++){ 
        for(int j = 0; j < cols; j++){
            printf("%.9f ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void mulLine(double **matrix, int cols, int resultLine, double mult){
    for(int i = 0; i < cols; i++) matrix[resultLine][i] = matrix[resultLine][i]*mult; 
}

void divLine(double **matrix, int cols, int resultLine, double divisor){
    for(int i = 0; i < cols; i++) matrix[resultLine][i] = matrix[resultLine][i]/divisor; 
}

void addLine(double **matrix, int cols, int resultLine, int sumLine, double sumLineMul){
    for(int i = 0; i < cols; i++) matrix[resultLine][i] = matrix[resultLine][i] + sumLineMul*matrix[sumLine][i];
}

void swapLine(double **matrix, int cols, int Line1, int Line2){
    double temp;
    for(int i = 0; i < cols; i++){
        temp = matrix[Line1][i];
        matrix[Line1][i] = matrix[Line2][i];
        matrix[Line2][i] = temp;
    }
}

// matriz com algum coeficiente 0 não está funcionando (sugestão: fazer função que troque as linhas)

void gaussJordan(double **matrix, int rows, int cols){
    // (1) A última coluna é a matriz B é tal que A.X = B, ou seja, são os valores que o sistema de equações deve satisfazer,...
    // ... assim, dado que a última coluna da matriz não se trata sobre as variáveis, j varia de 0 a cols-1 pois a última coluna...
    // ... não é usada no processo de escalonamento:
    for(int j = 0; j < cols-1; j++){

        // (2) i varia de j até rows pois se estamos na coluna j significa que já escalonas a coluna j-1 pela com a linha j-1,...
        // ... ou seja, devemos agora escalonar para a variável x_j visto que já que escalonamos para x_j-1:
        for(int i = j; i < rows; i++){
            // (2.1) Se estivermos em uma linha cujo pivô da atual coluna seria 0, deve-se trocar essa linha com a seguinte,...
            // ... e caso isso também resulte em um pivô nulo, deve-se repetir o processo até que não se possa mais trocar...
            // ... de linhas:
            if(matrix[i][j] == 0 && i < rows-1){
                int k = i;
                while(matrix[k][j] == 0 && k < rows-1) swapLine(matrix, cols, i, i+1);
            }

            // (2.2) Caso tenhamos um pivô de coeficiente diferente de 0 na atual linha i e coluna j, podemos então dividir a...
            // ... linha deste pivô pelo coeficiente a_ij e então realizar o escalonamento subtraindo a linha i nas outras linhas...
            // ... sempre multiplicando a linha i pelo coeficiente da outra linha na mesma coluna j ao realizar a subtração:
            if(matrix[i][j] != 0){
                divLine(matrix, cols, i, matrix[i][j]);
                for(int k = 0; k < rows; k++){
                    if(k != i) addLine(matrix, cols, k, i, -matrix[k][j]);
                }
                // (2.3) Caso o escalona mento tenha sido feito com pivô na linha i, deve-se mover para a proxima coluna e...
                // ... também para a próxima linha (o que é feito pois o for inicia com i=j), para se realizar o escalonamento...
                // ... para a próxima variável.
                break;
            }
        }
    }
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
    printMatrix(matrix, *rows, *cols);
    gaussJordan(matrix, *rows, *cols);
    printMatrix(matrix, *rows, *cols);
}
