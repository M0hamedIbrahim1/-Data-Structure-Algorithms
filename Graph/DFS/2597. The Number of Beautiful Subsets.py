# link : https://leetcode.com/problems/the-number-of-beautiful-subsets/description/
# author : Mohamed Ibrahim

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.cnt = 0
        nums.sort()
        def dfs(ind , path):
            if ind == len(nums) and len(path) >= 1:
                self.cnt += 1
                return
            if ind == len(nums):
                return 0
            
            dfs(ind+1 , path)
            if nums[ind]-k not in path:
                dfs(ind +1 , path + [nums[ind]])
            
        dfs(0 , [])
        return self.cnt
