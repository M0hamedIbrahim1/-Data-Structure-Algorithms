# Link   : https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
# Author : Mohamed Ibraihm


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights),sum(weights)
        while left <= right:

            mid,summ,cnt = (left+right) // 2,0,1 
            for c in weights:
                if c+summ > mid:
                    cnt+=1
                    summ =0
                summ+=c
            if cnt > days : left = mid+1
            else:right = mid-1
        return left
        
        
        
        
