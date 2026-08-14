class Solution {
public:
    int maximumLengthSubstring(string s) {
        unordered_map<char,int>freq;

        int maax = 0;
        int l = 0;
        int n = s.length();
        for(int i = 0;i<n;i++){
            freq[s[i]]++;
            while(freq[s[i]] > 2){
                --freq[s[l++]];
            }
            maax = max(maax,i-l+1);

        }
        return maax;
    }
};