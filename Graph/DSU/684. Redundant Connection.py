# link   : https://leetcode.com/problems/redundant-connection/description/
# author : Mohamed Ibrahim


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i : -1 for i in range(1,n+1)}
        def find(u):
            if parent[u] != -1:
                parent[u] = find(parent[u])
                return parent[u] 
            else:
                return u


        def union(u,v):
            parent_of_u = find(u)
            parent_of_v = find(v)
            if parent_of_u == parent_of_v:
                return True
            parent[parent_of_u] = parent_of_v
            return False
        res = None
        for u,v in edges:
            if union(u,v):
                res = [u,v]
                return res
                
                
                
