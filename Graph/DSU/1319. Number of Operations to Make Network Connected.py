# link   : https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
# author : Mohamed Ibrahim


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            graph[i] = i
        def find(node):
            if graph[node] != node:
                graph[node] = find(graph[node])
            return graph[node]
        def union(u,v):
            parent_u = find(u)
            parent_v = find(v)
            if parent_u == parent_v:
                return True
            
            graph[parent_u] = parent_v
            return False
        cnt = 0

       		# redundant connections
        redun = sum(1 for i, j in connections if union(i, j))
		
		# number of connected components
        comp = sum(1 for i in range(n) if find(i) == i)
        
        return comp - 1 if redun >= comp - 1 else -1
        
        
