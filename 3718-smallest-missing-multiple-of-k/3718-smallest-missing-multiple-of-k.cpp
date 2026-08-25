class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int t = k;
        for(int i = 0;i<n;i++){
            if(nums[i] == k){
                k+=t;
            }
        }
        return k;
    }
};