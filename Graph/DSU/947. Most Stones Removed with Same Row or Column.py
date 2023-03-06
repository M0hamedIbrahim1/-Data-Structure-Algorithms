# link   : https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
# author : Mohamed Ibrahim


class Solution:
    def removeStones(self, stones):
        UF = {}
        def find(parent):
            if UF[parent] != parent:
                UF[parent] = find(UF[parent])
            return UF[parent]
        def union(u,v):
            if u not in UF:
                UF[u] = u
            if v not in UF:
                UF[v] = v
            parent_u = find(u)
            parent_v = find(v)
            UF[parent_u] = parent_v

        for x,y in stones:
            union(x,y+10000000)
        return len(stones) - len({find(n) for n in UF})
        
