class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 == 0 and grid[0][0] == '(' and grid[-1][-1] == ')':
            dp = [[set() for _ in range(n)] for _ in range(m)]
            dp[0][0].add(1)

            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        continue

                    change = 1 if grid[i][j] == '(' else -1

                    if i > 0:
                        for b in dp[i - 1][j]:
                            if b + change >= 0:
                                dp[i][j].add(b + change)

                    if j > 0:
                        for b in dp[i][j - 1]:
                            if b + change >= 0:
                                dp[i][j].add(b + change)

            return 0 in dp[-1][-1]

        return False