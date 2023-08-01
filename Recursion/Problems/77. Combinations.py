# link  : https://leetcode.com/problems/combinations/description/
# auhor : Mohamed Ibrahim

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def rec(i , Len , subset):
            if Len == k:
                res.append(subset)
                return
            if i == n+1:
                return 
 
            rec(i + 1 , Len + 1 , subset + [i])
            rec(i + 1 , Len  , subset)
        rec(1 , 0 , [])
        return res
