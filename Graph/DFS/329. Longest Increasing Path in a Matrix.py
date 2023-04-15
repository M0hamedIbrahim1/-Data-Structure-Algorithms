# link   : https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# author : Mohamed Ibrahim

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N , C = len(matrix),len(matrix[0])
        dp = {}

        def dfs(row , col , prev_val):
            if (row < 0 or row >= N or
               col < 0 or col >= C or
               matrix[row][col] <= prev_val
               ): return 0
            if (row , col) in dp:
                return dp[(row , col)]
            
            res = 1
            res = max(res , 1 + dfs(row + 1 , col , matrix[row][col]))
            res = max(res , 1 + dfs(row - 1 , col , matrix[row][col]))
            res = max(res , 1 + dfs(row , col + 1 , matrix[row][col]))
            res = max(res , 1 + dfs(row , col - 1 , matrix[row][col]))
            dp[(row,col)] = res
            return res

        for i in range(N):
            for j in range(C):
                dfs(i , j , -1)
        return max(dp.values())
        
