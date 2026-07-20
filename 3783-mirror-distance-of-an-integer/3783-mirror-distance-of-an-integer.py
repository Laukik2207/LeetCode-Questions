class Solution:
    def mirrorDistance(self, n: int) -> int:
        og = n
        reverse = 0
        while(n > 0):
            reverse = reverse*10 + n%10
            n //= 10
        return abs(og - reverse)