# link   : https://leetcode.com/problems/sliding-window-maximum/description/
# author : Mohamed Ibrahim

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i , cur in enumerate(nums):
            
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)

            if q[0] < (i-k )+1:
                q.popleft()
            
            if i >= k-1:
                res.append(nums[q[0]])
        return res
      
