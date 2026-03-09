#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int i = 0;
        int j = n-1;
        while(i<j){
            int sum = numbers[i] + numbers[j];
            if(sum == target){
                return{i+1,j+1};
            }else if(sum > target){
                j--;
            }else{
                i++;
            }
        }
        return {};
    }

int main(){
    vector<int> numbers = {2,7,11,15};
    int target = 9;
    vector<int> ans = twoSum(numbers , target);
    for(int i = 0;i<ans.size();i++){
        cout<<ans[i]<<" ";
    }
}