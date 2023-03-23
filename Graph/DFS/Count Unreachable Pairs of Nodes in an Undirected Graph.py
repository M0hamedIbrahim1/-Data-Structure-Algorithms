# link : https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
# author : Mohamed Ibrahim


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node,visited):
            if visited[node]:
                return
            visited[node] = 1
            self.cnt+=1

            for nei in graph[node]:
                dfs(nei,visited)

        visited = [0]*n
        totalnodes = 0
        res = 0
        for i in range(n):
            if not visited[i]:
                self.cnt = 0
                dfs(i,visited)
                res+=self.cnt*totalnodes
                totalnodes+=self.cnt
        return res
        
