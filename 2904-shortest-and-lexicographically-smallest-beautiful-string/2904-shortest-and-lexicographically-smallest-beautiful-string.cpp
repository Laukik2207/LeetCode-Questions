class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        vector<int>pos;
        int n = s.size();
        for(int i = 0;i<n;i++){
            if(s[i] == '1'){
                pos.push_back(i);
            }
        }

        string ans = "";

        for(int i = 0;i+k-1<pos.size();i++){
            int start = pos[i];
            int end = pos[i+k-1];

            string curr = s.substr(start,end-start + 1);

            if(ans=="" || curr.size()<ans.size()){
                ans = curr;
            }
            else if(curr.size() == ans.size() && curr < ans){
                ans = curr;
            }
        }
        return ans;
    }
};