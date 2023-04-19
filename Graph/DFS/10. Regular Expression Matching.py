# link   : https://leetcode.com/problems/regular-expression-matching/description/
# author : Mohamed Ibrahim

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        Len_S , Len_P = len(s) , len(p)
        cache = {}
        def dfs(i , j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= Len_S and j >= Len_P:
                return True

            if j >= Len_P:
                return False

            match = i < Len_S and( s[i] == p[j] or p[j] == '.')
            if j+1 < Len_P and p[j+1] == '*':
                cache[(i,j)] =  (dfs(i , j+2) or           # don't use *
                                (match and dfs(i+1 , j)))  # use *
                return cache[(i,j)]
            if match:
                cache[(i,j)] =  dfs(i+1 , j+1)
                return cache[(i,j)]
            return False
        return dfs(0,0)


