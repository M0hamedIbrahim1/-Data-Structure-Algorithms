# link   : https://leetcode.com/problems/number-of-islands/
# author : Mohamed Ibrahim

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows , cols = len(grid),len(grid[0])

        def Islands(row,col):
            if row not in range(rows) or col not in range(cols):
                return
            if grid[row][col] != "1":
                return 

            grid[row][col] = "0"

            Islands(row + 1 , col)
            Islands(row - 1 , col)
            Islands(row , col + 1)
            Islands(row , col - 1)

        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    cnt+=1
                    Islands(i,j)
        return cnt
        
        
