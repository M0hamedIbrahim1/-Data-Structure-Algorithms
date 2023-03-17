# Link   : https://leetcode.com/problems/course-schedule-iv/description/
# author : Mohamed Ibrahim

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        ans = [[False]*numCourses for i in range(numCourses)]
        for pre,cors in prerequisites:
            graph[pre].append(cors)
        def dfs(node,visited):
            if node not in visited:
                visited.add(node)                
                for i in graph[node]:
                    dfs(i,visited)
        for i in range(numCourses):
            visited = set()
            dfs(i,visited)
            for j in visited:
                ans[i][j] = True
        return [ans[s][d] for s, d in queries]            
        
        
