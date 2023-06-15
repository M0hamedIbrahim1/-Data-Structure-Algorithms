# link   : https://leetcode.com/problems/movement-of-robots/description/
# author : Mohamed Ibrahim

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums) 
        for i in range(n):
            if s[i] == 'R':
                nums[i]+=d
            else:
                nums[i]-=d
        s , ans = 0,0
        mod = 10 ** 9 + 7

        nums.sort()
        for i in range(n):
            ans+= (nums[i]*i - s)
            s+=nums[i]
            ans %= mod
            s %= mod
        return ans

