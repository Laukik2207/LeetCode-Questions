class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = []

        def back(s,curr):
            if len(curr) == k:
                l.append(curr[:])
                return
            
            for i in range(s,n+1):
                curr.append(i)
                back(i+1,curr)
                curr.pop()
        back(1,[])
        return l