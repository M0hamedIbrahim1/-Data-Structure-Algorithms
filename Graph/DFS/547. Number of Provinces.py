# link   : https://leetcode.com/problems/number-of-provinces/description/
# author : Mohamed Ibrahim


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        def dfs(node):
            for c in graph[node]:
                if not visited[c]:
                    visited[c] = 1
                    dfs(c)

        cnt = 0 
        for i in range(n):
            if not visited[i]:
                cnt+=1
                visited[i] = 1
                dfs(i)
        return cnt
        
        
