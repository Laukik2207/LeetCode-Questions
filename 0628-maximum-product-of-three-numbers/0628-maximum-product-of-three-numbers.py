class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        m1 = m2 = m3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            if num > m1:
                m3 = m2
                m2 = m1
                m1 = num
            elif num > m2:
                m3 = m2
                m2 = num
            elif num > m3:
                m3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(m1*m2*m3,m1*min1*min2)
