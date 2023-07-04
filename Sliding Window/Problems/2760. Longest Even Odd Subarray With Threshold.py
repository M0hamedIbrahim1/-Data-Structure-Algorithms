# link   : https://leetcode.com/contest/weekly-contest-352/problems/longest-even-odd-subarray-with-threshold/
# author : Mohamed Ibrahim


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        i = 0
        res , cnt = 0,0
        while i < len(nums):
            cnt = 0
            if nums[i] <= threshold and nums[i]%2 == 0:
                cnt=1
                j = i+1
                while j < len(nums) and nums[j]%2 != nums[j-1]%2 and nums[j] <= threshold:
                    cnt+=1
                    j+=1
                res = max(cnt , res)
                i = j-1
            i+=1
        return res
