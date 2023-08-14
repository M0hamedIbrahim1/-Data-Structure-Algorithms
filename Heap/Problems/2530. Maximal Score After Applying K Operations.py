# link : https://leetcode.com/contest/weekly-contest-327/problems/maximal-score-after-applying-k-operations/
# autor : Mohamed Ibrahim

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        res = 0
        while k :
            val = heappop(heap)
            res+= -val
            heappush(heap , -ceil((-val)/3))
            k-=1
        return res
      
