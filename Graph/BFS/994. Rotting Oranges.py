# link : https://leetcode.com/problems/rotting-oranges/description/
# author : Mohamed Ibrahim

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        d = deque()
        level,fresh = 0,0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    d.append((i , j))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while d:
            for i in range(len(d)):
                r , c = d.popleft()
                for x,y in directions:
                    if r+x < 0 or r+x == n or c+y < 0 or c+y == m or grid[r+x][c+y] != 1:
                        continue
                    grid[r+x][c+y] = 2
                    d.append((r+x , c+y))
                    fresh-=1
            level+=1
        return -1 if fresh != 0 else max(level-1 , 0)

      
