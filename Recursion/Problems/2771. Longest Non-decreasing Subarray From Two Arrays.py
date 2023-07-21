# link   : https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/description/
# author : Mohamed Ibrahim
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dfs(i , prev):
            if i == len(nums1) : return 0
            res = 0
            if prev <= nums1[i]:
                res = max(res , 1 + dfs(i+1 , nums1[i]))

            if prev <= nums2[i]:
                res = max(res , 1 + dfs(i+1 , nums2[i]))



            return res
        ans = 0
        for i in range(len(nums1)):
            ans = max(ans , dfs(i , float("-inf")))
        return ans
