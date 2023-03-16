# link   : https://leetcode.com/problems/satisfiability-of-equality-equations/description/
# author : Mohamed Ibrahim



class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        inequals,equals,full = set(),set(),set()
        for i in equations:
            if i[1] == '=':
                equals.add((i[0],i[3]))
            else:
                inequals.add((i[0],i[3]))
            full.add(i[0])
            full.add(i[3])

        graph = {c:c for c in full}
        def find(node):
            if graph[node] == node:
                return graph[node]
            graph[node] = find(graph[node])
            return graph[node]
        def union(Node1,Node2):
            Parent_Node1 = find(Node1)
            Parent_Node2 = find(Node2)
            graph[Parent_Node1] = Parent_Node2
        for x,y in equals:
            union(x,y)
        for x,y in inequals:
            if find(x) == find(y):
                return False
        return True
        
        
