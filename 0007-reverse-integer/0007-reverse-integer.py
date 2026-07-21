class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        neg = 1
        if(x < 0):
            neg = -1
            x = x*-1
        # x = abs(x)
        while x > 0:
            rev = rev*10 + x%10
            x//=10
        if(rev <= -2**31 or rev >= 2**31 - 1):
            return 0
        return rev*neg
        