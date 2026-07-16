class Solution {
public:
    long long gcdSum(vector<int>& nums) {
        int n = nums.size();
        vector<int>prefixgcd(n);
        int mx = nums[0];

        for (int i = 0; i < n; i++) {
            mx = max(mx, nums[i]);
            prefixgcd[i] = gcd(nums[i], mx);
        }

        sort(prefixgcd.begin(),prefixgcd.end());



        int l = 0;
        int r = n - 1;
        // if(nums.size() % 2 == 0){
        //     while
        // }
        long long sum = 0;
        while(l < r){
            sum = sum + gcd(prefixgcd[l],prefixgcd[r]);
            l++;
            r--;
        }
        return sum;
    }
};