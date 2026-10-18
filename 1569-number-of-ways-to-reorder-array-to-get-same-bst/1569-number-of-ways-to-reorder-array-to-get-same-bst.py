
import sys
sys.setrecursionlimit(10000)

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        # Precompute inverse factorials using Fermat's theorem
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # Calculate nCr in O(1)
        def comb(n, r):
            return (
                fact[n] * inv_fact[r] % MOD
                * inv_fact[n - r] % MOD
            )

        def dfs(arr):
            # No interleaving needed for 0 or 1 element
            if len(arr) <= 1:
                return 1

            root = arr[0]

            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            L = len(left)
            R = len(right)

            left_ways = dfs(left)
            right_ways = dfs(right)

            # Interleave left and right subtree elements
            ways = comb(L + R, L)
            ways = ways * left_ways % MOD
            ways = ways * right_ways % MOD

            return ways

        # Exclude the original ordering exactly once
        return (dfs(nums) - 1) % MOD
