# link   : https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
# author : Mohamed Ibrahim

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n,m = len(mat),len(mat[0])
        heap = []
        for i in range(n):
            s = sum(mat[i])
            heappush(heap , [s , i])
        ans = []
        for i in range(k):
            _,indx = heappop(heap)
            ans.append(indx)
        return ans
