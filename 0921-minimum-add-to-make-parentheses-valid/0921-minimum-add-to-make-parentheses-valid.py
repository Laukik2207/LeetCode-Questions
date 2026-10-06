class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        oc = 0
        m = 0
        for c in s:
            if c == '(':
                oc+=1
            else:
                if oc > 0:
                    oc-=1
                else:
                    m+=1
        return oc+m