# link : https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/submissions/
# author : Mohamed Ibrahim

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        n = len(cost)
        self.res = 0
        def dfs(i):
            if i-1 >= n :
                return 0
            left = dfs(2*i)
            right = dfs(2*i +1)

            self.res+=abs(right - left)
            return max(left,right)+cost[i-1]
        dfs(1)
        return self.res
        
