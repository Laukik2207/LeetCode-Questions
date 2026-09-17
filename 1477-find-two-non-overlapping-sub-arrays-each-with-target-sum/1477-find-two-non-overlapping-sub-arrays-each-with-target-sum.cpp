class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();
        int INF = 1e9;

        vector<int> prefix(n, INF);
        vector<int> suffix(n, INF);
        int left = 0, sum = 0;

        for (int right = 0; right < n; right++) {
            sum += arr[right];

            while (sum > target) {
                sum -= arr[left++];
            }

            if (sum == target) {
                prefix[right] = right - left + 1;
            }

            if (right > 0) {
                prefix[right] = min(prefix[right], prefix[right - 1]);
            }
        }
        int right = n - 1;
        sum = 0;

        for (int left = n - 1; left >= 0; left--) {
            sum += arr[left];

            while (sum > target) {
                sum -= arr[right--];
            }

            if (sum == target) {
                suffix[left] = right - left + 1;
            }

            if (left < n - 1) {
                suffix[left] = min(suffix[left], suffix[left + 1]);
            }
        }

        // Split between i and i + 1
        int ans = INF;

        for (int i = 0; i < n - 1; i++) {
            if (prefix[i] != INF && suffix[i + 1] != INF) {
                ans = min(ans, prefix[i] + suffix[i + 1]);
            }
        }

        return ans == INF ? -1 : ans;
    }
};