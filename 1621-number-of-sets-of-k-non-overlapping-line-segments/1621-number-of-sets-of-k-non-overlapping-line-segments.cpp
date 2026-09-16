class Solution {
public:
    int numberOfSets(int n, int k) {
        const int MOD = 1e9 + 7;

        long long ans = 1;

        for (int i = 1; i <= 2 * k; i++) {
            ans = ans * (n + k - i) % MOD;

            // Modular inverse using Fermat's Little Theorem
            ans = ans * modInverse(i) % MOD;
        }

        return ans;
    }

private:
    long long modInverse(long long x) {
        return power(x, 1e9 + 5);
    }

    long long power(long long a, long long b) {
        long long result = 1;

        while (b > 0) {
            if (b & 1) {
                result = result * a % 1000000007;
            }

            a = a * a % 1000000007;
            b >>= 1;
        }

        return result;
    }
};