# link : https://leetcode.com/contest/weekly-contest-342/problems/sliding-subarray-beauty/
# author : Mohamed Ibrahim

from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        s = SortedList()
        res = []
        for i in range(len(nums)):
            s.add(nums[i])
            if i >= k -1:
                res.append(min(s[x-1],0))
                s.discard(nums[(i+1 )-k])
        return res
