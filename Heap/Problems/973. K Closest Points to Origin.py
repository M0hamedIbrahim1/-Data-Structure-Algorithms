# link   : https://leetcode.com/problems/k-closest-points-to-origin/description/
# author : Mohamed Ibrahim

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap,res = [],[]
        for x,y in points:
            d = sqrt(x**2 + y**2)
            heapq.heappush(heap,(d , x , y))
        while k:
            d , x , y = heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res
      
