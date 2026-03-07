// 54. Spiral Matrix

#include<iostream>
#include<vector>
using namespace std;

 vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        vector<int> ans;
        
        int n = matrix.size();
        if(n == 0) return ans;
        int m = matrix[0].size();
        
        int srow = 0, scol = 0;
        int erow = n - 1, ecol = m - 1;
        
        while(srow <= erow && scol <= ecol){
            
            // TOP
            for(int j = scol; j <= ecol; j++){
                ans.push_back(matrix[srow][j]);
            }
            
            // RIGHT
            for(int i = srow + 1; i <= erow; i++){
                ans.push_back(matrix[i][ecol]);
            }
            
            // BOTTOM
            if(srow < erow){
                for(int j = ecol - 1; j >= scol; j--){
                    ans.push_back(matrix[erow][j]);
                }
            }
            
            // LEFT
            if(scol < ecol){
                for(int i = erow - 1; i > srow; i--){
                    ans.push_back(matrix[i][scol]);
                }
            }
            
            srow++;
            scol++;
            erow--;
            ecol--;
        }
        
        return ans;
    }

int main(){
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    vector<int> result = spiralOrder(matrix);
    cout << "Spiral Order: ";
    for(int val : result){
        cout << val << " ";
    }
    cout << endl;
    return 0;
}