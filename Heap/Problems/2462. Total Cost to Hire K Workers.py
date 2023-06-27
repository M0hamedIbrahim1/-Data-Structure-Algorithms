# link   : https://leetcode.com/problems/total-cost-to-hire-k-workers/description/
# author : Mohamed Ibrahim

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap,res = [],0
        for i in range(candidates):
            heap.append([costs[i] , 0])
        for i in range(max(candidates , len(costs)-candidates) , len(costs)):
            heap.append([costs[i] , 1])
        left , right = candidates , len(costs) - 1 - candidates 
        heapify(heap)
        for i in range(k):
            val , direct = heappop(heap)
            res+=val

            if left <= right:
                if direct == 0:
                    heappush(heap , [costs[left] , 0])
                    left+=1
                else:
                    heappush(heap , [costs[right] , 1])
                    right-=1
        return res
