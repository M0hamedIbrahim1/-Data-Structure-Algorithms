# link : https://leetcode.com/contest/weekly-contest-332/problems/count-the-number-of-fair-pairs/
# author : Mohamed Ibrahim

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        left , right = 0 , len(nums)-1
        res = 0
        while left < right:
            if nums[left]+nums[right] <= upper:
                res+=right - left
                left+=1
            else:
                right-=1
        left , right = 0 , len(nums)-1
        while left < right:
            if nums[left]+nums[right] < lower:
                res-= right-left
                left+=1
            else:
                right-=1
        return res        
    
        
