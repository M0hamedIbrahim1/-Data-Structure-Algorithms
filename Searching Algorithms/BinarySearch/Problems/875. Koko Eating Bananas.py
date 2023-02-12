# link   : https://leetcode.com/problems/koko-eating-bananas/description/
# author : Mohamed Ibrahim


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        if len(piles) == h:
            return mx
        left,right = 1,mx
        res = mx
        while left <= right:
            mid = (left+right) // 2
            k = 0
            for i in piles:
                k+=ceil(i/mid)
            if k <= h: 
                res = min(res,mid)
                right = mid-1
            else:
                left = mid+1
        return res
        
        
