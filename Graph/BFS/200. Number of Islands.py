# link   : https://leetcode.com/problems/number-of-islands/description/
# author : Mohamed Ibrahim

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0]) 
        visited = set()
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visited.add((i,j))
            while q:
                row,col = q.popleft()
                dir = [(1,0),(-1,0),(0,-1),(0,1)]
                for x,y in dir:
                    if row+x in range(rows) and col+y in range(cols):
                        if grid[row+x][col+y] == "1" and (row+x , col+y) not in visited:
                            q.append((row+x , col+y))
                            visited.add((row+x , col+y))
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i,j)
                    cnt+=1
        return cnt
      
      
