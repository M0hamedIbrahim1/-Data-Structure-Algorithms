# link   : https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:return [target.val]
        graph = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)

                q.append(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)

                q.append(node.right)
        d = deque([(target , 0)])
        visited = set([target])
        res = []
        while d:
            node,distance = d.popleft()
            if distance == k:
                res.append(node.val)
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    d.append([neigh , distance+1])

        return res
