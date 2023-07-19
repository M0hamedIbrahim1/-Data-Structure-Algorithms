# link   : https://leetcode.com/contest/weekly-contest-353/problems/maximum-number-of-jumps-to-reach-the-last-index/
# author : Mohamed Ibrahim

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        res = 0;n=len(nums)
        d = defaultdict(list)
   # Build reachable indexes from every index
        for i in range(n):
            for j in range(i+1,n):
                if -target<=nums[j]-nums[i]<=target : 
                    d[i].append(j)
        # print(d)
        @cache
   # simple dfs start from index zero 
        def dfs(x):
            if x == n-1 : return 0 # if reach to n-1 
            if not d[x]: return float('-inf') # if no way to go from curr index
            cur = float("-inf")
            for nei in d[x]:
                cur = max(cur , 1+dfs(nei)) # max solution to each node
            return cur
        ans = dfs(0)
        return ans if ans>0 else -1
