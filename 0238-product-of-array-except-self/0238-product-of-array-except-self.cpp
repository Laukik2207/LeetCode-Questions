class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n,1);

        int pf = 1;
        for(int i = 0;i<n;i++){
            ans[i] = pf;
            pf *= nums[i];
        }

        int sf = 1;
        for(int i = n-1;i>=0;i--){
            ans[i] *= sf;
            sf *= nums[i];
        }

        return ans;
    }
};