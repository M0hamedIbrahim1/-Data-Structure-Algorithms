# link   : https://leetcode.com/problems/find-if-path-exists-in-graph/description/
# author : Mohamed Ibrahim


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        queue = collections.deque([source])
        visited = [False]*n
        while queue:
            q = queue.popleft()
            if q == destination:
                return True
            for neighbours in graph[q]:
                if not visited[neighbours]:
                    queue.append(neighbours)
                    visited[neighbours] = True
        return False
        
        
                                                         # Complexity Analysis

            # Time complexity: O(n+m)                             &                                     Space complexity: O(n+m)



