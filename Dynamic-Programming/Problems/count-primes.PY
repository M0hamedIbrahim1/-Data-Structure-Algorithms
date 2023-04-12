# link   : https://leetcode.com/problems/count-primes/
# author : Mohamed Ibrahim

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False

        for i in range(2 , int(n ** 0.5)+1):
            if dp[i]:
                dp[i*i : n : i] = [False]*(len(dp[i*i : n : i]))
        return sum(dp)
        
