# link   : https://leetcode.com/problems/01-matrix/description/
# author : Mohamed Ibrahim

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n , m = len(mat),len(mat[0])

        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    top = mat[i-1][j] if i-1 >= 0 else float('inf')
                    left = mat[i][j-1] if j-1 >=0 else float('inf')
                    mat[i][j] = 1+min(top , left) 
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if mat[i][j] != 0:
                    bottom = mat[i+1][j] if i+1 < n else float('inf')
                    right = mat[i][j+1] if j+1 < m else float('inf')
                    mat[i][j] = min(1+min(right,bottom) , mat[i][j]  )
        return mat
      
