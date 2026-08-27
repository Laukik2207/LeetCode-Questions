class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int cnt[26] = {};

        for (char c : s)
            cnt[c - 'a']++;

        for (int i = 0; i < target.size(); i++) {

            // Try to match target[i]
            if (cnt[target[i] - 'a']) {
                cnt[target[i] - 'a']--;
                continue;
            }

            // Can't match -> choose smallest character greater than target[i]
            for (int c = target[i] - 'a' + 1; c < 26; c++) {
                if (cnt[c]) {
                    string ans = target.substr(0, i);
                    ans += char('a' + c);
                    cnt[c]--;

                    for (int j = 0; j < 26; j++)
                        while (cnt[j]--)
                            ans += char('a' + j);

                    return ans;
                }
            }

            // Need to backtrack
            for (int j = i - 1; j >= 0; j--) {
                cnt[target[j] - 'a']++;

                for (int c = target[j] - 'a' + 1; c < 26; c++) {
                    if (cnt[c]) {
                        string ans = target.substr(0, j);
                        ans += char('a' + c);
                        cnt[c]--;

                        for (int k = 0; k < 26; k++)
                            while (cnt[k]--)
                                ans += char('a' + k);

                        return ans;
                    }
                }
            }

            return "";
        }

        // s can form exactly target, but we need strictly greater.
        for (int i = target.size() - 1; i >= 0; i--) {
            cnt[target[i] - 'a']++;

            for (int c = target[i] - 'a' + 1; c < 26; c++) {
                if (cnt[c]) {
                    string ans = target.substr(0, i);
                    ans += char('a' + c);
                    cnt[c]--;

                    for (int k = 0; k < 26; k++)
                        while (cnt[k]--)
                            ans += char('a' + k);

                    return ans;
                }
            }
        }

        return "";
    }
};