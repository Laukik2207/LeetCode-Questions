
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {v: i for i, v in enumerate(nums)}
        swaps = 0

        for i, v in enumerate(arr):
            j = pos[v]
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
                pos[nums[j]] = j
                pos[nums[i]] = i
                swaps += 1

        return swaps
