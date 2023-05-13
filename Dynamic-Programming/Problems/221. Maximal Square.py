# link   : https://leetcode.com/problems/maximal-square/description/
# author : Mohamed Ibrahim

class Solution:
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		max_val = 0
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				matrix[i][j]=int(matrix[i][j])
				if matrix[i][j] and i and j:
					matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
				max_val = max(max_val,matrix[i][j])
		return len(matrix) and max_val ** 2
    
