//153. Find Minimum in Rotated Sorted Array

#include<iostream>
#include<vector>
using namespace std;

int findMin(vector<int>& nums) {
        int st = 0;
        int end = nums.size() - 1;
        while(st < end){
            int mid = st + (end-st) / 2;
            if(nums[mid] > nums[end]){
                st = mid+1;
            }else{
                end = mid;
            }
        }
        return nums[st];
    }

int main(){
    vector<int> nums = {3,4,5,1,2};
    cout<<findMin(nums)<<endl;
    return 0;
}