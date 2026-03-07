// 59. Spiral Matrix 2

#include<iostream>
#include<vector>
using namespace std;

vector<vector<int>> generateMatrix(int n) {
        
        vector<vector<int>> matrix(n, vector<int>(n));
        
        int srow = 0, scol = 0;
        int erow = n - 1, ecol = n - 1;
        
        int num = 1;
        
        while(srow <= erow && scol <= ecol){
            
            // TOP
            for(int j = scol; j <= ecol; j++){
                matrix[srow][j] = num++;
            }
            
            // RIGHT
            for(int i = srow + 1; i <= erow; i++){
                matrix[i][ecol] = num++;
            }
            
            // BOTTOM
            if(srow < erow){
                for(int j = ecol - 1; j >= scol; j--){
                    matrix[erow][j] = num++;
                }
            }
            
            // LEFT
            if(scol < ecol){
                for(int i = erow - 1; i > srow; i--){
                    matrix[i][scol] = num++;
                }
            }
            
            srow++;
            scol++;
            erow--;
            ecol--;
        }
        
        return matrix;
    }

    int main(){
        
    }