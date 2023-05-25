# link   : https://leetcode.com/problems/count-the-number-of-complete-components/description/
# author : Mohamed Ibrahim

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(i):
            nodes.add(i)
            for neigh in graph[i]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)

        ans = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                nodes = set()
                dfs(i)
                if all(len(graph[node]) == len(nodes)-1 for node in nodes):
                    ans+=1
        return ans

