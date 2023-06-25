# link   : https://leetcode.com/problems/count-all-possible-routes/description/ 
# author : Mohamed Ibrahim

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        def dfs(indx , cur_fuel):
            if cur_fuel < 0 :
                return 0
            if (indx , cur_fuel) in dp:
                return dp[(indx , cur_fuel)]
            ans = 0    
            if indx == finish:
                ans = 1
            for i in range(len(locations )):
                if i != indx:
                    ans=( ans+dfs(i , cur_fuel - abs(locations[indx] - locations[i]))) % 1000000007
            dp[(indx , cur_fuel) ] = ans
            return ans
        return dfs(start , fuel)
