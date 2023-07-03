# link : 
# author : Mohamed Ibrahim
class Solution:

    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        if 1 not in nums :
            return 0
        ind = nums.index(1)  

        cnt = 1 
        for i in range(ind + 1 , len(nums)) :
            if nums[i] == 1 :
                # i-ind gives the no of zeros between 2 1s                
                cnt = (cnt * (i-ind))%1000000007
                ind = i 
        return cnt
