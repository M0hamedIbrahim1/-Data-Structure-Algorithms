# link   : https://leetcode.com/problems/squares-of-a-sorted-array/
# author : Mohamed Ibrahim



class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = [None]*len(nums)
        left , right = 0 , len(nums)-1

        for index in range(len(nums)-1 , -1 ,-1):
            if abs(nums[left]) > abs(nums[right]):
                lst[index] = abs(nums[left])**2
                left+=1
            else:
                lst[index] = abs(nums[right])**2
                right-=1
        return lst
