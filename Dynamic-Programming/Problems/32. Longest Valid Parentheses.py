# link   : https://leetcode.com/problems/longest-valid-parentheses/description/
# author : Mohamed Ibrahim

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mx = 0
        s =')' + s 
        dp = [0]*len(s)

        for i in range(1,len(s)):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = dp[i-2] + 2

            elif s[i] == ')' and s[i-1] == ')':
                if s[i - dp[i-1] - 1 ] == '(':
                    dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
            mx = max(dp[i] , mx)
        return mx
      
