class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        t = 1
        for i in s:
            sum += t* (26-(ord(i)-ord('a')))
            t+=1
        return sum