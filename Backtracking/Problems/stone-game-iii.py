# link : https://leetcode.com/problems/stone-game-iii/
# author : Mohaned Ibrahim

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = {}
        def dfs(indx):
            if indx == len(stoneValue) : 
                return 0 
            if indx in cache:
                return cache[indx]
            res = float('-inf') 

            for i in range(indx , min(indx+3 , len(stoneValue))):
                res = max(res , sum(stoneValue[indx : i+1]) - dfs(i+1) )
            cache[indx] = res
            return res

        val = dfs(0)
        if val > 0 : 
            return "Alice"
        elif val < 0 : 
            return "Bob"
        else:
            return "Tie"
            
