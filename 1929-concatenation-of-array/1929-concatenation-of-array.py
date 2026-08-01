class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        l = 0
        for i in range(2 * len(nums)):
            ans.append(nums[l])
            l+=1
            if l == len(nums):
                l = 0
        return ans
