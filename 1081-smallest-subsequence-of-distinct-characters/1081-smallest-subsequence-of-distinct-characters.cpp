class Solution {
public:
    string smallestSubsequence(string s) {

        vector<int> freq(26, 0);
        vector<bool> visited(26, false);

        for (char c : s)
            freq[c - 'a']++;

        stack<char> st;

        for (char c : s) {

            freq[c - 'a']--;

            if (visited[c - 'a'])
                continue;

            while (!st.empty() &&
                   c < st.top() &&
                   freq[st.top() - 'a'] > 0) {

                visited[st.top() - 'a'] = false;
                st.pop();
            }

            st.push(c);
            visited[c - 'a'] = true;
        }

        string ans;

        while (!st.empty()) {
            ans += st.top();
            st.pop();
        }

        reverse(ans.begin(), ans.end());

        return ans;
    }
};