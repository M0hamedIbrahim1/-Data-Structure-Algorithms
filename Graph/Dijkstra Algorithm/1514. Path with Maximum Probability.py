# link   : https://leetcode.com/problems/path-with-maximum-probability/description 
# author : Mohamed ibrahim



class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            x,y = edges[i]
            graph[x].append((y,succProb[i]))
            graph[y].append((x,succProb[i]))

        q = [(-1,start)]
        visited = set()
        while q:
            d , cur = heapq.heappop(q)
            visited.add(cur)
            if cur == end:
                return  -d
            for neig,c in graph[cur]:
                if neig not in visited:
                    heapq.heappush(q,(d * c ,  neig))
        return 0
        
        
