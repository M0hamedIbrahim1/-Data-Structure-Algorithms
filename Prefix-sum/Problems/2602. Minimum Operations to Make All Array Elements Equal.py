# link : https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/description/
# author : Mohamed Ibrahim

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans , prefix = [] , [0]
        n = len(nums)
        for num in nums:
            prefix.append(prefix[-1]+num)
        for i in range(len(queries)):
            indx = bisect.bisect_left(nums , queries[i] )
            first_half = queries[i] * indx
            first_half-= prefix[indx] 

            sec_half = prefix[-1] - prefix[indx]
            sec_half-= (queries[i] * (n - indx))
            ans.append(sec_half + first_half)
        return ans
