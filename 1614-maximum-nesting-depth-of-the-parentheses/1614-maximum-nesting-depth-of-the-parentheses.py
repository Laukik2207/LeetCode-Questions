class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        cr = 0

        for c in s:
            if c == '(':
                cr+=1
                if cr > mx:
                    mx = cr
            elif c == ')':
                cr -= 1
        return mx