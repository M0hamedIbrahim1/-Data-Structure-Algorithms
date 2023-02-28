# link   : https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
# author : Mohamed Ibrahim


# DFS
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for x,y in connections:
            graph[x].append((y,1))
            graph[y].append((x,-1))
        visited = [0]*n
        self.cnt = 0

        def dfs(node):
            visited[node] = 1
            for x,d in graph[node]:
                if not visited[x]:
                    if d == 1:self.cnt+=1
                    dfs(x)
        dfs(0)
        return self.cnt
 

# Stack
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected_graph = defaultdict(list)
        
        for origin, destination in connections:
            undirected_graph[origin].append(destination)
            undirected_graph[destination].append(origin)
            
        connections = set(map(tuple, connections))

        stack = [(0,0)]
        cnt = -1
        visited = {0}
        while stack:
            cur , prev = stack.pop()
            if (cur , prev) not in connections:
                cnt+=1
            for c in undirected_graph[cur]:
                if c not in visited:
                    stack.append((c,cur)) 
                    visited.add(c)
        return cnt
        
        
