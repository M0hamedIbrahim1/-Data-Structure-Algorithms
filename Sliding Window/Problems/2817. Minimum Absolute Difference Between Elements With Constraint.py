# link   : https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/description/
# author : Mohamed Ibrahim

from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        s = SortedList()
        res = float('inf')

        for i in range(x, n):
            s.add(nums[i])
        for i in range(n):
            if i+x < n:
                r = s.bisect_right(nums[i])
                if r < len(s):
                    res = min(res, abs(s[r]-nums[i]))
                if r-1 >= 0:
                    res = min(res, abs(s[r-1]-nums[i]))
                s.remove(nums[i+x])
        return res
            
            

