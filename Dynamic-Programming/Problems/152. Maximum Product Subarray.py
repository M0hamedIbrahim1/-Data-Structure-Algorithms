# Link   : https://leetcode.com/problems/maximum-product-subarray/description/
# author : Mohamed Ibrahim

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_Product = min_Product = res = nums[0]

        for i in range(1 , len(nums)):
            temp_max = max(nums[i] , nums[i] * max_Product ,nums[i] * min_Product)              
            min_Product = min(nums[i] , nums[i] * max_Product ,nums[i] * min_Product)

            max_Product = temp_max
            res = max(res , max_Product)
        return res
        
        
