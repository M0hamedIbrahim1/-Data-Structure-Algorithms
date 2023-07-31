# link   : https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
# author : Mohamed ibrahim

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1

        r , c = len(grid) , len(grid[0])
        visited = set()
        heap = [(grid[0][0] , 0 , 0)]

        while heap:
            time , row , col = heapq.heappop(heap)
            if row == r-1 and col == c-1 : return time
            if (row , col) in visited : continue
            visited.add((row , col))
            for x , y in [(1 , 0) , (0 , 1) , (0 , -1) , (-1 , 0)]:
                if 0 <= x + row < r and 0 <= y + col < c and (x + row , y + col) not in visited:
                    wait = 1 if ((grid[row + x][col + y] - time) % 2 == 0) else 0
                    heappush(heap, (max(time + 1, grid[row+x][col+y] + wait), x + row,  col + y))

        
