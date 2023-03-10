# link   : https://leetcode.com/problems/is-graph-bipartite/description/
# author : Mohamed Ibrahim



class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        two_set = [set(),set()]
        for i in range(len(graph)):
            queue = [(i , 0)]
            if i not in visited:
                while queue:
                    node , level = queue.pop()
                    visited.add(node)
                    two_set[level].add(node)

                    for j in graph[node]:
                        if j in two_set[level]:
                            return False
                        if j not in visited:
                            queue.append((j, 1 if level == 0 else 0))
        return True
        
