# Link   : https://leetcode.com/problems/unique-paths/description/
# Author : Mohamed Ibrahim

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1]*n]*m

        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
        return matrix[m-1][n-1]
        
        
