from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        # Base case
        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        # Fill DP from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                best = -1
                cnt = 0

                # Down, Right, Diagonal
                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni >= n or nj >= n or score[ni][nj] == -1:
                        continue

                    if score[ni][nj] > best:
                        best = score[ni][nj]
                        cnt = ways[ni][nj]
                    elif score[ni][nj] == best:
                        cnt = (cnt + ways[ni][nj]) % MOD

                if best == -1:
                    continue

                val = 0 if board[i][j] in "SE" else int(board[i][j])

                score[i][j] = best + val
                ways[i][j] = cnt

        # If start is unreachable
        if score[0][0] == -1:
            return [0, 0]

        return [score[0][0], ways[0][0]]