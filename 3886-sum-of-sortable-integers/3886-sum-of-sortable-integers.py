from collections import Counter
from math import isqrt
from typing import List
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        # Find all divisors of n
        divisors = []
        for k in range(1, isqrt(n) + 1):
            if n % k == 0:
                divisors.append(k)
                if k != n // k:
                    divisors.append(n // k)

        for k in divisors:
            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                target_block = target[start:start + k]

                # Both blocks must contain the same elements
                if Counter(block) != Counter(target_block):
                    valid = False
                    break

                # A cyclic rotation of a sorted block has at most
                # one strict descent in circular order.
                descents = 0
                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        descents += 1

                if descents > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans