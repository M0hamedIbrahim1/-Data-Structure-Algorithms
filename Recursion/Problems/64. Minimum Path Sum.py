# link : https://leetcode.com/problems/minimum-path-sum/
# author : Mohamed Ibrahim

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        cache = {}
        def resc(i , j):
            if i >= n or j >= m:
                return float('inf')
            if (i,j) in cache: 
                return cache[(i , j)]
            if i == n-1 and j == m-1:
                return grid[i][j]
            cache[(i , j)] = grid[i][j] + min(resc(i+1 , j) , resc(i , j+1))
            return cache[(i , j)]
        return resc(0,0)
      
      
