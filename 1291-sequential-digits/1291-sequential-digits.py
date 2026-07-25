class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        for start in range(1, 10):
            num = start
            nxt = start + 1

            while nxt <= 9:
                num = num * 10 + nxt

                if low <= num <= high:
                    ans.append(num)

                nxt += 1

        ans.sort()
        return ans