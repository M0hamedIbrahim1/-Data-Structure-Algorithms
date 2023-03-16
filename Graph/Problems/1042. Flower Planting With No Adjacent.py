# link   : https://leetcode.com/problems/flower-planting-with-no-adjacent/
# author : Mohamed Ibrahim

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        res = [0]*(n+1)
        for x,y in paths:
            graph[x].append(y)
            graph[y].append(x)
        for i in range(n):
            res[i+1] = ({1,2,3,4} - {res[j] for j in graph[i+1]}).pop()
        return res[1:]
      
      
      
