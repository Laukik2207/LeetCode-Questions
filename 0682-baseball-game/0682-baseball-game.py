class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a = []

        for i in operations:
            if i == 'C':
                a.pop()
            elif i == 'D':
                a.append(2*a[-1])
            elif i == '+':
                a.append(a[-2] + a[-1])
            else:
                a.append(int(i))
        return sum(a)