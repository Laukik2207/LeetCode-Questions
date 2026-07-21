class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        prev_zero = float('-inf')
        maxgain = 0

        n = len(s)
        i = 0

        while i < n:
            j = i
            while j<n and s[i] == s[j]:
                j += 1
            length = j-i

            if s[i] == '0':
                maxgain = max(maxgain, prev_zero + length)
                prev_zero = length
            i = j
        return ones + maxgain