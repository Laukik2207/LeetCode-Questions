class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split()
        n = len(text)
        i = 0
        l = n-1
        while i < l:
            t = text[i]
            text[i] = text[l]
            text[l] = t
            i += 1
            l -= 1

        return " ".join(text)