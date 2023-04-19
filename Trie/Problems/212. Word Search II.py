# link   : https://leetcode.com/problems/word-search-ii/description/
# author : Mohamed Ibrahim

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        n , m = len(board) , len(board[0])
        res = set()

        def dfs(r , c, node,path):
            if  (r < 0 or c < 0 or 
                r == n or c == m or
                board[r][c] == '#' or board[r][c] not in node.children):return 

            visited.add((r,c))
            path+=board[r][c]
            node = node.children[board[r][c]]
            if node.isWord:
                res.add(path)
                if len(node.children) == 0:
                    del node

            temp = board[r][c]
            board[r][c] = '#'

            dfs(r + 1 , c, node,path)
            dfs(r - 1 , c, node,path)
            dfs(r , c + 1, node,path)
            dfs(r , c - 1, node,path)

            board[r][c] = temp
        
        for i in range(n):
            for j in range(m):
                dfs(i , j, root,"")
        return list(res)
        
