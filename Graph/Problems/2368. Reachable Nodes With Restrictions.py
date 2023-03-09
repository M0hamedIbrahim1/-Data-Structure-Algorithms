# link   : https://leetcode.com/problems/reachable-nodes-with-restrictions/description/?orderBy=most_votes
# author : Mohamed Ibrahim



class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = [0]*n
        visited[0] = 1
        for i in restricted:
            visited[i] = -1
        stack = [0]
        s = 0
        while stack:
            s+=1
            node = stack.pop()
            for i in graph[node]:
                if visited[i] == 0:
                    stack.append(i)
                    visited[i]=1

        return s
        
        
