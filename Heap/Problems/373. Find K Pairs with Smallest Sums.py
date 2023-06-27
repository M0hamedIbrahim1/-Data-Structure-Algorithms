# link   : https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# author : Mohamed Ibrahim

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        n = len(nums1)
        m = len(nums2)
        visited = set()
        heap = [(nums1[0]+nums1[0] , 0 , 0)]
        res = []
        while k and heap:
            val , i , j = heappop(heap)
            res.append([nums1[i] , nums2[j]])
            if i + 1 < n and (i+1 , j) not in visited:
                heappush(heap , (nums1[i+1]+nums2[j] , i+1 , j))
                visited.add((i+1 , j))
            if  j + 1 < m and (i , j+1) not in visited:
                heappush(heap , (nums1[i]+nums2[j+1] , i , j+1))
                visited.add((i , j+1))

            k-=1
        return res
