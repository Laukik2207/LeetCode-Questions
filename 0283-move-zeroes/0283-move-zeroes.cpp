class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int l = 0;
        for(int r = 0;r<n;r++){
            if(nums[r] == 0){
                continue;
            }else{
                swap(nums[r],nums[l]);
                l++;
            }
        }
        return;
    }
};