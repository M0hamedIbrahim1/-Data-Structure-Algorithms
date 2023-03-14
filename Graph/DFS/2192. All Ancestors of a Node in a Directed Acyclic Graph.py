# link   : https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
# author : Mohamed Ibrahim

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for x,y in edges:
            graph[y].append(x)

        def dfs(root,node):
            visited[root] = 1
            for i in graph[root]:
                if visited[i] == 0:
                    ans[node].add(i)
                    dfs(i,node)

        ans = [set() for _ in range(n)]
        for i in range(n):
            visited = [0]*n
            dfs(i,i)
        return [sorted(row) for row in ans]


