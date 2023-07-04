# link   : https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/description/
# author : Mohamed Ibrahim


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        
        ans = 0
        
        for i,start in enumerate(nums):
            d = {}
            d[start] = 1
            cnt = 0
            
            for j in range(i+1, len(nums)):
                n = nums[j]
                if n in d:
                    pass
                else:
                    if n+1 in d and n-1 in d:
                        cnt -= 1
                    elif n+1 not in d and n-1 not in d:
                        cnt += 1
                d[n] = 1
                ans += cnt
                print(nums[i] , ans)
        
        return ans

