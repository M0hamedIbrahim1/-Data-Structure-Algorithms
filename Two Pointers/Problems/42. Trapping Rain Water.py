# link   : https://leetcode.com/problems/trapping-rain-water/description/
# author : Mohamed Ibrahim
class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height) - 1
        leftMax , RightMax = height[l] , height[r]
        res = 0
        while l < r :
            if height[l] <= height[r]:
                if height[l] < leftMax:
                    res+=leftMax-height[l]
                leftMax = max(leftMax , height[l])
                l+=1
            else:
                if height[r] < RightMax:
                    res+=RightMax-height[r]
                RightMax = max(RightMax , height[r])
                r-=1
        return res
        
        
