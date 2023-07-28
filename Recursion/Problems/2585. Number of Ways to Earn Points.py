# link   : https://leetcode.com/problems/number-of-ways-to-earn-points/description/
# author : Mohamed Ibrahim

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        @cache
        def dfs(total , i):
            if total == target : return 1
            if total > target or i == len(types):return 0
            
            res = 0 
            for j in range(types[i][0]+1):
                res+=dfs(total + types[i][1]*j , i+1)
            return res % (10**9 + 7)


        return dfs(0 , 0)
