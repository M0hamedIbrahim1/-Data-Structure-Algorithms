# link   : https://leetcode.com/problems/perfect-squares/description/
# author : Mohamed Ibrahim


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")]*(n+1)
        dp[0] = 0

        for i in range(n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i] , dp[i - j*j] + 1)
                j+=1
        return dp[n]
        
        
        
