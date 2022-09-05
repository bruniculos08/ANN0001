#include <math.h>
#include <stdio.h>

void mulLine(int rows, int cols, int resultLine, int mult, int matrix[rows][cols]){
    for(int i = 0; i < cols; i++) matrix[resultLine][i] = mult*matrix[resultLine][i]; 
}

void addLine(int rows, int cols, int resultLine, int sumLine, int sumLineMul, int matrix[rows][cols]){
    for(int i = 0; i < cols; i++) matrix[resultLine][i] = matrix[resultLine][i] + sumLineMul*matrix[sumLine][i];
}


void gaussJordan(int rows, int cols, int matrix[rows][cols]){
    for(int i = 0; i < cols; i++) for(int j = 0; j < rows; j++){ // Andar pelas colunas e em cada coluna andar pelas linhas
            if(matrix[i][j] != 0){
                    for(int k = 0; k < rows; k++){ // Quando achar a primeira linha diferente de 0:
                        if(k == j && matrix[i][k] == 1) continue;
                        else if(k == j && matrix[i][k] != 0){
                            mulLine(rows, cols, k, 1/matrix[i][k], matrix);
                            continue;
                        }
                        addLine(rows, cols, k, j, -(matrix[i][k])/matrix[i][j], matrix);                    
                }
            }
    }
}

void printMatrix(int rows, int cols, int matrix[rows][cols]){
    for(int i = 0; i < rows; i++) for(int j = 0; j < cols; j++){
        printf("%i ", matrix[i][j]);
        if(j = cols-1) printf("\n");
    }
}

int main(){
    int matrix[3][3] = {{1, 2, 4}, {5, 1, 3}};
    gaussJordan(3, 3, matrix);
}
