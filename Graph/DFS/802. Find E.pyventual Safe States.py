# link   : https://leetcode.com/problems/find-eventual-safe-states/description/
# author : Mohamed Ibrahim


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        visited = [-1] * n
        def dfs(i):
            if visited[i] == 0:return False
            if visited[i] == 1:return True
            visited[i] = 0
            for node in  graph[i]:
                if not dfs(node):
                    return False
            visited[i] = 1
            return True
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
        
