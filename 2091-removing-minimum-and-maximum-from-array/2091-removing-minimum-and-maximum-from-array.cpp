class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();
        int maxi = 0;
        int mini = 0;

        for(int i = 0;i<n;i++){
            if(nums[i] > nums[maxi]){
                maxi = i;
            }else if(nums[i] < nums[mini]){
                mini = i;
            }
        }

        int l = min(mini,maxi);
        int r = max(mini,maxi);

        int front = r+1;
        int back = n - l;
        int both = (l+1)+(n-r);
        return min({front,back,both});
    }
};