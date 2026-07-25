from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort (value, original_index)
        arr = sorted((v, i) for i, v in enumerate(nums))

        # pos[original_index] = position in sorted array
        pos = [0] * n
        values = [0] * n
        for i, (v, idx) in enumerate(arr):
            values[i] = v
            pos[idx] = i

        # next_pos[i] = farthest position reachable in one edge
        next_pos = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and values[j + 1] - values[i] <= maxDiff:
                j += 1
            next_pos[i] = j

        LOG = 18  # 2^17 > 1e5

        # Binary lifting table
        up = [[0] * n for _ in range(LOG)]
        up[0] = next_pos[:]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            if next_pos[l] == l:
                ans.append(-1)
                continue

            steps = 0
            cur = l

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    steps += 1 << k

            if next_pos[cur] >= r:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans
        