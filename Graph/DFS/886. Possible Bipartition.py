# Link   : https://leetcode.com/problems/possible-bipartition/description/
# author : Mohamed Ibrahim

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        color = {}

        def dfs(node , c):
            color[node] = c
            for enemy in graph[node]:
                if enemy in color:
                    if color[enemy] == c:
                        return False
                else:
                    if not dfs(enemy,1-c):
                        return False
            return True
        for i in range(n):
            if i+1 not in color:
                if not dfs(i+1 , 1):
                    return False
        return True 
        
        
