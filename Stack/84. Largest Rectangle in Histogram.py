# link   : https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# author : Mohamed Ibrahim

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_val = 0
        for index , cur in enumerate(heights):
            start = index
            while stack and stack[-1][1] > cur:
                start , val = stack.pop()
                max_val = max(max_val , val * (index - start))
            stack.append((start , cur))
            
        for start , val in stack:
            max_val = max(max_val , val * (len(heights) - start))
        return max_val


