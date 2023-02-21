# Link   : https://leetcode.com/problems/keys-and-rooms/description/
# author : Mohamed Ibrahim

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        visited[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for i in rooms[node]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
        return all(visited)
        
# ---------------------------------------------        
        
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]*len(rooms)
        s = set()
        def dfs(root):
            s.add(root)
            if visited[root] == -1:
                return
            visited[root] = -1
            for i in rooms[root]:
                dfs(i)
        dfs(0)
        return len(s) == len(rooms)
        
