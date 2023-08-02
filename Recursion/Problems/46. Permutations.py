# link : https://leetcode.com/problems/permutations/description/
# author : Mohamed Ibrahim


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def resc(lst , subset):
            if not lst:
                res.append(subset)

            for i in range(len(lst)):
                resc(lst[:i]+lst[i+1:] , subset + [lst[i]])

        resc( nums , [])
        return res
