class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        arr = []
        for i in range(mini , maxi):
            if i not in nums:
                arr.append(i)
        return arr