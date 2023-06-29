# link   : https://leetcode.com/problems/painting-the-walls/description/
# author : Mohamed Ibrahim

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(time)
        d = {}
        def dfs(t , c):
            if (t , c) in d:return d[(t , c)]
            if t >= n:return 0
            if c >= n:return float('inf')
            res = min(
                cost[c] + dfs(t+time[c]+1 , c+1),
                dfs(t , c+1)
            )
            d[(t , c)] = res
            return res
        return dfs(0 , 0)
