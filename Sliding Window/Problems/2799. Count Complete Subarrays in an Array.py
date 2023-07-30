# link   : https://leetcode.com/problems/count-complete-subarrays-in-an-array/
# author : Mohamed Ibrahim

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c=len(set(nums))
        n=len(nums)
        res=0
        for i in range(n):
            seen=set()
            for j in range(i,n):
                seen.add(nums[j])
                if(len(seen)==c):
                    res+=1
        return res
