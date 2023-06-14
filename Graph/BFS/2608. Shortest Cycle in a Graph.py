# link   : https://leetcode.com/problems/shortest-cycle-in-a-graph/description/
# author : Mohamed Ibrahim 

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = float('inf')
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        for i in range(n):
            q = deque([i])
            distance = [float('inf')]*n
            parent = [-1]*n
            distance[i] = 0
            while q:
                node = q.popleft()
                for neigh in graph[node]:
                    if distance[node]+1 < distance[neigh]:
                        distance[neigh] = distance[node]+1
                        q.append(neigh)
                        parent[neigh] = node
                    elif parent[node] != neigh:
                        res = min(res ,distance[neigh]+distance[node]+1)
        return res if res != float('inf') else -1
