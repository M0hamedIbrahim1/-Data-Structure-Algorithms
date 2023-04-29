# link   : https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/
# author : Mohamed ibrahim

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        directions = [(1 , 0) ,(-1 , 0) ,(0 , 1) ,(0 , -1)]
        def dfs(i , j):
            if( i < 0 or i == n or 
               j < 0 or j == m or
               grid[i][j] == 0): return 0

            fish = grid[i][j]
            grid[i][j] = 0
            for x,y in directions:
                fish+=dfs(i+x , y+j)
            return fish


        mx = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    
                    mx = max(mx , dfs(i , j))
        return mx
        
