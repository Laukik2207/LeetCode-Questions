class Solution {
public:
    long long findKthSmallest(vector<int>& a, int k) {
        int n = a.size();

        auto count = [&](long long x) {
            long long res = 0;

            for (int mask = 1; mask < (1 << n); mask++) {
                long long l = 1;
                int bits = 0;

                for (int i = 0; i < n; i++) {
                    if (mask >> i & 1) {
                        bits++;
                        l = l / gcd(l, (long long)a[i]) * a[i];
                        if (l > x) break;
                    }
                }

                if (l <= x)
                    res += (bits & 1) ? x / l : -x / l;
            }

            return res;
        };

        long long lo = 1, hi = 1LL * *min_element(a.begin(), a.end()) * k;

        while (lo < hi) {
            long long mid = (lo + hi) / 2;

            if (count(mid) >= k)
                hi = mid;
            else
                lo = mid + 1;
        }

        return lo;
    }
};