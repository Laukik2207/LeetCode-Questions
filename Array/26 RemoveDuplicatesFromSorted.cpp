// 26. Remove Duplicates from Sorted Array

#include<iostream>
#include<vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
        int s = nums.size();
        int l = 1;
        for(int i = 1;i<s;i++){
            if(nums[i] != nums[i-1]){
                nums[l] = nums[i];
                l++;
            }
        }
        return l;
    }

int main(){
    vector<int> nums = {1,1,2};
    int newLength = removeDuplicates(nums);
    cout << "New length: " << newLength << endl;
    cout << "Modified array: ";
    for(int i = 0; i < newLength; i++){
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}