# link   : https://leetcode.com/problems/maximal-network-rank/description/
# author : Mohamed Ibrahim

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        self.mx = 0
        for x, y in roads:
            graph[x].add(y)
            graph[y].add(x)


        def dfs(node1 , node2):
            if node2 in graph[node1]:
                return len(graph[node1]) + len(graph[node2]) - 1
            return len(graph[node1]) + len(graph[node2])

        for i in range(n):
            for j in range(i+1 , n):
                self.mx = max(self.mx , dfs(i , j))
        return self.mx  
