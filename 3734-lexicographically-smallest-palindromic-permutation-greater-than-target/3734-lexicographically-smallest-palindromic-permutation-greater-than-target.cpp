class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.size();
        int h = n / 2;

        vector<int> cnt(26);

        for (char c : s)
            cnt[c - 'a']++;

        int odd = 0;
        char mid = 0;

        for (int c = 0; c < 26; c++) {
            if (cnt[c] & 1) {
                odd++;
                mid = char('a' + c);
            }
            cnt[c] /= 2;
        }

        if (odd > 1)
            return "";

        auto makePal = [&](const string& left) {
            string ans = left;

            if (n & 1)
                ans += mid;

            for (int i = h - 1; i >= 0; --i)
                ans += left[i];

            return ans;
        };

        string best = "";

        /*
         * Try every possible position i where the answer's
         * left half first differs from target.
         */
        for (int i = 0; i < h; i++) {

            vector<int> rem = cnt;
            bool ok = true;

            // Match target[0 ... i-1].
            for (int j = 0; j < i; j++) {
                int c = target[j] - 'a';

                if (rem[c] == 0) {
                    ok = false;
                    break;
                }

                rem[c]--;
            }

            if (!ok)
                continue;

            int cur = target[i] - 'a';

            // Make the first difference as small as possible.
            for (int c = cur + 1; c < 26; c++) {

                if (rem[c] == 0)
                    continue;

                vector<int> r = rem;
                r[c]--;

                string left = target.substr(0, i);
                left += char('a' + c);

                // Minimum suffix.
                for (int x = 0; x < 26; x++) {
                    left += string(r[x], char('a' + x));
                }

                string candidate = makePal(left);

                if (candidate > target &&
                    (best.empty() || candidate < best)) {
                    best = candidate;
                }

                // Because c is increasing, the first valid one
                // is the best for this particular i.
                break;
            }
        }

        /*
         * Finally consider the palindrome whose entire left half
         * equals target's left half.
         *
         * This handles:
         *
         * s = "bb"
         * target = "ba"
         * candidate = "bb"
         */
        vector<int> rem = cnt;
        bool ok = true;

        for (int i = 0; i < h; i++) {
            int c = target[i] - 'a';

            if (rem[c] == 0) {
                ok = false;
                break;
            }

            rem[c]--;
        }

        if (ok) {
            string left = target.substr(0, h);
            string candidate = makePal(left);

            if (candidate > target &&
                (best.empty() || candidate < best)) {
                best = candidate;
            }
        }

        return best;
    }
};