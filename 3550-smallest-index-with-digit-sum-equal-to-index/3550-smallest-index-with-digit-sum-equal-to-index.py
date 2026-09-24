class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(nums[i] < 10):
                if(i == nums[i]):
                    return i
                continue
            n = nums[i]
            t = 0
            while(n>0):
                t += n%10
                n //= 10
            if(t==i):
                return i
        return -1