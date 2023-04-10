# link   : https://leetcode.com/problems/maximum-subarray/description/
# author : Mohamed Ibrahim

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[-1] = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            if nums[i]+dp[i+1] > 0:
                dp[i] = max(nums[i],nums[i]+dp[i+1])
            else:
                dp[i] = nums[i]
        return max(dp)
        
        
