# link   : https://leetcode.com/problems/flood-fill/description/
# author : Mohamed Ibrahim

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n , m = len(image) , len(image[0])
        visited = set()
    

        def dfs(i , j , COLOR):
            if( i < 0 or i == n or
               j < 0 or j == m or
               (i , j) in visited or
               image[i][j] != COLOR
               ):
                    return 

            image[i][j] = color
            visited.add((i,j))
            dfs(i + 1 , j , COLOR)
            dfs(i - 1 , j , COLOR)
            dfs(i , j + 1 , COLOR)
            dfs(i , j - 1 , COLOR)
        
        dfs(sr , sc ,image[sr][sc])
        return image
        
