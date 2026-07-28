class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if(n==0) :
             return 0

        bb = [float('inf')] + [0] * (n - 1)

        for i in range (1,n):
            bb[i] = min(bb[i-1],prices[i-1])
        
        mx = 0

        for i in range(n):
            curr = prices[i] - bb[i]
            mx = max(curr,mx)
        return mx