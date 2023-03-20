# link   : https://leetcode.com/problems/validate-binary-tree-nodes/description/
# author : Mohamed ibrahim


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        childrenNodes = set(leftChild + rightChild)
        graph = defaultdict(list)
        visited = [0]*n
        root = 0
        for i in range(n):
            if i not in childrenNodes:
                root = i

        for i in range(n):
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])
            if rightChild[i] != -1:
                graph[i].append(rightChild[i])

        def dfs(node):
            if visited[node]:
                return False

            visited[node] = 1
   
            for neigh in graph[node]:
                if not dfs(neigh):return False
            return True
        return dfs(root) and all(visited) 
        
        
        
