# link   : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# author : Mohamed ibrahim

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(nums, target):
            l , r = 0 , len(nums) - 1
            while l <= r:
                mid = (l+r) // 2

                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def binarySearchRight(nums, target):
            l , r = 0 , len(nums) - 1
            while l <= r:
                mid = (l+r) // 2

                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
        LeftIndx = binarySearchLeft(nums, target)
        RightIndx = binarySearchRight(nums, target)

        if LeftIndx <= RightIndx:
            return [LeftIndx,RightIndx]
        else:
            return [-1,-1]
