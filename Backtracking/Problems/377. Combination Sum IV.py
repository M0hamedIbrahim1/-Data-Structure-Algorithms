# link   : https://leetcode.com/problems/combination-sum-iv/description/
# author : Mohamed Ibrahim
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        return self.dfs(nums, target, dp)
        
    def dfs(self,nums , target , dp):
        if target < 0 :
            return 0
        if target == 0:
            return 1
        if target in dp:
            return dp[target]
        
        res = 0
        for n in nums:
            res+=self.dfs(nums , target - n , dp)
        dp[target] = res
        return res
