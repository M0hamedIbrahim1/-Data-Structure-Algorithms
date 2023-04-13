# link   : https://leetcode.com/problems/decode-ways/description/
# author : Mohamed Ibrahim

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s :
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2 , n + 1):
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] = dp[i-2]
            if 1 <= int(s[i-1:i]) <= 9:
                dp[i]+=dp[i-1]
        return dp[n]

