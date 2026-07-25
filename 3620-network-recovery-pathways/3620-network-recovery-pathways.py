from collections import defaultdict
from heapq import heappush, heappop
from math import inf

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        graph = defaultdict(list)

        low = float("inf")
        high = 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue

            graph[u].append((v, w))
            low = min(low, w)
            high = max(high, w)

        if low == float("inf"):
            return -1

        def check(mid):
            dist = [inf] * n
            dist[0] = 0

            pq = [(0, 0)]      # (cost, node)

            while pq:
                cost, u = heappop(pq)

                if cost > dist[u]:
                    continue

                if cost > k:
                    continue

                if u == n - 1:
                    return True

                for v, w in graph[u]:
                    if w < mid:
                        continue

                    new_cost = cost + w

                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        heappush(pq, (new_cost, v))

            return False

        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans