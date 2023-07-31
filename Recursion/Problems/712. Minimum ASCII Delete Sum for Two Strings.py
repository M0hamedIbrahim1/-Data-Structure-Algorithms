# link : https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/ 
# author : Mohamed Ibrahim

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        cache = {}
        def dfs(i , j):
            if (i , j) in cache:return cache[(i , j)]
            if i < 0 :
                cost = 0
                for k in range(j+1):
                    cost+=ord(s2[k])
                return cost
            if j < 0 : 
                cost = 0
                for k in range(i+1):
                    cost+=ord(s1[k])
                return cost
            if s1[i] == s2[j]:
                return dfs(i-1 , j-1)
            else:
                mn = min(
                
                    ord(s1[i]) + dfs(i - 1 , j),
                    ord(s2[j]) + dfs(i , j - 1),
                    ord(s1[i]) + ord(s2[j]) + dfs(i - 1 , j - 1)
                
                )
                cache[(i , j)] = mn
                return mn

        return dfs(len(s1)-1 , len(s2)-1)
