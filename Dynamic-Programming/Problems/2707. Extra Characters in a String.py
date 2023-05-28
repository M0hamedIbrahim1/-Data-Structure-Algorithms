# link : https://leetcode.com/problems/extra-characters-in-a-string/description/
# author : Mohamed Ibrahim

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        n = len(s)+1
        dp = [0]*n

        for i in range(1,n):
            dp[i] = dp[i-1]+1
            for j in range(i-1 , -1 , -1):
                substring = s[j:i]
                if substring in dictionary :
                    dp[i] = min(dp[i] , dp[j])
        return dp[n-1]
        
