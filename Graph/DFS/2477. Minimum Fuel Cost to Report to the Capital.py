# link   : https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
# Author : Mohamed Ibrahim

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.ans , graph = 0  , defaultdict(list)
        
        for x,y in roads:
            graph[x].append(y)
            graph[y].append(x)
        def dfs(node,parent):
            people = 1
            for i in graph[node]:
                if i == parent:
                    continue
                people+=dfs(i,node)
            self.ans += ceil(people/seats) if node else 0    
            return people
        dfs(0,-1)
        return self.ans
        
        
