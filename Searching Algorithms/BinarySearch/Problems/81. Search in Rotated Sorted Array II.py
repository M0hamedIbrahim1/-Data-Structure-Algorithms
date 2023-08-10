# link   : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
# author : Mohamed Ibrahim

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l , r = 0 , len(nums)-1


        while l <= r :
            m = (l+r) // 2

            if nums[m] == target:
                return True


            if nums[l] == nums[m]:
                l += 1
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m+1

            else:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
                        
        return False
