# author : Mohamed Ibrahim
# link   : https://leetcode.com/problems/course-schedule/description/



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = [0] * numCourses
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 1
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True


