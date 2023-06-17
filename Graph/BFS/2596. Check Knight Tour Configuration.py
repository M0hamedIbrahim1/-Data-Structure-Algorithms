# link   : https://leetcode.com/contest/weekly-contest-337/problems/check-knight-tour-configuration/
# author : Mohamed Ibrahim
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0 : return False
        n,m ,cnt= len(grid) , len(grid[0]),1
        deq = collections.deque()
        deq.append((0,0,0))
        directions = [(1,2) , (-1,2) , (1,-2) , (-1,-2) , (2,1) , (2,-1) , (-2,1) , (-2,-1)]
        flag = False
            
        while deq:
            r , c , d = deq.popleft()
            if grid[r][c] == n*m - 1:return True
            for x,y in directions:
                if x+r >= 0 and x+r < n  and c+y >= 0 and  c+y < m:
                    if grid[x+r][c+y] == d+1:
                        deq.append((x+r , c+y , d+1))
                        flag = True
                        
            if not flag:return False
            flag = False

