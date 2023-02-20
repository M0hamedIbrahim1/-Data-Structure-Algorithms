# Link   : https://leetcode.com/problems/course-schedule-ii/description/
# Author : Mohamed Ibrahim


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        res = []
        for x,y in prerequisites:
            graph[x].append(y)
        visited = [0] * numCourses
        def dfs(root):
            if visited[root] == -1:
                return False
            if visited[root] == 1:
                return True
            visited[root] = -1
            for i in graph[root]:
                if not dfs(i):
                    return False
            res.append(root)
            visited[root] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        
        
