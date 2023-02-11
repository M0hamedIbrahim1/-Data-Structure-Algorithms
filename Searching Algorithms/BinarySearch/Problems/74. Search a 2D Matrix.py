# link   : https://leetcode.com/problems/search-a-2d-matrix/description/
# author : Mohamed Ibrahim



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            left,right = 0 , m-1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] == target : 
                    return True
                elif matrix[i][mid] > target:
                    right = mid-1
                else:
                    left = mid+1
        return False
        
        
