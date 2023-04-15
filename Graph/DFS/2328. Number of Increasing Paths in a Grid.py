# link   : https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/
# author : Mohamed Ibrahim

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        dp = [[0] * m for _ in range(n)]
        direction = [( 1 , 0) , ( -1 , 0 ) , (0 , + 1 ) , (0 , -1)]
        mod = 10 ** 9 + 7
        def dfs(i , j):
            if dp[i][j]:
                return dp[i][j]
            ans = 1
            for x,y in direction:
                if 0 <= x+i < n and 0 <= j+y < m and grid[i][j] < grid[x+i][j+y] :
                    ans+= dfs(x+i,j+y) % mod
            dp[i][j] = ans
            return ans
        return sum(dfs(i, j) for i in range(n) for j in range(m)) % mod
        
