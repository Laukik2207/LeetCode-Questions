class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapp = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for ch in s:
            if ch not in mapp : 
                stack.append(ch)
            else:
                if not stack:
                    return False

                if stack.pop() != mapp[ch]:
                    return False
        return not stack