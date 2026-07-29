class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans = ""
        len1 = len(word1)
        len2 = len(word2)
        while(i < len1 or i < len2):
            if(i < len1):
                ans+=word1[i]
            if(i < len2):
                ans+=word2[i]
            i+=1
        return ans