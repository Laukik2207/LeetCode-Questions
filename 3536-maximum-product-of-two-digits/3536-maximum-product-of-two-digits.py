class Solution:
    def maxProduct(self, n: int) -> int:
        # if n < 10:
        #     return n
        m1 = 0
        m2 = 0

        while n > 0 :
            t = n%10
            if t > m1:
                m2 = m1
                m1 = t
            elif t > m2:
                m2 = t
            n = n//10
        return m1*m2
