# link   : https://leetcode.com/problems/find-if-path-exists-in-graph/description/
# author : Mohamed Ibrahim


#  Depth First Search (DFS): Recursive

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False]*n
        def dfs(node):
            if node == destination:
                return True
            if not visited[node]:
                visited[node] = True
                for i in graph[node]:
                    if dfs(i):return True
            return False
        return dfs(source)
            



# Depth First Search (DFS): Iterative

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False]*n
        visited[source] = True
        stack = [source]
        while stack:
            s = stack.pop()
            if s == destination:return True
            for neighbours in graph[s]:
                if not visited[neighbours]:
                    visited[neighbours] = True
                    stack.append(neighbours)
        return False
        
                                                         # Complexity Analysis

            # Time complexity: O(n+m)                             &                                     Space complexity: O(n+m)

            
