# link   : https://leetcode.com/problems/longest-common-subsequence/description/
# author : Mohamed Ibrahim

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def resc(i,j):
            if (i,j) in cache:return cache[(i,j)]
            if i == 0 or j == 0:
                return 0
            elif text1[i-1] == text2[j-1]:
                cache[(i,j)] = 1+resc(i-1 , j-1)
                return cache[(i,j)]
            else:
                cache[(i,j)] = max(
                    resc(i-1 , j),
                    resc(i , j-1)
                )
                return cache[(i,j)]
        return resc(len(text1) , len(text2))

      
