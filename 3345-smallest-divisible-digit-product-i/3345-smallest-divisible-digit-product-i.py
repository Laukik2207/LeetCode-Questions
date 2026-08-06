class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            x = n
            pr = 1
            while(x > 0):
                pr *= x%10
                x //= 10
            if pr % t == 0:
                return n
            n += 1

