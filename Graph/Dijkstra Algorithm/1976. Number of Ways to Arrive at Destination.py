# link   : https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
# author : Mohamed Ibrahim


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
            
        times = [float('inf')] * n
        ways = [0] * n
        
        times[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            old_t, u = heapq.heappop(pq)
            
            for v, t in graph[u]:
                new_t = old_t + t
                
                if new_t < times[v]:
                    times[v] = new_t
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_t, v))
                
                elif new_t == times[v]:
                    ways[v] += ways[u]
                
        modulo = 10 ** 9 + 7
        
        return ways[n-1] % modulo
        
