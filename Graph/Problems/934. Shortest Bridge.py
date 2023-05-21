# link   : https://leetcode.com/problems/shortest-bridge/description/
# author : Mohamed Ibrahim
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island = []
        
        def dfs(row,col):
            grid[row][col] = 2
            island.append((row,col,0))
            moves = ((row+1,col),(row-1,col),(row,col+1),(row,col-1))
            for x,y in moves:
                if 0<=x<n and 0<=y<n and grid[x][y] == 1:
                    dfs(x,y)
        
        flag = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    flag = False
                    break
            if not flag:break
                
        queue = island
        while queue:
            r,c,dis = queue.pop(0)
            if grid[r][c] == 1:return dis
            moves = ((r+1,c),(r-1,c),(r,c-1),(r,c+1))
            for x,y in moves:
                if 0<=x<n and 0<=y<n and grid[x][y]!=2:
                    if grid[x][y] == 1:return dis
                    grid[x][y] = 2
                    queue.append((x,y,dis+1))
        return -1
