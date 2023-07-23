# link   : https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/
# author : Mohamed Ibrahim

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        i , j = 0 , 0 
        while j < len(nums):
            if nums[j] - nums[i] > 2*k:
                i+=1
            j+=1

        return j-i
    
    
