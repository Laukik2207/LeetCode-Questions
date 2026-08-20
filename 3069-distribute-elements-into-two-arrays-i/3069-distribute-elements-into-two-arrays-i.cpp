class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
        int n = nums.size();
        vector<int>arr1;
        vector<int>arr2;
        arr1.push_back(nums[0]);
        arr2.push_back(nums[1]);
        int l = 0;
        int r = 0;

        for(int i = 2;i<n;i++){
            if(arr1[l] > arr2[r]){
                arr1.push_back(nums[i]);
                l++;
            }else{
                arr2.push_back(nums[i]);
                r++;
            }
        }

        for(int x : arr2){
            arr1.push_back(x);
        }
        return arr1;
    }
};