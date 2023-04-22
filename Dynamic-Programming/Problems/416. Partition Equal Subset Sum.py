# link   : https://leetcode.com/problems/partition-equal-subset-sum/description/
# author : Mohamed Ibrahim

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 : return False
        target = sum(nums) / 2

        dp = set()
        dp.add(0)

        for n in nums:
            temp = set()
            for i in dp:
                temp.add(i+n)
                temp.add(i)
            dp = temp
        return True if target in dp else False
            
            
