# link   : https://leetcode.com/contest/weekly-contest-342/problems/sliding-subarray-beauty/
# author : Mohamed Ibrahim

from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        lst = SortedList()
        ans = []
        
        for indx , num in enumerate(nums):
            lst.add(nums[indx])
            if indx >= k:lst.remove(nums[indx-k])
            if indx >= k-1:ans.append(min(0,lst[x-1]))
        return ans
      
