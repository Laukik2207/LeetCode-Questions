class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        leftsum = 0
        for i in range(n):
            if(leftsum == total - leftsum - nums[i]):
                return i
            leftsum += nums[i]
        return -1