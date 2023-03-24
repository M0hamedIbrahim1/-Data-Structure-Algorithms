# Link   : https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# Author : Mohamed Ibrahim

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")]*n
        prices[src] = 0
        for i in range(k+1):
            temp = prices.copy()
            for Src,Dst,cost in flights:
                if prices[Src] == float("inf"):continue
                if prices[Src]+cost < temp[Dst]:
                    temp[Dst] = prices[Src]+cost
            prices = temp
        return -1 if prices[dst] == float("inf") else prices[dst]
        
        
