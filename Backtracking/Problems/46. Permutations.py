# link   : https://leetcode.com/problems/permutations/description/
# author : Mohamed Ibrahim

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(arr, path):
            if not arr:
                res.append(path)
                return
            for i in range(len(arr)):
                dfs(arr[:i]+arr[i+1:], path+[arr[i]])
        dfs(nums, [])
        return res
      
      
