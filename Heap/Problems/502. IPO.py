# Link   : https://leetcode.com/problems/ipo/description/
# Author : Mohamed Ibrahim

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int],
                             capital: List[int]) -> int:

        mincapital = [(c,p) for c,p in zip(capital,profits)]
        maxprofit = []
        heapq.heapify(mincapital)
        profit = 0
        for i in range(k):
            while mincapital and mincapital[0][0] <= w:
                c,p = heapq.heappop(mincapital)
                heapq.heappush(maxprofit,-1*p)
            if not maxprofit:break
            profit=-1*heapq.heappop(maxprofit)
            w+=profit
        return w
        
        
        
