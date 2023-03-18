# link   : https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# author : Mohamed ibrahim

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x,y,w in roads:
            graph[x].append((y,w))            
            graph[y].append((x,w))
        visited = set()
        mn = inf
        def dfs(node):
            nonlocal mn
            visited.add(node)
            for n,d in graph[node]:
                mn = min(mn,d)
                if n not in visited:
                    dfs(n)
        dfs(1)
        return mn
        
