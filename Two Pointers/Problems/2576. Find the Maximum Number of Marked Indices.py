# link   : https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/description/
# author : Mohamed Ibrahim

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        j = n-1

        ans = 0
        for i in range((n//2) -1 , -1 , -1):
            if nums[i]*2 <= nums[j]:
                ans+=2
                j-=1
        return ans
