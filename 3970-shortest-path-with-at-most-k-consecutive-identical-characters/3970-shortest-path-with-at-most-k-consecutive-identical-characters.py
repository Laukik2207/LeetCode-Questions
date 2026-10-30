import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Step 1: Build the adjacency list for the directed weighted graph
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Step 2: dist[u][c] stores the minimum cost to reach node 'u'
        # with exactly 'c' consecutive identical characters trailing.
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        
        # Step 3: Priority queue stores tuples of (cost, current_node, consecutive_count)
        # Starting at node 0, the first character counts as a run of 1.
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            cost, u, consec = heapq.heappop(pq)
            
            # If we reached the destination node, since it's a min-heap,
            # this is guaranteed to be the minimum valid path weight.
            if u == n - 1:
                return cost
                
            # Skip processing if we found a strictly better path to this exact state
            if cost > dist[u][consec]:
                continue
                
            for v, w in adj[u]:
                # Determine the new consecutive character count for neighbor v
                if labels[u] == labels[v]:
                    next_consec = consec + 1
                else:
                    next_consec = 1
                    
                # If the sequence violates the constraint, this path is invalid
                if next_consec > k:
                    continue
                    
                # Relaxation step
                if cost + w < dist[v][next_consec]:
                    dist[v][next_consec] = cost + w
                    heapq.heappush(pq, (cost + w, v, next_consec))
                    
        return -1
