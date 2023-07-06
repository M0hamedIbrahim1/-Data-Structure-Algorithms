# link   : https://leetcode.com/problems/minimum-size-subarray-sum/description/
# author : Mohamed Ibrahim

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r , s = 0 , 0 , 0
        res = float('inf')
        if target in nums:return 1
        while r < len(nums):
            s+=nums[r]
            while s >= target:
                res = min(res , r+1 - l)
                s-=nums[l]
                l+=1

            r+=1
        return res if res != float('inf') else 0 
