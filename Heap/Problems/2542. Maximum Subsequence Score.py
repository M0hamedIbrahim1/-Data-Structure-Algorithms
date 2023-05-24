# link   : https://leetcode.com/problems/maximum-subsequence-score/description/
# author : Mohamed Ibrahim

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        pairs = list(zip(nums1, nums2))
        pairs = sorted(pairs , key = lambda x : -x[1])

        heap = [x[0] for x in pairs[:k]]
        sum_top = sum(heap)
        ans = sum_top*pairs[k-1][1]
        heapq.heapify(heap)

        for i in range(k , len(nums1)):
            sum_top-= heapq.heappop(heap)
            sum_top+= pairs[i][0]
            heapq.heappush(heap , pairs[i][0])

            ans = max(ans , sum_top*pairs[i][1] )
        return ans
        
