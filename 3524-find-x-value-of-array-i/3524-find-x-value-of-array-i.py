class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        curr = [0] * k
        for num in nums:
            new = [0] * k
            new[num%k] += 1
            for r in range(k):
                if curr[r]:
                    new[(r*num)%k] += curr[r]
            curr = new

            for r in range(k):
                ans[r] += curr[r]
        return ans