# link   : https://leetcode.com/problems/longest-increasing-subsequence/
# author : Mohamed ibrahim

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i == n-1:
                return 1
            
            r1 = 1 

            for j in range(i+1 , n):
                if nums[j] > nums[i]:
                    r1 = max(r1 , 1 + dfs(j))
            
            return r1

        res = 1
        for i in range(n):
            res = max(res , dfs(i))
        return res
