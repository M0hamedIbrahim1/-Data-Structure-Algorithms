# link   : https://leetcode.com/problems/combination-sum/description/
# author : Mohamed Ibrahim

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,n = [],len(candidates)

        def dfs(indx , path , cur_sum):
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(path)

            for i in range(indx , n):
                dfs(i , path+[candidates[i]] , cur_sum+ candidates[i])
        dfs(0 , [] , 0)
        return res
        
        
