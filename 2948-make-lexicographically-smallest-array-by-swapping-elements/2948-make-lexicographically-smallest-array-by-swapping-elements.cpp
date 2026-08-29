class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();

        // Store indices and sort them according to nums[index]
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);

        sort(idx.begin(), idx.end(), [&](int a, int b) {
            return nums[a] < nums[b];
        });

        vector<int> ans(n);

        for (int i = 0; i < n; ) {
            int j = i + 1;

            // Find one connected group
            while (j < n &&
                   nums[idx[j]] - nums[idx[j - 1]] <= limit) {
                j++;
            }

            // Get original indices of this group
            vector<int> positions(idx.begin() + i, idx.begin() + j);

            // Smaller values should go to smaller indices
            sort(positions.begin(), positions.end());

            // Assign sorted values to sorted positions
            for (int k = i; k < j; k++) {
                ans[positions[k - i]] = nums[idx[k]];
            }

            i = j;
        }

        return ans;
    }
};