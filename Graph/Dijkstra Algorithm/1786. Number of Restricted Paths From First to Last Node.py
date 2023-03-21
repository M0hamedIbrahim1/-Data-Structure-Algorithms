# link   : https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
# author : Mohamed ibrahim

from queue import PriorityQueue

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(dict)
        
        for u, v, w in edges: # create adjacency list
            g[u][v] = w
            g[v][u] = w
        
        def dijkstras(start): # calculate shortests paths
            d = {v: float('inf') for v in range(1, n+1)}
            d[start] = 0
            q = PriorityQueue()
            q.put((0, start))
            
            while not q.empty():
                u = q.get()[1]
                
                for v in g[u]:
                    if d[u] + g[u][v] < d[v]:
                        d[v] = d[u] + g[u][v]
                        q.put((d[v], v))
            
            return d
            
        d = dijkstras(n)
        seen = set()
        
        @cache
        def dfs(node):
            if node == n:
                return 1
            
            seen.add(node)
            count = 0
            for neighbor in g[node].keys():
                if d[neighbor] < d[node] and neighbor not in seen:
                    count += dfs(neighbor)
            seen.discard(node)
            return count
       
        return dfs(1) % (10**9 + 7)
        
        
