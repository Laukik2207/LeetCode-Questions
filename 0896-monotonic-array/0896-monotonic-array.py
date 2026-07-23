class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        # if(n)
        if(n < 3):
            return True
        k = 0
        if(nums[k] == nums[k+1]):
            while(k < n-1 and nums[k] == nums[k+1]):
                k+=1
        if(k >= n-1):
            return True
        if(nums[k] < nums[k+1]):
            for i in range(n-1):
                if(nums[i] > nums[i+1]):
                    return False
        else:
            for i in range(n-1):
                if( nums[i] < nums[i+1]):
                    return False
        return True