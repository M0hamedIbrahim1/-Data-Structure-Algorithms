# link : https://leetcode.com/problems/longest-alternating-subarray/description/
# author : Mohamed Ibrahim

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            p = 1
            for j in range(i+1 , len(nums)):
                
                if nums[j] - nums[j-1] != p:break
                res = max(res , j+1 -i)
                p = p * -1
        return res
