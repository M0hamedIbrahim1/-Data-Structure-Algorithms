# link   : https://leetcode.com/problems/candy/description/
# author : Mohamed Ibrahim

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        minHeap = [(ratings[i], i) for i in range(n)]
        heapify(minHeap)  
        candies = [1] * n

        while minHeap:
            rating, idx = heappop(minHeap)

            if (idx > 0) and (ratings[idx] > ratings[idx - 1]):
                candies[idx] = candies[idx - 1] + 1

            if (idx < n - 1) and (ratings[idx] > ratings[idx + 1]):
                candies[idx] = max(candies[idx], candies[idx + 1] + 1)

        return sum(candies)

