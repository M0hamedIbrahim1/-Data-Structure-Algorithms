# link   : https://leetcode.com/problems/network-delay-time/description/
# author : Mohamed Ibrahim

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        for x,y,d in times:
            graph[x].append((y,d))
        minheap = [(0,k)]
        s = 0
        while minheap:
            d,node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            s = max(s,d)
            for N,dd in graph[node]:
                if N not in visited:
                    heapq.heappush(minheap,(dd+d,N))
        return s if len(visited) == n else -1
        
        
