# link   : https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# author : Mohamed Ibrahim

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])
        Pacific,Atlantic  = set(),set()
        def dfs(i , j,visited,PrevHeight):
            if ((i,j) in visited or 
                i < 0 or i == n or 
                j < 0 or j == m or
                heights[i][j] < PrevHeight
                ): return
            visited.add((i,j))
            dfs(i + 1 , j,visited,heights[i][j])
            dfs(i -1 , j,visited,heights[i][j])
            dfs(i , j + 1,visited,heights[i][j])
            dfs(i , j - 1,visited,heights[i][j])
        
        for i in range(n):
            dfs(i , 0,Pacific,-1)
            dfs(i , m-1,Atlantic,-1)
        for i in range(m):
            dfs(0 , i,Pacific,-1)
            dfs(n-1 , i,Atlantic,-1)
        res = []
        for i in range(n):
            for j in range(m):
                if (i,j) in Pacific and (i,j) in Atlantic :
                    res.append([i,j])
        return res
        
