# link   : https://leetcode.com/problems/last-day-where-you-can-still-cross/description/
# author : Mohamed Ibrahim

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(1,0) , (-1,0) , (0,1) , (0,-1)]

        def check(day):
            grid = [[0]*col for i in range(row)] 

            for X,Y in cells[:day]:
                grid[X-1][Y-1] = 1
            def dfs(r , c):
                if r == row-1:
                    return True
                grid[r][c] = 1
                for x , y in directions:
                    if 0 <= x+r < row and 0 <= y+c < col and grid[x+r][y+c]!=1 :
                        if dfs(x+r , y+c):return True
                return False
            for i in range(col):
                if grid[0][i] != 1 and dfs(0 , i ):
                    return True
            return False
                    
        left, right = 1, row * col
        while left < right:
            mid = right - (right - left) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1
                
        return left
