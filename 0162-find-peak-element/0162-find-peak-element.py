class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        idx = 0
        n=len(nums)
        for i in range(n):
            if nums[i] > nums[idx]:
                idx = i
        return idx