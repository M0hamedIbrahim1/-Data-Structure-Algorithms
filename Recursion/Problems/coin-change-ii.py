# link : https://leetcode.com/problems/coin-change-ii/
author : Mohamed Ibrahim

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(total , i):
            if total == amount : return 1
            if i == len(coins) or total > amount:return 0
            res = 0
            for j in range((amount - total) // coins[i] + 1):
                res += dfs(total + coins[i]*j , i+1)
            return res
        mx = max(coins)
        return dfs(0 , 0)
