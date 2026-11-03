class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        mv = 0
        for i in nums:
            mv += mx - i
        return mv