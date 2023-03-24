# link   : https://leetcode.com/problems/maximum-star-sum-of-a-graph/description/
# author : Mohamed Ibrahim

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        n = len(vals)
        for x,y in edges:
            if vals[y] > 0 : graph[x].append(vals[y])
            if vals[x] > 0 : graph[y].append(vals[x])
        mx = float("-inf")    
        for i in range(n):
            x = sorted(graph[i],reverse = True)
            mx = max(mx,vals[i]+sum(x[:k]))
        return mx
        
        
