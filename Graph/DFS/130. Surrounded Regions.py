# Link   : https://leetcode.com/problems/surrounded-regions/description/
# author : Mohamed Ibrahim

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n , m = len(board) , len(board[0])
        def DFS(i , j):
            if (
                 i < 0 or j < 0 or
                 i == n or j == m or
                 board[i][j] != "O"
            ):return
            
            board[i][j] = "T"
            DFS(i + 1 , j)
            DFS(i - 1, j)
            DFS(i , j + 1)
            DFS(i , j - 1)

        for i in range(n):
            for j in range(m):
                if (board[i][j] == 'O' and (i in [0 , n-1] or j in [0,m-1])):
                    DFS(i , j)
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(n):
            for j in range(m):
                if board[i][j] == "T":
                    board[i][j] = "O"  
                    
