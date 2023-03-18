class Solution:
  # link   : https://leetcode.com/problems/most-profitable-path-in-a-tree/description/
  # author : Mohamed Ibrahim
  
  def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        x = []
        def dfs(node,Path,parent):

            Path.append(node)
            if node == 0:
                x.extend(Path)
                return
            for neigh in graph[node]:
                if neigh == parent:continue
                dfs(neigh,Path,node)
                Path.pop()

        dfs(bob,[],-1)

        for i in range(len(x)//2):
            amount[x[i]] = 0
        if len(x) % 2 : amount[x[len(x)//2]] //= 2

        def mostprofit(node,parent):
            if len(graph[node]) == 1 and graph[node][0] == parent:
                return amount[node]
            mx = -inf
            for neigh in graph[node]:
                if neigh ==  parent:continue
                mx = max(mx , mostprofit(neigh,node))
            return mx + amount[node]

        return mostprofit(0,parent = -1)
        
        
