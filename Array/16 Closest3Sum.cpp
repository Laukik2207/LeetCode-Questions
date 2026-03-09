#include<iostream>
#include<vector>
#include<cmath>
#include <algorithm>
using namespace std;

int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin() , nums.end());

        int closest = 100000;

        for(int i = 0;i<n;i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int j = i+1;
            int k = n-1;
            while(j < k){
                int sum = nums[i] + nums[j] + nums[k];
                if(sum > target){
                    k--;
                }else if(sum < target){
                    j++;
                }else{
                    return target;
                }

                if(abs(target - sum) < abs(target - closest)){
                    closest = sum;
                }
            }
        }
        return closest;
    }


int main(){
    vector<int> nums = {-1,2,1,-4};
    int target = 1;
    int ans = threeSumClosest(nums , target);
    cout<<ans;
}