class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        if(k == nums.size()){
            return nums;
        }
        vector<int>ans;

        unordered_map<int,int>freq;
        for(auto x : nums){
            freq[x]++;
        }

        while(k > 0){
            int maxfreq = 0;
            int ele = 0;

            for(auto x : freq){
                if(x.second > maxfreq){
                    maxfreq = x.second;
                    ele = x.first;
                }
            }
            ans.push_back(ele);
            freq.erase(ele);
            k--;
        }
        return ans;

        

    }
};