# link   : https://leetcode.com/problems/unique-paths-ii/description/
# author : Mohamed Ibrahim

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n , m = len(obstacleGrid),len(obstacleGrid[0])
        @cache
        def dfs(i , j):
            if i == n or j == m:return 0
            if obstacleGrid[i][j]:return 0
            if i == n-1 and j == m-1:return 1
            res = 0
            for x,y in [(1 , 0) , (0 , 1)]:
                res += dfs(x + i ,y + j)

            return res

        return dfs(0 , 0)


