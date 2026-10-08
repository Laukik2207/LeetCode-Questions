class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        depth = 0

        for c in s:
            if c == '(':
                if depth > 0:
                    ans += c
                depth += 1

            else:
                depth -= 1
                if depth > 0:
                    ans += c

        return ans